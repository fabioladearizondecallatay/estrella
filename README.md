Para dibujar una estrella de x puntas he empezado por importar el modulo turtle que me permite hacer grafismos.

Primero he definido la funcion draw_star que tiene tres varibales.

- La varibale size, que va en funcion de la talla elegida, dibujar la estrela mas grande o mas pequena.
- La varibale t que es la instacia que dibuja la tortuga.
- La varibale num_points que es el numero de puntas que tiene la estrela, que se pregunta con un input y se usaz para calcular los angulos de las puntas y el numero de veces que se hace el bucle.
- 
Luego hacemos un loop con "for _ in range (9)" para que se haga un bucle de lineas del numero de num_points. Vamos a usar "t" para definir que tiene que avanzar hacia alante en funcion de la talla de la tortuga "size" y que tiene que hacer un giro del angulo que se calcula con num_points. 
  
Luego definimos parametros para hacer nuestra estrella como queramos con turtle (la velocidad, la talla del marcador y el colord de la estrella. Tambien he querido definir una nueva varibale "my_turtle" para transformar la flecha que dibuja mi estrella en una tortuga usando "my_turle.shape"

Acabamos llamando la funcion draw_star para que haga el dibujo y luego ponemos turtle.done para quese cierre ezl programa cuando se ha dibujado la estrella.
