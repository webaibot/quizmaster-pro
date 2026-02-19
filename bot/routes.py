from flask import jsonify, request, render_template
from flask_cors import CORS
from .engine import QuizEngine

CORS_HEADERS = {'Access-Control-Allow-Origin': '*'}

quiz_engine = QuizEngine()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html', bot_name='QuizMaster Pro')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    session_id = request.json.get('session_id', '')
    response = quiz_engine.process_input(user_input, session_id)
    return jsonify(response), 200, CORS_HEADERS

@app.route('/api/health')
def health_check():
    return jsonify(status='healthy'), 200, CORS_HEADERS

@app.route('/api/stats')
def stats():
    stats = quiz_engine.get_statistics()
    return jsonify(stats), 200, CORS_HEADERS
