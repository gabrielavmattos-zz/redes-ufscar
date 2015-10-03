#!/usr/bin/python

import cgi, cgitb

# Importando o código do backend aqui no webServer
import backend.py
# Criando uma instancia de FieldStorage
form = cgi.FieldStorage()

# Cabeçalho que informa o browser para renderizar como HTML
print "Content-type:text/html\r\n\r\n"

#loop para percorrer as máquinas:
for i in range(3):

	# Variavel mensagem vai armazenar as informações do cabeçalho do protocolo da camada de aplicação	
	# Definindo quais foram os comandos selecionados pelo usuário
	# Lembrando: 
	# { 1 - ps; 2 - df; 3 - finger; 3 - uptime}

	if form.getvalue('selPsM'+str(i+1)):
		mensagem = "REQUEST " + " 1 " + form.getvalue('ArgPsM'+str(i+1))
	if form.getvalue('selDfM'+str(i+1)):
		mensagem = "REQUEST " + " 2 " + form.getvalue('ArgDfM'+str(i+1))
	if form.getvalue('selFingerM'+str(i+1)):
		mensagem = "REQUEST " + " 3 " + form.getvalue('ArgFingerM'+str(i+1))
	if form.getvalue('selUpTimeM'+str(i+1)):
		mensagem = "REQUEST " + " 4 " + form.getvalue('ArgUpTimeM'+str(i+1))