# Create a class called Numbers, which has a single class attribute called MULTIPLIER, and
# a constructor which takes the parameters x and y (these should all be numbers).
# Write a method called add which returns the sum of the attributes x and y.
# Write a class method called multiply, which takes a single number parameter a and
# returns the product of a and MULTIPLIER. Write a static method called subtract, which
# takes two number parameters, b and c, and returns b -c. Write a method called value
# which returns a tuple containing the values of x and y. Make this method into a property,
# and write a setter and getter methods for manipulating the values of x and y.

class Numbers:
    MULTIPLIER = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y

    def multiply(self, a):
        return self.MULTIPLIER*a

    @staticmethod
    def subtract(b, c):
        return b-c
    

    # (PROPERTY) a method called value which returns a tuple containing the values of x and y

    @property
    def value(self):
        t = (self.x, self.y)
        return t

    # Create a setter and a getter method for value.

    def getX(self):
        return self.x

    def setX(self, value):
        self.x = value

    def getY(self):
        return self.y

    def setY(self, value):
        self.y = value


# test the class.
num = Numbers(5, 6)
print("Numbers: "+str(num.x)+" & "+str(num.y))
print("Value of MULTIPLIER: "+str(num.MULTIPLIER))
print("Sum: "+str(num.add()))
print("Product(2): "+str(num.multiply(2)))
print("Difference(2,4): "+str(num.subtract(2, 4)))
print("Original Values: "+str(num.value))
num.setX(2)
num.setY(5)
num.getX()
num.getY()
print("Manipulated Values: "+str(num.value))
