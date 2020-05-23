import arcade, math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
PLAYER_SPRITE_FILENAME = "peppa.png"
PLAYER_BULLET_SPRITE_FILENAME = "playerbullet.png"

class Game(arcade.Window):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        self.player = Player(self, width/2, height/2)
        self.playerBullet = PlayerBullet(self, self.player, 200, 300)
        self.width = width
        self.height = height

    def getDimensions(self):
        return (self.width, self.height)

    def start(self):
        arcade.run()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def update(self, delta_time):
        self.player.move(delta_time)
        self.playerBullet.move(delta_time)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.addDirection(0, 1)
        elif key == arcade.key.DOWN:
            self.player.addDirection(0, -1)
        elif key == arcade.key.LEFT:
            self.player.addDirection(-1, 0)
        elif key == arcade.key.RIGHT:
            self.player.addDirection(1, 0)
        elif key == arcade.key.W:
            self.playerBullet.draw()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.addDirection(0, -1)
        elif key == arcade.key.DOWN:
            self.player.addDirection(0, 1)
        elif key == arcade.key.LEFT:
            self.player.addDirection(1, 0)
        elif key == arcade.key.RIGHT:
            self.player.addDirection(-1, 0)

    def checkWallCollision(self, gameObject):
        x, y = gameObject.getPosition()
        hitRadius = gameObject.getHitRadius()

        leftCollision = x - hitRadius <= 0
        rightCollision = x + hitRadius > self.width
        bottomCollision = y - hitRadius <= 0
        topCollision = y + hitRadius > self.height

        return {
            "left": leftCollision,
            "right": rightCollision,
            "top": topCollision,
            "bottom": bottomCollision
        }
         
class Player:
    
    MOVEMENT_SPEED = 250
    HIT_RADIUS = 10
    
    def __init__(self, game, x, y):
        self.sprite = arcade.Sprite(PLAYER_SPRITE_FILENAME, scale = 0.5)
        self.game = game
        self.x = x
        self.y = y
        self.xDirection = 0
        self.yDirection = 0

    def draw(self):
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y
        self.sprite.draw()

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
        
    def getVelocity(self):
        magnitude = math.sqrt(self.xDirection ** 2 + self.yDirection ** 2)
        if magnitude == 0:
            return (0, 0)
        xNormalised = self.xDirection/magnitude
        yNormalised = self.yDirection/magnitude
        return (xNormalised * Player.MOVEMENT_SPEED, yNormalised * Player.MOVEMENT_SPEED)

    def getPosition(self):
        return (self.x, self.y)

    def getHitRadius(self):
        return Player.HIT_RADIUS

class PlayerBullet:

    MOVEMENT_SPEED = 250
    HIT_RADIUS = 10

    def __init__(self, game, player, x, y):
        self.sprite = arcade.Sprite(PLAYER_BULLET_SPRITE_FILENAME, scale = 0.5)
        self.game = game
        self.player = player
        self.x = x
        self.y = y
        self.xDirection = 0
        self.yDirection = 0

    def draw(self):
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y
        self.sprite.draw()

    def addDirection(self, x, y):
        self.xDirection += x
        self.yDirection += y

    def move(self, timeDelta):
        self.x += PlayerBullet.MOVEMENT_SPEED * timeDelta
        self.y += PlayerBullet.MOVEMENT_SPEED * timeDelta    

    def getPosition(self):
        return (self.x, self.y)

    def getHitRadius(self):
        return PlayerBullet.HIT_RADIUS


    

Game(SCREEN_WIDTH, SCREEN_HEIGHT).start()        