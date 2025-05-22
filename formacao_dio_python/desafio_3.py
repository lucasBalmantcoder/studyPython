# Recebe a entrada do usuário como uma string e divide essa string nos caracteres ',' (vírgula),
temperaturas_celsius = input().split(',')

# função chamada converter_celsius_para_fahrenheit que recebe uma lista de strings
def converter_celsius_para_fahrenheit(temperaturas_celsius):
    temperaturas_celsius = [float(temp) for temp in temperaturas_celsius]
    
    # TODO: Calcule as temperaturas em Fahrenheit para cada temperatura em Celsius convertida para float
    temperaturas_fahrenheit = []
    for temp in temperaturas_celsius:
        temperatura_fahrenheit = (temp * 9/5) + 32
        temperaturas_fahrenheit.append(temperatura_fahrenheit)
    
    # fórmula matemática:

    # TF = (TC × 9/5) + 32

    # Onde:
    
    # TF representa a temperatura em graus Fahrenheit,
    # TC representa a temperatura em graus Celsius.

    
    return temperaturas_fahrenheit

# Imprime o resultado das temperaturas convertidas para Fahrenheit.
print(converter_celsius_para_fahrenheit(temperaturas_celsius))