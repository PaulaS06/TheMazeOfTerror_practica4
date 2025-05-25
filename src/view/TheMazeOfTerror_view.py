# from logic.TheMazeOfTerror_logic import Laberinto, Movimientos

import sys
sys.path.append("src")
from logic.TheMazeOfTerror_logic import Laberinto, Movimientos, ArbolRutasPosibles, NodoRutaFinal

def obtener_datos():
    n = input("Ingrese el valor de n: ")
    if n.isdigit() and int(n) > 0:
        return int(n)
    else: 
        print("Ingrese un valor válido")
        return obtener_datos()
    

def ejecutar_simulacion(laberinto):
    for persona in laberinto.personas:
        persona.posicion_actual = (persona.fila, persona.columna)
        persona.ruta_realizada.root = NodoRutaFinal(persona.posicion_actual)
        print(f"\nSimulando para persona en posición ({persona.fila}, {persona.columna}):")
        arbol = ArbolRutasPosibles()
        arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
        rutas = Movimientos.filtrar_rutas_llegan_salida(laberinto, arbol)
        persona.simular_movimiento(laberinto, arbol)


def menu():
    laberinto = None
    while True:
        print("\n--- Menú ---")
        print("1. Iniciar Laberinto")
        print("2. Colocar bloqueos")
        print("3. Colocar trampas")
        print("4. Colocar retrasadores")
        print("5. Visualizar estado actual del laberinto")
        print("6. Calcular la siguiente iteración")
        print("7. Salir del juego")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = obtener_datos()
            laberinto = Laberinto(n)
            laberinto.ubicar_salida()
            laberinto.generar_personas()
            laberinto.ubicar_persona()
            laberinto.ubicar_bloqueo()
            laberinto.ubicar_trampa()
            laberinto.ubicar_retraso()
            print("Laberinto inicial")
            print()
            print(laberinto)
            print()

        elif opcion == "2" and laberinto:
            laberinto.colocar_bloqueos_usuario()
        elif opcion == "3" and laberinto:
            laberinto.colocar_trampas_usuario()
        elif opcion == "4" and laberinto:
            laberinto.colocar_retrasadores_usuario()

        elif opcion == "5" and laberinto:
            print("Estado actual del laberinto:")
            print()
            print(laberinto)
            print()

        elif opcion == "6" and laberinto:
            laberinto.ejecutar_simulacion()

        elif opcion == "7":
            print("Saliendo del juego...")
            break
        
        elif laberinto is None:
            print("Inicie primero la simulación")
        else:
            print("Opción no válida")

def main():
    menu()


# print("\nEstado final del laberinto:")
# print(laberinto)

# print("\nRuta realizada por la persona:")
# persona.ruta_realizada.print()

if __name__ == "__main__":
    main()




# p = l.personas[0]
# tree = ArbolRutasPosibles()
# tree = Movimientos.crear_arbol_rutas_posibles(l, p, tree)
# tree.print(tree.root)
# rutas = Movimientos.filtrar_rutas_llegan_salida(l, tree)
# print("Rutas que llegan a la salida:")
# for i in rutas:
#     print(i)
# ruta_corta = Movimientos.buscar_ruta_mas_corta(l, tree)
# print("la ruta mas corta es:", ruta_corta)

# p.simular_movimiento(l, tree)
# print(l)