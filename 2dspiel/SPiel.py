import arcade, random

BREITE = 2200
HÖHE = 1100

class Spiel(arcade.Window):
    def __init__ (self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)

        arcade.set_background_color(arcade.color.DARK_KHAKI)
        self.gegenstand_liste= arcade.SpriteList()
        self.ton_abgespielt = False
        self.ton = arcade.load_sound("harri pattor.wav")
        arcade.play_sound(self.ton) 
        self.setup()

    def setup(self):

        self.anzahl = 0
        self.zeit = 15

        BLUME = arcade.Sprite("BLUME.png")
        BLUME.center_x = random.randrange(BREITE)
        BLUME.center_y = random.randrange(HÖHE)
        self.gegenstand_liste.append(BLUME)

        Python = arcade.Sprite("Python.png")
        Python.center_x = random.randrange(BREITE)
        Python.center_y = random.randrange(HÖHE)
        self.gegenstand_liste.append(Python)
        self.hindernis_liste = arcade.SpriteList()

        glas = arcade.Sprite("Sprite-0003.png")
        glas.center_x = random.randrange(BREITE)
        glas.center_y = random.randrange(HÖHE)
        self.gegenstand_liste.append(glas)
        self.hindernis_liste = arcade.SpriteList()


        i=1
        while i<=1000:
            apfelbaum = arcade.Sprite("apfelbaum.png")
            apfelbaum.center_x = random.randrange(BREITE)
            apfelbaum.center_y = random.randrange(HÖHE)
            self.hindernis_liste.append(apfelbaum)
            i = i + 1

        i=1
        while i<=1000:
            busch = arcade.Sprite("BUsch .png")
            busch.center_x = random.randrange(BREITE)
            busch.center_y = random.randrange(HÖHE)
            self.hindernis_liste.append(busch)
            i = i + 1 

        i=1
        while i<=1000:
            baum = arcade.Sprite("bimibaumi.png")
            baum.center_x = random.randrange(BREITE)
            baum.center_y = random.randrange(HÖHE)
            self.hindernis_liste.append(baum)
            i = i + 1

    def on_update(self, delta_time):
        self.zeit = self.zeit - delta_time
 
    
    def on_mouse_press(self, x, y, button, modifiers):
        pseudosprite = arcade.Sprite()
        pseudosprite.center_x = x
        pseudosprite.center_y = y
        pseudosprite.set_hit_box([(-10000000000000, -100000000000000), (100000000000000,-10000000000000),(-1000000000000, 10000000000000), (10000000000000, 10000000000000)])

        gegenstand_hitliste = arcade.check_for_collision_with_list(pseudosprite, self.gegenstand_liste)
        
        i = 0
        while i < len(gegenstand_hitliste):
            gegenstand_hitliste[i].kill()
            self.anzahl = self.anzahl + 1
            i = i + 1

            self.ton = arcade.load_sound("sus.wav")
            arcade.play_sound(self.ton) 

    def on_draw(self):
        self.clear()



        self.gegenstand_liste.draw()
        self.hindernis_liste.draw()

        arcade.draw_text(self.anzahl, 30,30, arcade.color.BLACK_LEATHER_JACKET, 30)

        arcade.draw_text(round(self.zeit,1), 600,30, arcade.color.BLACK_LEATHER_JACKET, 30)

        if self.anzahl == 3:
            arcade.draw_lrtb_rectangle_filled(0, 2200, 1100, 0, arcade.color.BLACK_LEATHER_JACKET)
            arcade.draw_text("!!!!!VICTORY!!!!!", 1100, 550, arcade.color.WHITE, font_size=60, font_name="Kenney Blocks", anchor_x="center", anchor_y="center")

            if self.ton_abgespielt == False:
                self.ton = arcade.load_sound("rizz.wav")
                arcade.play_sound(self.ton)
                self.ton_abgespielt = True

        
            if self.zeit < 0:
                 arcade.draw_lrtb_rectangle_filled(0, 2200, 1100, 0, arcade.color.BLACK_LEATHER_JACKET)
                 arcade.draw_text("!!!!!LOSER!!!!!", 1100, 550, arcade.color.WHITE, font_size=60, font_name="Kenney Blocks", anchor_x="center", anchor_y="center")
            
                 if self.ton_abgespielt == False:
                    self.ton = arcade.load_sound("nis_gemakt.wav")
                    arcade.play_sound(self.ton)
                    self.ton_abgespielt = True
    

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.exit()
        if symbol == arcade.key.R:
            self.setup()


spiel = Spiel(2200,1100, "Osterspiel")
arcade.run()  