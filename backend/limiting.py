from flask import Flask, request, jsonify
from time import time
from main import app

#НЕ ХОРОШИЙ ВАРИАНТ ДЛЯ ПРОДАКШЕНА
#ИСПОЛЬЗОВАТЬ REDIS БУДЕТ ПРАВИЛЬНОЕ

RATE_LIMIT = 5
RATE_PERIOD = 10
clients = {}

@app.before_request
def limiting_remote_addr():
    if request.path == "/game":
        return
    
    ip = request.remote_addr
    now = time()
    
    request_times = clients.get(ip, [])
    request_times = [t for t in request_times if now - t < RATE_PERIOD]
    
    if len(request_times) >= RATE_LIMIT:
        return jsonify({"error" : "Too many request"}), 429
    
    request_times.append(now)
    clients[ip] = request_times