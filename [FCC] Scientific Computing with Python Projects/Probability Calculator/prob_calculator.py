import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        
        self.contents = list()

        for x in kwargs:
            for y in range(kwargs[x]):
                self.contents.append(x)


    def draw(self, quantity):

        drawn = list()
        
        if quantity > len(self.contents):
            quantity = len(self.contents)

        for x in range(quantity):
            ball = random.choice(self.contents)
            drawn.append(ball)
            self.contents.remove(ball)
        
        return drawn
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    success = 0
    expected = list()

    for x in expected_balls:
        for y in range(expected_balls[x]):
            expected.append(x)

    hat_copy = copy.deepcopy(hat.contents)

    for x in range(num_experiments):

        hat.contents = copy.deepcopy(hat_copy)
        drawn = hat.draw(num_balls_drawn)
        check = True

        for y in expected:
            if y in drawn:
                drawn.remove(y)
            else:
                check = False

        if check:
            success = success + 1

    return success/num_experiments # Success ratio