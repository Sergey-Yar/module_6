class Horse: #лошадь

    def __init__(self):
        self.x_distance = 0 #пройденный путь
        self.sound = 'Frrr' #звук, который издаёт лошадь


    def run(self, dx):
        self.x_distance += dx


class Eagle: #орел
    def __init__(self):
        self.y_distance = 0 #высота полёта
        self.sound = 'I train, eat, sleep, and repeat' #звук, который издаёт орёл (отсылка)

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle): #пегас
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)


    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()