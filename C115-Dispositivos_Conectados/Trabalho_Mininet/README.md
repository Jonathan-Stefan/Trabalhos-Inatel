### Comando para adionar eth1 na vm mininet e iniciar conexão com o putty
sudo ifconfig eth1 192.168.56.101 netmask 255.255.255.0 up

### Comando para apagar uma topologia existente
sudo mn -c

### Comando para executar arquivo python
sudo python mnbasic.py

## Criando a topologia via mininet
sudo mn --custom topo_5switches_6hosts.py --topo mytopo

## Comando para fechar o putty
exit