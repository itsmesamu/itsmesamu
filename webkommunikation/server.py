import socket, threading

addresse_zu_name = dict()

def handle_client(client_socket, client_address):
    try:
        client_socket.send("Hallo bitte gib deinen Namen ein".encode("utf-8"))
        request =client_socket.recv(1024)
        request = request.decode("utf-8")
        addresse_zu_name[client_address] = request
        msg = "Hallo" + str(addresse_zu_name[client_address])
        client_socket.send(msg.encode("utf-8"))
        while True:
            request = client_socket.recv(1024) # 1024 Bytes empfangen
            request = request.decode("utf-8") # Bytes zu String konvertieren

            print(request)
            
            if request == "ende":
                break
        client_socket.close()
    except Exception as e:
         print("Feheler mit Client")
         print(e)
    finally:
         client_socket.close()

def aktion():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Ein Socket, der mittels IPv4 ind TCP kommuniziert

    server_ip = "127.0.0.1"
    port = 8000

    server.bind((server_ip, port))

    server.listen()

    print("server bereit")

    while True:
       client_socket, client_address = server.accept()
       print("neuen client akzeptiert.")
       thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
       thread.start()

aktion()