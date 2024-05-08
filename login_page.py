import streamlit as st
import os
import db as db
import utils as utils
import camera as camera
placeholder = st.empty()

if 'session' not in st.session_state:
    st.session_state.session = None
    st.session_state.loginStatus = False
    st.session_state.page = "Login"
if 'loginStatus' not in st.session_state:
    st.session_state.loginStatus = False
if 'page' not in st.session_state:
    st.session_state.page = "Login"
if 'data' not in st.session_state:
    st.session_state.data = None

print("data:",st.session_state.data)
# Add data to db if exist then remove from session
if st.session_state.data != None:
    data = st.session_state.data
    db.insert_data(data[0], data[1], data[2], data[3], data[4], data[5])
    data = None
    st.session_state.data = None

def set_session(session):
    st.session_state.session = session
def set_login_status(login):
    st.session_state.loginStatus = login
def get_login_status():
    return st.session_state.loginStatus
    
def login():
    # import streamlit as st
    # Create an empty container
    placeholder = st.empty()
    login_form = placeholder.form("login")

    # Insert a form in the container
    with login_form:

        st.markdown("#### Student / Lecturer Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit and len(username) > 0 and len(password) > 0:
            # check if the user exist in the db
            # If the form is submitted and the username and password are correct,
            # clear the form/container
            returnStatus = db.login(username, password)
            if returnStatus != None :
                set_session(returnStatus)
                set_login_status(True)
            else :
                st.error("Login failed. Please try again!")
                set_login_status(False)
        # debug
        # st.write("login")
        # st.write(st.session_state.loginStatus)
        # st.write(st.session_state.session)

    if st.session_state.session != None:
        if st.session_state.session[1] == "student":
            placeholder.empty()
            page_names_to_funcs["student_dashboard"]()
        else :
            placeholder.empty()
            page_names_to_funcs["lecturer_dashboard"]()
    
    
def student_dashboard():
    # import streamlit as st
    
    container = placeholder.container()
    hCol1, hCol2 = st.columns(2, gap="large")
    student_id = st.session_state.session[0]

    with container:
        # Header
        if st.button("logout"):
            set_login_status(False)
            set_session(None)
            
            
        st.markdown(f'# Student Dashboard')
        
        student_info = db.get_student_info(student_id)
        col1, col2 = st.columns(2)
        student_id = student_info['id']
        student_name = student_info['name']
        student_email = student_info['email']
        student_phoneNo = student_info['phone_no']
        
        with col1:
            st.markdown('#### Student Details:')
            st.text(f'Student ID: {student_id}')
            st.text(f'Student Name: {student_name}')
            st.text(f'Email: {student_email}')
            st.text(f'Phone No: {student_phoneNo}')

        with col2:
            st.markdown('#### Student Engagement Level Record:')
            if st.button(f'View Record'):
                st.session_state.page = 'student log'
                
            st.markdown('##### Record Engagement Level:')
            placeholder2 = st.empty()
            cameraBtn = placeholder2.button(f'Camera Activation', disabled=False, key=1)
            if cameraBtn :
                placeholder2.button(f'Camera Activation',  disabled=True, key=2)
                # open camera
                camera.openCameraV1(student_id, student_name)
        

        # debug
        # st.write("student dashboard")
        # st.write(st.session_state.loginStatus)
        # st.write(st.session_state.session)
        # st.write(get_login_status())

    if st.session_state.loginStatus == False:
        placeholder.empty()
        page_names_to_funcs["Login"]()
        
    if st.session_state.page == 'student log':
        placeholder.empty()
        page_names_to_funcs["student log"]()

def lecturer_dashboard():
    # import streamlit as st
    placeholder = st.empty()
    container = placeholder.container()
    hCol1, hCol2 = st.columns(2, gap="large")
    lecturer_id = st.session_state.session[0]

    with container:
        # Header
        if st.button("logout"):
            set_login_status(False)
            set_session(None)
            
            
        st.markdown(f'# Lecturer Dashboard')
        
        lecturer_info = db.get_lecturer_info(lecturer_id)
        col1, col2 = st.columns(2)
        lecturer_id = lecturer_info['id']
        lecturer_name = lecturer_info['name']
        lecturer_email = lecturer_info['email']
        lecturer_phoneNo = lecturer_info['phone_no']
        
        with col1:
            st.markdown('#### Lecturer Details:')
            st.text(f'Lecturer ID: {lecturer_id}')
            st.text(f'Lecturer Name: {lecturer_name}')
            st.text(f'Email: {lecturer_email}')
            st.text(f'Phone No: {lecturer_phoneNo}')

        with col2:
            st.markdown('#### Student Engagement Level Record:')
            if st.button(f'View Record'):
                st.session_state.page = 'all_student_records'
            
        

        # debug
        # st.write("lecturer dashboard")
        # st.write(st.session_state.loginStatus)
        # st.write(st.session_state.session)
        # st.write(get_login_status())

    if st.session_state.loginStatus == False:
        placeholder.empty()
        page_names_to_funcs["Login"]()
        
    if st.session_state.page == 'all_student_records':
        placeholder.empty()
        page_names_to_funcs["all_student_records"]()

def student_log():
    # import streamlit as st
    import pandas as pd
    placeholder = st.empty()

    with placeholder.container():

        if st.button("back"):
            st.session_state.page = "Login"
            

        st.markdown("# Student Engagement Level Record")

        st.markdown(        
        """<style>
            .css-4sszyo {text-align: left !important}
            .col_heading {text-align: left !important}
        </style>
        """, unsafe_allow_html=True) 

        data = db.student_log(st.session_state.session[0])
        # name_map = {"a":"total lost attention time","b":"total attention time"}
        # new_rows = [dict(zip(map(lambda x: name_map[x], r.keys()), r.values())) for r in data]
        df = pd.DataFrame(data)
        st.table(df)

    if st.session_state.page == "Login":
        placeholder.empty()
        page_names_to_funcs["student_dashboard"]()

def all_student_records():
    # import streamlit as st
    import pandas as pd
    placeholder = st.empty()

    with placeholder.container():
        data = db.all_log()
        # name_map = {"a":"total lost attention time","b":"total attention time"}
        # new_rows = [dict(zip(map(lambda x: name_map[x], r.keys()), r.values())) for r in data]
        df = pd.DataFrame(data)

        if st.button("back"):
            st.session_state.page = "Login"
            

        st.markdown("# Student Engagement Level Record")

        csv = utils.convert_df(df)

        st.download_button(
            "Press to Download",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv'
        )

        st.markdown(        
        """<style>
            .css-4sszyo {text-align: left !important}
            .col_heading {text-align: left !important}
        </style>
        """, unsafe_allow_html=True) 

        st.table(df)

    if st.session_state.page == "Login":
        placeholder.empty()
        page_names_to_funcs["lecturer_dashboard"]()


page_names_to_funcs = {
    "student_dashboard": student_dashboard,
    "lecturer_dashboard": lecturer_dashboard,
    "Login": login,
    "student log": student_log,
    "all_student_records": all_student_records,
}

# demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
if st.session_state.loginStatus == False:
    placeholder.empty()
    page_names_to_funcs["Login"]()

elif st.session_state.loginStatus == True:
    if st.session_state.session[1] == "student" and st.session_state.page == "Login":
        placeholder.empty()
        print("opening dashboard")
        page_names_to_funcs["student_dashboard"]()
    elif st.session_state.session[1] == "lecturer" and st.session_state.page == "Login" :
        page_names_to_funcs["lecturer_dashboard"]()
    elif st.session_state.session[1] == "student" and st.session_state.page == "student log" :
        page_names_to_funcs["student log"]()
    elif st.session_state.session[1] == "lecturer" and st.session_state.page == "all_student_records" :
        page_names_to_funcs["all_student_records"]()
