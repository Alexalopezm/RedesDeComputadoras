import os
import time
import subprocess
import speedtest

# ---- Código para Windows ----
# Función para desconectar y conectar a la red en Windows
def reconnect_network_windows(network_name):
    print(f"Desconectando de la red actual...")
    os.system("netsh wlan disconnect")  # Desconectar de la red actual (Windows)
    time.sleep(5)  # Esperar 5 segundos
    
    print(f"Conectando a la red {network_name}...")
    os.system(f'netsh wlan connect name="{network_name}"')  # Conectar a la red especificada (Windows)
    time.sleep(10)  # Esperar a que la conexión sea estable
# ---- Fin del Código para Windows ----

# # ---- Código para Linux ----
# # Función para desconectar y conectar a la red en Linux
# def reconnect_network_linux(network_name):
#     print(f"Desconectando de la red actual...")
#     os.system("nmcli device disconnect wlan0")  # Desconectar de la red actual (Linux)
#     time.sleep(5)  # Esperar 5 segundos

#     print(f"Conectando a la red {network_name}...")
#     os.system(f"nmcli device wifi connect '{network_name}'")  # Conectar a la red especificada (Linux)
#     time.sleep(10)  # Esperar a que la conexión sea estable
# # ---- Fin del Código para Linux ----

# Función para realizar la prueba de velocidad
def run_speedtest():
    print("Ejecutando prueba de velocidad...")
    st = speedtest.Speedtest()
    st.download()  # Prueba de descarga
    st.upload()    # Prueba de carga
    results = st.results.dict()
    
    download_speed = results['download'] / 1_000_000  # Convertir a Mbps
    upload_speed = results['upload'] / 1_000_000  # Convertir a Mbps
    ping = results['ping']
    
    return download_speed, upload_speed, ping

# Función para guardar los resultados en un archivo de texto
def save_results(download, upload, ping, iteration):
    with open("Rep_resultados_speedtest.txt", "a") as f:
        f.write(f"Medicion {iteration}: Descarga: {download:.2f} Mbps, Carga: {upload:.2f} Mbps, Ping: {ping:.2f} ms\n")
        print(f"Resultados guardados para la medición {iteration}.")

def main():
    network_name = "Apt 6-5G"  # Cambia esto por el nombre de la red a la que quieres conectarte
    total_measurements = 10  # Número de mediciones
    wait_time = 300  # 5 minutos en segundos

    for i in range(1, total_measurements + 1):
        print(f"\nIniciando medición {i}/{total_measurements}...\n")
        
        # Usar la función correcta dependiendo del sistema operativo
        if os.name == 'nt':  # Windows
            reconnect_network_windows(network_name)
        else:  # Linux
            reconnect_network_linux(network_name)

        download, upload, ping = run_speedtest()  # Ejecutar prueba de velocidad
        save_results(download, upload, ping, i)   # Guardar los resultados
        
        print("Desconectando de la red...")
        if os.name == 'nt':  # Windows
            os.system("netsh wlan disconnect")  # Desconectar de la red nuevamente
        else:  # Linux
            os.system("nmcli device disconnect wlan0")  # Desconectar de la red nuevamente

        if i < total_measurements:
            print(f"Esperando {wait_time / 60} minutos antes de la siguiente medición...\n")
            time.sleep(wait_time)  # Espera de 5 minutos entre mediciones
    
    print("Pruebas completadas. Los resultados están guardados en 'Rep_resultados_speedtest.txt'.")

if __name__ == "__main__":
    main()
