# Socket Programming Project
## Summary
In this short programming project, I wrote a client that uses sockets to communicate with a server that I wrote.  
Here’s what my client and server do:

 

 My client will first accept an integer between 1 and 100 from the keyboard, open a TCP socket to the server and send a message containing (i) a string containing my name (e.g., “Client of Tharushika Dehipitiarachchi) and (ii) the entered integer value and then wait for a sever reply.

 

 My server creates a string containing its name (e.g., “Server of Bob Smith”) and then begin accepting connections from clients.  On receipt of a client message, my server 

 i. prints (display) the client’s name (extracted from the received message) and the server’s name

 ii. Server picks a random integer number between 1 and 100 and finds the sum of its number and client number

 iii. Server send its name string and the server-chosen integer value and the sum to the client

iv. Client prints the server name and numbers.

## How to run the project
    python server.py
Open new terminal and run: 
```
python client.py
```
   Enter integer when prompted

Exit server when done.

 
