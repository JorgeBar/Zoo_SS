from app.vistas import VistaEntrada, VistaGrupo
from app.modelos import Grupo_Entrada
from simple_screen import DIMENSIONS , cls , locate , Input, Screen_manager


with Screen_manager:
    #Instaciamos lo necesario,modelos y componentes gráficos
    grupo_entradas = Grupo_Entrada()
    x = (DIMENSIONS.w - 37) //2

    vista_grupo = VistaGrupo(grupo_entradas ,x ,1)
    entrada_edad = VistaEntrada("EDAD: ", x,10)
    entrada_seguir = VistaEntrada("Otra vez (S/N): ",x,12)

    #Bucle de pantalla
    while True:
        cls()
        vista_grupo.paint()
        edad = entrada_edad.paint()
        if edad == "":
            respuesta = entrada_seguir.paint()
            if respuesta == "S":
                grupo_entradas = Grupo_Entrada()
                vista_grupo.grupo = grupo_entradas
                continue
            else:
                break



        edad = int(edad)    
        grupo_entradas.add_entrada(edad)
        

    #Final controlado del programa
    locate(1, DIMENSIONS.h -2)  
    Input("Pulse enter para salir")  
    