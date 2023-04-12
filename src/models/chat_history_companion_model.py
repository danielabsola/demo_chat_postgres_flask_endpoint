import json
from database.db import get_connection
from .entities.chat_history import ChatHistory

class ChatHistoryCompanionModel():
    @classmethod
    def get_all_chat_history_companion(self):
        try:
            connection = get_connection()
            chatsHistory = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT session_id, created_at, chat FROM chat_history_companion ORDER BY created_at ASC")
                result_set = cursor.fetchall()
                for row in result_set:
                    chatHistory=ChatHistory(row[0], row[1], row[2])
                    chatsHistory.append(chatHistory.to_JSON())

            connection.close()
            return chatsHistory
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_session_id_chat_history_companion(self, session_id):
        try:
            connection = get_connection()
            chatsHistory = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT session_id, created_at, chat FROM chat_history_companion 
                WHERE session_id = %s ORDER BY created_at ASC""", (session_id,))
                result_set = cursor.fetchall()
                for row in result_set:
                    chatHistory=ChatHistory(row[0], row[1], row[2])
                    chatsHistory.append(chatHistory.to_JSON())

            connection.close()
            return chatsHistory
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_chat_history_companion(self,chatHistory):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                chat_json = json.dumps(chatHistory.chat)
                cursor.execute("""INSERT INTO chat_history_companion (session_id, created_at, chat)
                                 VALUES (%s, %s, %s)""", (chatHistory.session_id, chatHistory.created_at, chat_json))
                
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    # @classmethod
    # def update_movie(self,movie):
    #     try:
    #         connection = get_connection()

    #         with connection.cursor() as cursor:
    #             cursor.execute("""UPDATE movie SET title = %s, duration = %s, released = %s
    #                              WHERE id = %s""", (movie.title, movie.duration, movie.released, movie.id))
                
    #             affected_rows = cursor.rowcount
    #             connection.commit()
    #         connection.close()
    #         return affected_rows
    #     except Exception as ex:
    #         raise Exception(ex)
        
    # @classmethod
    # def delete_movie(self,movie):
    #     try:
    #         connection = get_connection()

    #         with connection.cursor() as cursor:
    #             cursor.execute("DELETE FROM movie WHERE id = %s", (movie.id,))
    #             affected_rows = cursor.rowcount
    #             connection.commit()
    #         connection.close()
    #         return affected_rows
    #     except Exception as ex:
    #         raise Exception(ex)