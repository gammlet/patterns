class Publisher:
    def __init__(self):
        self._observers = []
    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

class Data(Publisher):
    def __init__(self, name =""):
        Publisher.__init__(self)
        self.name = name
        self.data = 0

    def set_data(self, value):
        self.data = value
        self.notify()

class SubsciberAdd:
    def __init__(self):
        self.numbers = []
        self.res = 1

    def update(self, subject):
        self.numbers.append(subject.data)
        res = 1
        for i in self.numbers:
            self.res *= i
            print(self.res)
        print("Total multiplication is ", self.res)

        print(self.numbers)

class SubscriberPlus:
    def __init__(self):
        self.numbers = []
    def update(self, subject):
        self.numbers.append(subject.data)
        total = sum(self.numbers)
        print("Total sum is", total)
        print(self.numbers)



obj1 = Data("Data 1 ")
obj2 = Data("Data 2 ")

v1 = SubsciberAdd()
v2 = SubscriberPlus()

obj1.attach(v1)
obj1.attach(v2)

obj2.attach(v1)
obj2.attach(v2)

obj1.set_data(10)
obj1.set_data(12)

