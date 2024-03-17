import arcade

arcade.open_window(600, 600, "Koordinatemsystem")

arcade.set_background_color(arcade.color.HONEYDEW)

arcade.start_render()

pos = 60
while pos <= 540:
    arcade.draw_line(0, pos, 600, pos, arcade.color.BLACK_LEATHER_JACKET)
    arcade.draw_line(pos, 0, pos, 600, arcade.color.BLACK_LEATHER_JACKET)
    pos = pos + 60

arcade.draw_line(0, 300, 600, 300, arcade.color.BLACK_LEATHER_JACKET,5)
arcade.draw_line(300, 0, 300, 600, arcade.color.BLACK_LEATHER_JACKET,5)

arcade.draw_triangle_filled(600, 300, 580, 285, 580, 315, arcade.color.BLACK_LEATHER_JACKET)
arcade.draw_triangle_filled(300, 600, 285, 580, 315, 580, arcade.color.BLACK_LEATHER_JACKET)

pos = 60
while pos <= 540:
    arcade.draw_line(pos, 290, pos, 310, arcade.color.BLACK_LEATHER_JACKET)
    arcade.draw_line(290, pos, 310, pos, arcade.color.BLACK_LEATHER_JACKET)
    pos = pos + 60

zahl = -4
while zahl <= 4:
    if zahl != 0:
        arcade.draw_text(zahl, 300 + zahl * 60, 260, arcade.color.BLACK_LEATHER_JACKET, 18, anchor_x="center")
        arcade.draw_text(zahl, 260, 300 + zahl * 60, arcade.color.BLACK_LEATHER_JACKET, 18, anchor_y="center")
    zahl = zahl + 1


arcade.draw_triangle_filled(600, 300, 580, 285, 580, 315, arcade.color.BLACK_LEATHER_JACKET)
arcade.draw_triangle_filled(300, 600, 285, 580, 315, 580, arcade.color.BLACK_LEATHER_JACKET)

arcade.finish_render()

arcade.run()