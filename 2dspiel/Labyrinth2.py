import arcade

class Labyrinth(arcade.Window):
     def __init__(self):
        super().__init__(816, 660, "Labyrinth")

        arcade.set_background_color(arcade.color.ANTIQUE_BRONZE)

        self.setup()

     def setup(self):
        self.zeit = 30#

        

        self.gegenstand_liste = arcade.SpriteList()
        self.fake_liste = arcade.SpriteList()
        self.gegner_liste = arcade.SpriteList()


    
        
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

          

        self.Tür = arcade.Sprite("FN.png")
        self.Tür.center_x = 24
        self.Tür.center_y = 408
        self.hindernis_liste.append(self.Tür)

        

        self.cion = arcade.Sprite("cionn.png",2)
        self.cion.center_x = 492- 24
        self.cion.center_y = 372 - 24 
        self.gegenstand_liste.append(self.cion)

        self.cion2 = arcade.Sprite("cionn.png",2)
        self.cion2.center_x = 408- 24
        self.cion2.center_y = 288 - 24 
        self.gegenstand_liste.append(self.cion2)

        



        self.oz = arcade.Sprite("OZ.png")
        self.oz.center_x = 120-24
        self.oz.center_y = 578-24
        self.gegner_liste.append(self.oz)

        self.oz2 = arcade.Sprite("oz.png")
        self.oz2.center_x =140-24
        self.oz2.center_y = 120-24
        self.gegner_liste.append(self.oz2)

        self.oz3 = arcade.Sprite("oz.png")
        self.oz3.center_x =134-24
        self.oz3.center_y = 426-24
        self.gegner_liste.append(self.oz3)

        self.oz4 = arcade.Sprite("oz.png")
        self.oz4.center_x = 538
        self.oz4.center_y = 237
        self.gegner_liste.append(self.oz4)

        self.oz5 = arcade.Sprite("oz.png")
        self.oz5.center_x = 638
        self.oz5.center_y = 327
        self.gegner_liste.append(self.oz5)

        

        self.dia = arcade.Sprite("dia.png")
        self.dia.center_x = 168
        self.dia.center_y = 464
        self.gegenstand_liste.append(self.dia)

       


        
        self.spielerliste = arcade.SpriteList()


        self.oz.change_x = 10
        self.oz2.change_y= 10
        self.oz3.change_x= 10
        self.oz4.change_x=10
        self.oz5.change_x=10
     
       
       
          
        
        self.SCHAF = arcade.Sprite("SChaff.png")
        self.SCHAF.center_x = 24 + 8 * 90
        self.SCHAF.center_y = 24 + 6 * 4
        self.spielerliste.append(self.SCHAF)

        self.physik_engine = arcade.PhysicsEngineSimple(self.SCHAF, self.hindernis_liste)

     def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.W:
                 self.SCHAF.change_y = 5
            if symbol == arcade.key.S:
                 self.SCHAF.change_y = -5
            if symbol == arcade.key.A:
                self.SCHAF.change_x = -5
            if symbol == arcade.key.D:
                 self.SCHAF.change_x = 5

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
              self.zeit = 5
              
    


     def on_update(self, delta_time):
          if self.zeit > 0 and self.SCHAF.center_x >= 24:
             self.physik_engine.update()
             self.spielerliste.update()
             self.zeit = self.zeit - delta_time
             self.gegner_liste.update()
          

          if self.dia   not in self.gegenstand_liste and self.cion not in self.gegenstand_liste and self.cion2 not in self.gegenstand_liste and  arcade.check_for_collision(self.SCHAF, self.Schalter):
               self.Schalter.texture = arcade.load_texture("Schalter.png")
               self.Tür.kill()

          gegenstand_hitliste = arcade.check_for_collision_with_list(self.SCHAF, self.gegenstand_liste)

          for gegenstand in gegenstand_hitliste:
               gegenstand.kill()

          if len(self.gegenstand_liste) == 0:
               self.Schalter = arcade.Sprite("Schalter.png")
               self.Schalter.center_x = 744
               self.Schalter.center_y = 72
               self.gegenstand_liste.append(self.Schalter)
               


          if self.oz.center_x > 768 - 24:
           self.oz.change_x = -10

          if self.oz.center_x < 96 -24:
            self.oz.change_x = 10

          if self.oz2.center_y > 630- 24:
            self.oz2.change_y = -10   

          if self.oz2.center_y < 96 -24:
              self.oz2.change_y = 10

                
          if self.oz3.center_x > 800 - 24:
              self.oz3.change_x = -10

          if self.oz3.center_x < 94 - 24:
              self.oz3.change_x = 10

          if self.oz4.center_x > 816-24:
               self.oz4.change_x=-10

          if self.oz4.center_x < 104-24:
              self.oz4.change_x = 10

          if self.oz5.center_x > 816-24:
               self.oz5.change_x=-10

          if self.oz5.center_x < 104-24:
              self.oz5.change_x = 10




          

         
                  

    

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

          if arcade.check_for_collision(self.oz4, self.SCHAF):
              self.zeit = 0.0000000000000000000000000001  

          if arcade.check_for_collision(self.oz5, self.SCHAF):
              self.zeit = 0.0000000000000000000000000001        

                  
              
              
          
        


          if self.SCHAF.center_x < 24:
               arcade.draw_text("!!!!!!!!WINNER!!!!!!!!!!", 408, 314, font_size=60,font_name= "Kenney Blocks", anchor_x="center", anchor_y="center")
     
          
          arcade.draw_text(round(self.zeit,1), 10,624, arcade.color.BLACK_LEATHER_JACKET, 30)


Labyrinth()

arcade.run()

