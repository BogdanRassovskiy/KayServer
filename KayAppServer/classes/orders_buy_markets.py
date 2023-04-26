class orders_buy_markets:
    changed = "1"
    removed = "0"
    #
    name = "name"
    type = "type"
    dolgType = "dolgType"
    dolgVal = "dolgVal"
    dolgHave = "dolgHave"
    dolgMax = "dolgMax"
    wallet = "wallet"
    merchName = "0"
    def __init__(self,
        name,
        type,
        dolgType,
        dolgVal,
        dolgHave,
        dolgMax,
        wallet,
        merchName,
        ):
        self.name = name
        self.type = type
        self.dolgType = dolgType
        self.dolgVal = dolgVal
        self.dolgHave = dolgHave
        self.dolgMax = dolgMax
        self.wallet = wallet
        self.merchName = merchName
