class person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height  = height
        self.weight = weight

    def prp(self):
        print("name: ",self.name," age: ",self.age," height: ",self.height," weight: ",self.weight)