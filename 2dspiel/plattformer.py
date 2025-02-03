import arcade.color
import arcade.color
import arcade.key
import pyglet
pyglet.options["osx_alt_loop"]  = True

import arcade

class Plattformer(arcade.Window):
    def __init__(self):
        super().__init__(2000,1000,"Plattformer")
        
        self.setup()
    def setup(self):
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)



        self.tile_map= arcade.load_tilemap("map.tmx")

        self.szene = arcade.Scene.from_tilemap(self.tile_map)

        self.spielfigur = arcade.Sprite("knighte.png")
        self.spielfigur.center_x = 160
        self.spielfigur.center_y = 510
        self.szene.add_sprite("Spielfigur",self.spielfigur)

    

        self.szene.get_sprite_list("Tile Layer 1")

        self.szene.get_sprite_list("leiter layer")

        self.szene.get_sprite_list("power ups")
        
        self.kamera = arcade.Camera(self.width, self.height)

        self.physik_engine = arcade.PhysicsEnginePlatformer(self.spielfigur, self.szene.get_sprite_list("Tile Layer 1"))

    def on_key_press(self,symbol,modifiers):
        if symbol == arcade.key.RIGHT:
            self.spielfigur.change_x = 2
        if symbol == arcade.key.LEFT:
            self.spielfigur.change_x = -2
        if symbol == arcade.key.SPACE:
            self.spielfigur.change_y = 4
        if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("leiter layer")):
            if arcade.key.UP:
                self.spielfigur.change_y = 5
        if symbol == arcade.key.R:
            self.setup()
            


    def on_key_release(self,symbol,modifiers):
        if symbol==arcade.key.RIGHT:
            self.spielfigur.change_x = 0
        if symbol == arcade.key.LEFT:
            self.spielfigur.change_x = 0
        if symbol == arcade.key.SPACE:
            self.spielfigur.change_y=-5


    def center_camera_to_player(self):
        screen_center_x = self.spielfigur.center_x - (self.kamera.viewport_width / 2)
        screen_center_y= self.spielfigur.center_y - (
            self.kamera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0

        spielfigur_centered = screen_center_x, screen_center_y
        self.kamera.move_to(spielfigur_centered)

    def on_draw(self):
        self.clear()
        self.kamera.use()
        self.szene.draw()
        if self.spielfigur.center_y < 0:
            arcade.draw_text("LOOSER",self.spielfigur.center_x, 500, arcade.color.BLACK_LEATHER_JACKET, font_size=300,font_name="Kenney Blocks",anchor_x="center",anchor_y="center")

        

        
    def on_update(self, deltatime):
        self.spielfigur.update()
        self.physik_engine.update()
        self.kamera.move_to((self.spielfigur.center_x, self.spielfigur.center_y))
        self.kamera.update()
<<<<<<< HEAD
        self.center_camera_to_player() 
=======
        self.center_camera_to_player()
>>>>>>> parent of fd6b8f9 (123)
        
            

Plattformer()
arcade.run()