Project Overview
================
Goal:
-----

    Client sends a request (filename + word to search) to the server.
    Server processes the request by using search.py to find the word in the file.
    The result (lines containing the word) is sent back to the client.
    The client displays the result to the user.

Breakdown of the Files
---------------------
1. Client (client.py): User Interface and Request Sender
 ====================================================

This is where the user interacts. The client program asks the user for:

    The name of the file to search (e.g., default.txt).
    The word or pattern to search for in the file.

Steps the Client Follows:

    Take Input from the User:
        The client asks the user to provide:
            The filename (e.g., default.txt).
            The word they want to search for in that file (e.g., Cisco).

    Establish a Connection to the Server:
        The client connects to the server using a network socket.
        Socket: Think of a socket as a phone line that connects two computers, allowing them to send and receive data.

    Send Data to the Server:
        The client prepares a message (filename + word) in JSON format (a common data format).
        It sends this data to the server over the socket.

    Receive the Result:
        After the server processes the request, it sends back the result (list of lines containing the word).
        The client receives this result.

    Display the Result:
        The client processes the result and displays it in a readable format to the user.

Example of Client Code Interaction:
-----------------------------------
filename = input("Enter the filename (e.g., default.txt): ")
word = input("Enter the word to search for: ")

# Connect to the server and send the request
client_socket.connect(("127.0.0.1", 9999))
client_socket.send(data.encode('utf-8'))  # Send filename and word

# Receive and display the result from the server
response = client_socket.recv(1024).decode('utf-8')


2. Server (server.py): Request Handler and Coordinator
 ===================================================

The server acts like a middleman. It listens for client connections and handles their requests by using the search.py logic.
Steps the Server Follows:

    Listen for Connections:
        The server is continuously running and listening for client connections on a specific port (9999 in this case).
        Once a client connects, the server accepts the connection and starts handling the request.

    Receive Data from Client:
        The server receives the filename and word that the client wants to search for.

    Use search.py to Process the Request:
        The server imports the Search class from search.py.
        It creates an instance of Search with the provided filename.
        The server then calls the getLines() method from Search to get the lines containing the word.

    Send the Result Back to the Client:
        Once the server has the result (lines containing the word), it sends this data back to the client in JSON format.
        The client will display this data to the user.

Example of Server Code Interaction:
-----------------------------------
# Receive filename and word from the client
data = client_socket.recv(1024).decode('utf-8')
filename = data.get("filename")
word = data.get("word")

# Use the Search class to find the word in the file
search_obj = Search(filename)
result = search_obj.getLines(word)

# Send the result back to the client
client_socket.send(response.encode('utf-8'))

How Server Handles Multiple Clients:

    The server is multithreaded, meaning it can handle multiple client requests at the same time. For each new client connection, a new thread is created to handle that client separately. This ensures that multiple users can search for different words at the same time without the server crashing.


3. Search Logic (search.py): The Core Logic of Searching
 ======================================================

This file contains all the logic for reading the file, cleaning the text, and finding the word the user wants to search for. It’s the core engine that drives the search process.
Steps search.py Follows:

    Read the File:
        When a Search object is created, it reads the file (e.g., default.txt) and stores each line of the file in a list.

    Clean the File (Optional):
        The clean() method removes any special characters (like punctuation) from each line. This makes the search process more accurate.

    Search for the Word:
        The getLines() method takes the word provided by the user and searches for it in the list of lines.
        It uses a case-insensitive search, meaning it will find the word even if it’s written in different cases (e.g., "Cisco" vs "cisco").

    Return the Result:
        The getLines() method returns a list of tuples where each tuple contains:
            The line number.
            The line that contains the word.

Example of Search Code Interaction:
----------------------------------
def getLines(self, word):
    result = [word]  # Start with the word
    for idx, line in enumerate(self.lines, 1):
        if word.lower() in line.lower():  # Case-insensitive search
            result.append((idx, line.strip()))  # Add line number and line
    return result  # Return the list of results

Step-by-Step Process:
======================
1. Client Starts the Process:

    The client asks the user for the filename and word to search for.
    It sends this data to the server.

2. Server Receives and Processes the Request:

    The server receives the data (filename + word).
    It uses the Search class from search.py to search for the word in the specified file.

3. Search Logic is Performed:

    The Search class reads the file and looks for all the lines containing the word.
    The result is prepared as a list of lines with their line numbers.

4. Server Sends the Result Back:

    Once the search is complete, the server converts the result into JSON format.
    It sends the JSON data back to the client.

5. Client Displays the Result:

    The client receives the result and displays it to the user in a readable format (line number + line).


