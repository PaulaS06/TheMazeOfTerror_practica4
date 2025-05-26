import random

class Persona:
    def __init__(self, fila = -1, columna = -1):
        self.nombre = "Persona"
        self.fila = fila
        self.columna = columna
        self.direcciones_permitidas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.esta_retrasada = False       # será true si cae en un retraso, de esto depende que se mueva (PONER UN WHILE, MIENTRAS FALSE SE MUEVE)
        self.posicion_actual = None
        self.ruta_realizada = Arbol()
        self.posibilidad_rutas = Arbol()

    def simular_movimiento(self, laberinto, arbol):
        self.posibilidad_rutas = Movimientos.crear_arbol_rutas_posibles(laberinto, self, Arbol())
        ruta_ejecutar = Movimientos.buscar_ruta_mas_corta(laberinto, arbol)

        # if len(ruta_ejecutar) < 2:
        #     return

        nueva_pos = ruta_ejecutar[1]
        fila_nueva, col_nueva = nueva_pos

        if nueva_pos == laberinto.salida:
            laberinto.matriz[self.fila][self.columna] = "_"
            self.fila, self.columna = fila_nueva, col_nueva
            self.ruta_realizada.insert(self.posicion_actual, nueva_pos, "Salida")
            self.posicion_actual = nueva_pos
            print(f"🏁 Has llegado a la salida!!!")
            return

        if self.esta_retrasada:
            print("⏭️ Persona está retrasada. Turno perdido.")
            self.esta_retrasada = False
            return

        laberinto.matriz[self.fila][self.columna] = "_"

        if laberinto.matriz[fila_nueva][col_nueva] == "T":
            if self.direcciones_permitidas:
                movimiento_perdido = random.choice(self.direcciones_permitidas)
                self.direcciones_permitidas.remove(movimiento_perdido)
                print(f"Trampa activada. Se perdió el movimiento: {movimiento_perdido}")
            else:
                print("No hay movimientos disponibles para moverse, la persona quedará siendo un obstaculo en la posición actual.")
                
        elif laberinto.matriz[fila_nueva][col_nueva] == "R":
            self.esta_retrasada = True
            print("⏳ Pierde un turno.")

        anterior_pos = self.posicion_actual  # Guarda la posición anterior
        self.ruta_realizada.insert(anterior_pos, nueva_pos)  # Inserta con la posición anterior como padre
        self.posicion_actual = nueva_pos  # Luego actualiza la posición actual
        self.fila = fila_nueva
        self.columna = col_nueva
        laberinto.matriz[self.fila][self.columna] = self
        print(f"✅ Se movió a {nueva_pos}")

    def __repr__(self):
        return "🧍"


class Laberinto:
    def __init__(self, n):
        self.n = n
        self.matriz = self.generar_matriz()
        self.salida = None
        self.personas = []

    def generar_matriz(self):
        matriz = []
        for i in range(self.n):
            fila = []
            for j in range(self.n):
                fila.append("_")
            matriz.append(fila)
        return matriz

    def posiciones_matriz(self):  # Retorna TODAS las posiciones de la matriz
        posiciones = []
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                posiciones.append((i, j))
        return posiciones

    def ubicar_salida(self):
        posiciones = self.posiciones_matriz()
        posicion_salida = random.choice(posiciones)
        self.matriz[posicion_salida[0]][posicion_salida[1]] = "🏁"
        self.salida = posicion_salida

    def generar_personas(self):
        cantidad_personas =  1
        for i in range(cantidad_personas):
            persona = Persona()
            persona.nombre = f"Persona {i + 1}"
            self.personas.append(persona)

    def ubicar_persona(self):
        posiciones = self.posiciones_matriz()

        if self.salida in posiciones:
            posiciones.remove(self.salida)

        for persona in self.personas:
            posicion_inicial_persona = random.choice(posiciones)

            if self.matriz[posicion_inicial_persona[0]][posicion_inicial_persona[1]] == "_":
                posiciones.remove(posicion_inicial_persona)
                self.matriz[posicion_inicial_persona[0]][posicion_inicial_persona[1]] = persona
                persona.fila = posicion_inicial_persona[0]
                persona.columna = posicion_inicial_persona[1]
                persona.posicion_actual = posicion_inicial_persona

    def ubicar_trampa(self):
        posiciones = self.posiciones_matriz()

        if self.salida in posiciones:
            posiciones.remove(self.salida)

        for i in range(self.n - 1):
            posicion_trampa = random.choice(posiciones)

            if self.matriz[posicion_trampa[0]][posicion_trampa[1]] == "_":
                posiciones.remove(posicion_trampa)
                self.matriz[posicion_trampa[0]][posicion_trampa[1]] = "T"

    def ubicar_bloqueo(self):
        posiciones = self.posiciones_matriz()
        if self.salida in posiciones:
            posiciones.remove(self.salida)
        for i in range(self.n - 1):
            posicion_bloqueo = random.choice(posiciones)
            if self.matriz[posicion_bloqueo[0]][posicion_bloqueo[1]] == "_":
                posiciones.remove(posicion_bloqueo)
                self.matriz[posicion_bloqueo[0]][posicion_bloqueo[1]] = "❌"

    def ubicar_retraso(self):
        posiciones = self.posiciones_matriz()
        if self.salida in posiciones:
            posiciones.remove(self.salida)
        for i in range(self.n - 1):
            posicion_retraso = random.choice(posiciones)
            if self.matriz[posicion_retraso[0]][posicion_retraso[1]] == "_":
                posiciones.remove(posicion_retraso)
                self.matriz[posicion_retraso[0]][posicion_retraso[1]] = "R"
        
    def limpiar_laberinto_TBR(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matriz[i][j] == "T" or self.matriz[i][j] == "R" or self.matriz[i][j] == "❌":
                    self.matriz[i][j] = "_"

    def __str__(self):
        resultado = []
        for fila in self.matriz:
            fila_str = "   ".join(str(celda) for celda in fila)
            resultado.append(fila_str)
        return "\n\n".join(resultado)


class Nodo:
    def __init__(self, posicion: tuple, children: list = []):
        self.value = posicion  # En este voy a almacernar una tupla con la posicion
        self.children = children

class Arbol:
    def __init__(self, root: Nodo = None):
        self.root = root

    def insert(self, parent, child, current_node = None):
        if (self.root is None):
            new_root = Nodo(parent)
            self.root = new_root
            new_child = Nodo(child)
            self.root.children.append(new_child)
            return

        por_visitar = []
        visitados = []

        if current_node is None:
            current_node = self.root
            por_visitar.append(current_node)

        while por_visitar:
            visitados.append(current_node)
            current_node = por_visitar.pop()

            for children in current_node.children:
                por_visitar.append(children)

            if (current_node.value == parent):
                new_child = Nodo(child)
                current_node.children.append(new_child)
                return 
        return

    def print(self, node=None, prefix="", is_last=True):
        if node is None:
            node = self.root
            if node is None:
                print("Árbol vacío")
                return
        print(prefix + ("└── " if is_last else "├── ") + str(node.value))
        new_prefix = prefix + ("    " if is_last else "│   ")
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            is_last_child = (i == child_count - 1)
            self.print(child, new_prefix, is_last_child)


class Movimientos:

    @staticmethod
    def crear_arbol_rutas_posibles(laberinto, persona, arbol, current_pos = None, visitados = None):
        if current_pos is None:
            current_pos = (persona.fila, persona.columna)   # es decir la posicion original de la persona
            arbol.root = Nodo(current_pos)
            visitados = []
        visitados.append(current_pos)
        if current_pos == laberinto.salida:
            return arbol

        posiciones_a_mover = []

        for i, j in persona.direcciones_permitidas:
            fila = current_pos[0] + i
            columna = current_pos[1] + j
            if (0 <= fila < laberinto.n) and (0 <= columna < laberinto.n):
                nueva_pos = (fila, columna)
                if laberinto.matriz[nueva_pos[0]][nueva_pos[1]] != "❌" and not isinstance(laberinto.matriz[nueva_pos[0]][nueva_pos[1]], Persona):
                    posiciones_a_mover.append(nueva_pos)
        if len(posiciones_a_mover) == 0:
            print("ay muchachos...")
            return arbol
        for siguiente_pos in posiciones_a_mover:
            if siguiente_pos not in visitados:
                arbol.insert(current_pos, siguiente_pos)
                Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol, siguiente_pos, visitados)
                visitados.pop()
        return arbol

    @staticmethod
    def filtrar_rutas_llegan_salida(laberinto, arbol, current_node = None, ruta_actual = None, rutas = None):
        if ruta_actual is None:
            ruta_actual = []
        if rutas is None:
            rutas = []

        if current_node is None:
            current_node = arbol.root

        ruta_actual.append(current_node.value)

        if current_node.value == laberinto.salida:
            rutas.append((ruta_actual[:]))
        else:
            for child in current_node.children:
                Movimientos.filtrar_rutas_llegan_salida(laberinto, arbol, current_node = child, ruta_actual = ruta_actual, rutas = rutas)
        ruta_actual.pop()
        return rutas

    @staticmethod
    def generar_arbol_rutas_llegan_salida(laberinto, arbol):
        rutas = Movimientos.filtrar_rutas_llegan_salida(laberinto, arbol)
        if not rutas:
            print("Ay muchachos... No hay rutas que lleguen a la salida.")
            return 
        
        arbol_rutas_llegan_salida = Arbol()
        
        for ruta in rutas:
            for i in range(1, len(ruta)):
                padre = ruta[i - 1]
                hijo = ruta[i]
                arbol_rutas_llegan_salida.insert(padre, hijo)
        return arbol_rutas_llegan_salida

    @staticmethod
    def buscar_ruta_mas_corta(laberinto, arbol):
        rutas = Movimientos.filtrar_rutas_llegan_salida(laberinto, arbol)
        if not rutas:
            print("Ay muchachos... No hay rutas que lleguen a la salida.")
            return 
        return min(rutas, key = len)

    @staticmethod
    def generar_arbol_rutas_mas_corta(laberinto, arbol):
        ruta_mas_corta = Movimientos.buscar_ruta_mas_corta(laberinto, arbol)
        if not ruta_mas_corta:
            print("Ay muchachos... No hay rutas que lleguen a la salida.")
            return 
        arbol_ruta_mas_corta = Arbol()
        
        for i in range(1, len(ruta_mas_corta)):
            padre = ruta_mas_corta[i - 1]
            hijo = ruta_mas_corta[i]
            arbol_ruta_mas_corta.insert(padre, hijo)
        return arbol_ruta_mas_corta