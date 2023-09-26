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
        self.x = xf
        self.y = y

    def add(self):
        return self.x+self.y

    def multiply(self, a):
        return self.MULTIPLIER*a

    @staticmethod
    def subtract(b, c):
        return b-c

    @property
    def value(self):
        return self.x, self.y

    # Create a setter and a deleter for value.

    def setX(self, value):
        self.x = value

    def deleteX(self):
        del self.x

    def setY(self, value):
        self.y = value

    def deleteY(self):
        del self.y


# test the class.
num = Numbers(5, 6)
print(num.add())
print(num.multiply(2))
print(num.subtract(2, 4))
print(num.value)
num.setX(2)
num.setY(5)
print(num.value)
num.deleteX()
num.deleteY()
