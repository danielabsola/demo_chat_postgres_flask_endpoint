from flask import Blueprint, jsonify, request
# Blueprint: permite manjear las rutas y asociarlas para que trabaje con una colleccion de rutas
# Key
import uuid
# Entities
from models.entities.chat_history import ChatHistory
# Models
from models.chat_history_companion_model import ChatHistoryCompanionModel

main=Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_chat_history_companio():
    try:
        chatHistory = ChatHistoryCompanionModel.get_chat_history_companion()
        return jsonify(chatHistory)
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500
    
@main.route('/<session_id>', methods=['GET'])
def get_session_id_chat_history_companion(session_id):
    try:
        chatHistory = ChatHistoryCompanionModel.get_session_id_chat_history_companion(session_id)
        if not chatHistory:
            return jsonify({'mensaje':'Session_ID not found'}),404
        return jsonify(chatHistory)
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500
    
@main.route('/add', methods=['POST'])
def add_chat_history_companion():
    try:
        session_id = request.json['session_id']
        chat = request.json['chat']
        created_at = request.json['created_at']
        chatHistory = ChatHistory(session_id, created_at, chat)

        affected_rows = ChatHistoryCompanionModel.add_chat_history_companion(chatHistory)
        if affected_rows == 1:
            return jsonify(chatHistory.session_id, chatHistory.created_at)
        else:
            return jsonify({'mensaje':"Error on insert"}),500
    except Exception as ex:
        return jsonify({'mensaje':str(ex)}),500

# @main.route('/update/<id>', methods=['PUT'])
# def update_movie(id):
#     try:
#         title = request.json['title']
#         duration = int(request.json['duration'])
#         released = request.json['released']
#         movie = Movie(id, title, duration, released)

#         affected_rows = MovieModel.update_movie(movie)
#         if affected_rows == 1:
#             return jsonify(movie.id)
#         else:
#             return jsonify({'mensaje':"No movie updated"}),404
#     except Exception as ex:
#         return jsonify({'mensaje':str(ex)}),500

# @main.route('/delete/<id>', methods=['DELETE'])
# def delete_movie(id):
#     try:
#         movie = Movie(id)
#         affected_rows = MovieModel.delete_movie(movie)
#         if affected_rows == 1:
#             return jsonify(movie.id)
#         else:
#             return jsonify({'mensaje':"No movie deleted"}),404
#     except Exception as ex:
#         return jsonify({'mensaje':str(ex)}),500
    