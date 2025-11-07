def calcular_eficiencia(potencia_saida, potencia_entrada):
    if potencia_entrada <=0:
        raise ValueError
    eficiencia = (potencia_saida/potencia_entrada) * 100
    return round(eficiencia, 2)

def classificar_eficiencia(eficiencia):
    """
    Classifica a eficiencia conforme os padrões siplificados(didáticos):
    -Abaixo de 80% = IE1 (Baixa eficiência)
    -Entre 80 e 89.9% = IE2 (Eficiência média)
    -90% ou mais = IE3 (Alta eficiência)
    """
    if eficiencia < 80:
        return "IE1 - Baixa eficiência"
    
    elif eficiencia < 90:
        return "ie2 - Eficiência média"

    else:
        return "IE3 _ Alta eficiência"

def analise_motor(potencia_saida, potencia_entrada):
    "Funcção principal: retorna dicionário com os resultados."""
    eficiencia = calcular_eficiencia(potencia_saida, potencia_entrada)
    classificacao = classificar_eficiencia(eficiencia)
    return{
        "potencia_saida": potencia_saida,
        "potencia_entrada" : potencia_entrada,
        "eficiencia": eficiencia,
        "classificacao": classificacao,
    }