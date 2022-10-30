#!/usr/bin/python3
"""Module Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise the class"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @staticmethod
    def validate_input(name, value):
        """Raise TypeError if `value` of `name` is not int"""

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

    @staticmethod
    def validate_dimension(name, value):
        """Validate dimension"""

        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    @staticmethod
    def validate_axis(name, value):
        """Raise value error if value is < 0"""

        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        self.validate_input("width", value)
        self.validate_dimension("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        self.validate_input("height", value)
        self.validate_dimension("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""

        return self.__x

    @x.setter
    def x(self, value):
        self.validate_input("x", value)
        self.validate_axis("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        self.validate_input("y", value)
        self.validate_axis("y", value)
        self.__y = value

    def __str__(self):
        """Return string representation of a class"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
    " - {self.__width}/{self.__height}"

    def area(self):
        """calculate the `area` of a rectangle"""

        return self.__height * self.__width

    def display(self):
        """Print rectangle"""

        print(self.__y * "\n", end="")
        for line in range(self.__height):
            print(self.__x * " ", self.__width * "#")

    def update(self, *args, **kwargs):
        """Update the class Rectangle"""

        attr = self.__dict__
        if (len(args) != 0):
            i = 0
            for key in attr.keys():
                if i == len(args):
                    break
                self.__dict__[key] = args[i]
                i += 1
            return
        for key, value in kwargs.items():
            if key != "id":
                key = "_Rectangle__" + key
            attr[key] = value

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""

        new_dict = {"id": self.id, "width": self.__width,
                    "height": self.__height, "x": self.__x, "y": self.__y}
        return new_dict
