class orders_actHistory:
    changed = "1"
    removed = "0"
    #
    login = "login"
    Data = "Data"
    Date = "Date"
    merchName = "0"
    def __init__(self,
        login,
        Data,
        Date,
        merchName,
        ):
        self.login = login
        self.Data = Data
        self.Date = Date
        self.merchName = merchName
