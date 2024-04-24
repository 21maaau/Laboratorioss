import turtle
import random


def obtener_datos_usuario():
    nombre = input("Ingresa tu nombre: ")
    colores = {'rojo': 'red', 'azul': 'blue', 'verde': 'green', 'amarillo': 'yellow', 'morado': 'purple'}
   
    while True:
        color_input = input("Ingresa tu color favorito (rojo, azul, verde, amarillo, morado): ")
        if color_input in colores:
            color = colores[color_input]
            break
        else:
            print("Por favor, elige un color de la lista.")
    edad = int(input("Ingresa tu edad: "))
    return nombre, color, edad

def dibujar_panel(panel_id, nombre, edad, color):
    screen = turtle.Screen()
    screen.clear()
    screen.title("El viaje de a las estrellas")
    t = turtle.Turtle()
    t.speed(0)

    # Configuraciones iniciales para el título y líneas divisorias
    t.penup()
    t.goto(-300, 300)
    t.pendown()
    t.color("black")
    t.write("El viaje a las estrellas", font=("Arial", 16, "bold"), align="left")
    t.penup()
    t.goto(-400, 280)
    t.pendown()
    t.forward(800)
    t.penup()
    t.goto(-400, -150)
    t.pendown()
    t.forward(800)
    t.penup()
    t.goto(0, 100)
    t.pendown()

    # Narrativas con saltos de línea adecuados
    narrativas =[
    f"En un pequeño pueblo geométrico vive un Punto llamado {nombre} de {edad} años, {nombre} es un pequeño círculo con sueños de aventurero.\nUn día, {nombre} decide explorar el mundo más allá de su hogar para poder cumplir su sueño de ver las estrellas.",
    f" En el comienzo de su aventura {nombre} encuentra un obstáculo, un pequeño río.\nPara poder curzar el río {nombre} debe de usar un pequeño camino de piedras que se encontraba atravesando en río.",
    f"Al cruzar el río, {nombre} se encuentra con un bosque lleno de árboles muy redondos, {nombre} queda maravillado con esto\ny decide tomarse un pequeño descanso entre los árboles.",
    f"Al continuar su camino, {nombre} se topa con una montaña muy imponente y queda impresionado,\nal ver el gran tamaño de la montaña, {nombre} piensa que es un buen lugar para ver las estrellas\ny decide escalar la montaña.",
    f"Tras un arduo esfuerzo {nombre} llega a la cima de la montaña y espera el anochecer.\nAl caer la noche, {nombre} finalmente puedo cumplir su sueño de ver las estrellas."]
    

    texto = narrativas[panel_id - 1]

    # Dibujos para cada panel
    if panel_id == 1:
        t.color("lightblue")
        t.begin_fill()
        t.penup()
        t.goto(-400, 279)  # Ir a la esquina superior izquierda
        t.pendown()
        for _ in range(2):
            t.forward(800)  # Ancho del recuadro
            t.right(90)
            t.forward(250)  # Altura del recuadro
            t.right(90)
        t.end_fill()
    # Dibujar fondo verde claro
        t.color("lightgreen")
        t.begin_fill()
        t.penup()
        t.goto(-400, 100)  # Ir a la esquina superior izquierda
        t.pendown()
        for _ in range(2):
            t.forward(800)  # Ancho del recuadro
            t.right(90)
            t.forward(240)  # Altura del recuadro
            t.right(90)
        t.end_fill()

        t.penup()
        t.goto(200, 180)
        t.pendown()
        t.color("orange")
        t.begin_fill()
        t.circle(30)
        t.end_fill()

        # Dibujar círculo relleno
        
        t.penup()
        t.goto(0, 50)
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        # Dibujar aldea
        for x in range(-150, 200, 100):
            t.color("brown")
            t.penup()
            t.goto(x, -50)
            t.pendown()
            t.begin_fill()
            for _ in range(4):
                t.forward(50)
                t.right(90)
            t.end_fill()
            t.color("red")
            t.penup()
            t.goto(x, -50)
            t.pendown()
            t.begin_fill()
            t.goto(x + 25, -25)
            t.goto(x + 50, -50)
            t.goto(x, -50)
            t.end_fill()
    elif panel_id == 2:
        t.color("lightgreen")
        t.begin_fill()
        t.penup()
        t.goto(-400, 279)  # Ir a la esquina superior izquierda
        t.pendown()
        for _ in range(2):
            t.forward(800)  # Ancho del recuadro
            t.right(90)
            t.forward(420)  # Altura del recuadro
            t.right(90)
        t.end_fill()

        t.color("lightblue")
        t.begin_fill()
        t.penup()
        t.goto(-90, 279)
        t.pendown()
        for _ in range(2):
            t.forward(180)  # Ancho del recuadro
            t.right(90)
            t.forward(420)  # Altura del recuadro
            t.right(90)
        t.end_fill()

        t.color("blue")
        t.penup()
        t.goto(0, 240)
        t.pendown()
        t.right(90)
        t.forward(30)
        t.penup()
        t.goto(-62, 0)
        t.pendown()
        t.forward(30)
        t.penup()
        t.goto(58, -100)
        t.pendown()
        t.forward(30)
        t.penup()
        t.goto(24, 120)
        t.pendown()
        t.forward(30)

        t.color("gray")
        for x in range(-80, 81, 10):
            t.penup()
            t.goto(x, 30)
            t.pendown()
            t.begin_fill()
            t.goto(x + 5, 40)
            t.goto(x + 10, 30)
            t.goto(x, 30)
            t.end_fill()
        
        t.penup()
        t.goto(-120, 30)
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    elif panel_id == 3:
        t.color("lightblue")
        t.begin_fill()
        t.penup()
        t.goto(-400, 279)  # Ir a la esquina superior izquierda
        t.pendown()
        for _ in range(2):
            t.forward(800)  # Ancho del recuadro
            t.right(90)
            t.forward(250)  # Altura del recuadro
            t.right(90)
        t.end_fill()
    # Dibujar fondo verde claro
        t.color("lightgreen")
        t.begin_fill()
        t.penup()
        t.goto(-400, 100)  # Ir a la esquina superior izquierda
        t.pendown()
        for _ in range(2):
            t.forward(800)  # Ancho del recuadro
            t.right(90)
            t.forward(240)  # Altura del recuadro
            t.right(90)
        t.end_fill()

        t.penup()
        t.goto(200, 180)
        t.pendown()
        t.color("orange")
        t.begin_fill()
        t.circle(30)
        t.end_fill()

        def draw_flower(x, y):
            t.begin_fill()
            t.up()
            t.goto(x, y)
            t.down()
            
            t.color("yellow")
            t.circle(4)
            t.end_fill()
        
        for _ in range(20):
            x = random.randint(-380, 380)
            y = random.randint(-140, 90)
            draw_flower(x, y)
        
        # Definir una función para dibujar un árbol
        def draw_tree(x, y):
            t.up()
            t.goto(x, y)  # Mover la tortuga a la posición del árbolo
            t.down()

            # Dibujar el tronco
            t.color("brown")
            t.begin_fill()
            for _ in range(2):
                t.forward(30)
                t.right(90)
                t.forward(40)
                t.right(90)
            t.end_fill()

            # Dibujar el follaje
            t.up()
            t.goto(x + 15, y + -5)  # Ajustar la posición del círculo
            t.color("green")
            t.begin_fill()
            t.down()
            t.circle(40)
            t.end_fill()

        # Dibujar una fila de 6 árboles en la parte superior
        for i in range(6):
            x = -250 + i * (560 / 6)
            y = 30  # Ajustar la posición y para la fila superior
            draw_tree(x, y)

        # Dibujar una fila de 5 árboles en la parte inferior
        for i in range(5):
            x = -260 + i * (560 / 5)
            y = -80  # Ajustar la posición y para la fila inferior
            draw_tree(x, y)
        
    elif panel_id == 4:
        t.color("lightblue")
        t.begin_fill()
        t.penup()
        t.goto(-400, 279)  # Ir a la esquina superior izquierda
        t.pendown()
        for _ in range(2):
            t.forward(800)  # Ancho del recuadro
            t.right(90)
            t.forward(299)  # Altura del recuadro
            t.right(90)
        t.end_fill()
        t.color("grey")
        t.begin_fill()
        t.penup()
        t.goto(-400, 0)  # Ir a la esquina superior izquierda
        t.pendown()
        for _ in range(2):
            t.forward(800)  # Ancho del recuadro
            t.right(90)
            t.forward(140)  # Altura del recuadro
            t.right(90)
        t.end_fill()
        t.penup()
        t.goto(-200, 180)
        t.pendown()
        t.color("orange")
        t.begin_fill()
        t.circle(30)
        t.end_fill()

        t.color("green")
        for i in range(15):
            t.penup()
            t.goto(-100 + 20*i, 0 + 20*i)
            t.pendown()
            t.begin_fill()
            for _ in range(2):
                t.forward(1000 - 20*i)
                t.right(90)
                t.forward(20)
                t.right(90)
            t.end_fill()

        t.color(color)
        t.penup()
        t.begin_fill()
        t.goto(-120, -5)
        t.pendown()
        t.circle(10)
        t.end_fill()

    elif panel_id == 5:
        t.color("black")
        t.begin_fill()
        t.penup()
        t.goto(-400, 279)  # Ir a la esquina superior izquierda
        t.pendown()
        for _ in range(2):
            t.forward(800)  # Ancho del recuadro
            t.right(90)
            t.forward(299)  # Altura del recuadro
            t.right(90)
        t.end_fill()
        t.color("green")
        t.begin_fill()
        t.penup()
        t.goto(-400, 0)  # Ir a la esquina superior izquierda
        t.pendown()
        for _ in range(2):
            t.forward(800)  # Ancho del recuadro
            t.right(90)
            t.forward(140)  # Altura del recuadro
            t.right(90)
        t.end_fill()

        def estrellita(t, x, y):
            t.penup()
            t.color(color)
            t.goto(x, y)
            t.pendown()
            t.begin_fill()
            for _ in range(5): 
                t.forward(30)
                t.right(144)
            t.end_fill()

        for _ in range(15):
            x = random.randint(-380, 380)
            y = random.randint(20, 250)
            estrellita(t, x, y)

        t.penup()
        t.goto(200, 150)
        t.pendown()
        t.color("lightgrey")
        t.begin_fill()
        t.circle(30)
        t.end_fill()
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    # Texto en la parte inferior
    t.penup()
    t.goto(-380, -200)
    t.pendown()
    t.color("black")
    t.write(texto, font=("Arial", 12, "normal"), align="left")
    t.hideturtle()

def main():
    nombre, color, edad = obtener_datos_usuario()
    current_panel = 1
    max_panel = 5
    while True:
        dibujar_panel(current_panel, nombre, edad, color)
        if current_panel == max_panel:
            user_input = input("Presiona (1) para regresar al panel anterior o (2) para cerrar el programa: ")
            if user_input == "1":
                current_panel -= 1
            elif user_input == "2":
                break
        else:
            user_input = input("Presiona (1) para regresar al panel anterior, (2) para pasar al siguiente panel: ")
            if user_input == "1" and current_panel > 1:
                current_panel -= 1
            elif user_input == "2":
                current_panel += 1

if __name__ == "__main__":
   main()