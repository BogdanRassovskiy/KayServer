class orders_nakSpace:
    changed = "1"
    removed = "0"
    #
    id = "id"
    nak = "nak"
    date = "date"
    nakNum = "nakNum"
    owner = "owner"
    merchName = "0"
    def __init__(self,
        id,
        nak,
        date,
        nakNum,
        owner,
        merchName,
        ):
        self.id = id
        self.nak = nak
        self.date = date
        self.nakNum = nakNum
        self.owner = owner
        self.merchName = merchName
