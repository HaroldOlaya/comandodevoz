#include <WiFi.h>
const char* ssid = "Ospina_Beltran";
const char* password = "D4NN418_D4V1D13_0SC4R85";
int pin=12;
WiFiServer server(80); // Crear un servidor en el puerto 80

void setup() {
  pinMode(pin,OUTPUT);
  Serial.begin(115200);
  delay(10);

  // Conectar a la red Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando a la red Wi-Fi...");
  }

  Serial.println("Conexión Wi-Fi exitosa");
  Serial.println("Dirección IP del ESP8266: " + WiFi.localIP().toString());

  // Inicializar el servidor
  server.begin();
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("Nuevo cliente conectado");

    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (c =='a'){
          digitalWrite(pin,HIGH);

        }
        if (c =='b'){
          digitalWrite(pin,LOW);
        }
        Serial.write(c); // Mostrar datos recibidos en el monitor serie

        // Realizar acciones adicionales según los datos recibidos si es necesario
      }
    }

  }
}



