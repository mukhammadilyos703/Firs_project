class Talaba:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def getName(self):
        return self.lastname + self.firstname

t1 = Talaba("ali", "Aliev", 18)