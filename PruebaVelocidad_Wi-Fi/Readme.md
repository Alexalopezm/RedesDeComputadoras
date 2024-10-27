# Script de Prueba Automática de Velocidad de Conexión

Este script automatiza la realización de pruebas de velocidad de conexión a Internet utilizando la herramienta `speedtest-cli`. El script desconecta y conecta la computadora a una red específica, realiza una prueba de velocidad de carga y descarga, guarda los resultados en un archivo de texto, y repite el proceso por 10 iteraciones, con un intervalo de 5 minutos entre cada prueba.

## Requisitos

### Herramientas Necesarias:

- **Python 3** debe estar instalado en tu sistema.
- **Librería `speedtest-cli`** para realizar las pruebas de velocidad.
  - Para instalarla, ejecuta:
  
    ```bash
    pip install speedtest-cli
    ```

- En **Linux**: la herramienta `nmcli` debe estar disponible para gestionar las conexiones de red.
- En **Windows**: se utiliza la herramienta `netsh` para gestionar las conexiones de red inalámbricas.

## Ejecución

### Windows

1. Asegúrate de tener Python 3 instalado. Puedes verificar la instalación ejecutando:

   ```bash
   python --version

2. Instala la librería speedtest-cli si no lo has hecho:
    ```bash
    pip install speedtest-cli

3. Clona o descarga el script en tu máquina.

4. Abre el script y cambia el valor de network_name por el nombre de la red WiFi a la que te quieres conectar (debes usar el nombre exacto).

5. Abre una ventana de símbolo del sistema y navega hasta la carpeta donde está el script.

6. Ejecuta el script:

    ```bash
    python speedtest_automation.py


### Linux
1. Asegúrate de tener Python 3 instalado. Puedes verificar la instalación ejecutando:

    ```bash
    python3 --version

2. Instala la librería speedtest-cli:

    ```bash 
    pip3 install speedtest-cli

3. Verifica que la herramienta `nmcli` esté instalada en tu sistema para gestionar las conexiones de red. En la mayoría de las distribuciones modernas debería estar instalada por defecto. Si no lo está, puedes instalarla con el siguiente comando dependiendo de tu distribución:

    ```bash
    sudo apt-get install network-manager


4. Abre el script y cambia el valor de network_name por el nombre de la red WiFi a la que te quieres conectar.

5. Abre una terminal y navega hasta la carpeta donde está el script.

6. Ejecuta el script:

    ```bash
    python3 speedtest_automation.py


### Resultados

El script se ejecutará automáticamente, realizará las pruebas de velocidad, y guardará los resultados en un archivo de texto llamado Rep_resultados_speedtest.txt en el mismo directorio.