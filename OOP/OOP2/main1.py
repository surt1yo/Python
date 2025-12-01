class IOstring:
    def __init__(self):
        print("constructor initializer")
        self.string=""
    def get_string(self):
        self.string=input("Enter a string: ")
    def print_string(self):
        print(self.string)
obj=IOstring()
obj.get_string()
obj1=IOstring()
obj1.get_string()
obj.print_string()
obj1.print_string()