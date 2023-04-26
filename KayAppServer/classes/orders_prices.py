class orders_prices:
    changed = "1"
    removed = "0"
    #
    id = "id"
    name = "name"
    price = "price"
    merchName = "0"
    def __init__(self,
        id,
        name,
        price,
        merchName,
        ):
        self.id = id
        self.name = name
        self.price = price
        self.merchName = merchName
