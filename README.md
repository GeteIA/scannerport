![imagem](https://imgur.com/qojDlMr)


Importação do módulo socket

O módulo socket é importado para permitir a comunicação em rede. Ele fornece a interface necessária para criar, conectar e gerenciar sockets, que são os pontos de extremidade de uma comunicação bidirecional.

Função is_port_open

Esta função verifica se uma porta específica está aberta em um host.

- s = socket.socket(socket.AF_INET, socket.SOCK_STREAM): Cria um objeto socket. AF_INET indica que são usados endereços IPv4 e SOCK_STREAM indica que o protocolo é TCP.
- s.settimeout(1): Define um tempo limite de 1 segundo para a tentativa de conexão. Isso evita que o programa fique travado esperando uma resposta indefinidamente.
- s.connect((host, port)): Tenta se conectar ao host na porta especificada. Se a conexão for bem-sucedida, isso indica que a porta está aberta.
- except (socket.timeout, socket.error): Captura exceções de tempo limite e erros de socket. Se qualquer uma dessas exceções ocorrer, a porta é considerada fechada.
- return False: Retorna False se a porta estiver fechada ou se ocorrer um erro.
- return True: Retorna True se a conexão for bem-sucedida, indicando que a porta está aberta.
- finally: s.close(): Fecha o socket após a tentativa de conexão, independentemente do resultado, para liberar recursos.

Função scan_ports

Esta função varre um intervalo de portas em um host para verificar quais estão abertas.

- open_ports = []: Inicializa uma lista para armazenar as portas abertas.
- for port in range(start_port, end_port + 1): Itera sobre o intervalo de portas especificado.
- if is_port_open(host, port): Verifica se a porta está aberta usando a função is_port_open.
- open_ports.append(port): Adiciona a porta à lista de portas abertas se ela estiver aberta.
- return open_ports: Retorna a lista de portas abertas.

Especificação do Host e Intervalo de Portas

- host = '127.0.0.1': Define o host a ser escaneado (neste caso, localhost).
- start_port = 21 e end_port = 443: Define o intervalo de portas a ser escaneado (da porta 21 à porta 443).

Chamada da Função de Escaneamento

- open_ports = scan_ports(host, start_port, end_port): Chama a função scan_ports para escanear as portas no host especificado e armazena a lista de portas abertas em open_ports.
- print(f"Portas abertas em {host}: {open_ports}"): Exibe as portas abertas encontradas no host
