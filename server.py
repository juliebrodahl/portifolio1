import socket
import threading
import argparse

list = []  # creating a list
dataList = []  # creating a list to implement the client names

# providing a parser to check argument and as a help line for how to get the server running.
argument = argparse.ArgumentParser(
    description='Start the chat server and listen for incoming connections. Example: server.py 8080')
argument.add_argument('port', type=int, help='The port number the server is running on. Example: 8080')
a = argument.parse_args()
port = a.port

#  creating a socket at server side using TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', port))  # binding the socket with the server and port number
print(f'Socket binded to port {port}')  # defining which port the sever is running on.
s.listen()  # listen for connections - no strings for how many allowed connections
print(f'STATUS: Socket is listening')  # server status
print('Looking for clients ... \n')  # server status while looking for connections


# creating a function to send out messages within the server. From clients to other connected clients.
def broadcast(replay, klient):
    for m in list:
        # sends replay to all other bots that are in the chat, but not the one that send it
        if m is not klient:
            m.send(replay)


# chatting inbetween the list(host and bots) and functions to handle if clients are terminating chatroom or leaving
def chatWKlient(klient):
    while True:
        try:
            replay = klient.recv(1024)
            command = replay.decode().split(": ")

            if command[1] == "CLOSE":  # creating a way for a host to close down the connecting clients.
                print("Discard connecting clients")  # print out a message to the client
                for d in list:  # checking all the connected clients in the list
                    d.close()  # closing all the connections
                print("Status update: No connected clients. Socket not listening.")  # print to the other -
                # connected clients
                exit()

            else:
                broadcast(replay, klient)  # send to all bots

        except:
            # if a client closes down its own program by exit the terminal. This is the only one that are leaving the -
            # chat room. And the other users will be informed about the leaving
            index = list.index(klient)
            list.remove(klient)  # removing the clients from the list
            klient.close()
            data = dataList[index]
            broadcast(f'{data} is no longer here!'.encode('utf-8'), klient)
            print(f'{data} is no longer in the chat room')  # printing out who left the chat
            dataList.remove(data)  # removing the data from the datalist
            break


# set server status and connect incoming list to the server(chat room)
def connectionsToServer():
    while True:
        klient, address = s.accept()  # waiting till a client accepts connection
        klient.send('data?'.encode('utf-8'))
        data = klient.recv(1024)
        dataList.append(data)  # implementing the data of the client in the data list
        list.append(klient)
        print(f' {data} is now connected with address {str(address)}')  # printing the connections, to make a list

        broadcast(f'{data} is now in the chat'.encode('utf-8'),
                  klient)  # displaying client connection address for every member
        klient.send('Connection up and running! You can now chat with the others'.encode('utf-8'))

        t = threading.Thread(target=chatWKlient, args=(klient,))
        t.start()


connectionsToServer()
