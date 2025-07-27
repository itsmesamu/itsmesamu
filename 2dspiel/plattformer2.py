
import math
import pyglet
import arcade.color
import arcade.key
pyglet.options["osx_alt_loop"]  = True
import arcade

class Plattformer2(arcade.Window):
    def __init__(self):
        super().__init__(900,700,"Plattformer2")
        self.setup()
    def setup(self):   
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
        self.tilemap = arcade.load_tilemap("map2.tmx")
        self.szene = arcade.Scene.from_tilemap(self.tilemap)

        self.spielfigur = arcade.Sprite("knighte.png")
        self.spielfigur.center_x = 160
        self.spielfigur.center_y = 700
        self.szene.add_sprite("Spielfigur",self.spielfigur)

        self.szene.get_sprite_list("Palme")

        self.szene.get_sprite_list("1. csemperéteg")

        self.physik_engine = arcade.PhysicsEnginePlatformer(self.spielfigur, self.szene.get_sprite_list("1. csemperéteg"))

        self.kamera = arcade.Camera(self.width, self.height)

        self.geschwindigkeit = 2
        self.geschwindigkeit2 = -2
        self.höhe = 4.5

    def on_key_press(self,symbol,modifiers):
        if symbol == arcade.key.RIGHT:
            self.spielfigur.change_x = self.geschwindigkeit
        if symbol == arcade.key.LEFT:
            self.spielfigur.change_x = -self.geschwindigkeit2
        if symbol == arcade.key.SPACE:
            self.spielfigur.change_y = self.höhe
        if symbol == arcade.key.D:
            self.spielfigur.change_x = self.geschwindigkeit
        if symbol == arcade.key.A:
            self.spielfigur.change_x = -self.geschwindigkeit2


    
    def on_key_release(self,symbol,modifiers):
        if symbol==arcade.key.RIGHT:
            self.spielfigur.change_x = 0
        if symbol == arcade.key.LEFT:
            self.spielfigur.change_x = 0
        if symbol == arcade.key.SPACE:
            self.spielfigur.change_y=-5
        if symbol == arcade.key.DOWN:
            self.spielfigur.change_x = 0
        if symbol == arcade.key.C:
              self.spielfigur.change_x = 0
        if symbol==arcade.key.D:
            self.spielfigur.change_x = 0
        if symbol==arcade.key.A:
            self.spielfigur.change_x = 0
        if symbol==arcade.key.W:
            self.spielfigur.change_y = 0

    def center_camera_to_player(self):
        screen_center_x = self.spielfigur.center_x - (self.kamera.viewport_width / 2)
        screen_center_y= self.spielfigur.center_y - (
            self.kamera.viewport_height / 2
        )
        if screen_center_x < 16:
            screen_center_x = 16
        if screen_center_y < 38:
            screen_center_y = 38 
        if screen_center_x > 5250:
            screen_center_x = 5250

        spielfigur_centered = screen_center_x, screen_center_y
        self.kamera.move_to(spielfigur_centered)

    def on_draw(self):
        self.clear()
        self.kamera.use()
        self.szene.draw()

    def on_update(self, deltatime):
            self.spielfigur.update()
            self.physik_engine.update()
            self.kamera.move_to((self.spielfigur.center_x, self.spielfigur.center_y))
            self.kamera.update()
            self.center_camera_to_player()
Plattformer2()
arcade.run()