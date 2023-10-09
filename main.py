def on_button_pressed_a():
    turtle.turn_left()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    turtle.forward(1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    turtle.turn_right()
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HAPPY)
basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)
basic.show_string("Draw the letter E")
turtle.pen(TurtlePenMode.DOWN)