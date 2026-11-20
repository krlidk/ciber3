import os
from flask import Flask, request
from markupsafe import escape
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.after_request
def agregar_cabeceras_seguridad(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    return response

@app.route('/hello')
def hello():
    raw_name = request.args.get('name', 'Invitado')
    safe_name = escape(raw_name)
    return f"Hello, {safe_name}!"

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    app.run(host=host, port=5000, debug=debug_mode)