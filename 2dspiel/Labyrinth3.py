import arcade

class Gegner(arcade.Sprite):
     def on_update(self, delta_time):
         self.center_x += self.change_x * delta_time
         self.center_y += self.change_y * delta_time


class Labyrinth(arcade.Window):
     def __init__(self):
        super().__init__(816, 660, "Labyrinth")

        arcade.set_background_color(arcade.color.ANTIQUE_BRONZE)

        self.setup()

     def setup(self):
        self.zeit = 60

        self.gegenstand_liste = arcade.SpriteList(use_spatial_hash=True)
        self.fake_liste = arcade.SpriteList()
        self.gegner_liste = arcade.SpriteList()


    
        
        self.hindernis_liste = arcade.SpriteList()

        Koordinaten_liste = [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,10), (1,11), (1,12), (1,13),
                             (2,13), (3,13), (4,13), (5,13), (6,13), (7,13), (8,13), (9,13), (10,13), (11,13), (12,13), (13,13), (14,13), (15,13), (16,13), (17,13),
                             (17,12), (17,11), (17,10), (17,9), (17,8), (17,7), (17,6), (17, 5), (17,4), (17,3), (17,2), (17,1),
                             (2,1), (3,1), (4,1), (5,1), (6,1), (7,1), (8,1), (9,1), (10,1), (11,1), (12,1), (13,1), (14,1), (15,1), (16,1), (17,1),
                             (2,12), (2,10), (2,8), (2,7),
                             (3,10), (3,8), (3,5), (3,4), (3,3),
                             (4,11), (4,10), (4,8), (4,6), (4,4), 
                             (5,10),
                             (6,12), (6,7), (6,6), (6,4),  
                             (7,12), (7,10), (7,9), (7,6), (7,4), 
                             (8,10), (8,7), (8,6), (8,4), (8,3),
                             (9,11), (9,10), (9,9), (9,7), (9,6), (9,4), (9,3), (9,2),
                             (10,7), (10,6), (10,4), (10,8),
                             (11,12), (11,10), (11,6), (11,3),
                             (12,11), (12,10), (12,9), (12,8), (12,6), (12,5), (12,3),
                             (13,9), (13,8), (13,6), (13,3), 
                             (14,12), (14,11), (14,8), (14,6), (14,4), (14,3),
                             (15,11), (15,10), (15,6), (15,3),
                             (16,8)]
        i = 0
        while i < len(Koordinaten_liste):
            koordinaten = Koordinaten_liste[i]
            busch2 = arcade.Sprite("busch2.png")
            busch2.center_x = koordinaten[0] * 48 - 24
            busch2.center_y = koordinaten[1] * 48 - 24
            self.hindernis_liste.append(busch2)
            i = i + 1

          

        self.Tür = arcade.Sprite("FN.png")
        self.Tür.center_x = 24
        self.Tür.center_y = 408
        self.hindernis_liste.append(self.Tür)

        

        self.cion = arcade.Sprite("cionn.png",2)
        self.cion.center_x = 768 - 24
        self.cion.center_y = 576 - 24 
        self.gegenstand_liste.append(self.cion)

        self.cion2 = arcade.Sprite("cionn.png",2)
        self.cion2.center_x = 144 - 24
        self.cion2.center_y = 336 - 24 
        self.gegenstand_liste.append(self.cion2)


        self.oz = Gegner("OZ.png")
        self.oz.center_x = 240 - 24
        self.oz.center_y = 240 - 24
        self.gegner_liste.append(self.oz)

        self.oz2 = Gegner("OZ.png")
        self.oz2.center_x = 768 - 24
        self.oz2.center_y = 96 - 24
        self.gegner_liste.append(self.oz2)
        
        self.oz3 = Gegner("OZ.png")
        self.oz3.center_x = 336- 24
        self.oz3.center_y = 96 - 24
        self.gegner_liste.append(self.oz3)

        self.cion3 = arcade.Sprite("cionn.png",2)
        self.cion3.center_x = 528-24
        self.cion3.center_y = 432-24
        self.gegenstand_liste.append(self.cion3)

        self.busch2 = arcade. Sprite("busch4.png")
        self.busch2.center_x = 480 - 24
        self.busch2.center_y = 480 - 24
        self.fake_liste.append(self.busch2)

        self.busch9 = arcade.Sprite("busch4.png")
        self.busch9.center_x = 192 - 24
        self.busch9.center_y = 144 - 24
        self.fake_liste.append(self.busch9)

        self.busch10 = arcade.Sprite("busch4.png")
        self.busch10.center_x = 288 - 24
        self.busch10.center_y = 144 - 24
        self.fake_liste.append(self.busch10)


        self.busch3 = arcade. Sprite("busch4.png")
        self.busch3.center_x = 528 - 24
        self.busch3.center_y = 384 - 24
        self.fake_liste.append(self.busch3)

        self.busch4 = arcade.Sprite("busch4.png")
        self.busch4.center_x = 768 - 24
        self.busch4.center_y = 480 - 24
        self.fake_liste.append(self.busch4)

        self.busch5 = arcade.Sprite("busch4.png")
        self.busch5.center_x = 768 - 24
        self.busch5.center_y = 432 - 24
        self.fake_liste.append(self.busch5)

        self.busch6 = arcade.Sprite("busch4.png")
        self.busch6.center_x = 192 - 24
        self.busch6.center_y = 336- 24
        self.fake_liste.append(self.busch6)

        self.busch7 = arcade.Sprite("busch4.png")
        self.busch7.center_x = 240 - 24
        self.busch7.center_y = 192 - 24
        self.fake_liste.append(self.busch7)

        self.busch8 = arcade.Sprite("busch4.png")
        self.busch8.center_x = 288 - 24
        self.busch8.center_y = 432 - 24
        self.fake_liste.append(self.busch8)

        self.dia = arcade.Sprite("dia.png")
        self.dia.center_x = 96-24
        self.dia.center_y = 528-24
        self.gegenstand_liste.append(self.dia)
       
        self.spielerliste = arcade.SpriteList()

        self.oz.change_y = 830
        self.oz2.change_y = 300
        self.oz3.change_x =-300

        self.SCHAF = arcade.Sprite("SChaff.png")
        self.SCHAF.center_x = 24 + 7 * 90
        self.SCHAF.center_y = 24 + 6 * 4
        self.spielerliste.append(self.SCHAF)

        self.physik_engine = arcade.PhysicsEngineSimple(self.SCHAF, self.hindernis_liste)

     def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.W:
                 self.SCHAF.change_y = 2
            if symbol == arcade.key.S:
                 self.SCHAF.change_y = -2
            if symbol == arcade.key.A:
                self.SCHAF.change_x = -2
            if symbol == arcade.key.D:
                 self.SCHAF.change_x = 2

     def on_key_release(self, symbol, modifiers):
         if symbol == arcade.key.W:
              self.SCHAF.change_y = 0
         if symbol == arcade.key.S:
              self.SCHAF.change_y = 0
         if symbol == arcade.key.A:
              self.SCHAF.change_x = 0
         if symbol == arcade.key.D:
              self.SCHAF.change_x = 0 

         if arcade.check_for_collision(self.SCHAF, self.Schalter):
              self.zeit = 8

     def on_update(self, delta_time):
          if self.zeit > 0 and self.SCHAF.center_x >= 24:
             self.physik_engine.update()
             self.spielerliste.update()
             self.zeit = self.zeit - delta_time
          
          self.gegner_liste.on_update(delta_time)


          

          if self.dia   not in self.gegenstand_liste and self.cion not in self.gegenstand_liste and self.cion2 not in self.gegenstand_liste and self.cion3 not in self.gegenstand_liste and arcade.check_for_collision(self.SCHAF, self.Schalter):
               self.Schalter.texture = arcade.load_texture("Schalter.png")
               self.Tür.kill()

          gegenstand_hitliste = arcade.check_for_collision_with_list(self.SCHAF, self.gegenstand_liste)

          for gegenstand in gegenstand_hitliste:
               gegenstand.kill()

          if len(self.gegenstand_liste) == 0:
               self.Schalter = arcade.Sprite("Schalter.png")
               self.Schalter.center_x = 384-24
               self.Schalter.center_y = 72
               self.gegenstand_liste.append(self.Schalter)

         
          if self.oz.center_y > 432 - 24:
              self.oz.change_y = -250
          if self.oz.center_y < 240 - 24:
              self.oz.change_y = 250

          if self.oz2.center_y > 336 - 24:
               self.oz2.change_y = -250
          if self.oz2.center_y < 104-24:
               self.oz2.change_y = 250

          if self.oz3.center_x < 104 - 24:
               self.oz3.change_x = 175
          if self.oz3.center_x >336 -24:
               self.oz3.change_x = -175


               

     def on_draw(self):
          self.clear()

          self.hindernis_liste.draw()
          self.spielerliste.draw()
          self.gegenstand_liste.draw()
          self.fake_liste.draw()
          self.gegner_liste.draw()

          if self.zeit < 0:
              arcade.draw_lrtb_rectangle_filled(0, 816, 660, 0, arcade.color.BLACK_LEATHER_JACKET)
              arcade.draw_text("!!!!!LOSER!!!!!", 408, 330, arcade.color.WHITE, font_size=60, font_name="Kenney Blocks", anchor_x="center", anchor_y="center")

          if arcade.check_for_collision(self.oz, self.SCHAF):
              self.zeit=0.000000000000000000000000001
              
             

          if arcade.check_for_collision(self.oz2, self.SCHAF):
              self.zeit = 0.0000000000000000000000000001

          if arcade.check_for_collision(self.oz3, self.SCHAF):
              self.zeit = 0.0000000000000000000000000001


          
          if self.SCHAF.center_x < 24:
               arcade.draw_text("!!!!!!!!WINNER!!!!!!!!!!", 408, 314, font_size=60,font_name= "Kenney Blocks", anchor_x="center", anchor_y="center")
     
          
          arcade.draw_text(round(self.zeit,1), 10,624, arcade.color.BLACK_LEATHER_JACKET, 30)

print("you are gay")


Labyrinth()

arcade.run()