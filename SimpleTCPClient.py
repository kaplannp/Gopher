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

    clientSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSock.connect((server, port))
    print("Connected to server; sending message")

    clientSock.send(message.encode("ascii"))
    print("Sent message; waiting for reply")

    returned = clientSock.recv(1024)
    print("Received reply:", returned.decode("ascii"))

    clientSock.close()

main()
