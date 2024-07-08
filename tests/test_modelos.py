from app.modelos import Entrada, TipoEntrada

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