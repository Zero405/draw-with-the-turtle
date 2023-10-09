input.onButtonPressed(Button.A, function () {
    turtle.turnLeft()
})
input.onButtonPressed(Button.AB, function () {
    turtle.forward(1)
})
input.onButtonPressed(Button.B, function () {
    turtle.turnRight()
})
basic.showIcon(IconNames.Happy)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showString("Draw the letter E")
turtle.pen(TurtlePenMode.Down)
