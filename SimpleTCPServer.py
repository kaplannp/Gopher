'''
A simple TCP "echo" server written in Python.
'''
import sys, socket

class TCPServer:
    def __init__(self, port=50000):
        self.port = port
        self.host = ""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)

        while True:
            clientSock, clientAddr = self.sock.accept()
            print("Connection received from", clientSock.getpeername())
            while True:
                data = clientSock.recv(1024)
                if not data: break
                print ("Received message:", data.decode("ascii"))
                clientSock.sendall(data)
            clientSock.close()

def main():
    if len(sys.argv) > 1:
        try:
            server = TCPServer(int(sys.argv[1]))
        except ValueError as e:
            print("Error in specifying port. Creating server on default port.")
            server = TCPServer()
    else:
        server = TCPServer()

    print("Listening on port", str(server.port))
    server.listen()

main()
