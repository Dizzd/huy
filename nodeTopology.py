from mininet.topo import Topo  

class MyTopo( Topo ): 
"Simple topology example." 
 
   def __init__( self ): 
         "Create custom topo." 
  
         # Khởi tạo cấu hình mạng 
        Topo.__init__( self ) 
 
        # Khai báo các host và bộ chuyển mạch 
	h1 = self.addHost( 'h1', ip= '10.0.0.1' ) 
	h2 = self.addHost( 'h2', ip= '10.0.0.2' ) 
	h3 = self.addHost( 'h3', ip= '10.0.0.3' )   
	h4 = self.addHost( 'h4', ip= '10.0.0.4' ) 
         
	s1 = self.addSwitch( 's1' ) 
	s2 = self.addSwitch( 's2' ) 
	s3 = self.addSwitch( 's3' ) 
	s4 = self.addSwitch( 's4' ) 
	s5 = self.addSwitch( 's5' ) 
	s6 = self.addSwitch( 's6' ) 
        
        # Khai báo liên kết 
         
	self.addLink( h1, s1 ) 
	self.addLink( h3, s3 )           
	self.addLink( h2, s2 )  
	self.addLink( h4, s6 ) 
 
	self.addLink( s1, s2 ) 
	self.addLink( s1, s3 ) 
	self.addLink( s2, s3 ) 
	self.addLink( s2, s4 ) 
	self.addLink( s2, s5 ) 
	self.addLink( s3, s4 ) 
	self.addLink( s4, s5 ) 
	self.addLink( s4, s6 ) 
	self.addLink( s5, s6 ) 
	topos = { 'mytopo': ( lambda: MyTopo() ) } 
