import socket
import json

def start_client(filename, word):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))

    data = json.dumps({"filename": filename, "word": word})
    client.send(data.encode('utf-8'))

    response = client.recv(1024).decode('utf-8')
    result = json.loads(response)

    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Search results for '{word}':")
        for line in result[1:]:
            print(f"Line {line[0]}: {line[1]}")

    client.close()

if __name__ == "__main__":
    filename = input("Enter filename: ")
    word = input("Enter word to search: ")
    start_client(filename, word)
