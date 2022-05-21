# client.py
import socket
import sys

def main():
    # creating the socket
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # just connecting
    #sck.connect(("localhost", 7456))
    sck.connect(("10.2.5.3", 7456))

    print('Type exit to quit')

    while(1):

        print("Enter Message to Send")

        data = input('>')
        #sck.sendall(b"Hola server, are you bored?")
        #sck.sendall(data.encode())
        sck.sendall(data.encode())
        #sck.send(data.encode())

        if 'exit' in data:
            # I don't care about your response server, I'm closing
            sck.close()
            break
        print("Sending data...")

if __name__ == "__main__":
    main()
