from os import getenv
USERNAME = getenv("USERNAME") or "invitado"
LANGUAGE = getenv("LANGUAGE") or "desconocido"

print("Hola, " + USERNAME + "! Tu lenguaje favorito es " + LANGUAGE + ".")