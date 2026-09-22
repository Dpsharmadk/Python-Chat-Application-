# Python Chat Application

## Overview

This project demonstrates a simple Chat Application using Python Socket Programming. It enables communication between a client and a server over a network connection.

The application establishes a connection between the client and server and allows both sides to exchange messages in real time through the terminal.

---

## Features

- Socket-based communication
- Client-Server architecture
- Two-way message exchange
- Displays sent and received messages
- Separate implementation for client and server
- Simple and easy-to-understand code structure

---

## Project Structure

```
PythonChatApplication-DevPratapSharma/
│
├── client.py
├── server.py
├── layout.py
├── main.py
└── README.md
```

---

## Requirements

- Python 3.x

No external libraries are required as the project uses Python's built-in `socket` module.

---

## How to Run

### Step 1: Start the Server

Open a terminal and run:

```bash
python server.py
```

Output:

```
Server is waiting for connection...
```

---

### Step 2: Start the Client

Open another terminal and run:

```bash
python client.py
```

Output:

```
Connected to server.
```

---

### Step 3: Start Chatting

Client sends a message:

```
Client: Hello
```

Server receives and replies:

```
Client: Hello
Server: Hi there
```

Client receives the response:

```
Server: Hi there
```

Both sides can continue exchanging messages.

---

## Technologies Used

- Python
- Socket Programming

---

## Learning Outcomes

Through this project, I learned:

- Basics of Socket Programming
- Client-Server communication
- Creating network connections using Python
- Sending and receiving data between systems
- Handling real-time communication

---

## Author

**Dev Pratap Sharma**


