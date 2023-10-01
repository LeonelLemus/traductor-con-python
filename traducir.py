def cargar_diccionario(archivo):
  
    
    diccionario = {}
    try:
        with open(archivo, "r", encoding="utf-8") as archivo_diccionario:
            for linea in archivo_diccionario:
                clave, valor = linea.strip().split("=")
                diccionario[clave] = valor
    except FileNotFoundError:
        print("El archivo no existe. Creando un nuevo diccionario.")
    return diccionario

def guardar_diccionario(diccionario, archivo):
  
    with open(archivo, "w", encoding="utf-8") as archivo_diccionario:
        for clave, valor in diccionario.items():
            archivo_diccionario.write(f"{clave}={valor}\n")

def agregar_traduccion(diccionario, clave, valor):
    
    diccionario[clave] = valor

def traducir_palabra(diccionario, codigo_origen, codigo_destino, palabra):
   
    clave_busqueda = f"{codigo_origen}-{codigo_destino}"
    if clave_busqueda in diccionario:
        traduccion = diccionario[clave_busqueda]
        return f"{codigo_origen}-{codigo_destino} {palabra} --> {traduccion}"
    else:
        return "Traducción no encontrada."

if __name__ == "__main__":
    archivo_diccionario = "EN-ES.txt"
    diccionario = cargar_diccionario(archivo_diccionario)

    while True:
        print("\nMenú:")
        print("1. Agregar nueva traducción")
        print("2. Traducir palabra")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clave = input("Ingrese la palabra en inglés: ")
            valor = input("Ingrese la traducción al español: ")
            agregar_traduccion(diccionario, clave, valor)
            guardar_diccionario(diccionario, archivo_diccionario)
            print("Traducción agregada con éxito.")

        elif opcion == "2":
            codigo_origen = "EN"
            codigo_destino = "ES"
            palabra = input("Ingrese la palabra que desea traducir de Ingles a Español: ")
            resultado = traducir_palabra(diccionario, codigo_origen, codigo_destino, palabra)
            print(resultado)

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
