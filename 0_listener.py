from multiprocessing.connection import Listener
import sys

def main(ip_address): #dirección ip de mi ordenador
    listener = Listener(address=(ip_address, 6000), #puerto 6000
                        authkey=b'secret password') #contraseña
    print ('listener starting')
    conn = listener.accept() #se queda escuchando en el puerto 6000, y recibe conexiones.
    print ('connection accepted from', listener.last_accepted)
    m = conn.recv() # se queda esperando a que reciba el mensaje
    print ('received message:', m)
    conn.send('ok') #le dice que ha recibido.
    conn.close()
    print ('connection closed')
    listener.close() #hay que cerrar el canal de conexión.


if __name__=="__main__":
    ip_address = "147.96.132.169"
    if len(sys.argv)>1:
        ip_address = sys.argv[1]
    main(ip_address)

#emacs 0_client.py 
#cd..
#cd listener
#rm -r listener*
#cd listener-client/
#ls
#more 0_listener.py 
    
#lsof -i TCP:6000 Nos dice el programa que esta escuchando en el puerto 6000.
#kill -9 13518 (Numero que salga arriba)