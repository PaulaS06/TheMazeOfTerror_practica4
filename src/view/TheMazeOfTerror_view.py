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
    

def menu_secundario(laberinto):
    while True:
        print("\nPara más información de la simulación, elija una de las siguientes opciones:")
        print("\n--- Menú Simulación ---")
        print("\n1. Ver las posiciones recorridas por cada persona")
        print("2. Ver rutas que llegan a la salida por persona")
        print("3. Ver ruta más corta por persona")
        print("4. Ver las posibilidades de movimiento por persona")

        print("5. Mostrar estado actual del laberinto")
        print("6. Volver al menú principal")
        print()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for persona in laberinto.personas:
                print(f"\nRuta de {persona.nombre}:")
                persona.ruta_realizada.print()
        elif opcion == "2":
            for persona in laberinto.personas:
                arbol = ArbolRutasPosibles()
                arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
                arbol_rutas_salida = Movimientos.generar_arbol_rutas_llegan_salida(laberinto, arbol)
                print(f"\n🔍 Calculando las rutas que llegan a la salida para {persona.nombre} desde ({persona.fila}, {persona.columna})...")
                print(f"\nRutas que llegan a la salida para {persona.nombre})")
                arbol_rutas_salida.print(arbol_rutas_salida.root)
        elif opcion == "3":
            for persona in laberinto.personas:
                arbol = ArbolRutasPosibles()
                arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
                arbol_ruta_corta = Movimientos.generar_arbol_rutas_mas_corta(laberinto, arbol)
                print(f"\n🔍 Calculando ruta más corta para {persona.nombre} desde ({persona.fila}, {persona.columna})...")
                print(f"\nRuta más corta para {persona.nombre}")
                arbol_ruta_corta.print(arbol_ruta_corta.root)
        elif opcion == "4":
            for persona in laberinto.personas:
                arbol = ArbolRutasPosibles()
                arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
                print(f"\n🔍 Calculando las rutas que puede tomar {persona.nombre} desde ({persona.fila}, {persona.columna})...")
                print(f"\nPosibilidades de movimiento para {persona.nombre}")
                arbol.print(arbol.root)
        elif opcion == "5":
            print("\nEstado actual del laberinto:")
            print(laberinto)
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")



def ejecutar_simulacion(laberinto):
    if len(laberinto.personas) == 0:
        print("No hay personas en el laberinto. Fin de la simulación.")
        return
    
    for persona in laberinto.personas:
        persona.posicion_actual = (persona.fila, persona.columna)
        persona.ruta_realizada.root = NodoRutaFinal(persona.posicion_actual)
        print(f"\nSimulando para persona en posición ({persona.fila}, {persona.columna}):")
        arbol = ArbolRutasPosibles()
        arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
        rutas = Movimientos.filtrar_rutas_llegan_salida(laberinto, arbol)
        persona.simular_movimiento(laberinto, arbol)
    # Vamos a cambiar de puesto las trampas, bloqueos y retrasos para la siguiente iteración
    laberinto.limpiar_laberinto_TBR()
    laberinto.ubicar_bloqueo()
    laberinto.ubicar_trampa()
    laberinto.ubicar_retraso()

def show_menu():
    print("\n--- Menú ---")
    print("1. Iniciar Laberinto")
    print("2. Colocar bloqueos X")
    print("3. Colocar trampas X")
    print("4. Colocar retrasadores X")
    print("5. Visualizar estado actual del laberinto")
    print("6. Calcular la siguiente iteración")
    print("7. --- Ver detalles de la simulación")
    print("8. Salir del juego")
    print()

def menu_principal():
    simulacion_iniciada = False 
    laberinto = None
    print()
    print("================================")
    print("BIENVENIDO A THE MAZE OF TERROR")
    print("================================")

    while True:
        input("\nPresiona Enter para mostrar el menú...")
        show_menu()
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if simulacion_iniciada:
                print()
                print("La simulación ya fue iniciada. Salga de la simulación para iniciar una nueva.")
                return 
            
            n = obtener_datos()
            laberinto = Laberinto(n)
            laberinto.ubicar_salida()
            laberinto.generar_personas()
            laberinto.ubicar_persona()
            laberinto.ubicar_bloqueo()
            laberinto.ubicar_trampa()
            laberinto.ubicar_retraso()
            simulacion_iniciada = True
            print("Laberinto inicial")
            print()
            print(laberinto)
            print()


        elif opcion == "2":
            if laberinto is None:
                print()
                print("Inicie primero la simulación antes de realizar cualquier acción.")
                continue
            laberinto.colocar_bloqueos_usuario()
        elif opcion == "3":
            if laberinto is None:
                print()
                print("Inicie primero la simulación antes de realizar cualquier acción.")
                continue
            laberinto.colocar_trampas_usuario()
        elif opcion == "4":
            if laberinto is None:
                print()
                print("Inicie primero la simulación antes de realizar cualquier acción.")
                continue
            laberinto.colocar_retrasadores_usuario()


        elif opcion == "5":
            if laberinto is None:
                print()
                print("Inicie primero la simulación antes de realizar cualquier acción.")
                continue
            print("Estado actual del laberinto:")
            print()
            print(laberinto)
            print()

        elif opcion == "6":
            if laberinto is None:
                print()
                print("Inicie primero la simulación antes de realizar cualquier acción.")
                continue
            ejecutar_simulacion(laberinto)
            print("\nEstado  del laberinto después de la simulación:\n")
            print(laberinto)
            print()
        
        elif opcion == "7":
            if laberinto is None:
                print()
                print("Inicie primero la simulación antes de realizar cualquier acción.")
                continue
            menu_secundario(laberinto)

        elif opcion == "8":
            print()
            print("Saliendo del juego...")
            break

        else:
            print("Opción no válida, intente nuevamente.")
            continue


def main():
    menu_principal()

if __name__ == "__main__":
    main()