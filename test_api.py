import pytest
from app import app  # Importa a aplicação Flask

# Configura o cliente de teste do Flask
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Testes para a rota /api/saque
@pytest.mark.parametrize("json_data, expected_status, expected_response", [
    # Cenário: Campo 'valor' ausente
    ({}, 400, {
        "erro": "Campo 'valor' é obrigatório.",
        "detalhes": "Por favor, forneça o valor que deseja sacar."
    }),
    # Cenário: Valor inválido (string)
    ({"valor": "z"}, 400, {
        "erro": "O valor deve ser um número inteiro positivo."
    }),
    # Cenário: Valor negativo
    ({"valor": -10}, 400, {
        "erro": "O valor deve ser um número inteiro positivo."
    })
])
def test_saque_invalid_inputs(client, json_data, expected_status, expected_response):
    """Testa cenários de entradas inválidas para o endpoint /api/saque."""
    response = client.post('/api/saque', json=json_data)
    assert response.status_code == expected_status
    assert response.json == expected_response
