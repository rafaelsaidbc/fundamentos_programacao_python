import turtle


def desenhar_triangulo(triangulo):
    for i in range(1, 4):
        triangulo.forward(80)
        triangulo.left(120)
        triangulo.forward(120)
        triangulo.left(120)
        triangulo.forward(120)


def arte_desenho():
    window = turtle.Screen()
    window.bgcolor('black')

    rafa = turtle.Turtle()
    rafa.shape('arrow')
    rafa.color('red')
    rafa.speed(100)

    for i in range(1, 37):
        desenhar_triangulo(rafa)
        rafa.right(10)

    window.exitonclick()


arte_desenho()
