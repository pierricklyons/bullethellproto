class GameObject:

    def __init__(self, game, sprite, hitRadius, x, y):
        self.game = game
        self.sprite = sprite
        self.width = sprite.width 
        self.height = sprite.height
        self.hitRadius = hitRadius
        self.x = x
        self.y = y 

    def getPosition(self):
        return (self.x, self.y)
    
    def getHitRadius(self):
        return self.hitRadius

    def isOnScreen(self):
        gameWidth, gameHeight = self.game.getDimensions()
        
        if self.x - self.width / 2 > gameWidth:
            return False
        elif self.x + self.width / 2 <= 0:
            return False
        elif self.y - self.height / 2 > gameHeight:
            return False
        elif self.y + self.height / 2 <= 0:
            return False
        else:
            return True
        
    def draw(self):
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y
        self.sprite.draw()            