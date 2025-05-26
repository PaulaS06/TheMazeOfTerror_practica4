# TheMazeOfTerror_practica4
🌀The Maze of Terror🌳

**Contexto del Juego**
Un grupo de M personas está atrapado en un laberinto dinámico de tamaño NxN. Existe solo una salida, ubicada aleatoriamente en la matriz.
Cada persona intentará escapar, pero el laberinto colocará dinámicamente bloqueos, trampas y retrasadores, dificultando su objetivo de sobrevivir.🕹

**Reglas del Juego**
● Inicialmente, cada persona se ubica en una posición aleatoria de la matriz.
● En cada iteración:
○ Cada persona calcula la ruta más corta hacia la salida, utilizando estructuras tipo árbol.
○ Las personas solo se mueven una celda por iteración, incluyendo diagonales si están disponibles.
● Cada iteración, el laberinto atacará colocando de manera aleatoria bloqueos, trampas o retrasadores.

📌 Efectos de Elementos en el Laberinto
● Bloqueos (muros):
○ Impiden totalmente el paso y se consideran celdas bloqueadas en el cálculo de ruta.
● Trampas:
○ Al activarse, hacen que la persona afectada pierda permanentemente una dirección aleatoria de movimiento (arriba, abajo, izquierda, derecha o diagonales).
○ Las trampas no bloquean la celda para el cálculo de ruta.
● Retrasadores:
🎯

 ○ Al activarse, hacen que la persona pierda un turno.
○ Tampoco bloquean la celda para el cálculo de ruta.
Si la ruta hacia la salida deja de existir debido a bloqueos, el personaje declara "ay muchachos..." y deja de moverse, aceptando su destino.
🎨
Visualización
Es clave que en cada iteración, por cada persona:
● Se visualice claramente el laberinto en consola o interfaz gráfica.
● Se destaque en un color llamativo la ruta completa desde la posición actual de cada persona hasta la salida.
● Los elementos del laberinto deben distinguirse claramente:
○ Personas: caracteres o iconos específicos.
○ Salida: un símbolo claro (ej: ). 🏁
○ Bloqueos: celdas rellenas en negro o símbolos tipo "X".
○ Trampas: símbolos diferentes, como "T".
○ Retrasadores: símbolos diferentes, como "R". Recuerda:
● Solo los bloqueos afectan el cálculo de la ruta más corta.
● Las trampas y retrasadores se deben ver claramente en el mapa pero no afectan la
elección de ruta.
📋
Menú Interactivo
La aplicación deberá contar con un menú que permita al usuario:
1. Iniciar simulación: comienza el juego con posiciones aleatorias de salida y personajes.

 2. Colocar bloqueos: permitir al usuario definir posiciones arbitrarias para nuevos bloqueos.
3. Colocar trampas: permitir al usuario definir posiciones arbitrarias para nuevas trampas.
4. Colocar retrasadores: permitir al usuario definir posiciones arbitrarias para nuevos retrasadores.
5. Visualizar estado actual del laberinto.
6. Ejecutar siguiente iteración: recalcula rutas y actualiza posiciones.
7. Salir del juego.
⚙
Estructuras Técnicas Requeridas Árbol de Rutas:
●
○ Representar la ruta más corta calculada en cada iteración mediante árboles (BFS o Dijkstra).
●
Árbol Histórico de Decisiones:
○ Cada persona deberá mantener un registro en forma de árbol que registre
todas las decisiones tomadas en cada iteración:
■ Nodo raíz: posición inicial del personaje.
■ Cada nodo: celda visitada con información sobre la iteración y
dirección elegida.
■ Ramas: representan decisiones alternativas disponibles desde cada
celda.
○ Este árbol permitirá analizar posteriormente la lógica detrás de cada decisión
tomada por los personajes.
🌟
 
