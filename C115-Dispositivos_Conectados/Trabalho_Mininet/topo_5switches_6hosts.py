from mininet.topo import Topo

class MyTopo( Topo ):
    # Builds network topology
    def __init__( self ):

        Topo.__init__( self )

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



topos = { 'mytopo': ( lambda: MyTopo() ) }