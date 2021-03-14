import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((socket.gethostname(), 0))

server.listen(5)

print("{}:{} dinleniyor...".format(*server.getsockname()))

while True:
    try:
        client, address = server.accept()
        print("{}:{} baglandi".format(*address))
        print(client.recv(4096))
        client.send("mrb")
        client.close()
    except KeyboardInterrupt:
        break

server.close()