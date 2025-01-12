# Project: Client-Server Communication with Sockets

This project demonstrates a simple client-server communication using Python sockets. The server and client exchange messages and perform basic operations based on the inputs provided.

## Project Overview

- **Server**: Listens for incoming connections, processes client messages, and sends a response.
  - Generates a random integer between 1 and 100.
  - Calculates the sum of its random number and the number sent by the client.
  - Sends the result and its details back to the client.
  
- **Client**: Sends a name and an integer to the server, receives a response, and displays the result.
  - Accepts an integer between 1 and 100 from the user.
  - Connects to the server and sends a message containing the client's name and the integer.
  - Displays the server's name, random number, and the calculated sum received from the server.

## How to Run the Project

1. **Start the Server**:
   - Open a terminal and run:
     ```bash
     python server.py
     ```
   - The server will start listening for incoming connections on `localhost:12345`.

2. **Run the Client**:
   - Open a new terminal and run:
     ```bash
     python client.py
     ```
   - Enter an integer between 1 and 100 when prompted.

3. **Interaction**:
   - The client sends the entered integer to the server.
   - The server generates a random integer, calculates the sum, and sends the details back.
   - The client displays the server's name, random number, and the sum.

4. **Stop the Server**:
   - Close the server terminal when you are done.

## Notes

- Ensure that both `server.py` and `client.py` are in the same directory or accessible from your working directory.
- The server and client communicate over `localhost` and port `12345` by default. Update these settings in the scripts if needed.
