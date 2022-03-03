import turtle;

longitud_lado = 0;
def verificarLongitud(longitud):
    if (not isinstance(longitud, float) or longitud <= 0):
        print("---Lo siento hermana, longitud incorrecta :(---")
    

print("---Hola, hermana. Vamos a dibujar un hexágono---");
print("Recuerda que todos sus lados deben ser iguales. \n\n¿Cuánto quieres que mida cada lado?");

try:
    longitud_lado = float(input());
except: 
    longitud_lado = float(0);
    
verificarLongitud(longitud_lado);
