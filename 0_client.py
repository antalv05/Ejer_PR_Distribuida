from multiprocessing.connection import Client

import sys
def main(ip_address):
    print (f'trying to connect {ip_address}')
    conn = Client(address=(ip_address, 6000), authkey=b'secret password') 
    #pongo ip_Adress del que me quiero conectar. 
    print ('connection accepted')

    print ('sending message')
    conn.send('hello world')
    ok=conn.recv()
    print ('received message', ok)
    conn.close()


if __name__=="__main__":
    ip_address = "147.96.132.169"
    if len(sys.argv)>1:
        ip_address = sys.argv[1]
    main(ip_address)


#ip adress show
    
#cd Descargas/listener-client/
#ls
#python3 0_listener.py 147.96.132.169
