#!/usr/bin/env python
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import socket
import sys
import threading, time

class SimpleEcho(WebSocket):
    sock = None

    def handleMessage(self):
        # echo message back to client
        if(self.sock == None):
            # scrapowanie hosta dodać
            host = self.data
            if ":" in host:
                port = int(host.split(':')[1])
                host = host.split(':')[0]
            else:
                port = 6667
            self.connect_to_irc(host, port=port)
            self.sendMessage('ok')            
            return

        self.sock.send( str.encode(self.data) )

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')
        try:
            self.sock.close()
        except:
            pass
        
    
    def irc_thread_func(self):
        #time.sleep(2)
        try:
            while(True):
                recv=self.sock.recv(2040).decode("utf-8").split("\r\n")
                for r in recv:
                    if(r==""):
                        continue

                    if(r[0:5] == "ERROR"): # jak jakis blad to zamykaj
                        try:
                            self.sock.close()
                        except:
                            pass
                        try:
                            self.close()
                        except:
                            pass
                        print(r)
                        print("JAKIS ERROR ubijam!")
                        break

                    #print(r) # privacy!!
                    self.sendMessage(r) 
        except Exception as e: # tutaj tez jak error to baj baj
            print("blad sock")
            print(e)
            try:
                self.sock.close()
            except:
                pass
            try:
                self.close()
            except:
                pass


    def connect_to_irc(self, host, port=6667):
        self.sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.sock.connect((host, port))
        print("Połączono z IRC ", host, port)
        self.irc_thread = threading.Thread(target=self.irc_thread_func)
        self.irc_thread.start()

server = SimpleWebSocketServer('', 1988, SimpleEcho)
server.serveforever()



"""
irc.freenode.net:6667
USER gkill_test gkill_test gkill_test :This is fun bot!\n
NICK gkill_test\n
JOIN ##test\n
PRIVMSG ##test :Write your message text here!\r\n
"""
