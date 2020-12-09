class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


    def set_width(self, width):
        self.width = width


    def set_height(self, height):
        self.height = height


    def get_area(self): 
        return self.width * self.height


    def get_perimeter(self): 
        return (self.width * 2) + (self.height * 2)
        # Returns perimeter (2 * width + 2 * height)

    def get_diagonal(self): 
        return (self.width ** 2 + self.height ** 2) ** .5
        # Returns diagonal ((width ** 2 + height ** 2) ** .5)

    def get_picture(self): 

        if self.width > 50 or self.height > 50:
            picture = "Too big for picture."

        else:
            picture = ""

            for y in range(0, self.height):
                for x in range(0, self.width):

                    picture = picture + "*"

                picture = picture + "\n"
        
        return picture


    def get_amount_inside(self, shape): 
        times = 0

        height_left = self.height
        width_left = self.width

        minus_height = shape.height
        minus_width = shape.width

        while True:
            if height_left >= minus_height:
                if width_left < minus_width:
                    break

                while width_left >= minus_width:
                    width_left = width_left - minus_width
                    times = times + 1

                height_left = height_left - minus_height
                width_left = self.width 
                # After going through the width once, height decreases and width resets.

            else:
                break
        
        return times


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side


    def __str__(self):
        return f"Square(side={self.width})"
    

    def set_side(self, side):
        self.width = side
        self.height = side

    
    def set_width(self, side):
        self.width = side
        self.height = side


    def set_height(self, side):
        self.width = side
        self.height = side 