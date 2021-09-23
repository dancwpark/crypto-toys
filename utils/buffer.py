from utils import party

class Buffer:
    def __init__(self, id):
        self.id = id
        self.parties = set()
        self.msgs = []

    def add_party(self, party):
        self.parties.add(party)

    def remove_party(self, party):
        self.parties.remove(party)

    def send(self, msg):
        self.msgs.append(msg)

    def read(self):
        return self.msgs.pop(0)
    
    def list_parties(self):
        for x in self.parties:
            print(x.name)
