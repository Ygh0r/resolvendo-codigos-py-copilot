# Repetindo Textos

# Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. 
# Depois teremos que retornar a string repetindo o número de vezes informado.

# Constantes para melhor visualização e alteração futura do código.
MENSAGEM_APRESENTAÇÃO = "Bem-vindo ao programa de repetição de texto!"
PRIMEIRA_MENSAGEM = "Insira a palavra que deseja repetir: "
SEGUNDA_MENSAGEM = "Insira a quantidade de vezes que desejar repetir a palavra: "

# Primeira e segunda entrada do usuário. Sendo a segunda, convertida em inteiro.
primeiro_valor : str = str(input(PRIMEIRA_MENSAGEM))
segundo_valor : int = int(input(SEGUNDA_MENSAGEM))

# Multiplicação da string pelo número inteiro, com um espaço entre as repetições.
palavra_formada = (primeiro_valor + " ") * segundo_valor

# Impressão do resultado final.
print(palavra_formada)