import socket
import threading
import argparse
import random
import sys

# creating a parser so that new clients can approve how to run.
# implementing -h in the line or -help will show a discription about how to run.
argument = argparse.ArgumentParser(description='To connect to the server type inn: python3 '
                                               'klient.py localhost 8080 + bot name or client name ')
argument.add_argument('ip', type=str, help='ip- address of the server. Use localhost')
argument.add_argument('port', type=int, help='The port to the server to establish connections')
argument.add_argument('data', type=str, help='The data of the client. Connect as a host or a bot(june, may, '
                                             'july or august)')

a = argument.parse_args()
ip = a.ip
port = a.port
data = a.data

#  connecting to a socket by ip and Port
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect((ip, port))  # initiate TCP server connection by IP - address and port

#  creating a list for the four bots
bots = ["june", "may", "july", "august"]


# creating a function that responses to the words defined in 'tvshow' or 'sport' list.
# if the bot can find the word it responses with a random choise of responses from the 'reactionTo....'(A-D) list
# if the bot cant find the word it will return with a pre automated answer
def may(action):
    if action in sports:
        reactionsToSportA = [
            # RESPONSE ______________________________________
            "{} replays: Did you say {}? I would love to try that out!".format(data, action),
            "{} replays: I think {} sounds fun!".format(data, action),
            "{} replays: Finally, i hoped you would say {}, lets do it!".format(data, action),
            "{} replays: No. Dont' like that sport".format(data, action)
        ]
        return random.choice(reactionsToSportA)

    elif action in tvShows:
        reactionsToShowsA = [
            # RESPONSE ______________________________________
            "{} replays: {}? That TV show rocks!".format(data, action),
            "{} replays: Not my favourite show. But lets try it out".format(data, action),
            "{} replays: I LOVE THAT SHOW. I would rate it a 6 out of 6 stars".format(data, action),
            "{} replays: {} is a show i always think about but never watch. Such a good idea".format(data, action)
        ]
        return random.choice(reactionsToShowsA)

    else:
        # RESPONSE IF IT'S NOT A WORD FROM THE LIST_________________
        return "{} replays: hi. Didnt catch what you say. What is your favourite sport?".format(data)


def june(action):
    if action in sports:
        if action in sports:
            reactionsToSportB = [
                # RESPONSE ______________________________________
                "{} replays: {} sounds something really fun.".format(data, action),
                "{} replays: {} is not my kind of activity. Something else?".format(data, action),
                "{} replays: Sport is not my kind of activity. What about tv shows to watch?".format(data, action),
                "{} replays: {} is the sport i used to practice as young".format(data, action)

            ]
        return random.choice(reactionsToSportB)

    elif action in tvShows:
        reactionsToShowB = [
            # RESPONSE ______________________________________
            "{} replays: Never heard about that show... ".format(data, action),
            "{} replays: I've already binged that show. Some new show maybe?".format(data, action),
            "{} replays: {} is a wonderful show. Lets watch".format(data, action),
            "{} replays: wow! We really like the same shows".format(data, action)
        ]
        return random.choice(reactionsToShowB)

    else:
        # RESPONSE IF IT'S NOT A WORD FROM THE LIST_________________
        return "{} replays: Hey, what is your favourite TV- show?".format(data)


def july(action):
    if action in sports:
        reactionsToSportC = [
            # RESPONSE ______________________________________
            "{} replays: {} really sounds like a heavy sport. Something easier for me?".format(data, action),
            "{} replays: FUN! I tried it out last week. Ofcourse i would do that".format(data, action),
            "{} replays: Nope. I'm tired today. Do you have a good show to watch?".format(data, action),
            "{} replays: I would rater try something else...".format(data, action)

        ]
        return random.choice(reactionsToSportC)

    elif action in tvShows:
        reactionsToShowC = [
            # RESPONSE ______________________________________
            "{} replays: Have {} been launched? I checked Netflix yesterday...".format(data, action),
            "{} replays: Lovely. Like {} so much ".format(data, action),
            "{} replays: No. That show is not something for me".format(data, action),
            "{} replays: I give that show 4 out of 6 stars!".format(data, action),
            "{} replays: I really like that show. But what about after life?".format(data, action)
        ]
        return random.choice(reactionsToShowC)

    else:
        # RESPONSE IF IT'S NOT A WORD FROM THE LIST_________________
        return "{} replays: Can you say that again? Or maybe we can talk about sport?".format(data)


def august(action):
    if action in sports:
        reactionsToSportD = [
            # RESPONSE ______________________________________
            "{} replays: {} is that even a sport? I'm not invested in the sports world".format(data, action),
            "{} replays: My sister loves that sport. Always wanted to try it out".format(data, action),
            "{} replays: Not today... {} is too hard for a person like me".format(data, action),
            "{} replays: Not quite sure about that...".format(data, action)
        ]
        return random.choice(reactionsToSportD)

    elif action in tvShows:
        reactionsToShowD = [
            # RESPONSE ______________________________________
            "{} replays: Is it good? have heard lots of different meanings about it {}".format(data, action),
            "{} replays: I cant find it anywhere. But i would like to watch {}".format(data, action),
            "{} replays: My all time favourite show".format(data, action),
            "{} replays: I would give that show 1 out of 6 stars. Sooo boring...".format(data, action)
        ]
        return random.choice(reactionsToShowD)

    else:
        # RESPONSE IF IT'S NOT A WORD FROM THE LIST_________________
        return "{} replays: I would love to hear about your favourite sport. ".format(data)


# lists of actions by sports or tv shows________________________________________________
sports = ["handball", "football", "tennis", "padle", "squash", "wakeboarding", "hockey", "swimming", "hiking", "polo",
          "fetching", "cross-country skiing", "volleyball", "curling", "bandy", "basket"]
tvShows = ["game of thrones", "yellowstone", "prett little liars", "riverdale", "designated survivor", "friends",
           "one three hill", "gossip girl", "formula 1", "kompani lauritsen", "rested development", "breaking bad",
           "prison break", "brooklyn 99", "suits", "ozark"]


# handles the messages received from other clients.
def clientInput():
    while True:
        # takes inn message from client, decodes it from bytes to utf-8 format (æ,ø,å)
        # saves the message in the variable receive
        receive = sk.recv(1024).decode('utf-8')

        # if the message is equal to the data? in server.py we will send the client name to sk. in utf-8 format
        if receive == "data?":
            sk.send(data.encode('utf-8'))

        else:  # if the receive isn't equal to data goes it into this method
            # if ":" is in the message. The message divides with ":" as separator.
            # the split method returns a list of the elements in the message divided by :
            if ":" in receive:

                receivesplit = receive.split(": ")

                if receivesplit[0] not in bots:
                    j = ""
                    i = 0
                    # as long i are shorter than the length of the list of tvshows will the while loop run
                    while i < len(tvShows):
                        # if the index in list tvshows (starting on 0) also is in the message from the client
                        # receive.lower = makes every letter small. So it works with key sensitivity
                        if tvShows[i] in receive.lower():
                            # the variable sets to j, which was an empty string to the index value in tvshow list
                            j = tvShows[i]
                        # same as above but compared to the sport list
                        if sports[i] in receive.lower():
                            j = sports[i]
                        # plus i with 1 for each time the loop run
                        i += 1

                    sendBot = ""
                    # if data converted to small letters is equal to "june"
                    if data.lower() == "june":
                        # calling the method june and sends in "j" who gets set to a sport or tvshow above
                        # method june returns a random sentence from the june-method that implements in sendBot
                        sendBot = june(j)
                        # if the name with lower case equals may, calls the may-method with j as argument.
                        # Method returns a sentence
                    elif data.lower() == "may":
                        sendBot = may(j)
                        # if the name with lower case equals july, calls the may-method with j as argument.
                        # Method returns a sentence
                    elif data.lower() == "july":
                        sendBot = july(j)
                        # if the name with lower case equals august, calls the may-method with j as argument.
                        # Method returns a sentence
                    elif data.lower() == "august":
                        sendBot = august(j)
                        # receive prints to console explicit to check
                    print(receive)
                    # calling th clientSend method with sendBot as argument. So the message gets printed
                    # to socket when called
                    clientSend(sendBot)
                # if receiveSplit[0] not in bots : doesn't run, else parameter will run:
                else:
                    # prints receive to see if there exists something
                    print(receive)
            # if the method : if ":" in receive doesnt run. Prints a message to see it exists.
            else:
                print(receive)


# sending the data over the socket
def clientSend(receive):
    print(receive)
    sk.send(receive.encode('utf-8'))  # encode = sending. Sk. is calling for the socket.


# checking for error messages and the format of the client messages. If correct the message will send over the socket.
def clientMessager():
    while True:
        try:
            receive = f'{data}: {input()}'  # the format for the message, the input is the text
            split = receive.split(": ")
            if split[1].isspace() or split[1] == "":  # checking if there is a writing in the message
                print(
                    "Can't send an empty string. Please write something!")  # responses within own terminal if there is
                #  an empty string send. Gets an error. And the message will fail sending.
                continue
            else:
                sk.send(receive.encode('utf-8'))  # sending the message if the parameters of the string is correct over
                # the socket. And only sending the message to the others in the chatroom.
        except:
            print("\nYou left. And are now out of the chatroom. \n")
            sys.exit()
            break


receive_t = threading.Thread(target=clientInput)
receive_t.start()  # starting the thread clientInput

if data not in bots:  # if the name from the client connection is not in defined bot names, there will be a
    # connection as a regular client with normal interaction possibilities
    send_t = threading.Thread(target=clientMessager)
    send_t.start()  # starting simultaneously the method clientMessager
