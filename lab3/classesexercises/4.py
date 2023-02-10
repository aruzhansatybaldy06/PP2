class Point:
    def __init__(self, x_coord = 0, y_coord = 0):
        self.x = x_coord
        self.y = y_coord

    def show(self):
        print("X:", self.x," ",  "Y:", self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist_between_2(self, x1, y1, x2, y2):
        self.dist_between_2 = pow(pow(x1-x2, 2)+pow(y1-y2, 2), 0.5)

    def show_dist_between_2(self):
        print(self.dist_between_2)

    def dist(self, x, y):
        self.dist = pow(pow(x-self.x, 2) + pow(y-self.y, 2), 0.5)
        
    def show_dist(self):
        print(self.dist)

