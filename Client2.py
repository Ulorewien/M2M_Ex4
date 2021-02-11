"""
M2M Lab Exercise 4
ROHAN MADHAV SHINGRE (MSM19B012)
"""
import socket, time, random, base64

PORT = 10007

SERVER = socket.gethostbyname(socket.gethostname()) # Automatically gets the Local IP Address
server_address = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

# Sends the request to Server
def send(data):
    print(f"Sending {data} to the server")
    message = base64.b64encode(data.encode("utf-8"))
    client.send(message)
    print(client.recv(2048).decode('utf-8')) # Prints the Data received from Server


if __name__ == '__main__':
    try:
        while True:
            A = random.randint(70, 1000)
            B = random.randint(70, 1000)
            data = f"C2:(A, B)=({A}, {B})"
            send(data)
            time.sleep(2)
    except:
        print("\nRequests are stopped")
    finally:
        client.close()