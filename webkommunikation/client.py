import socket

def aktion():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "192.168.178.57"
    server_port = 8000

    client.connect((server_ip, server_port))

    while True:
        nachricht = input("Nachricht: ")

        client.send(nachricht.encode("utf-8")[:1024])

        if nachricht =="ende":
            break
    
    client.close()
aktion()