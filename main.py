import socket
import ipaddress
import subprocess
import platform
from colorama import Fore, Style

#* Dependencia para mostrar el texto de color:
#* pip install colorama

def is_pingable(ip):
    operating_system = platform.system().lower()
    if operating_system == "windows":
        command = f"ping -n 1 -w 1000 {ip}"
    else:
        command = f"ping -c 1 -W 1 {ip}"
    result = subprocess.call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result == 0

def port_scanner(ip, protocol, start_port, end_port):
    print(f"Escaneando puertos en {ip} utilizando el protocolo {protocol}...")
    
    for port in range(start_port, end_port + 1):
        try:
            if protocol == "TCP":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            elif protocol == "UDP":
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            sock.settimeout(0.5)
            
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                print(Fore.RED + f"Puerto {port} abierto")
            else:
                print(Fore.GREEN + f"Puerto {port} cerrado")
            
            sock.close()
        
        except socket.error:
            pass
        
    print(Style.RESET_ALL + "El análisis ha sido realizado correctamente!!")

def main():
    print("Bienvenido al programa de escaneo de puertos")
    target_type = input("Ingrese '1' para escanear un dispositivo específico o '2' para escanear una red de dispositivos: ")
    
    if target_type == "1":
        ip = input("Ingrese la dirección IP a escanear: ")
        protocol = input("Seleccione el protocolo de transporte (TCP/UDP): ")
        
        if protocol.upper() not in ["TCP", "UDP"]:
            print("Protocolo no válido. Saliendo del programa.")
            return
        
        if is_pingable(ip):
            port_scanner(ip, protocol.upper(), 1, 1024)
        else:
            print("La dirección IP no está en uso.")
    
    elif target_type == "2":
        network = input("Ingrese la dirección de red en formato CIDR (por ejemplo, 192.168.0.0/24): ")
        protocol = input("Seleccione el protocolo de transporte (TCP/UDP): ")
        
        if protocol.upper() not in ["TCP", "UDP"]:
            print("Protocolo no válido. Saliendo del programa.")
            return
        
        start_port = int(input("Ingrese el puerto inicial: "))
        end_port = int(input("Ingrese el puerto final: "))
        
        try:
            ip_net = ipaddress.IPv4Network(network, strict=False)
        except ValueError as e:
            print("Dirección de red no válida. Saliendo del programa.")
            return

        for ip in ip_net.hosts():
            ip_str = str(ip)
            if ip_str != ip_net.network_address and ip_str != ip_net.broadcast_address:
                if is_pingable(ip):
                    port_scanner(ip_str, protocol.upper(), start_port, end_port)
                else:
                    print(f"La dirección IP {ip} no está en uso.")
    
    else:
        print("Opción no válida. Saliendo del programa.")

if __name__ == "__main__":
    main()
