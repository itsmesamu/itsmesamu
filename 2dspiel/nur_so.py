import arcade

class nur_so(arcade.Window):
    def __init__(self):
       super().__init__(800, 600,"nur_so" )

    arcade.set_background_color(arcade.color.ANTIQUE_BRONZE)


nur_so()
arcade.run()      