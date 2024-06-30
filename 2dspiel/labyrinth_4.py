import arcade

class Labyrinth(arcade.Window):
     def __init__(self):
        super().__init__(816, 660, "Labyrinth")

        arcade.set_background_color(arcade.color.ANTIQUE_BRONZE)

        self.setup()

     def setup(self):
        self.zeit = 278364827364782634823648
        self.zahl = 0

        

        self.gegenstand_liste = arcade.SpriteList()
        
        self.gegner_liste = arcade.SpriteList()
        self.gegenstand_liste2 = arcade.SpriteList()
        self.spielerliste = arcade.SpriteList()
        self.Schussliste = arcade.SpriteList()

    
        
        self.hindernis_liste = arcade.SpriteList()

        Koordinaten_liste = [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,10), (1,11),(1,12), (1,13),
                             (2,13), (3,13), (4,13), (5,13), (6,13), (7,13), (8,13), (9,13), (10,13), (11,13), (12,13),
                             (13,13), (14,13), (15,13), (16,13), (17,13),(17,12), (17,11),(17,10),(17,9),(17,8),(17,7),
                             (17,6),(17,5),(17,4),(17,3),(17,2),(17,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),
                             (10,1),(11,1),(12,1),(13,1),(14,1),(15,1), (16,1)]
        


        i = 0
        while i < len(Koordinaten_liste):
            koordinaten = Koordinaten_liste[i]
            busch2 = arcade.Sprite("busch2.png")
            busch2.center_x = koordinaten[0] * 48 - 24
            busch2.center_y = koordinaten[1] * 48 - 24
            self.hindernis_liste.append(busch2)
            i = i + 1
        
        Koordinaten_liste2 = [(4,10), (10,10), (10,4), (14,8), (4,5), (6,7)]

        i = 0        
        while i < len(Koordinaten_liste2):
            koordinaten = Koordinaten_liste2[i]
            stein = arcade.Sprite("stein.png")
            stein.center_x = koordinaten[0] * 48 - 24
            stein.center_y = koordinaten[1] * 48 - 24
            self.hindernis_liste.append(stein)
            i = i + 1
        
        self.SCHAF = arcade.Sprite("schaf2.png")
        self.SCHAF.center_x = 24 + 8 * 90
        self.SCHAF.center_y = 24 + 6 * 56
        self.spielerliste.append(self.SCHAF)


        
        self.Tür = arcade.Sprite("FN.png")
        self.Tür.center_x = 24
        self.Tür.center_y = 408
        self.hindernis_liste.append(self.Tür)
        
        self.physik_engine = arcade.PhysicsEngineSimple(self.SCHAF, self.hindernis_liste)
        self.physik_engine1 = arcade.PhysicsEngineSimple(self.patrone, self.hindernis_liste)


     def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.W:
                 self.SCHAF.change_y = 2
            if symbol == arcade.key.S:
                 self.SCHAF.change_y = -2
            if symbol == arcade.key.A:
                self.SCHAF.change_x = -2
            if symbol == arcade.key.D:
                 self.SCHAF.change_x = 2
            if symbol == arcade.key.UP:
                 self.patrone = arcade.Sprite("patrone.png")
                 self.patrone.center_x = self.SCHAF.center_x
                 self.patrone.center_y = self.SCHAF.center_y
                 self.Schussliste.append(self.patrone)
                 self.patrone.change_x = 10
                 
            
     def on_key_release(self, symbol, modifiers):
         if symbol == arcade.key.W:
              self.SCHAF.change_y = 0
         if symbol == arcade.key.S:
              self.SCHAF.change_y = 0
         if symbol == arcade.key.A:
              self.SCHAF.change_x = 0
         if symbol == arcade.key.D:
              self.SCHAF.change_x = 0



          

     def on_update(self, delta_time):
        if self.zeit > 0 and self.SCHAF.center_x >= 24:
             self.physik_engine.update()
             self.spielerliste.update()
             self.zeit = self.zeit - delta_time
             self.gegner_liste.update()
             if arcade.check_for_collision_with_list(self.SCHAF,self.gegenstand_liste):
                 self.zahl = self.zahl +1
             self.gegenstand_liste2.update()
             self.Schussliste.update()
             self.physik_engine1
        
     def on_draw(self):
          self.clear()

          self.hindernis_liste.draw()
          self.spielerliste.draw()
          self.gegenstand_liste.draw()
          self.gegner_liste.draw()
          self.gegenstand_liste2.draw()
          self.Schussliste.draw()

          arcade.draw_text(round(self.zeit,1), 10,624, arcade.color.BLACK_LEATHER_JACKET,30)
          if self.zeit > 0:
               arcade.draw_text(self.zahl,300,624,arcade.color.BARN_RED,30)


Labyrinth()

arcade.run()
      