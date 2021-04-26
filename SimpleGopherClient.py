'''
A simple "echo" client written in Python.
'''
import sys, socket

def usage():
    print("Usage:  python3 SimpleTCPClient <server IP> <port number> <message>")
    sys.exit()

def main():
    if len(sys.argv) < 4:
        usage()

    try:
        server = sys.argv[1]
        port = int(sys.argv[2])
        message = sys.argv[3]
    except ValueError as e:
        usage()

    message += "\r\n"

    clientSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSock.connect((server, port))
    print("Connected to server; sending message")

    clientSock.send(message.encode("ascii"))
    print("Sent message; waiting for reply")

    while True:
        data = clientSock.recv(1024)
        if not data: break
        print(data.decode("ascii"))

    clientSock.close()

main()
