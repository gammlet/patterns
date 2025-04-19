class States():
    name = ""
    def change_state(self, go_to_state):
        print(self.name, "-->", go_to_state.name)

class StateA(States):
    name = "A"

    def out_put(self):
        print("this is what you get in State A")
        x = [1, 2, 3]
        for i in x:
            print(i)
        print("bey")

class StateB(States):
    name = "B"
    def out_put(self):
        print("this is what you get in State B")
        x = [4, 5, 6]
        for i in x:
            print(i)
        print("bey")

class Context(States):
    def __init__(self, state):
        self.state = state
    def request_to(self, go_to_state):
        self.state.change_state(go_to_state)
        self.state = go_to_state


a = StateA()
b = StateB()

d1 = Context(a)
d1.request_to(b)
d1.request_to(a)

d1.state.out_put()

d1.request_to(b)
d1.state.out_put()