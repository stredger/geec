
import socket

port = 9876
resp = 'HTTP/1.0 200 OK\r\n\nnothin!'
div = '---------------------------------'

soc = socket.socket()
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind(('', port))
soc.listen(1)

print 'Echo server listening on port %s' % (port)
while True:
    c, a = soc.accept()
    req = c.recv(4096)
    print '\n%s\nConnection from %s\n%s\n%s' % (div, a, req, div)
    c.send(resp)
    c.close()
