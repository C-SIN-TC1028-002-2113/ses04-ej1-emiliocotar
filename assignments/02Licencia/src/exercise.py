def main():
    #escribe tu código abajo de esta línea

    edad=int(input("Ingresa tu edad: "))
    if edad>=18:
        id=input("¿Tienes identificación oficial? (s/n): ")
        if id=="s":
            print("Trámite de licencia concedido")
        elif id=="n":
            print("No cumples requisitos")  
        elif id!="n":
            print("Respuesta incorrecta") 
    elif edad<=0:
        print("Respuesta incorrecta")
    else:
        print("No cumples requisitos")



        
if __name__ == '__main__':
    main()
