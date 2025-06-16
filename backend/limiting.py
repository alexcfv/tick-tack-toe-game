from flask import Flask, request, jsonify
from time import time

#НЕ ХОРОШИЙ ВАРИАНТ ДЛЯ ПРОДАКШЕНА
#ИСПОЛЬЗОВАТЬ REDIS БУДЕТ ПРАВИЛЬНОЕ

RATE_LIMIT = 10
RATE_PERIOD = 10
clients = {}

def limiting_remote_addr():
    if request.path == "/game":
        return
    
    ip = request.remote_addr
    now = time()
    
    if ip not in clients:
        clients[ip] = []

    clients[ip] = [timestamp for timestamp in clients[ip] if now - timestamp < RATE_PERIOD]

    if len(clients[ip]) >= RATE_LIMIT:
        return jsonify({"error": "Too many requests"}), 429

    clients[ip].append(now)