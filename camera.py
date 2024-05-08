import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import db as db
import time
from datetime import datetime

if 'data' not in st.session_state:
    st.session_state.data = None


def seconds_passed(oldepoch):
    print("sh",time.time() - oldepoch > 1)
    return time.time() - oldepoch > 1



def openCameraV1(studentId, student_name):
    imageLocation = st.empty()
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh=mp_face_mesh.FaceMesh(min_detection_confidence=0.5,min_tracking_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

    cap = cv2.VideoCapture(0)

    text=None
    counter=0
    count_non=0
    
    start = time.time()
    stopBtn = st.button("Stop")

    while cap.isOpened():
        #startFps = time.time()
        success, image = cap.read()

        #convert BGR to RGB
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        image.flags.writeable = False
        
        # result
        results = face_mesh.process(image)
        
        
        image.flags.writeable = True
        
        # Convert RGB to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
        img_h, img_w, img_c = image.shape
        face_3d = []
        face_2d = []

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for idx, lm in enumerate(face_landmarks.landmark):
                    if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                        if idx == 1:
                            nose_2d = (lm.x * img_w, lm.y * img_h)
                            nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 3000)

                        x, y = int(lm.x * img_w), int(lm.y * img_h)
                    

                        # 2D Coordinates & 3D Coordinates
                        face_2d.append([x, y])
                        face_3d.append([x, y, lm.z])       
                
                # Convert to NumPy array
                face_2d = np.array(face_2d, dtype=np.float64)
                face_3d = np.array(face_3d, dtype=np.float64)
                
                # The camera matrix
                focal_length = 1 * img_w

                cam_matrix = np.array([ [focal_length, 0, img_h / 2],
                                        [0, focal_length, img_w / 2],
                                        [0, 0, 1]])

                # The distortion parameters
                dist_matrix = np.zeros((4, 1), dtype=np.float64)

                # Solve PnP
                success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

                # rotational matrix
                rmat, jac = cv2.Rodrigues(rot_vec)

                # angles
                angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

                # rotation degree
                x = angles[0] * 360
                y = angles[1] * 360
                z = angles[2] * 360
                
                # Attention of Student
                if y < -13 or y> 13 or x < -13 or x > 13:
                    text ="Disengage"
                    if seconds_passed(start):
                        count_non+=1
                        print("Disengage",count_non,"Time", time.time())
                        start = time.time()
                    
                else:
                    text="Engage"
                    if seconds_passed(start):
                        counter+=1
                        print("Disengage",counter,"Time", time.time())
                        start = time.time()

                # Display the nose direction
                nose_3d_projection, jacobian = cv2.projectPoints(nose_3d, rot_vec, trans_vec, cam_matrix, dist_matrix)

                p1 = (int(nose_2d[0]), int(nose_2d[1]))
                p2 = (int(nose_2d[0] + y * 13) , int(nose_2d[1] - x * 13))
                
                cv2.line(image, p1, p2, (255, 0, 0), 3)

                # Add the text on the image
                cv2.putText(image,text,(60, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (108, 0, 12), 2)
                cv2.putText(image, "x: " + str(np.round(x,2)), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 200), 2)
                cv2.putText(image, "y: " + str(np.round(y,2)), (500, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 200), 2)
                cv2.putText(image, "z: " + str(np.round(z,2)), (500, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 200), 2)


           # end = time.time()
            #totalTime = end - startFps

            #fps = 1 / totalTime
            # print("FPS: ", fps)

            #cv2.putText(image, f'FPS: {int(fps)}', (20,450), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)
            
            #it shows the drawing of the contour

        # cv2.imshow('Engagement level of Student', image)
        image_bytes = cv2.imencode('.jpg', image)[1].tobytes()
        cv2.imshow('image', image)
        
        imageLocation.image(image_bytes)

        # average = counter > 0 and counter or 1 / (counter > 0 and counter or 1 + count_non > 0 and count_non or 1)
        cTotal = (counter  > 0 and counter or 1) + count_non
        average = round((counter / cTotal) * 100)
        
        status = 0
        if average > 70 :
            status = "Engage"
        else:
            status = "Disengage"
        st.session_state.data = [studentId, student_name, str(count_non), str(counter), str(average), status]
        # print("data camera:",st.session_state.data)
        # print("camera: ", count_non, counter)
        if cv2.waitKey(5) & 0xFF == 27:
            break
        if stopBtn:
            print("program break")
            break

    print("data upload")
    cap.release()
    cv2.destroyAllWindows()
    # Insert data into db