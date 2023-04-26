class inCar_naks:
    changed = "1"
    removed = "0"
    #
    name = "name"
    prod_id = "prod_id"
    free = "free"
    reserve = "reserve"
    sell = "sell"
    owner = "owner"
    merchName = "0"
    def __init__(self,
        name,
        prod_id,
        free,
        reserve,
        sell,
        owner,
        merchName,
        ):
        self.name = name
        self.prod_id = prod_id
        self.free = free
        self.reserve = reserve
        self.sell = sell
        self.owner = owner
        self.merchName = merchName
