from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de notas disponíveis, de acordo com o enunciado
NOTAS_DISPONIVEIS = [100, 50, 20, 10, 5, 2]

def calcular_saque(valor, notas_disponiveis):

    #Calcula a quantidade de cédulas necessárias para realizar o saque.
    #Utiliza um algoritmo guloso para distribuição de cédulas.

    resultado = {}
    for nota in notas_disponiveis:
        quantidade, valor = divmod(valor, nota)
        resultado[str(nota)] = quantidade

    return resultado if valor == 0 else None


def saque_backtracking(valor, notas):
    #Resolve o problema do saque usando backtracking.
    #Retorna uma combinação válida de notas ou None, caso não possível.
    
    if valor == 0:
        return {}
    elif valor < 0 or not notas:
        return None

    nota_atual = notas[0]
    max_qtd = valor // nota_atual

    for qtd in range(max_qtd, -1, -1):
        restante = valor - qtd * nota_atual
        resultado_parcial = saque_backtracking(restante, notas[1:])
        if resultado_parcial is not None:
            resultado_parcial[str(nota_atual)] = qtd
            return resultado_parcial

    return None


@app.route('/api/saque', methods=['POST'])
def saque():
    #Endpoint para calcular a distribuição de notas para o valor requisitado.  
    
    try:
        # Validação dos dados recebidos
        dados = request.get_json()
        erro = validar_entrada(dados)
        if erro:
            return jsonify(erro), 400

        valor = dados['valor']

        # Calcula a distribuição de notas
        resultado = saque_backtracking(valor, NOTAS_DISPONIVEIS)
        if resultado is None:
            return jsonify({
                "erro": "Não é possível realizar o saque com as cédulas disponíveis."
            }), 400

        # Adiciona 0 para cédulas não usadas no resultado, uma forma de formatação
        resultado = {str(nota): resultado.get(str(nota), 0) for nota in NOTAS_DISPONIVEIS}

        return jsonify(resultado), 200

    except Exception as e:
        return jsonify({
            "erro": "Erro interno no servidor.",
            "detalhes": "Esse formato não é aceito."
        }), 500


def validar_entrada(dados):
    """
    Valida os dados da requisição, retornando uma mensagem de erro caso inválidos.
    """
    if not dados or 'valor' not in dados:
        return {
            "erro": "Campo 'valor' é obrigatório.",
            "detalhes": "Por favor, forneça o valor que deseja sacar."
        }
    
    try:
        valor = int(dados['valor'])
    except (ValueError, TypeError):
        return {"erro": "O valor deve ser um número inteiro positivo."}

    if valor <= 0:
        return {"erro": "O valor deve ser um número inteiro positivo."}
    elif valor < 2:
        return {"erro": "O valor mínimo para saque é R$ 2."}

    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
