# 3 - Operações Matemáticas Simples

# Descrição: Vamos solicitar como entrada de dois números e depois vamos realizar uma operação simples entre eles.

# Constantes para melhor visualização e alteração futura do código.
MENSAGEM_APRESENTAÇÃO : str = "Bem-vindo a nossa mini-calculadora!"
PRIMEIRA_MENSAGEM : str = "Insira um número qualquer: "
SEGUNDA_MENSAGEM : str = "Insira outro número qualquer: "
TERCEIRA_MENSAGEM : str = "Agora escolha a operação que deseja realizar (+, -, *, /): "
MENSAGEM_RESULTADO : str = "O resultado da operação foi: "


# Três entradas do usuário. Sendo as duas primeiras valores inteiros, e a terceira, o operador de cálculo.
primeiro_valor : float = float(input(PRIMEIRA_MENSAGEM))
segundo_valor : float = float(input(SEGUNDA_MENSAGEM))
operador : str = str(input(TERCEIRA_MENSAGEM))
resultado : float = 0

# De acordo com o operador que o usuário escolher, irá realizar a op2eração matemática desejada,
# e ao realizar a subtração, irá retornar o valor absoluto da subtração.
match operador:
    case "+":
        resultado = primeiro_valor + segundo_valor
    case "-":
        resultado = abs(primeiro_valor - segundo_valor)
    case "*":
        resultado = primeiro_valor * segundo_valor
    case "/":
        resultado = primeiro_valor / segundo_valor

# Impressão do resultado final.
print(MENSAGEM_RESULTADO + str(resultado))