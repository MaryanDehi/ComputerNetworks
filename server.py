import socket
import random

# Server details
server_name = "Server of Tharushika Dehipitiarachchi"
server_host = 'localhost'  # You can use '127.0.0.1' or the actual server IP
server_port = 12345  # Choose any available port

def start_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind((server_host, server_port))
    
    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"{server_name} is listening on {server_host}:{server_port}")
    
    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # Receive the message from the client
        client_message = client_socket.recv(1024).decode()
        print(f"Message from client: {client_message}")
        
        # Extract client name and client number from the message
        client_name, client_number = client_message.split(', ')
        client_number = int(client_number)
        
        # Print server and client details
        print(f"Client Name: {client_name}")
        print(f"Server Name: {server_name}")
        
        # Generate a random integer between 1 and 100
        server_number = random.randint(1, 100)
        
        # Calculate the sum of the client's number and the server's number
        total_sum = client_number + server_number
        
        # Prepare the reply message
        reply_message = f"{server_name}, {server_number}, {total_sum}"
        
        # Send the reply to the client
        client_socket.send(reply_message.encode())
        
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
