# Resolvendo Códigos Python com o Copilot

Esse repositório tem como único e exclusivo objetivo, resolver o desafio de projeto da [DIO](https://web.dio.me/).

## Desafios

1 - Concatenando Dados

Descrição: Vamos receber dois dados diferentes do usuário e concatená-los em uma única string.

Resolução: Se uma usuário irá fornecer dois dados, podendo ser diferentes ou qualquer tipo de informação como string (textos), números (inteiros ou decimais), devemos tratar esses dados antes de realizar a ação que queremos, como a conversão de número para string, caso contrário, dependendo da forma que for programada, o código pode acabar somando dois números se utilizarmos o operador de soma (+) para concatenar os dados.

Com isso em mente, irei criar duas variáveis, a "primeiro_valor" e a "segundo_valor", para conseguir distinguir com facilidade as variáveis dentro do código e acabar confundindo elas.
Explicitarei o tipo da variável como string, usando o comando "[variável] : str", para deixar claro que o tipo de dado que quero receber é uma string.

Utilizarei o comando "input()" nas variáveis mencionadas anteriormente com uma mensagem orientando o usuário o que deve ser feito de maneira intuitiva. O ideal inclusive, seria criar uma variável para cada entrada, visto que caso eu queira alterar a mensagem posteriormente, ficaria mais fácil de localizar e alterar, principalemente por se tratar de uma mensagem constante.

Porém, apenas o comando "input()" não é suficiente, visto que o usuário pode inserir qualquer tipo de dado, como números inteiros ou decimais, e caso isso aconteça, o código pode acabar somando os dois números ao invés de concatenar eles. Para evitar isso, utilizarei o comando "str()" para converter qualquer tipo de dado que o usuário insira em uma string, evitando qualquer tipo de erro crítico que possa travar o código.

Para finalizar o código, o comando "print()" será utilizado para exibir o resultado final, concatenando (juntando) as duas variáveis com o valor inserido pelo usuário, utilizando o comando "+" para juntar as duas variáveis.

Mas para deixar o código mais flexível, irei fazer com que a concatenação seja armazenada em uma nova variável chamada "palavra_formada" e com a adição de um espaço entre as duas palavras, para que o resultado final fique mais legível para o usuário final.

2 - Repetindo Textos

Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetindo o número de vezes informado.

Solução: Um desafio simples, mas que pode ocasionar erros que podem travar o código, principalmente por se tratar de um valor de entrada como um número.

Como na última solução, irei criar duas variáveis para armazenar os valores do usuário, porém no lugar de definir a variável "segundo_valor" como string, irei definir ela como um número inteiro, utilizando o comando "int()", primeiro que, repetições não podem ser parciais, como por exemplo, repetir a palavra amor 2.5 vezes, segundo que, como iremos utilizar o operador de multiplicação (*) para repetir a string, o valor precisa ser um número inteiro, caso contrário, o código pode acabar travando.

Irei realizar os mesmos cuidados feitos anteriormente, e como o bônus solicitado pela professora de fazer com que tenha um espaço entre cada palavra repetida.

3 - Operações Matemáticas Simples

Descrição: Vamos solicitar como entrada de dois números e depois vamos realizar uma operação simples entre eles.

Solução: Diferente dos desafios anteriores, agora o usuário irá inserir três valores para que uma operação matemática seja realizada entre dois números, utilizando o terceiro valor como operador.

Vou deixar explicito o valor da variável "primeiro_valor" e "segundo_valor" como números decimais, utilizando o comando "float()", para que o usuário possa inserir tanto números inteiros quanto decimais, e a variável "operacao" como string, visto que o operador será inserido como um caractere.

Também poderia utilizar o comando if/elif/else para cada operação, mas como o desafio pede uma operação simples, irei utilizar o comando "match/case" para deixar o código mais limpo e organizado.

E assim como nos desafios anteriores, irei utilizar o comando "print()" para exibir o resultado final para o usuário. Porém desta vez precisei utilizar o comando "str()" para converter o resultado em string e conseguir concatenar com o restante da mensagem.
