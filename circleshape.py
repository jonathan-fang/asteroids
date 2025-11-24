import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
    
    def collides_with(self, other):
        # calc distance between center of the two circles
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        # calc radius of each circle, r1 and r2
        r1 = self.radius
        r2 = other.radius
        # if distance <= r1 + r2 return True else False
        return distance <= r1 + r2