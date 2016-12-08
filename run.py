import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from initialize import joinRoom
from random import randint

s = openSocket()
joinRoom(s)
readbuffer = ""
#TODO: Add leveling,add gambling,announcements,profanity filter
while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break
			user = getUser(line)
			message = getMessage(line)
			print( user + " typed :" + message)
			s.send("text")
			s.send(line.replace("PING", "PONG"))
			if message == "!rand":
				rnum = randint(0,10)
				s.send(str(rnum))
				#sendMessage(s, "randit(0,10)")
				break
				
		for line in temp:
			print(line)
			if "!rand" in line:
				rnum = randint(0,10)
				s.send(str(rnum))
				s.send(line.replace("!rand",str(rnum)))
				break
			user = getUser(line)
			message = getMessage(line)
			print( user + " typed :" + message)
			s.send("text")
			s.send(line.replace("PING", "PONG"))
			if message == "!rand":
				rnum = randint(0,10)
				s.send(str(rnum))
				#sendMessage(s, "randit(0,10)")
				
				break
