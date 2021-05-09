"""import for the functions and this file is acting as a client side"""
import socket
import sys
import final_assignment_module as sm

HOST = "127.0.0.1"
PORT = 65431
STUDENTS_FINAL_FILE_NAME = 'final_students.txt'
MAX_PASSWORD_TRAILS = 3

if __name__ == '__main__':
    StudentData = sm.StudentsId
    StudentData.load_students()
    STUDENT_ID = input("Please enter your student ID: ")
    if not StudentData.is_valid_id(STUDENT_ID):
        print("The provided student id was not found!")
        sys.exit(1)
    TRIAL_PASS = 0
    USER_PASSWORD = input("Please enter a valid password: ")
    PASS_UP = sm.is_valid_password(USER_PASSWORD)

    IS_VALID_PASSWORD = PASS_UP
    while not IS_VALID_PASSWORD and TRIAL_PASS < MAX_PASSWORD_TRAILS - 1:
        INVALID_USER_PASSWORD = input("Invalid password, please try again: ")
        IS_VALID_PASSWORD = PASS_UP
        TRIAL_PASS += 1
    if not IS_VALID_PASSWORD:
        print("You have exhausted your password trials."
              "Please restart again")
        sys.exit(1)
    STUDENT_RECORD = StudentData.get_student_record(STUDENT_ID)
    STUDENT_RECORD = STUDENT_RECORD.replace('\n', '')
    STUDENT_RECORD = f'{STUDENT_RECORD},password:{USER_PASSWORD}\n'
    STUDENT_UPDATE = sm.StudentsInfo()
    if STUDENT_UPDATE.update_final_list(STUDENTS_FINAL_FILE_NAME, STUDENT_ID, STUDENT_RECORD):
        print("Your record was successfully updated!")
    else:
        print("Relax, your record is already up to date!")
    FILE_FORMAT_INPUT3 = input("Enter a File Format: ")
    ACTION_INPUT = sm.FileFormat()
    ACTION_VALUE1 = str(ACTION_INPUT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(FILE_FORMAT_INPUT3.encode())
