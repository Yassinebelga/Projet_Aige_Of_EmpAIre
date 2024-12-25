from GLOBAL_VAR import *
import shutil

class TerminalCamera:
    def __init__(self, position = PVector2(0, 0)):
        self.position = position
        self.last_time_moved = pygame.time.get_ticks()
        self.move_flags = 0

    def indexes_in_point_of_view_terminal(self):
        col, row = shutil.get_terminal_size()

        return self.position.x, self.position.y, self.position.x + col - 1, self.position.y + row - 1

    def move(self, current_time):
        if (current_time - self.last_time_moved >= ONE_SEC*(0.1)):
            if (self.move_flags & 0b0001):
                self.position.x -= 1
            
            if (self.move_flags & 0b0010):
                self.position.x += 1

            if (self.move_flags & 0b0100):
                self.position.y += 1
            
            if (self.move_flags & 0b1000):
                self.position.y -= 1
                
            self.last_time_moved = current_time
            self.move_flags = 0 # reset flags