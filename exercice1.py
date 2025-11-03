class StringFoo:
    def __init__(self):
        self.message = ""

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(f"{self.message.upper()}")


message = StringFoo()
message.set_string(input("Quel est votre message: "))
message.print_string()
