import pyglet
pyglet.options["osx_alt_loop"] = True

import arcade,random
class ab(arcade.Window):
    def __init__(self):
        super().__init__(626,417,"ab")

        self.boom = arcade.Sprite("boom.png", 0.12)
        self.boom.center_x = self.width / 2
        self.boom.center_y = 50

        self.schwert_liste = arcade.SpriteList

        self.zeit = 30  

        def on_key_press(self, symbol,modifiers):
             if symbol == arcade.key.A:
                self.boom.change_x = -5
             elif symbol == arcade.key.D:
                 self.boom.change_y = 5
        
        self.background = arcade.load_texture("eine-landschaft-im-pixel-art-stil-mit-bergen-und-baeumen_720722-1156.png")     

        

        self.spieler_liste = arcade.SpriteList
        self.hindernis_liste = arcade.SpriteList


    
    def on_update(self,deltatime):
        if self.zeit > 0:
            self.zeit = self.zeit-deltatime

    def on_draw(self):
        if self.zeit < 0:
               arcade.draw_text("Loser",50,100,arcade.color.BARN_RED,200)
        arcade.draw_lrwh_rectangle_textured(0,0,626,417, self.background)
        self.spieler_liste


spiel = ab(626,417,"ab")
arcade.run()                                