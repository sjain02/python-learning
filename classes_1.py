class Dog():
    def __init__(self,name,age):
        """Constructor Initializes the class Dog Object """
        self.name=name
        self.age=age
    def sit(self):
        """Simulate a dog sitting """
        print(self.name.title, " is sitting now")
    def roll_over(self):
        """Simulate rolling over of dog"""
        print(self.name.title(), " had rolled over")

dg1= Dog('Eagle',12)
dg1.roll_over()