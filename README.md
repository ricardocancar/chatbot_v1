# Módulo 3: Integración Telegram.
### **infoecoVLC**
### **Asistente virtual para información económica municipal**

Modulo responsable de gestionar todos los mensajes que se reciben de Telegram. Se comunica con el módulo 3 (agente inteligente) y el módulo 2 (servició web) para obtener la respuesta para el usuario. Si quieres más información entra al proyecto **[infoecoVLC: Asistente virtual para información económica municipal](https://github.com/areahackerscivics/infoecoVLC)**

## Descripción

![Diseño de comunicacion](https://github.com/ricardocancar/chatbot_v1/blob/master/imagen/infoecoVLC.png)


## Guía de uso

### Lenguaje de programación
Python 3.6.3

### Librerías empleadas
Las librerías actualizadas siempre estarán actualizadas en el documento [**requirements.txt**](./requirements.txt) consultar en caso de errores.

    pymongo = 3.6.0
    python-telegram-bot = 9.0.0
    requests = 2.18.4


### Instalación
El modulo consta con todos los archivos necesarios para ser ejecutado en Docker y la guía de instalación contara como que se tiene instalado Docker. De no ser el caso podéis instalarlo siguiendo la [guía de instalación para Ubuntu](./instalacionDocker.md).

**Pasos**
1. Descargar desde github el proyecto.

        sudo git clone https://github.com/areahackerscivics/infoecoVLC_M3_Integracion_Telegram

2. Entramos en la carpeta descargada que contiene el proyecto.

        cd infoecoVLC_M3_Integracion_Telegram

3. Cambiamos el  nombre de variables_ejemplo.py por **variables.py**.

        sudo mv variables_ejemplo.py variables.py

4. Sustituir las “XXX” de dentro de **variables.py** por las variables personales.

        sudo nano variables.py

4. Creamos la imagen con nombre "mTelegram".

        sudo docker build . -t mtelegram

5. Ejecutamos el contenedor en segundo plano

        sudo docker run -d --name modulTelegram mtelegram



## Colaboración
Se puede colaborar:
- Difundiendo.
- Ampliando o modificando el proyecto.

## Términos de uso

El contenido de este repositorio está sujeto a la licencia [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

![](https://www.gnu.org/graphics/gplv3-127x51.png)

