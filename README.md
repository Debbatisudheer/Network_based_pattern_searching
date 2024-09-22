# cisco_project
Overview
========
•	client.py is the program where the user interacts. It sends a request (filename + search word) to the server.py.
•	server.py is always running and waiting for requests from client.py. When it gets a request, it uses search.py to find the requested word in the specified file.
•	search.py contains the logic for finding the word (or pattern) in the file. It processes the file and gives the results back to server.py.
•	The server.py sends the results back to client.py, which displays the results to the user.

Step-by-Step Breakdown
=====================
1.	Client (client.py) Sends Request:
o	The user starts the client and enters:
	The filename (e.g., default.txt).
	The word to search (e.g., Cisco).
o	The client sends this data (filename + word) over the network to the server.
2.	Server (server.py) Receives Request:
o	The server listens for incoming requests from the client.
o	When the server gets a request from the client, it extracts:
	The filename (default.txt).
	The word to search (Cisco).
o	Now, the server needs to search the word in the file. It uses the Search class from search.py to do this.
3.	Search Logic (search.py) Performs the Search:
o	The server creates a Search object (from search.py), giving it the filename.
o	The Search class reads the file and removes special characters (cleans the file).
o	It then finds all lines that contain the word (e.g., "Cisco") and stores the results in a list.
4.	Server Sends Results Back to Client:
o	Once the server gets the search results from search.py, it converts them into a format the client can understand (JSON format).
o	The server sends the search results back to the client over the network.
5.	Client Displays Results:
o	The client receives the search results from the server.
o	The results (like lines where the word "Cisco" was found) are shown to the user in the terminal.
Example Interaction
•	Client (client.py): Sends:
{
  "filename": "default.txt",
  "word": "Cisco"
}
•  Server (server.py):
•	Receives this request.
•	Uses search.py to find the word "Cisco" in default.txt.
•  search.py:
•	Processes the file and finds:
["Cisco", (1, "Cisco Systems, Inc. is a global leader in networking technology."), (4, "The word Cisco is synonymous with innovation in network technology.")]
•	Server (server.py): Sends these results back to the client.
•	Client (client.py): Displays the results to the user.
In short:
•	client.py → sends request to server.py.
•	server.py → uses search.py to find the word and send results back to client.py.
•	client.py → displays results to the user.

