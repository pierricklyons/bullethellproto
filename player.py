import arcade, math
from gameObject import GameObject

class Player(GameObject):
    
    SPRITE_FILENAME = "peppa.png"
    MOVEMENT_SPEED = 250
    HIT_RADIUS = 10

    def __init__(self, game, x, y):
        sprite = arcade.Sprite(Player.SPRITE_FILENAME, scale = 0.5)
        super().__init__(game, sprite, Player.HIT_RADIUS, x, y)
        self.xDirection = 0
        self.yDirection = 0
        self.shooting = False

    def getVelocity(self):
        magnitude = math.sqrt(self.xDirection ** 2 + self.yDirection ** 2)
        if magnitude == 0:
            return (0, 0)
        xNormalised = self.xDirection/magnitude
        yNormalised = self.yDirection/magnitude
        return (xNormalised * Player.MOVEMENT_SPEED, yNormalised * Player.MOVEMENT_SPEED)

    def isShooting(self):
        return self.shooting

    def addDirection(self, x, y):
        self.xDirection += x
        self.yDirection += y

    def move(self, timeDelta):
        xVelocity, yVelocity = self.getVelocity()
        self.x += xVelocity * timeDelta
        self.y += yVelocity * timeDelta
        wallCollision = self.game.checkWallCollision(self)

        if wallCollision["left"]:
            self.x = Player.HIT_RADIUS + 1
        elif wallCollision["right"]:
            self.x = self.game.getDimensions()[0] - Player.HIT_RADIUS    

        if wallCollision["bottom"]:
            self.y = Player.HIT_RADIUS + 1
        elif wallCollision["top"]:
            self.y = self.game.getDimensions()[1] - Player.HIT_RADIUS    

    def shoot(self):    
        self.game.addPlayerBullet(self.x, self.y + self.sprite.height / 2)

    def startShooting(self):
        self.shooting = True

    def stopShooting(self):
        self.shooting = False