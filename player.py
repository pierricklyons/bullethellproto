import arcade, math
from entity import Entity

class Player(Entity):

    def __init__(self, game, spriteFilename, hitRadius, movementSpeed, x, y):
        super().__init__(game, spriteFilename, hitRadius, movementSpeed, x, y)
        self.shooting = False

    def isShooting(self):
        return self.shooting

    def shoot(self):    
        self.game.addPlayerBullet(self.x, self.y + self.sprite.height / 2)

    def startShooting(self):
        self.shooting = True

    def stopShooting(self):
        self.shooting = False