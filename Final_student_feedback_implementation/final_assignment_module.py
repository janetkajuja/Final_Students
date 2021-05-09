"""This is the file for all functions that will be used in this project"""
import re
import json
import xml.etree.ElementTree as xml

LINE_SEPARATOR = ","
PART_SEPARATOR = ":"
FINAL_OBJECT = {}
FILE_FINAL_NAME = "final_students.txt"
MIN_PASSWORD_LENGTH = 8
STUDENTS_RECORDS = {}


class StudentsId:
    """This class contained all information about student ID and file"""

    def __init__(self):
        self.students_record = {}

    @staticmethod
    def load_students():
        """This function is for reading file student.txt """
        try:
            with open(FILE_FINAL_NAME, 'r') as students:
                for student in students:
                    student_line = student.replace("\n", "").strip()
                    id_part = student_line.strip().split(LINE_SEPARATOR)
                    id_value = id_part[0].strip().split(PART_SEPARATOR)[1]
                    STUDENTS_RECORDS.update({id_value: student_line})

        except FileNotFoundError:
            pass
        return STUDENTS_RECORDS

    @staticmethod
    def is_valid_id(student_id: str) -> bool:
        """function for checking the entered valid ID"""
        if STUDENTS_RECORDS.get(student_id):
            return True
        return False

    @staticmethod
    def get_student_record(student_id: str) -> str:
        """function for checking if the entered records is displayed"""
        return STUDENTS_RECORDS.get(student_id)


def is_valid_password(password: str) -> bool:
    """function for checking if password is valid"""
    reserved_characters = ['!', '+', '=']

    password_copy = password
    regex = '^[0-9A-Za-z]+$'
    if len(password) < MIN_PASSWORD_LENGTH:
        return False
    for character in password:
        if character in reserved_characters:
            print("Please entered new password wih no !,=,+")
        elif not character.isalnum():
            password_copy = password_copy.replace(character, '', 1)
    if len(password_copy) == len(password):
        return False
    if re.search(regex, password_copy):
        return True
    return False


class StudentsInfo:
    """students updated info"""

    @staticmethod
    def is_record_updated(file_name: str, student_id: str) -> bool:
        """function for checking if the file is updated"""

        try:
            with open(file_name, 'r') as final_file:
                for record in final_file:
                    if record.startswith(f'id:{student_id}'):
                        return record
        except FileNotFoundError:
            pass

    def update_final_list(self, file_name: str, student_id: str, student_record: str) -> int:
        """function for updating and writing student information into final_students.txt"""
        if self.is_record_updated(file_name, student_id):
            return 0
        try:
            with open(file_name, 'a') as final_file:
                final_file.write(student_record)
        except FileNotFoundError:
            return 0
        return 1


class FileFormat:
    """this class is for the file format"""

    def __init__(self):
        self.file_format_name_json = "JSON"
        self.file_format_name_xml = "XML"
        self.file_format_name_csv = "CSV"

    def convert_format_json(self, exte):
        """this function is for creating json format file"""
        self.file_format_name_json.upper()
        with open(f'final_students.{exte}', "w") as json_file:
            try:
                with open("final_students.txt", "r") as final_students:
                    for final_student in final_students:
                        user = final_student.strip().split(LINE_SEPARATOR)
                        user_id = user[0].strip().split(PART_SEPARATOR)[1]
                        FINAL_OBJECT.update({user_id: final_student.strip().replace("\n", "")})
                json.dump(FINAL_OBJECT, json_file, indent=4)
            except FileNotFoundError:
                print("File not found")

    def convert_format_xml(self):
        """this function is for creating xml format file"""
        self.file_format_name_xml.upper()

        with open("final_students.xml", "w") as xml_file:
            students = xml.Element("students")
            final_xml_data = ""

            try:
                with open(FILE_FINAL_NAME, "r") as final_students:
                    for lines in final_students:
                        xml_file_dict = {}
                        new_lines = lines.replace("\n", "")
                        list_new_lines = new_lines.split(LINE_SEPARATOR)
                        for new in list_new_lines:
                            user_key_id = new.split(PART_SEPARATOR)
                            xml_file_dict[user_key_id[0].strip()] = user_key_id[1].strip()
                        student = xml.SubElement(students, "student",
                                                 attrib={"id": xml_file_dict["id"]})
                        firstname = xml.SubElement(student, "firstname")
                        lastname = xml.SubElement(student, "lastname")
                        firstname.text = xml_file_dict["firstname"]
                        lastname.text = xml_file_dict["lastname"]
                        final_xml_data = xml.tostring(students, encoding="unicode")
                xml_file.write(final_xml_data)
            except FileNotFoundError:
                print("File not found")

    def convert_csv(self):
        """this function is for creating csv format file"""
        self.file_format_name_csv.upper()
        with open("final_students.csv", "w") as file_csv:
            csv_final = ""
            try:
                with open(FILE_FINAL_NAME, "r") as student_txt_file:
                    csv_final = "ID, FIRSTNAME, LASTNAME,PASSWORD"
                    for lines in student_txt_file:
                        user_line = lines.replace("\n", "")
                        user_id = user_line.split(LINE_SEPARATOR)
                        csv_student_dict = {}
                        for csv_line in user_id:
                            user_csv = csv_line.split(PART_SEPARATOR)
                            csv_student_dict[user_csv[0]] = user_csv[1]
                        list_to_str = ','.join([str(elem) for elem in csv_student_dict.values()])
                        csv_final = str(f'{csv_final} \n') + list_to_str
                    file_csv.write(csv_final)
            except FileNotFoundError:
                print("create a file")
