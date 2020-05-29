import arcade, math
from player import Player
from playerBullet import PlayerBullet

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

class Game(arcade.Window):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        self.player = Player(self,"peppa.png", 10, 250, width/2, height/2)
        self.width = width
        self.height = height
        self.playerBullets = []

    def getDimensions(self):
        return (self.width, self.height)

    def start(self):
        arcade.run()

    def on_draw(self):
        arcade.start_render()
        
        self.player.draw()
        
        for bullet in self.playerBullets:
            bullet.draw()

    def update(self, delta_time):
        self.player.move(delta_time)
        
        if self.player.isShooting():
            self.player.shoot()
        
        for bullet in self.playerBullets:
            bullet.move(delta_time)
            if not bullet.isOnScreen():
                self.playerBullets.remove(bullet)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.addDirection(0, 1)
        if key == arcade.key.DOWN:
            self.player.addDirection(0, -1)
        if key == arcade.key.LEFT:
            self.player.addDirection(-1, 0)
        if key == arcade.key.RIGHT:
            self.player.addDirection(1, 0)
        if key == arcade.key.Z:
            self.player.startShooting()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.addDirection(0, -1)
        if key == arcade.key.DOWN:
            self.player.addDirection(0, 1)
        if key == arcade.key.LEFT:
            self.player.addDirection(1, 0)
        if key == arcade.key.RIGHT:
            self.player.addDirection(-1, 0)
        if key == arcade.key.Z:
            self.player.stopShooting()

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

    def addPlayerBullet(self, x, y):
        bullet = PlayerBullet(self, x, y)
        self.playerBullets.append(bullet)

Game(SCREEN_WIDTH, SCREEN_HEIGHT).start()