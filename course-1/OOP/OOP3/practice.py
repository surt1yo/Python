class dad:
    def __init__(self,eyes,hair,nature):
        self.eyes=eyes
        self.hair=hair
        self.nature=nature
    def display(self):
        print(f"Eyes: {self.eyes}, Hair: {self.hair}, Nature: {self.nature}")
class child(dad):
    def __init__(self,name,eyes,hair,nature):
        self.name=name
        super().__init__(eyes,hair,nature)
obj=child("Mezaan","Brown","Black","Creative")
obj.display()