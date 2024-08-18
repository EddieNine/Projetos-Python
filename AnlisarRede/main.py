import scapy.all as scapy
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp


def analisar_rede(ip_range):
    """
    Realiza uma varredura de IPs ativos na rede fornecida.
    :param ip_range: A faixa de IPs para escanear, por exemplo, '192.168.1.0/24'
    :return: None
    """

    # Cria um pacote ARP
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = ether / arp

    # Envia o pacote e recebe a resposta
    resposta = srp(pacote, timeout=2, verbose=False)[0]

    # Exibe os IPs e endereços MAC encontrados
    print("IPs ativos e seus endereços MAC na rede:")
    for _, resposta_arp in resposta:
        ip = resposta_arp.psrc
        mac = resposta_arp.hwsrc
        print(f"IP: {ip}, MAC: {mac}")


# Exemplo de uso
faixa_ip = '192.168.0.34'
analisar_rede(faixa_ip)
