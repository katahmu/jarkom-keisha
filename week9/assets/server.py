from socket import *
import sys
import os
import webbrowser
import time

# Create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Setup server
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Server running on http://localhost:6789")

# Auto open browser (with delay)
time.sleep(1)
webbrowser.open(f"http://localhost:{serverPort}/index.html")
print("Current directory:", os.getcwd())

while True:
    print("\nReady to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        print("Request:\n", message)

        filename = message.split()[1]

        if filename == "/":
            filename = "/index.html"

        # FIXED PATH
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, filename[1:])

        print("Opening file:", filepath)

        with open(filepath, "r") as f:
            outputdata = f.read()

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.sendall(outputdata.encode())

    except Exception as e:
        print("Error:", e)

        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<h1>404 Not Found</h1>".encode())

    finally:
        connectionSocket.close()

serverSocket.close()
sys.exit()