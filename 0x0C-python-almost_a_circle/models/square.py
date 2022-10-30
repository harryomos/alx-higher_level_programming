#!/usr/bin/python3
"""Square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square"""

        super().__init__(size, size, x=x, y=y, id=id)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """Print string representation of a square"""

        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}"

    @property
    def size(self):
        """Get the size of a square"""

        return self.__size

    @size.setter
    def size(self, value):
        self.validate_input("size", value)
        self.validate_dimension("size", value)
        self.__size = value

    def update(self, *args, **kwargs):
        """Update the class Rectangle"""

        attr = ["size", "x", "y"]
        if (len(args) != 0):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]
            return
        for key, value in kwargs.items():
            if key != "id":
                key = "_Square__" + key
            setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""

        new_dict = {"id": self.id, "size": self.__size,
                    "x": self.__x, "y": self.__y}
        return new_dict
