# IoT-parcial-1
Entrega de proyecto parcial 1
El objetivo de esta evaluación es desarrollar un sistema de monitoreo de temperatura basado en Internet de las Cosas (IoT) utilizando una Raspberry Pi Pico W y un sensor LM35. Se busca capturar, procesar y visualizar datos en la nube mediante ThingSpeak. Además, se empleará MathWorks en la plataforma para realizar análisis de datos en tiempo real, incluyendo el cálculo del promedio de temperatura y la generación de alertas cuando los valores superen un umbral predefinido.
El estudiante deberá diseñar un sistema IoT para la medición y monitoreo de temperatura en la nube utilizando los siguientes componentes y herramientas:
•	Raspberry Pi Pico W
•	Sensor de temperatura LM35
•	ThingSpeak (almacenamiento y visualización de datos)
•	MathWorks (análisis y procesamiento de datos en ThingSpeak)
En esta ocasión no se utilizó el sensor LM35 pero si se usó el sensor RP2040 que es el que mide la temperatura del procesador del rasperry pi pico w.
Primero se configuró el rapsberry correctamente en la computadora con el programa de Thonny, para verificar que el microcontrolador funcionará se utilizó un código para encender el led.
Luego se le puso el código correspondiente para verificar si los datos que mandaba eran correctos.
Por otra parte, se creó un canal en la plataforma de Thingspeak para poder visualizar los datos mediante una gráfica, al código se le puso el id del canal creado para que este pudiera recibir los datos y así se fuera formando la gráfica.
Después se hicieron las partes de alerta de temperatura y el promedio de temperatura.
