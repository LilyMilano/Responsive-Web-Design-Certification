import socket

#  NETWORKING

#  TCP Connections / Sockets:

#  TCP stands for Transmission Control Protocol. It is a fundamental protocol within the Internet protocol suite, which allows systems to communicate over the Internet.
#  A TCP connection is managed by an operating system through a resource that represents the local end-point for communications, known as the Internet socket.
#  In computer networking, an Internet socket or network is an endpoint of a bidirectional inter-process communication flow across an Internet Protocol-based computer network, such as the Internet.

# PROCESS <--------------- INTERNET ----------> PROCESS
# Browser: Chrome/ Edge                 Server: Apache / Tomcat

# ? An HTTP Request in Python:

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")
mysock.close()

"""
HTTP/1.1 200 OK
Date: Sat, 27 Jan 2024 23:22:26 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
"""
