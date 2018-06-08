#!/usr/bin/python                                                               
                                                                                
import socket                                                                   
                                                                                
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('0.0.0.0', 2222))                                                       
s.listen(1)                                                                     
                                                                                
while True:                                                                     
    conn, addr = s.accept()                                                 
    while True:                                                             
            data = conn.recv(1024)                                          
            print data.strip('\n')
            if data == 'close' or data == 'close\n': break                                       
            conn.send(data)                                                 
    conn.close()                                                            
