#IMPORTAR TURTLE
import turtle;

#CAMBIAR TAMAÑO DE VENTANA
turtle.setup(1000, 600)
turtle.pen();

#CAMBIAR VELOCIDAD AL DIBUJAR
turtle.speed(30);

#CAMBIAR TITULO Y TAMAÑO DE LAPIZ
turtle.title("Dinosaurio");
turtle.pensize(3);

#CENTRAR DIBUJO
turtle.up();
turtle.left(90);
turtle.forward(100);
turtle.right(90);
turtle.backward(200);
turtle.down();

#FUNCION PARA DIBUJAR TRIANGULO
def triangulo(fillColor, left = True, right = True, bottom = True):
    turtle.fillcolor(fillColor);
    turtle.begin_fill();

    if (left == False): 
        turtle.pencolor(fillColor);
    turtle.left(0);
    turtle.left(60);
    turtle.forward(100);
    turtle.pencolor("black");

    if (right == False):
        turtle.pencolor(fillColor); 
    turtle.left(-60);
    turtle.right(60);
    turtle.forward(100);
    turtle.pencolor("black");

    if (bottom == False):
        turtle.pencolor(fillColor); 
    turtle.left(-60);
    turtle.right(60);
    turtle.forward(100);
    turtle.right(180);
    turtle.forward(100);
    turtle.pencolor("black");

    turtle.end_fill();


#FUNCION PARA DIBUJAR TRIANGULO INVERTIDO
def trianguloInvertido(fillColor, left = True, right = True, bottom = True):
    turtle.fillcolor(fillColor);
    turtle.begin_fill();

    if (left == False): 
        turtle.pencolor(fillColor);
    turtle.right(0);
    turtle.right(60);
    turtle.forward(100);
    turtle.pencolor("black");

    if (right == False): 
        turtle.pencolor(fillColor);
    turtle.left(60);
    turtle.left(60);
    turtle.forward(100);
    turtle.pencolor("black");

    if (bottom == False): 
        turtle.pencolor(fillColor);
    turtle.left(0);
    turtle.left(-60);
    turtle.backward(100);
    turtle.forward(100);
    turtle.pencolor("black");

    turtle.end_fill();


#FUNCION PARA REGRESAR CURSOR A 0 GRADOS
def reiniciarPosicion(paraInvertido = False):
    if (paraInvertido == False):
        turtle.right(120);
        turtle.up();
        turtle.forward(100);
        turtle.left(120);
        turtle.down();
    
    if (paraInvertido == True):
        turtle.left(120);
        turtle.up();
        turtle.forward(100);
        turtle.right(120);
        turtle.down();   

#FUNCION PARA DIBUJAR CUADRADO
def cuadrado(fillColor):
    turtle.fillcolor(fillColor);
    turtle.begin_fill();
    for x in range(4):
        turtle.forward(100);
        turtle.right(90);
    turtle.end_fill();
    turtle.forward(100);

for x in range(4):
    triangulo("#ce7e00");
    
turtle.forward(100);
turtle.backward(700);

trianguloInvertido("#6aa74f");
reiniciarPosicion();

triangulo("#38751d", right = False);
reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#38751d", left = False);
reiniciarPosicion();

triangulo("#274e13", bottom = False, right = False);

reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#274e13", left = False, right = False);
reiniciarPosicion();

triangulo("#274e13", left = False, bottom = False);
reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#8e581f");
reiniciarPosicion();

triangulo("#274e13", right = False, bottom = False);
reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#274e13", left = False, right = False);
reiniciarPosicion();

triangulo("#274e13", left = False, bottom = False);
reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#8e581f");
reiniciarPosicion();

triangulo("#47b30f", right = False);
reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#47b30f", left = False, right = False);
reiniciarPosicion();

triangulo("#47b30f", left = False);

turtle.up();
turtle.backward(600);
turtle.down();

trianguloInvertido("#274e13", bottom = False, right = False);
reiniciarPosicion();

triangulo("#274e13", left = False, right = False);
reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#274e13", bottom = False, left = False);
reiniciarPosicion();

triangulo("#8e581f");
reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#284e12", bottom = False, right = False);
reiniciarPosicion();

triangulo("#274e13", left = False, right = False);
reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#274e13", bottom = False, left = False);
reiniciarPosicion();

triangulo("white", bottom = False);
reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#fff1cc");
reiniciarPosicion();

triangulo("white", bottom = False);
reiniciarPosicion(paraInvertido = True);

trianguloInvertido("#fff1cc");
reiniciarPosicion();

turtle.up();
turtle.backward(500);
turtle.down();

cuadrado("#744700");
turtle.forward(100);
cuadrado("#744700");

#OCULTAR CURSOR
turtle.hideturtle();

#CERRAR VENTANA AL PRESIONARLA
turtle.exitonclick();