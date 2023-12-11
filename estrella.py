import turtle
#importamos un modulo para dibujar graphismos

def draw_star(size,t,num_points): #definimos una funcion con dos variables 
    angle = 180/ num_points
    for _ in range(num_points): #hacemos un bucle para dibujar cada linea de la estrella 
        t.forward(size) #la funcion size es para quela tortuga vaya hacia alante a una distanbcia dependiendo de la variable size
        t.right(180-angle) #para que depues de avanzar de un girode 160° para formar los angulos de 20° de la estrella

#definimos como queremos que se haga la estrella con los detalles del dibujo
turtle.speed(5)
turtle.pensize(1)
turtle.pencolor("black")

#he definido una nueva variable para transformar la flecha de la estrella en una tortuga 
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

num_points = int(input("\nEnter the numer of points for the star :  "))
#llamamos a la funcion 
draw_star(200,my_turtle,num_points)

#para finalizar el programa cuando se acabe la estrella
turtle.done()