from flask import Flask, jsonify, request
import requests
from datetime import datetime
app = Flask(__name__)

API_KEY = '42fde131d519c8ac03b79872'  # Substitua pela sua chave de API do ExchangeRate-API
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair'


@app.route('/')
def home():
    return jsonify({
        'message': 'Bem-vindo à API de Cotação de Moedas!',
        'endpoints': {
            '/cotacao': 'Obtenha a cotação de uma moeda em relação a outra'
        },
        'instructions': 'Use /cotacao?moeda_origem=USD&moeda_destino=BRL para consultar as cotações.',
        'status': 'Em funcionamento'
    }), 200


@app.route('/cotacao', methods=['GET'])
def get_cotacao():
    moeda_origem = request.args.get('moeda_origem', 'USD')
    moeda_destino = request.args.get('moeda_destino', 'BRL')

    url = f'{BASE_URL}/{moeda_origem}/{moeda_destino}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data.get('result') == 'success':
            cotacao = data.get('conversion_rate')
            return jsonify({
                'moeda_origem': moeda_origem,
                'moeda_destino': moeda_destino,
                'cotacao': cotacao,
                'data_hora': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'mensagem': f'A cotação de {moeda_origem} para {moeda_destino} é {cotacao}.'
            })
        else:
            return jsonify({'erro': 'Estrutura inesperada na resposta', 'resposta': data}), 500
    else:
        return jsonify({'erro': 'Não foi possível obter a cotação', 'status_code': response.status_code}), 500


if __name__ == '__main__':
    app.run(debug=True)