import arcade
from gameObject import GameObject

class PlayerBullet(GameObject):
    
    SPRITE_FILENAME = "playerbullet.png"
    MOVEMENT_SPEED = 2000
    HIT_RADIUS = 10

    def __init__(self, game, x, y):
        sprite = arcade.Sprite(PlayerBullet.SPRITE_FILENAME, scale = 0.2)
        super().__init__(game, sprite, PlayerBullet.HIT_RADIUS, PlayerBullet.MOVEMENT_SPEED, x, y)
        
    def move(self, timeDelta):
        self.y += PlayerBullet.MOVEMENT_SPEED * timeDelta    