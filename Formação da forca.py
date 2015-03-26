import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("black")
window.title("Jogo da forca super hardcore")

lapis   = turtle.Turtle()  # Cria um objeto "desenhador"
turtle.setup (width = 1500)
lapis.width("8")
lapis.speed(10)  # define a velocidade
lapis.penup()       # Remova e veja o que acontece
lapis.setpos(700,-300)
lapis.pendown()
lapis.color("red")

for i in range(1):
    lapis.left(90)  # Vira o angulo pedido
    lapis.forward(600)# Avança a distancia pedida
    lapis.left(90)
    lapis.forward(1000)
for i in range(1):
    lapis.left(90)
    lapis.forward(100)
window.exitonclick()


