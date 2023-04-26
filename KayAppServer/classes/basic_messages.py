class basic_messages:
    changed = "1"
    removed = "0"
    #
    chat_id = "chat_id"
    message_id = "message_id"
    text_or_photo = "text_or_photo"
    sender = "sender"
    getter = "getter"
    date = "date"
    wasRead = "wasRead"
    text = "text"
    def __init__(self,
        chat_id,
        message_id,
        text_or_photo,
        sender,
        getter,
        date,
        wasRead,
        text,
        ):
        self.chat_id = chat_id
        self.message_id = message_id
        self.text_or_photo = text_or_photo
        self.sender = sender
        self.getter = getter
        self.date = date
        self.wasRead = wasRead
        self.text = text
