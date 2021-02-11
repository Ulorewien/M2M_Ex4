"""
M2M Lab Exercise 4
ROHAN MADHAV SHINGRE (MSM19B012)
"""
import socket, threading, base64

PORT = 10007

SERVER = socket.gethostbyname(socket.gethostname()) # Automatically gets the Local IP Address
server_address = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)

# Handles Individual Clients
def handle_client(connection,address):
    print(f"Client with address {address} connected.")
    while True:
        message = connection.recv(1024)
        if not message:
            break
        decoded_bytes = base64.b64decode(message)
        data = str(decoded_bytes, "utf-8")
        print(f"From Address:{address}, Message:{data}")
        connection.send(f"Received {data[3:]}!".encode('utf-8'))
    
    print(f"Client {address} is Disconnected!")
    connection.close() # Closes the connection when no message is sent from Particular Client


# Starts the Server
def run_server():
    server.listen()
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client,args=(connection, address)) # Creates a Thread for a new client
        thread.start()
        print(f"Total number of connected clients: {threading.activeCount()-1}") # Subtracts the initial Listening Thread

if __name__ == '__main__':
    try:
        print("Accepting requests...")
        run_server()
    except:
        print("\nClosing Server ")
    finally:
        server.close()