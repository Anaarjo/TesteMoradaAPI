# TesteMoradaAPI
Este projeto é uma API simples construída em Flask que calcula a distribuição de cédulas para um valor de saque solicitado.
O objetivo é utilizar dois algoritmos principais para resolver o problema de saque de valores: algoritmo guloso e backtracking. 
A API valida as entradas e retorna as cédulas necessárias ou mensagens de erro quando o valor solicitado não pode ser atendido.

**Principais Funcionalidades**

Recebe uma requisição POST contendo o valor do saque.
Calcula a quantidade de cédulas necessárias para atender ao valor solicitado.
Utiliza um algoritmo guloso para distribuição de cédulas.
Se o algoritmo guloso não for suficiente, aplica um algoritmo de backtracking para encontrar uma combinação válida de cédulas.
Valida as entradas e retorna erros caso o valor seja inválido ou impossível de ser atendido.

**Algoritmos Usados**

Algoritmo Guloso: A aplicação tenta usar as cédulas maiores primeiro, utilizando um algoritmo guloso.
Backtracking: Quando o algoritmo guloso não consegue encontrar uma solução exata, a aplicação tenta uma solução alternativa usando backtracking.

***Desafios Principais***

*Implementação do Algoritmo:*

O algoritmo guloso pode falhar quando não existe uma solução exata para o valor solicitado. Por exemplo, o valor 3 não pode ser retirado com as cédulas disponíveis usando apenas o algoritmo guloso. Neste caso, o backtracking foi aplicado para contornar essa limitação.
Backtracking:

A implementação do backtracking exige uma abordagem recursiva, o que pode tornar o código mais complexo e aumentar o tempo de execução para valores grandes, mas é uma técnica essencial para garantir que soluções alternativas sejam encontradas.
Validação da Entrada:

Garantir que os dados recebidos sejam válidos foi um desafio, pois precisávamos tratar diversos casos de erro (campo ausente, valor inválido, valor menor que o mínimo, etc.).

**Performance:**

A solução de backtracking, embora eficaz, pode não ser a mais eficiente para valores muito altos. Melhorias em termos de otimização de performance podem ser necessárias para casos de uso mais exigentes.

**Instalação e Execução do Projeto**

*Pré-requisitos*

Python 3.x
pip para instalar dependências
Flask: Framework utilizado para criar a API.
Postman ou cURL: Ferramentas utilizadas para testar a API.

**Passo 1: Clone o repositório**
Clone o repositório para sua máquina local:

bash

git clone https://github.com/seu-usuario/saque-cedulas-api.git

**Passo 2: Instalar dependências**
Dentro do diretório do projeto, instale as dependências usando o pip:

bash cd saque-cedulas-api
pip install -r requirements.txt
No arquivo requirements.txt, você encontrará as dependências necessárias para rodar o projeto, incluindo o Flask.

**Passo 3: Executar o servidor**
Execute o servidor Flask para rodar a API:

bash python app.py
Isso iniciará o servidor na URL http://127.0.0.1:5000/.

**Passo 4: Testar a API**
Para testar a API, você pode usar o Postman ou cURL.

Baixe e instale o Postman (se ainda não o fez).
Abra o Postman e crie uma nova requisição POST.
Insira a URL http://127.0.0.1:5000/api/saque.
Na aba Body, escolha raw e selecione o formato JSON.
Insira o seguinte JSON no corpo da requisição:
Exemplo de requisição (POST)
URL: http://127.0.0.1:5000/api/saque

Cabeçalhos:

http
Content-Type: application/json
Corpo da requisição:

json
{
  "valor": 270
}
Resposta (200 OK):

json
{
  "100": 2,
  "50": 1,
  "20": 1,
  "10": 0,
  "5": 0,
  "2": 0
}
Resposta (400 Bad Request):

json
{
  "erro": "O valor deve ser um número inteiro positivo."
}
**Passo 5: Testes (opcional)**
Se você quiser rodar os testes para garantir que a API está funcionando corretamente, você pode usar o pytest.

Instale o pytest se ainda não o tiver:

|bash|
pip install pytest
Para rodar os testes:

|bash| pytest test_api.py
