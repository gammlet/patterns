instance = None
class Class:

    @staticmethod
    def get_instance():
        global instance
        if instance is None:
            instance = Class()
        return instance

x = Class.get_instance()
y = Class.get_instance()

if x == y:
    print("ROVNO")

