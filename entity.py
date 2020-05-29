import arcade, math
from gameObject import GameObject

class Entity(GameObject):

    def __init__(self, game, spriteFilename, hitRadius, movementSpeed, x, y):
        sprite = arcade.Sprite(spriteFilename, scale = 0.5)
        super().__init__(game, sprite, hitRadius, movementSpeed, x, y)
        self.xDirection = 0
        self.yDirection = 0

    def getVelocity(self):
        magnitude = math.sqrt(self.xDirection ** 2 + self.yDirection ** 2)
        if magnitude == 0:
            return (0, 0)
        xNormalised = self.xDirection/magnitude
        yNormalised = self.yDirection/magnitude
        return (xNormalised * self.movementSpeed, yNormalised * self.movementSpeed)

    def addDirection(self, x, y):
        self.xDirection += x
        self.yDirection += y

    def move(self, timeDelta):
        xVelocity, yVelocity = self.getVelocity()
        self.x += xVelocity * timeDelta
        self.y += yVelocity * timeDelta
        wallCollision = self.game.checkWallCollision(self)

        if wallCollision["left"]:
            self.x = self.getHitRadius() + 1
        elif wallCollision["right"]:
            self.x = self.game.getDimensions()[0] - self.getHitRadius()    

        if wallCollision["bottom"]:
            self.y = self.getHitRadius() + 1
        elif wallCollision["top"]:
            self.y = self.game.getDimensions()[1] - self.getHitRadius()    