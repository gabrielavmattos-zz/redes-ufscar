from socket import *

import subprocess
import string

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

a = "|"
b = ";"
c = ">"
d = "<"
e = "1 "
f = "2 "
g = "3 "
h = "4 "

while 1:
	connectionSocket, addr = serverSocket.accept()
     
	sentence = connectionSocket.recv(1024)
	sentence = sentence.replace("REQUEST ","")
	if a in sentence:
		sentence = sentence.replace(a,"")
	if b in sentence:
		sentence = sentence.replace(b,"")
	if c in sentence:
		sentence = sentence.replace(c,"")
	if d in sentence:
		sentence = sentence.replace(d,"")
	if e in sentence:
		sentence = sentence.replace(e,"ps -")
		numero = e
	if f in sentence:
		sentence = sentence.replace(f,"ds -")
		numero = f
	if g in sentence:
		sentence = sentence.replace(g,"finger -")
		numero = g
	if h in sentence:
		sentence = sentence.replace(h,"uptime -")
		numero = h

	comando = subprocess.Popen(sentence, stdout=subprocess.PIPE, shell=True)
	(resposta, err) = comando.communicate()
	resposta = "RESPONSE " + numero + resposta
	connectionSocket.send(resposta)
	connectionSocket.close()
