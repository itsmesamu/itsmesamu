import arcade

arcade.open_window(201, 171, resizable=True)

arcade.start_render()

y = 0 
while y <= 170:
    arcade.draw_line(0, y, 200, y, arcade.color.BLUE)
    y = y + 10

x = 0
while x <= 200:
    arcade.draw_line(x, 0, x, 171, arcade.color.RED)
    x = x + 10 

arcade.finish_render()

arcade.run()