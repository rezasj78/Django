import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("localhost", 10000))
socket.listen(5)
while True:
    conn, add = socket.accept()
    # msg = conn.recv(1024).decode("utf-8")
    # print(msg)
    file = open("received_file.py", "w")
    while True:
        print("receiving data...")
        l = conn.recv(5).decode("utf-8")
        print(l)
        if not l:
            break
        file.write(l)
    file.close()
    print("recieved successfully!")
