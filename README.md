# Desofuscador-Basic-Bot
Herramienta básica para desofuscar código JavaScript con hex y base64, orientada a análisis forense
# 🔍 Desofuscador Bot

Pequeño script educativo en Python que detecta y decodifica cadenas ofuscadas en:
- Formato `\xNN` (hexadecimal)
- (Próximamente) Base64, Unicode, y más

## 📂 Estructura

- `desofuscador.py`: versión base que decodifica hex (`\xNN`)
- `samples/pruebas.txt`: ejemplos de cadenas maliciosas
- `desofuscador_base64.py`: para desofuscar Base64 (en desarrollo)

## 🧪 Ejemplo

```python
entrada = r'eval("\\x61\\x6c\\x65\\x72\\x74(\\x22Hola\\x22)")'

