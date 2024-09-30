import socket

# Client details
client_name = "Client of Tharushika Dehipitiarachchi"
server_host = 'localhost'  # Use the server's IP if it's not on localhost
server_port = 12345  # This must match the server's port

def start_client():
    # Ask the user for a number between 1 and 100
    client_number = int(input("Enter an integer between 1 and 100: "))
    
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((server_host, server_port))
    
    # Prepare the message to send to the server
    message = f"{client_name}, {client_number}"
    
    # Send the message to the server
    client_socket.send(message.encode())
    
    # Receive the server's reply
    server_reply = client_socket.recv(1024).decode()
    
    # Print the server's reply
    server_name, server_number, total_sum = server_reply.split(', ')
    print(f"Server Name: {server_name}")
    print(f"Server Number: {server_number}")
    print(f"Sum of numbers: {total_sum}")
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    start_client()
