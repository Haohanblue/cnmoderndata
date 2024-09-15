import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name, port):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            port=port
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# 替换这些值为你的数据库信息
host = "bj-cynosdbmysql-grp-3upmvv08.sql.tencentcdb.com"
port = 27017  # 确保这是整数，例如 3306
db_name = "school"
user = "haohanblue"
password = "Haohanblue233."

connection = create_connection(host, user, password, db_name, port)

# SQL语句来创建表
create_classes_table = """
CREATE TABLE IF NOT EXISTS Classes (
    ClassID INT AUTO_INCREMENT PRIMARY KEY,
    ClassName VARCHAR(100)
);
"""

create_teachers_table = """
CREATE TABLE IF NOT EXISTS Teachers (
    TeacherID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100)
);
"""

create_courses_table = """
CREATE TABLE IF NOT EXISTS Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    CourseName VARCHAR(100)
);
"""

create_course_instances_table = """
CREATE TABLE IF NOT EXISTS CourseInstances (
    InstanceID INT AUTO_INCREMENT PRIMARY KEY,
    CourseID INT,
    ClassID INT,
    TeacherID INT,
    Time VARCHAR(100),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID),
    UNIQUE (ClassID, Time)
);
"""

# 执行创建表的命令
execute_query(connection, create_classes_table)
execute_query(connection, create_teachers_table)
execute_query(connection, create_courses_table)
execute_query(connection, create_course_instances_table)
