from kivy.support import install_twisted_reactor
install_twisted_reactor()

from twisted.internet import reactor, protocol

import select, socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9096))
s.send('CONNECT')

rlist = (sys.stdin, s)
while 1:
    read, write, fail = select.select(rlist, (), ())
    for sock in read:
        if sock == s:  # receive message from server
            data = s.recv(4096)
            print(data)
        else:  # send message entered by user
            msg = sock.readline()
            s.send(msg)



class ChatClientFactory(protocol.ClientFactory):
    protocol = ChatClient

    def __init__(self, app):
        self.app = app

class ChatClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write('CONNECT')
        self.factory.app.on_connect(self.transport)

    def dataReceived(self, data):
        self.factory.app.on_message(data)

class ChatApp(App):
    def connect(self):
        host = self.root.ids.server.text
        self.nick = self.root.ids.nickname.text
        reactor.connectTCP(host, 9096,
                           ChatClientFactory(self))
