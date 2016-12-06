import socket
from settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():

	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("Pass " + PASS + "\r\n")
	s.send("NICK " + IDENT + "\r\n")
	s.send("JOIN #" + CHANNEL + "\r\n")
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(message + "\r\n")
	print("Sent: " + messageTemp)