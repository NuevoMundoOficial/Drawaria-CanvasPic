from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
from PIL import Image
from io import BytesIO

# Descargar y procesar la imagen
image_url = 'https://i.postimg.cc/44DLPR1F/1.png'
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img = img.convert('RGBA')
img_data = img.load()
width, height = img.size

pixel_data = []
for y in range(height):
    row = []
    for x in range(width):
        r, g, b, a = img_data[x, y]
        row.append(f'rgba({r}, {g}, {b}, {a/255})')
    pixel_data.append(row)

# Configuración del WebDriver
chrome_driver_path = r'C:\SeleniumDrivers\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# URL de la página
url = 'https://drawaria.online/room/edb6b1b8-ffa6-4997-881c-4a79007df2aa.3'
driver.get(url)

# Esperar a que la página cargue completamente
time.sleep(5)

# Generar el script de JavaScript para dibujar la imagen en el canvas
js_code = f"""
var canvas = document.querySelector('canvas');
var ctx = canvas.getContext('2d');
var imgData = {pixel_data};
var canvasData = [];

for (var y = 0; y < {height}; y++) {{
    for (var x = 0; x < {width}; x++) {{
        ctx.fillStyle = imgData[y][x];
        ctx.fillRect(x, y, 1, 1);
        canvasData.push({{x: x, y: y, color: imgData[y][x]}});
    }}
}}

// Función para enviar datos a través de WebSockets
function sendCanvasData(data) {{
    const socket = new WebSocket('wss://sv1.drawaria.online/socket.io/?sid1=undefined&hostname=drawaria.online&EIO=3&transport=websocket');
    socket.addEventListener('open', function (event) {{
        socket.send(JSON.stringify(data));
    }});
}}

// Función para recibir datos a través de WebSockets
function receiveCanvasData() {{
    const socket = new WebSocket('wss://sv1.drawaria.online/socket.io/?sid1=undefined&hostname=drawaria.online&EIO=3&transport=websocket');
    socket.addEventListener('message', function (event) {{
        const data = JSON.parse(event.data);
        // Procesar los datos recibidos y dibujar en el canvas
        drawReceivedData(data);
    }});
}}

// Función para dibujar los datos recibidos en el canvas
function drawReceivedData(data) {{
    var ctx = canvas.getContext('2d');
    data.forEach(function(pixel) {{
        ctx.fillStyle = pixel.color;
        ctx.fillRect(pixel.x, pixel.y, 1, 1);
    }});
}}

// Llamar a las funciones para enviar y recibir datos
sendCanvasData(canvasData);
receiveCanvasData();
"""

# Ejecutar el script de JavaScript
driver.execute_script(js_code)

# Mantener el navegador abierto para ver el resultado
time.sleep(10)

# Cerrar el navegador
driver.quit()
