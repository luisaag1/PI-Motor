Proyecto de sistemas embebidos. (Temas Selectos III)
===================================================

Control de velocidad de un motor de DC de imanes permanentes utilizando BeagleBone.

NOTA: La integral se debe de ajustar correctamente, se deben revisar a detalle los limites máximo y minimo de la misma y actualizar el programa.

Función del control:
--------------------

Cuando inicializa, lee el valor de un potenciometro para establecer el set point del motor. (Potenciometro conectado a P9_33)
El valor del set point, se va mostrando en pantalla, por lo que se puede cambiar variando el potenciometro.
El valor del set point debe ser voltaje y no velocidad angular. (Así se diseño el programa)

Una vez que el set point sea el deseado, se debe de presionar el botón que está conectado en P8_11.

Despues el usuario debe introducir valores de kp y ki.

El programa se queda esperando a que el usuario presione 1, para iniciar el control.

Cuando el control inicia, muestra en pantalla el valor de la retroalimentación y se va a detener cuando el error (error= set point- retroalimentacion) es igual a cero.

El control manda por medio de un PWM un voltaje necesario para que regular la velocidad del motor.


