import network
import urequests
import utime
from machine import ADC

# Configuración de Wi-Fi
SSID = "INFINITUM7E34"
PASSWORD = "Yu2Yu2Fd3r"

# Configuración de ThingSpeak
THINGSPEAK_API_KEY = "I15QW8COVA2DECM7"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Sensor de temperatura interno (Canal ADC 4)
sensor_temp = ADC(4)
VOLTAGE_REFERENCE = 3.3  # Voltaje de referencia del ADC
CONVERSION_FACTOR = VOLTAGE_REFERENCE / 65535  # Para convertir la lectura de 16 bits

# Conexión a Wi-Fi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Conectando a Wi-Fi...", end="")
    while not wlan.isconnected():
        print(".", end="")
        utime.sleep(1)
    print("\nConectado:", wlan.ifconfig())

# Lectura de temperatura interna en °C
def leer_temperatura():
    valor_adc = sensor_temp.read_u16()  # Leer ADC
    voltaje = valor_adc * CONVERSION_FACTOR  # Convertir a voltaje
    temperatura = 27 - (voltaje - 0.706) / 0.001721  # Fórmula del RP2040
    return temperatura

# Envío de datos a ThingSpeak
def enviar_a_thingspeak(temperatura):
    try:
        url = f"{THINGSPEAK_URL}?api_key={THINGSPEAK_API_KEY}&field1={temperatura}"
        respuesta = urequests.get(url)
        print("Datos enviados:", respuesta.text)
        respuesta.close()
    except Exception as e:
        print("Error al enviar datos:", e)

# Flujo principal
conectar_wifi()
while True:
    temp = leer_temperatura()
    print(f"Temperatura interna: {temp:.2f}°C")
    enviar_a_thingspeak(temp)
    utime.sleep(180)  # Esperar 180 segundos
