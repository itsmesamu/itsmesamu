import arcade.color
import arcade.color
import arcade.key
import pyglet
pyglet.options["osx_alt_loop"]  = True

import arcade

class Plattformer(arcade.Window):
    def __init__(self):
        super().__init__(1000,700,"Plattformer")
        
        self.setup()
    def setup(self):
        self.zeit = 500
        self.zahl = 0
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)



        self.tile_map= arcade.load_tilemap("map.tmx")

        self.szene = arcade.Scene.from_tilemap(self.tile_map)

        self.spielfigur = arcade.Sprite("knighte.png")
        self.spielfigur.center_x = 160
        self.spielfigur.center_y = 700
        self.szene.add_sprite("Spielfigur",self.spielfigur)

        self.szene.get_sprite_list("fruit 3")

        self.szene.get_sprite_list("Tile Layer 1")

        self.szene.get_sprite_list("pilz")

        self.szene.get_sprite_list("jump")

        self.szene.get_sprite_list("fruit 1")
        
        self.szene.get_sprite_list("fruit 2")
        
        self.szene.get_sprite_list("leiter layer")

        self.szene.get_sprite_list("power ups")

        self.szene.get_sprite_list("power ups")

        self.szene.get_sprite_list("lava layer")

        self.szene.get_sprite_list("eis layer")
        
        self.kamera = arcade.Camera(self.width, self.height)

        self.geschwindigkeit = 2
        self.geschwindigkeit2 = -2
        self.höhe = 4

        self.pilz = 

        self.physik_engine = arcade.PhysicsEnginePlatformer(self.spielfigur, self.szene.get_sprite_list("Tile Layer 1"))
    
    
    def on_key_press(self,symbol,modifiers):
            if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("leiter layer")):
                    if arcade.key.UP:
                        self.spielfigur.change_y = self.höhe + 2
            if arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("jump")):
                if arcade.key.UP:
                    self.spielfigur.change_y = 20
            if symbol == arcade.key.RIGHT:
                self.spielfigur.change_x = self.geschwindigkeit
            if symbol == arcade.key.LEFT:
                    self.spielfigur.change_x = self.geschwindigkeit2
            if symbol == arcade.key.SPACE:
                self.spielfigur.change_y = self.höhe
            if symbol == arcade.key.R:
                self.setup()
            if symbol == arcade.key.DOWN:
                self.spielfigur.change_x = 10
            if symbol == arcade.key.C:
                 self.spielfigur.change_x = -10
            if symbol == arcade.key.Q:
                 arcade.exit()
    
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
        if self.spielfigur.center_y < 0:
            arcade.draw_text("LOOSER",self.spielfigur.center_x, 350, arcade.color.BLACK_LEATHER_JACKET, font_size=100,font_name="Kenney Blocks",anchor_x="center",anchor_y="center")

        arcade.draw_text(round(self.zeit,1), self.spielfigur.center_x - 150, 750, arcade.color.BLACK_LEATHER_JACKET, 30)
        
        if self.zeit < 0:
            arcade.draw_text("LOOSER",self.spielfigur.center_x, 400, arcade.color.BLACK_LEATHER_JACKET, font_size=100,font_name="Kenney Blocks",anchor_x="center",anchor_y="center")
        
        if arcade.check_for_collision_with_list(self.spielfigur,self.szene.get_sprite_list("lava layer")):
                arcade.draw_text("LOOSER",self.spielfigur.center_x, 400, arcade.color.BLACK_LEATHER_JACKET, font_size=100,font_name="Kenney Blocks",anchor_x="center",anchor_y="center")
        
        arcade.draw_text(self.zahl,self.spielfigur.center_x + 150, 750, arcade.color.BARN_RED, 30)
        
        if self.spielfigur.center_x > 6000 and self.zahl > 130:
            arcade.draw_text("WINNER", self.spielfigur.center_x - 700, 500, arcade.color.BLACK_LEATHER_JACKET, font_size=100,font_name="Kenney Blocks",anchor_x="center",anchor_y="center")

        elif self.spielfigur.center_x > 6000 and self.zahl < 130:
            arcade.draw_text("LOOSER", self.spielfigur.center_x - 700, 500, arcade.color.BLACK_LEATHER_JACKET, font_size=100,font_name="Kenney Blocks",anchor_x="center",anchor_y="center")

    def on_update(self, deltatime):
        if self.zeit > 0:
            self.spielfigur.update()
            self.physik_engine.update()
            self.kamera.move_to((self.spielfigur.center_x, self.spielfigur.center_y))
            self.kamera.update()
            self.center_camera_to_player() 
            self.center_camera_to_player()
            self.zeit = self.zeit - deltatime
            
            self.hitliste = arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("power ups"))
            for arcade.sprite in self.hitliste:
                arcade.sprite.kill()
                self.zahl = self.zahl + 1
            
            self.hitliste2 = arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("fruit 1"))
            for arcade.sprite in self.hitliste2:
                arcade.sprite.kill() 
                self.geschwindigkeit = self.geschwindigkeit + 1
                self.geschwindigkeit2 = self.geschwindigkeit2 - 1
                
            
            self.hitliste3 = arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("fruit 2"))
            for arcade.sprite in self.hitliste3:
                 arcade.sprite.kill()
                 self.höhe = self.höhe + 1  
                 
            self.hitliste4 = arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("fruit 3"))
            for arcade.sprite in self.hitliste4:
                 arcade.sprite.kill()
                 self.spielfigur.scale = 1.5

            self.hitliste5 = arcade.check_for_collision_with_list(self.spielfigur, self.szene.get_sprite_list("power upsss"))
            for arcade.sprite in self.hitliste5:
                arcade.sprite.kill()  

            if arcade.check_for_collision_with_list(self.spielfigur,self.szene.get_sprite_list("lava layer")):
                self.spielfigur.kill()
            
            if arcade.check_for_collision_with_list(self.spielfigur,self.szene.get_sprite_list("eis layer")):
                self.spielfigur.change_x = 3



                    
Plattformer()
arcade.run()