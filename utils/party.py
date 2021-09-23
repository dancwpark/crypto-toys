from utils import buffer

class Actor:
    def __init__(self, name):
        self.name = name

    def send(self, msg, buffer):
        buffer.send(msg)

    def recieve(self, buffer):
        return buffer.read()

    def encrypt(self, m):
        pass

    def decrypt(self, c):
        pass
