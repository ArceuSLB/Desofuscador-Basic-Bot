import re

def from_hex_string(hex_str):
    try:
        clean = hex_str.replace("\\x", "")
        return bytes.fromhex(clean).decode("utf-8", errors="ignore")
    except Exception as e:
        return f"[ERROR] No se pudo decodificar: {e}"

def detectar_y_decodificar_hex(texto):
    matches = re.findall(r'(?:\\x[0-9a-fA-F]{2})+', texto)
    for match in matches:
        decodificado = from_hex_string(match)
        print(f"\n[+] Cadena original: {match}")
        print(f"[=] Decodificado: {decodificado}")
        print("-" * 30)

# 🧠 Input del usuario
entrada = input("🔐 Ingresa la cadena ofuscada con \\x: ")
detectar_y_decodificar_hex(entrada)
