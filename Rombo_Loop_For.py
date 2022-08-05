# Desafio Rombo Loop for @psre423p45

espacio = "      "
asterisco = "*"

for i in range(0, 5):
	print(espacio, asterisco)
	asterisco += "**"
	espacio = espacio[:-1]
	
for i in range(0, 1):
	asterisco = list(asterisco)
	asterisco.pop(); asterisco.pop()
	asterisco.pop(); asterisco.pop()
	asterisco = "".join(asterisco)
	espacio += "  "
	print(espacio, asterisco)
	
for i in range(0,3):
	asterisco = list(asterisco)
	asterisco.pop(); asterisco.pop()
	asterisco = "".join(asterisco)
	espacio += " "
	print(espacio, asterisco)
