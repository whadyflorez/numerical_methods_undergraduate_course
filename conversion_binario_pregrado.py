# Conversión manual de decimal a binario
def decimal_a_binario_manual(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario  # Se concatena a la izquierda
        numero = numero // 2  # División entera
    return binario

# Conversión usando la función integrada bin()
def decimal_a_binario_python(numero):
    return bin(numero)[2:]  # bin() retorna una cadena como '0b1010', quitamos el '0b'


numero_decimal = int(input("Ingrese un número decimal: "))
        
# Método manual
binario_manual = decimal_a_binario_manual(numero_decimal)
print(f"Binario (manual): {binario_manual}")
        
# Método con función de Python
binario_funcion = decimal_a_binario_python(numero_decimal)
print(f"Binario (con bin()): {binario_funcion}")
    
