class Pet:
    def __init__(self,name="",type="",age=""):
        self.__name = name
        self.__type = type
        self.__age = age
    def setName(self,name):
        self.name = name
    def setType(self,type):
        self.type = type
    def setAge(self,age):
        if age > 0:
            self.age = age
        else:
            self.age = 0
    def getName(self):
        return self.__name
    def getType(self):
        return self.__type
    def getAge(self):
        return self.__age
    def __str__(self):
        return "Name: {} Type: {} Age: {}".format(self.getName, self.getType, self.getAge)

