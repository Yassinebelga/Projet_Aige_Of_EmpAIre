class ViewPort:

    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height
    
    def adjust_position(self, amount_x, amount_y):
        self.position.x += amount_x
        self.position.y += amount_y