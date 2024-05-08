**Project Title:** Identifying Student Engagement Level using Computer Vision in Real-Time

**Description:**
This project aims to develop a real-time system using computer vision to identify and monitor student engagement levels in classrooms. By leveraging face detection and head pose estimation, the system provides insights into individual student focus, enabling lecturers to enhance teaching strategies 
**Features:**
- **Student Profile:** Displays total lost engagement time, total engagement time, average engagement, and engagement status.
- **Lecturer Profile:** Provides student ID, name, total lost engagement time, total engagement time, average engagement, and engagement status.
- **Engagement Status:** Determined based on the average engagement; students with over 70% engagement are marked as engaged.
- **Export to Excel:** Lecturers can download overall records into an Excel file for further analysis.

**Dependencies:**
- PyMySQL
- pandas
- MediaPipe

**Database:** Utilizes XAMPP, with the database folder provided in the repository.

**How to Run:**
1. Install dependencies using Anaconda:
   ```
   pip install PyMySQL
   pip install pandas
   pip install mediaPipe
   ```

2. Import the provided database folder into XAMPP.

3. Run the application by executing `streamlit run login_page.py` in the Anaconda prompt.

**Note:** Ensure XAMPP is properly configured and running before executing the application.
