# from logic.TheMazeOfTerror_logic import Laberinto, Movimientos
import sys
sys.path.append("src")
from logic.TheMazeOfTerror_logic import Laberinto, Movimientos, Arbol, Nodo

def obtener_datos():
    n = input("\n🧮 Ingrese el valor de n: ")
    if n.isdigit() and int(n) > 0:
        return int(n)
    else: 
        print("\n⚠️ Ingrese un valor válido\n")
        return obtener_datos()

def show_menu_principal():
    print("\n-------- MENÚ PRINCIPAL --------")
    print("\n1️⃣  Iniciar Laberinto")
    print("2️⃣  Visualizar estado actual del laberinto")
    print("3️⃣  Calcular la siguiente iteración")
    print("4️⃣  Ver detalles de la simulación")
    print("5️⃣  Salir del juego\n")

def show_menu_secundario():
    print("\n-------- SEGUNDO MENÚ --------")
    print("\n🧠 Para más información de la simulación, elija una de las siguientes opciones:")
    print("\n1️⃣  Ver las posiciones recorridas por cada persona")
    print("2️⃣  Ver rutas que llegan a la salida por persona")
    print("3️⃣  Ver ruta más corta por persona")
    print("4️⃣  Ver las posibilidades de movimiento por persona")
    print("5️⃣  Mostrar estado actual del laberinto")
    print("6️⃣  Volver al menú principal\n")

def menu_principal():
    simulacion_iniciada = False 
    laberinto = None
    print("\n========================================")
    print("🎮 BIENVENIDO A THE MAZE OF TERROR 🧟‍♂️")
    print("========================================\n")

    while True:
        input("\n🔽 Presiona Enter para mostrar el menú... \n")
        show_menu_principal()
        opcion = input("\n🤔 Seleccione una opción: ")
        if opcion == "1":
            if simulacion_iniciada:
                print("\n🚫 La simulación ya fue iniciada. Salga de la simulación para iniciar una nueva.\n")
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
            print("\n🧩 Laberinto inicial 🧩\n")
            print(laberinto)
            print(f"\n🚪 La posición de la salida es: {laberinto.salida}")
        elif opcion == "2":
            if laberinto is None:
                print("\n⚠️ Inicie primero la simulación antes de realizar cualquier acción.\n")
                continue
            print("\n🧭 Estado actual del laberinto: \n")
            print(laberinto)
            print(f"\n🚪 La posición de la salida es: {laberinto.salida}")
        elif opcion == "3":
            if laberinto is None:
                print("\n⚠️ Inicie primero la simulación antes de realizar cualquier acción.\n")
                continue
            ejecutar_simulacion(laberinto)
            print("\n🔁 Estado del laberinto después de la simulación:\n")
            print(laberinto)
            print(f"\n🚪 La posición de la salida es: {laberinto.salida}")
        elif opcion == "4":
            if laberinto is None:
                print("\n⚠️ Inicie primero la simulación antes de realizar cualquier acción.\n")
                continue
            menu_secundario(laberinto)
        elif opcion == "5":
            print("\n👋 Saliendo del juego... ¡Hasta la próxima!\n")
            break
        else:
            print("\n❌ Opción no válida, intente nuevamente.\n")
            continue

def menu_secundario(laberinto):
    while True:
        input("\n🔽 Presiona Enter para mostrar el segundo menú... \n")
        show_menu_secundario()
        opcion = input("\n🤔 Seleccione una opción: ")
        if opcion == "1":
            for persona in laberinto.personas:
                print(f"\n🧍 Ruta de {persona.nombre}:")
                persona.ruta_realizada.print()
        elif opcion == "2":
            for persona in laberinto.personas:
                arbol = Arbol()
                arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
                arbol_rutas_salida = Movimientos.generar_arbol_rutas_llegan_salida(laberinto, arbol)
                print(f"\n🔍  Calculando las rutas que llegan a la salida para {persona.nombre} desde ({persona.fila}, {persona.columna})...")
                print(f"\n🛣️  Rutas que llegan a la salida para {persona.nombre}")
                arbol_rutas_salida.print(arbol_rutas_salida.root)
        elif opcion == "3":
            for persona in laberinto.personas:
                arbol = Arbol()
                arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
                arbol_ruta_corta = Movimientos.generar_arbol_rutas_mas_corta(laberinto, arbol)
                print(f"\n🔍  Calculando ruta más corta para {persona.nombre} desde ({persona.fila}, {persona.columna})...")
                print(f"\n🧭  Ruta más corta para {persona.nombre}")
                arbol_ruta_corta.print(arbol_ruta_corta.root)
        elif opcion == "4":
            for persona in laberinto.personas:
                arbol = Arbol()
                arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
                print(f"\n🔍  Calculando las rutas que puede tomar {persona.nombre} desde ({persona.fila}, {persona.columna})...")
                print(f"\n🔀  Posibilidades de movimiento para {persona.nombre}")
                arbol.print(arbol.root)
        elif opcion == "5":
            print("\n🧭 Estado actual del laberinto: \n")
            print(laberinto)
        elif opcion == "6":
            break
        else:
            print("\n❌ Opción no válida.\n")

def ejecutar_simulacion(laberinto):
    if len(laberinto.personas) == 0:
        print("\n🚷 No hay personas en el laberinto. Fin de la simulación.\n")
        return
    for persona in laberinto.personas:
        persona.posicion_actual = (persona.fila, persona.columna)
        persona.ruta_realizada.root = Nodo(persona.posicion_actual)
        print(f"\n🧍 Simulando para {persona.nombre} en posición ({persona.fila}, {persona.columna})")
        arbol = Arbol()
        arbol = Movimientos.crear_arbol_rutas_posibles(laberinto, persona, arbol)
        rutas = Movimientos.filtrar_rutas_llegan_salida(laberinto, arbol)
        persona.simular_movimiento(laberinto, arbol)
    laberinto.limpiar_laberinto_TBR()
    laberinto.ubicar_bloqueo()
    laberinto.ubicar_trampa()
    laberinto.ubicar_retraso()


def main():
    menu_principal()

if __name__ == "__main__":
    main()