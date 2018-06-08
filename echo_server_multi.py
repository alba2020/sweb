#!/usr/bin/python                                                               
                                                                                
import socket                                                                   
import threading

class myThread(threading.Thread):
    
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        while True:                                                             
            data = self.conn.recv(1024)                                          
            print data.strip('\n')
            if data == 'close' or data == 'close\n': break                                       
            self.conn.send(data)                                                 
        self.conn.close()                                                            


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('0.0.0.0', 2222))                                                       
s.listen(10)                                                                     

while True:                                                                     
    conn, addr = s.accept()
    myThread(conn, addr).start()
