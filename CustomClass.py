class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):

        return iter([{'length': self.length}, {'width': self.width}])


rect = Rectangle(5, 10)

# Iterating over the rectangle instance
for attribute in rect:
    print(attribute)
