import socket, sys
# change me
ADDR=""
PORT=0
#-----------------------------------------------------------
def checkPort(p=0):
    if(p!=0):
        s=socket.socket(AF_INET,SOCK_STREAM)
        try:
            s.connect(ADDR,PORT)
            s.recv(1024)
        except OSError as error:
            s.close()
        finally:
            s=None
#-----------------------------------------------------------
# do stuff
checkPort()
sys.exit(0)
