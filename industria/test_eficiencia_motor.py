from eficiencia_motor import *

def test_calcular_eficiencia():
    assert calcular_eficiencia (900, 1000) == 90.0
    assert calcular_eficiencia(855, 100) == 85.5
    assert calcular_eficiencia(0, 1000) == False

def test_classificar_eficiencia():
    assert classificar_eficiencia (75.0) == "IE1 - Baixa eficiência".
    assert classificar_eficiencia (85.0) == "IE2 - Eficiência média".
    assert classificar_eficiencia (92.0) == "IE3 - Alta eficiência".

def test_analise_motor_integracao():
    resultado = analise_motor(880, 1000)
    assert resultado["eficiencia"] == 88.0
    assert resultado["classificacao"] == "IE2 - Eficiencia media"