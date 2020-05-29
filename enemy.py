import arcade, math
from entity import Entity

class Enemy(Entity):

    def __init__(self, game, spriteFilename, hitRadius, movementSpeed, x, y):
        sprite = arcade.Sprite(Enemy.SPRITE_FILENAME, scale = 0.5)
        super().__init__(game, sprite, Enemy.HIT_RADIUS, x, y)
