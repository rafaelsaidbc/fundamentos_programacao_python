import turtle


def draw_square(some_turtle):
    # define os passos para desenhar um quadrado
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    # cria uma janela com fundo vermelho
    window = turtle.Screen()
    window.bgcolor('red')

    # cria o brad para desenhar um quadrado com linhas pretas
    brad = turtle.Turtle()
    brad.shape('arrow')
    brad.color('black')
    brad.speed(4)

    # loop para repetir o desenho de quadrado até formar um círculo, o range vai de 1 a 37 pois o brad vira 10º a cada desenho, para fechar 360º(círculo), ele tem que fazer 36 quadrados.
    for i in range(1, 37):
        draw_square(brad)
        brad.right(10)

    # cria o angie para desenhar um círculo com linhas pretas
    # angie = turtle.Turtle()
    # angie.shape('arrow')
    # angie.color('black')
    # angie.circle(100)

    # sai da janela ao clicar nela
    window.exitonclick()


# executa a função de desenhar
draw_art()
