# Práctica de Árboles desarrollada en las clases 10 y 11

from arbol import ArbolBinario

arbol = ArbolBinario()

opcion = 0
def intinput(string):
    bandera = False
    while not bandera:
        try:
            entero = int(input(string))
            bandera = True
        except ValueError:
            print("No es un entero válido")
    return entero

while opcion !=12:
    opcion= intinput("Digite la opcion que requiera: \n"
                      "1. Agregar \n"
                      "2. In-order \n"
                      "3. Buscar \n"
                      "4. Modificar \n"
                      "5. Eliminar \n"
                      "6. Pre_order\n"
                      "7. Post-order\n"
                      "8. Buscar mínimo\n"
                      "9. Buscar máximo\n"
                      "10. Altura del árbol\n"
                      "11. Convertir a lista\n"
                      "12. Salir \n: ")
    match opcion:
        case 1:
            numero = intinput("Digite el número que desea agregar: ")
            arbol.agregar(numero)
        case 2:
            arbol.in_order_traversal()
        case 3:
            numero = intinput("Digite el número que desea buscar: ")
            arbol.buscar_nodo(numero)
        case 4:
            arbol.eliminar(intinput("Digite el número que desea modificar: "))
            arbol.agregar(intinput("Digite el número por el cual lo desea cambiar: "))
        case 5:
            arbol.eliminar(intinput("Digite el número que desea eliminar: "))
        case 6:
            arbol.pre_order()
        case 7:
            arbol.post_order()
        case 8:
            print(arbol.buscar_minimo())
        case 9:
            print(arbol.buscar_maximo())
        case 10:
            print(arbol.altura_arbol())
        case 11:
            print(arbol.convertir_lista())
        case 12:
            print("Saliendo del programa... ")
        case _:
            print("Opción inválida")
