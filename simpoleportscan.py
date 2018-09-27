import socket
import termcolor
from termcolor import colored


class simpleportscan(object):
    def __init__(self,IP,*port):
        self.IP = IP
        self.port = port

    def scan(self):
        s = socket.socket()
        for portss in self.port:
            for ports in portss:
                try:
                    target = str(self.IP) + ":" + str(ports)
                    # print(type(ports))
                    # print(type(self.port))
                    print(colored("[+]try to connect " + target, "white"))
                    s.settimeout(10)#设置超时
                    s.connect((self.IP,int(ports)))#port must be int
                    s.send(b'test')#best use byte type
                    banner = s.recv(512)
                    if banner:
                        print(colored("[+]"+target +" "+ "is open","green"))
                except Exception as error:
                    print(error)
                    print(colored("[!]"+target+" "+"is failed!","red"))
