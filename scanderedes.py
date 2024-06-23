import socket

# Função para verificar se uma porta está aberta
def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Define um tempo limite de 1 segundo para a conexão
    try:
        s.connect((host, port))
    except (socket.timeout, socket.error):
        return False
    else:
        return True
    finally:
        s.close()

# Função principal para escanear portas em um intervalo
def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if is_port_open(host, port):
            open_ports.append(port)
    return open_ports

# Especifica o host e o intervalo de portas para escanear
host = '127.0.0.1'  # IP do host a ser escaneado
start_port = 21
end_port = 443

# Chama a função de escaneamento e exibe as portas abertas
open_ports = scan_ports(host, start_port, end_port)
print(f"Portas abertas em {host}: {open_ports}")

echo  done