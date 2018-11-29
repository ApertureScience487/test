import socket

port = int(input('Enter the port: '))
sock = socket.socket()
sock.connect(('192.168.1.69', port))

while True:
 o = bytes(input('Enter: '), 'utf-8')
 sock.sendall(o)

sock.close()
