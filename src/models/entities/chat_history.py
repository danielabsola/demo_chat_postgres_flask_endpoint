from utils.date_format import DateFormat
class ChatHistory():

    def __init__(self, session_id, created_at, chat=None):
        self.session_id = session_id
        self.created_at = created_at
        self.chat = chat

    def to_JSON(self):
        return {
            'session_id':self.session_id,
            'created_at':DateFormat.convert_data(self.created_at),
            'chat':self.chat
        }