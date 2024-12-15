import arcade.color
import pyglet
pyglet.options["osx_alt_loop"]  = True

import arcade

class Plattformer(arcade.Window):
    def __init__(self):
        super().__init__(1000,500,"Plattformer")

        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

        self.tile_map= arcade.load_tilemap("map.tmx")

        self.szene = arcade.Scene.from_tilemap(self.tile_map)

        self.spielfigur = arcade.Sprite("knight.png")
        self.spielfigur.center_x = 160
        self.spielfigur.center_y = 510
        self.szene.add_sprite("Spielfigur",self.spielfigur)

        self.szene.get_sprite_list("Tile Layer 1")

        self.physik_engine = arcade.PhysicsEnginePlatformer(self.spielfigur, self.szene.get_sprite_list("Tile Layer 1"))

    def on_key_press(self,symbol,modifiers):
        if symbol == arcade.key.RIGHT:
            self.spielfigur.change_x = 2
        if symbol == arcade.key.LEFT:
            self.spielfigur.change_x = -2
        if symbol == arcade.key.SPACE:
            self.spielfigur.change_y = 4

    def on_key_release(self,symbol,modifiers):
        if symbol==arcade.key.RIGHT:
            self.spielfigur.change_x = 0
        if symbol == arcade.key.LEFT:
            self.spielfigur.change_x = 0
        if symbol == arcade.key.SPACE:
            self.spielfigur.change_y=-4 

    def on_draw(self):
        self.clear()

        self.szene.draw()
    def on_update(self, deltatime):
        self.spielfigur.update()
        self.physik_engine.update()

Plattformer()
arcade.run()