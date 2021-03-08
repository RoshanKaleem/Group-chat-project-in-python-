import socket

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024



# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
clients=[]
while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]
    clients.append(address)
    myset = set(clients)
    msgFromServer = " "+message.decode()

    bytesToSend = str.encode(msgFromServer)
    # Broadcasting
    for i in myset:
        if (i != address):
            UDPServerSocket.sendto(bytesToSend, i)

    clientIP = "Client IP Address:{}".format(address)

    print(message)

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)