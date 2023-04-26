class basic_telegram:
    changed = "1"
    removed = "0"
    #
    merchName = "merchName"
    token = "token"
    chat_id = "chat_id"
    def __init__(self,
        merchName,
        token,
        chat_id,
        ):
        self.merchName = merchName
        self.token = token
        self.chat_id = chat_id
