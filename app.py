from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
DATABASE_URL = os.getenv('DATABASE_URL')

@app.route('/')
def index():
    return jsonify({
        'service': 'Flask API - Supplier Intelligence',
        'status': 'running',
        'version': '1.0.0',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/health')
@app.route('/healthz')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/dbcheck')
def dbcheck():
    """Check database connection"""
    try:
        if not DATABASE_URL:
            return jsonify({
                'status': 'error',
                'message': 'DATABASE_URL not configured'
            }), 500
        
        # Simple connection test
        import psycopg
        conn = psycopg.connect(DATABASE_URL)
        conn.close()
        
        return jsonify({
            'status': 'ok',
            'database': 'connected',
            'timestamp': datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/v1/products/upsert', methods=['POST'])
def products_upsert():
    """Upsert product endpoint"""
    auth_token = request.headers.get('X-Workflow-Token')
    expected_token = os.getenv('WORKFLOW_AUTH_TOKEN')
    
    if not auth_token or auth_token != expected_token:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.get_json()
    
    return jsonify({
        'status': 'ok',
        'message': 'Product upsert endpoint',
        'data': data,
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/v1/workflows/run', methods=['POST'])
def workflows_run():
    """Run workflow endpoint"""
    auth_token = request.headers.get('X-Workflow-Token')
    expected_token = os.getenv('WORKFLOW_AUTH_TOKEN')
    
    if not auth_token or auth_token != expected_token:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.get_json()
    
    return jsonify({
        'status': 'ok',
        'message': 'Workflow run endpoint',
        'data': data,
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/v1/webhooks/make', methods=['POST'])
def webhooks_make():
    """Make.com webhook endpoint"""
    data = request.get_json()
    
    return jsonify({
        'status': 'ok',
        'message': 'Make.com webhook received',
        'data': data,
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/v1/supplier-intel', methods=['POST'])
def supplier_intel():
    """Supplier intelligence endpoint"""
    auth_token = request.headers.get('X-Workflow-Token')
    expected_token = os.getenv('WORKFLOW_AUTH_TOKEN')
    
    if not auth_token or auth_token != expected_token:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.get_json()
    
    # Simulate AI analysis
    response = {
        'status': 'ok',
        'action': 'alert',  # or 'auto_buy' or 'skip'
        'confidence': 0.75,
        'opportunities': [],
        'reasoning': 'Supplier intelligence analysis completed',
        'timestamp': datetime.utcnow().isoformat()
    }
    
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
