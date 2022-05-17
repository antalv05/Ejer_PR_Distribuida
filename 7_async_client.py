from multiprocessing.connection import Client
import sys

def main(ip_address):
    print ('trying to connect')
    with Client(address=('127.0.0.1', 6000), authkey=b'secret password') as conn:
        print ('connection accepted')
        for i in range(10):
            conn.send(i)
        for _ in range(10):
            m = conn.recv()
            print(m)

if __name__=="__main__":
    ip_address = "127.0.0.1"
    if len(sys.argv)>1:
        ip_address = sys.argv[1]
    main(ip_address)
