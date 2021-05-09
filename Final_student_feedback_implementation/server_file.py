"""import for the server side"""
import socket
import final_assignment_module as new


HOST = "127.0.0.1"
PORT = 65431
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.bind((HOST, PORT))
SOCKET.listen(4)
ACTION = new.FileFormat()
print("Waiting for user input........ ")
while True:

    CONN, ADDR = SOCKET.accept()
    print("Connecting to: ", ADDR)
    DATA = CONN.recv(1024)
    DATA = DATA.decode().lower()
    FINAL_NAME = str(f'final_students.{DATA}')

    if DATA == "xml":
        ACTION.convert_format_xml()
    elif DATA == "json":
        ACTION.convert_format_json(FINAL_NAME)
    elif DATA == "csv":
        ACTION.convert_csv()
    else:
        print("No selected file format")
        break


CONN.close()
