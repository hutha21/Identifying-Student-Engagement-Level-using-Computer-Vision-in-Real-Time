# Import
import pymysql.cursors
import utils as utils

# Insert Data to Database
def insert_data(studentId, studentName, lostEngagement, engagement, average, status):
    print("insert data:",studentId, studentName, lostEngagement, engagement, average, status)
    # Create connection
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='python_db',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `student_engagement_level` (`student_id`, `student_name`, `lost_engagement_time`, `engagement_time`, `average_engagement`, `engagement_status`) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (studentId, studentName, lostEngagement, engagement, average, status))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

def get_student_info(studentId):
    # Create connection
    result = None
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='python_db',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `name`, `email`, `phone_no` FROM `login_student` WHERE `id`=%s"
            cursor.execute(sql, (studentId,))
            result = cursor.fetchone()
        connection.commit()
    return result

def get_lecturer_info(lecturerId):
    # Create connection
    result = None
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='python_db',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `name`, `email`, `phone_no` FROM `login_lecturer` WHERE `id`=%s"
            cursor.execute(sql, (lecturerId,))
            result = cursor.fetchone()
        connection.commit()
    return result

def login(username, password):
    # Create connection
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='python_db',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `name`, `email`, `phone_no` FROM `login_student` WHERE `username`=%s AND `password` =%s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            print(result)
        connection.commit()
    if result != None :
        return [result['id'], "student"]
    else :
        # Create connection
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    database='python_db',
                                    cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `name`, `email`, `phone_no` FROM `login_lecturer` WHERE `username`=%s AND `password` =%s"
                cursor.execute(sql, (username, password))
                result = cursor.fetchone()
            connection.commit()
    if result != None :
        return [result['id'], "lecturer"]
    else :
        return result

# Retrive specific student log
def student_log(studentId):
    # Create connection

    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='python_db',
                                cursorclass=pymysql.cursors.DictCursor)
    # Create connection
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='python_db',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `lost_engagement_time` AS `Total Lost Engagement Time`, `engagement_time` AS `Total Engagement Time`, `average_engagement` AS `Average Engagement`, `engagement_status` AS `Engagement Status` FROM `student_engagement_level` WHERE `student_id`=%s"
            cursor.execute(sql, (studentId))
            result = cursor.fetchall()
            print(result)
        connection.commit()
    # Replicatate this function if want to add unit in other key
    utils.addUnit(result, "Average Engagement", " %")
    return result

# Retrieve every student log
def all_log():
    # Create connection

    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='python_db',
                                cursorclass=pymysql.cursors.DictCursor)
    # Create connection
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='python_db',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `student_id` AS `Student ID`, `student_name` AS `Student Name`, `lost_engagement_time` AS `Total Lost Engagement Time`, `engagement_time` AS `Total Engagement Time`, `average_engagement` AS `Average Engagement`, `engagement_status` AS `Engagement Status` FROM `student_engagement_level`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
        connection.commit()

    # Replicatate this function if want to add unit in other key
    utils.addUnit(result, "Average Engagement", "%")
    return result

