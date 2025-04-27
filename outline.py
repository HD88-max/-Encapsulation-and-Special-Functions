# Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.
class myclass:
    __privatevar = 2
    def __privMeth(self):
        print("this is inside class")
    def hello(self):
        print("privatevar",myclass.__privatevar)
obj1 = myclass()
obj1.hello()
obj1.__privMeth