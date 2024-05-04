#!/usr/bin/python

from __future__ import print_function

import os
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.util import dumpNodeConnections

class NetworkTopo(Topo):
    # Builds network topology
    def build(self, **_opts):

        # Add hosts and switches
        h1 = self.addHost( 'h1', ip='192.168.0.1/28', mac='00:00:00:00:00:01')       
        h2 = self.addHost( 'h2', ip='192.168.0.2/28', mac='00:00:00:00:00:02')  
        h3 = self.addHost( 'h3', ip='192.168.0.3/28', mac='00:00:00:00:00:03')  
        h4 = self.addHost( 'h4', ip='192.168.0.4/28', mac='00:00:00:00:00:04')  
        h5 = self.addHost( 'h5', ip='192.168.0.5/28', mac='00:00:00:00:00:05')  
        h6 = self.addHost( 'h6', ip='192.168.0.6/28', mac='00:00:00:00:00:06')  
        s1 = self.addSwitch( 's1', failMode='standalone' )
        s2 = self.addSwitch( 's2', failMode='standalone' )        
        s3 = self.addSwitch( 's3', failMode='standalone' )       
        s4 = self.addSwitch( 's4', failMode='standalone' )       
        s5 = self.addSwitch( 's5', failMode='standalone' ) 

        # Add links
        self.addLink( h1, s1 )
        self.addLink( s1, s2)
        self.addLink( h2, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s4 )
        self.addLink( h3, s4 )
        self.addLink( h4, s4 )
        self.addLink( s3, s5 )
        self.addLink( h5, s5 )
        self.addLink( h6, s5 )



def run():
    topo = NetworkTopo()

    net = Mininet(topo=topo, controller=None)

    net.start()
    print('\n#### Informacoes das portas####\n\n\n')
    dumpNodeConnections(net.hosts)

    print('\n#### Informacoes dos enderecos####\n\n\n')
    for host in net.hosts:
        print('Host: {name} | IP: {ip} | MAC: {mac}'.format(name=host.name, ip=host.IP(), mac=host.MAC()))


    print('\n#### Ping entre todos os hosts###\n\n\n')
    net.pingAll()

    print('\n#### Acessando os hosts pelo objeto net####\n\n')
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')
    
    print('\n#### Apagando as regras ###\n\n')
    print(h1.cmd('sudo ovs-ofctl del-flows s1'))
    print(h1.cmd('sudo ovs-ofctl dump-flows s1'))
    print(h2.cmd('sudo ovs-ofctl del-flows s2'))
    print(h2.cmd('sudo ovs-ofctl dump-flows s2'))
    print(h3.cmd('sudo ovs-ofctl del-flows s3'))
    print(h3.cmd('sudo ovs-ofctl dump-flows s3'))
    print(h4.cmd('sudo ovs-ofctl del-flows s4'))
    print(h4.cmd('sudo ovs-ofctl dump-flows s4'))
    print(h5.cmd('sudo ovs-ofctl del-flows s5'))
    print(h5.cmd('sudo ovs-ofctl dump-flows s5'))


    print('\n### Teste de ping sem regras ###\n\n')
    print(h1.cmd('ping -c1 192.168.0.2'))
    print(h2.cmd('ping -c1 192.168.0.1'))
    print(h3.cmd('ping -c1 192.168.0.4'))
    print(h4.cmd('ping -c1 192.168.0.3'))
    print(h5.cmd('ping -c1 192.168.0.6'))
    print(h6.cmd('ping -c1 192.168.0.5'))

    print('\n### Setando os switches para configuracao normal ###\n\n')
    net['s1'].cmd('ovs-ofctl add-flow s1 action=normal')
    net['s2'].cmd('ovs-ofctl add-flow s2 action=normal')
    net['s3'].cmd('ovs-ofctl add-flow s3 action=normal')
    net['s4'].cmd('ovs-ofctl add-flow s4 action=normal')
    net['s5'].cmd('ovs-ofctl add-flow s5 action=normal')
    

    print(h1.cmd('sudo ovs-ofctl dump-flows s1'))
    print(h2.cmd('sudo ovs-ofctl dump-flows s2'))
    print(h3.cmd('sudo ovs-ofctl dump-flows s3'))
    print(h4.cmd('sudo ovs-ofctl dump-flows s4'))
    print(h5.cmd('sudo ovs-ofctl dump-flows s5'))
    

    print('\n### Teste de ping switch normal ###\n\n')
    print(h1.cmd('ping -c1 192.168.0.2'))
    print(h2.cmd('ping -c1 192.168.0.1'))
    print(h3.cmd('ping -c1 192.168.0.4'))
    print(h4.cmd('ping -c1 192.168.0.3'))
    print(h5.cmd('ping -c1 192.168.0.6'))
    print(h6.cmd('ping -c1 192.168.0.5'))

    print('\n### Apagando as regras ###\n\n')
    print(h1.cmd('sudo ovs-ofctl del-flows s1'))
    print(h2.cmd('sudo ovs-ofctl del-flows s2'))
    print(h3.cmd('sudo ovs-ofctl del-flows s3'))
    print(h4.cmd('sudo ovs-ofctl del-flows s4'))
    print(h5.cmd('sudo ovs-ofctl del-flows s5'))

    print('\n### Criando as regras no switch s1 de mac ###\n\n')
    print(h1.cmd('sudo ovs-ofctl del-flows s1'))
    net['s1'].cmd('sudo ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,actions=output:2')
    net['s1'].cmd('sudo ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,actions=output:1')
    net['s1'].cmd('sudo ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:06,actions=output:2')
    net['s1'].cmd('sudo ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:01,actions=output:1')
    net['s1'].cmd('sudo ovs-ofctl add-flow s1 dl_type=0x806,nw_proto=1,action=flood')
    print(h1.cmd('sudo ovs-ofctl dump-flows s1'))

    print('\n### Criando as regras no switch s2 de mac ###\n\n')
    print(h2.cmd('sudo ovs-ofctl del-flows s2'))
    net['s2'].cmd('sudo ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,actions=output:1')
    net['s2'].cmd('sudo ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,actions=output:2')
    net['s2'].cmd('sudo ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:06,actions=output:3')
    net['s2'].cmd('sudo ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:01,actions=output:1')
    net['s2'].cmd('sudo ovs-ofctl add-flow s2 dl_type=0x806,nw_proto=1,action=flood')
    print(h2.cmd('sudo ovs-ofctl dump-flows s2'))

    print('\n### Criando as regras no switch s3 de mac ###\n\n')
    print(h3.cmd('sudo ovs-ofctl del-flows s3'))
    net['s3'].cmd('sudo ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:06,actions=output:3')
    net['s3'].cmd('sudo ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:01,actions=output:1')
    net['s3'].cmd('sudo ovs-ofctl add-flow s3 dl_type=0x806,nw_proto=1,action=flood')
    print(h3.cmd('sudo ovs-ofctl dump-flows s3'))

    print('\n### Criando as regras no switch s5 de mac ###\n\n')
    print(h6.cmd('sudo ovs-ofctl del-flows s5'))
    net['s5'].cmd('sudo ovs-ofctl add-flow s5 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:06,actions=output:3')
    net['s5'].cmd('sudo ovs-ofctl add-flow s5 dl_src=00:00:00:00:00:06,dl_dst=00:00:00:00:00:01,actions=output:1')
    net['s5'].cmd('sudo ovs-ofctl add-flow s5 dl_type=0x806,nw_proto=1,action=flood')
    print(h6.cmd('sudo ovs-ofctl dump-flows s5'))

    print(h1.cmd('ping -c1 192.168.0.2'))
    print(h1.cmd('ping -c1 192.168.0.6'))
    print(h2.cmd('ping -c1 192.168.0.1'))
    print(h6.cmd('ping -c1 192.168.0.1'))

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
