from app.modelos import Entrada, TipoEntrada ,  Grupo_Entrada

def test_crear_entrada():
    
    entrada = Entrada(12) 
    assert entrada.tipo == TipoEntrada.Niño
    assert entrada.precio == 14

    entrada = Entrada(35)
    assert entrada.tipo ==  TipoEntrada.Adulto
    assert entrada.precio == 23

    entrada = Entrada(70)
    assert entrada.tipo == TipoEntrada.Jubilado
    assert entrada.precio == 18

    entrada = Entrada(1)
    assert entrada.tipo == TipoEntrada.Bebe
    assert entrada.precio == 0

def xtest_crear_entrada_edad_negativa_error():
    pass

def test_crear_grupo_entradas():
    grupo = Grupo_Entrada()
    assert grupo.total == 0
    assert grupo.numero_entradas == 0

def test_anyadir_entradas_a_grupos():
    grupo = Grupo_Entrada()
    grupo.add_entrada(35)  
    assert grupo.numero_entradas == 1
    assert grupo.total == 23
    grupo.add_entrada(12)
    assert grupo.numero_entradas == 2
    assert grupo.total == 37 
    grupo.add_entrada(70)
    assert grupo.numero_entradas == 3
    assert grupo.total == 55
    grupo.add_entrada(2)
    assert grupo.numero_entradas == 4
    assert grupo.total == 55