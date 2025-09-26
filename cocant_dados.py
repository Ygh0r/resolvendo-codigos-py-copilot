# Desafio 1, Concatenando Dados.
# Vamos receber dois dados diferentes do usuário e concatená-los em uma única string.

# Constantes para melhor visualização e alteração futura do código.
MENSAGEM_APRESENTAÇÃO = "Bem-vindo ao programa de concatenação de dados!"
PRIMEIRA_MENSAGEM = "Insira um valor de sua escolha: "
SEGUNDA_MENSAGEM = "Insira outro valor: "

# Primeira e segunda entrada do usuário.
print(MENSAGEM_APRESENTAÇÃO)
primeiro_valor = str(input(PRIMEIRA_MENSAGEM))
segundo_valor = str(input(SEGUNDA_MENSAGEM))

# Armazenamento da palavra concatenada com espaço no meio
palavra_formada = primeiro_valor + " " + segundo_valor

# Exibição do resultado.
print(palavra_formada)