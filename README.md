# NL

_Write code with natural language_

# Como funciona

Bom, é isso mesmo que você viu acima, escreva código com linguagem natural.

Esse é um exemplo bem simples do que na verdade pretendo fazer.

Basicamente, nesse exemplo eu estou utilizando o modelo da OpenAI GPT-3.5-TURBO.

Onde passo algumas [instruções](./src/instructions.py) sobre como ele deve "compilar" o texto escrito em português.

# Como escrever "código"

Aqui temos algumas regras:

1. Todo arquivo `.nl` deve ter uma linha em branco no início e no final do arquivo
2. Cada linha deve ter no máximo 80 caracteres de tamanho [(configurável)](./src/syntax_checker.py).
3. O arquivo `.nl` não pode estar vazio
4. A tabulação deve ser feita com 4 espaços

Sabendo disso, nessa "linguagem" temos o que chamei de blocos.

```

Crie uma função chamada "repetir"

    crie uma variável chamada "i" com o valor inicial de 0

    faça um loop de 0 até 10 e para cada iteração incremente o valor de "i" com o
    produto do atual indíce com a atual variável "i" + 1
    e salve o resultado em um array.

    mostre os resultados no terminal um atrás do outro com
    uma linha em branco no final

```

1. Cada trecho de texto separado por uma linha em branco é um bloco.
2. Cada trecho de texto identado com 4 espaços está dentro do bloco superior

se fossemos traduzir o exemplo acima para python, ficaria algo como:

```python
def repetir():
    i = 0
    results = []
    for index in range(10):
        i = (index * i) + 1
        results.append(i)

    for result in results:
        print(result)

repetir()
```

> Como você deve imaginar, não seria necessário chamar solicitar que a função fosse chamada de "repetir" já que não vemos ela.

E o resultado será algo como:

```
1
2
5
16
65
326
1957
13700
109601
986410
```

# Minha ideia

Minha ideia inicial era ver a possibilidade de utilizar NLP (Natural Language Processing) para construir uma linguagem como essa.
Que seria interpretada, e não compilada.

De início poderia ter o código transformado em python por exemplo.

Não sou especialista em NLP, então, pesso que você compartilhe esse repositório e se desejar, pode criar uma issue com uma sugestão de implementação ou
que técnicas utilizar ou por onde começar a pesquisar.

Acredito que seria um projeto bem interessante e que poderia influenciar as pessoas que não programam a utilizar programação para tarefas simples.

> Imagine que você está precisando fazer um balanço de gastos e entrada rápido, bom, se você é programador é fácil
> Se você usar uma calculadora, também (para montantes pequenos)
> Agora imagine que você tem uma média de 200 registros para controlar
> Imagine como seria legal escrever um código em linguagem natural e construir um simples gerenciador de gastos e automatizar?

Esse é apenas um exemplo de algo divertido de fazer, mas poderia ser utilizado para várias outras pequenas tarefas do dia dia em que não queremos ficar pesquisando e descobrindo como faz, apenas escrever o que está na cabeça e boom, está pronto.

**Deixem sugestões ou links de projetos que já existam**

# Rodando um exemplo

0. Configure uma variável de ambiente chamada `OPENAI_API_KEY` com sua chave de api da open ai.
1. Inicie um novo ambiente `python3 venv -m venv`
2. Carrege o ambiente `source ./venv/bin/activate` (linux)
3. Instale as dependências `pip install -r requirements.txt`
4. Copie o exemplo anterior para um arquivo chamado `code.nl`.
5. Execute `./src/nl.py code.nl`.

# Curiosidades

Eu implementei um simples sistema de cache

Ou seja, da primeira vez irá levar um tempinho, mas, caso rode novamente, o resultado estará em cache então será beem mais rápido.
