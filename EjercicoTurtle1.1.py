#IMPORTAR TURLE
import turtle;

#INICIAR VARIABLES
longitud_lado = 0;
continuar = False;

#FUNCION PARA VERIFICAR LONGITUD
def verificarLongitud(longitud):
    if (not isinstance(longitud, float) or longitud <= 0):
        print("\n---Lo siento hermana, longitud incorrecta :(---");
        print("¿Cuánto quieres que mida cada lado?");
        return False;
    return True;
    
#MOSTRAR TEXTO
print("---Hola, hermana. Vamos a dibujar un hexágono---");
print("Recuerda que todos sus lados deben ser iguales. \n\n¿Cuánto quieres que mida cada lado?");

#BUCLE PAREA PREGUNAR LONGITUD
while not continuar:
    try:
        longitud_lado = float(input("Longitud: "));
    except: 
        longitud_lado = float(0);
    continuar = verificarLongitud(longitud_lado);

print("---Excelente, continuemos---")

#INICIAR TURTLE
turtle.title("Hexágono");
turtle.pen();
turtle.pensize(4);
turtle.fillcolor("#fdf198");

#CENTRAR FIGURA
turtle.up();
turtle.backward(longitud_lado / 2);
turtle.down();

#BUCLE PARA PINTAR HEXAGONO
turtle.begin_fill();
for x in range(6):
    turtle.forward(longitud_lado);
    turtle.left(60);
    turtle.up();
    turtle.dot(18, "black");
    turtle.dot(15, "red");
    turtle.forward(9);
    turtle.down();

#PINTAR FONDO DE HEXAGONO    
turtle.end_fill();

#OCULTAR FLECHA
turtle.hideturtle();

#CERRAR VENTANA AL PRESIONAR VENTANA
turtle.exitonclick();