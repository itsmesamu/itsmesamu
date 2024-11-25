import arcade.color
import pyglet
pyglet.options["osx_alt_loop"]  = True

import arcade

class Plattformer(arcade.Window):
    def __init__(self):
        super().__init__(1000,500,"Plattformer")

        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

        self.tile_map= arcade.load_tilemap("untitled.tmx")

        self.szene = arcade.Scene.from_tilemap(self.tile_map)

    def on_draw(self):
        self.clear()

        self.szene.draw()

Plattformer()
arcade.run()