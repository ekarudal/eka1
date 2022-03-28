class intan:
# Initializer / Instance Attributes
    def __init__ (self, name, kesukaan):
        self.name = name
        self.kesukaan = kesukaan
# instance method
    def description(self):
        return (self.name + " anak siapa " + self.kesukaan + " banget si ")
# Instantiate the Dog object
gua = intan ("Intan", "cantik")
# call our instance methods
print(gua.description())