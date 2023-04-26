class orders_order:
    changed = "1"
    removed = "0"
    #
    data = "data"
    getter = "getter"
    owner = "owner"
    last_index = "last_index"
    date = "date"
    get_type = "get_type"
    price = "price"
    payForm = "payForm"
    merchName = "0"
    def __init__(self,
        data,
        getter,
        owner,
        last_index,
        date,
        get_type,
        price,
        payForm,
        merchName,
        ):
        self.data = data
        self.getter = getter
        self.owner = owner
        self.last_index = last_index
        self.date = date
        self.get_type = get_type
        self.price = price
        self.payForm = payForm
        self.merchName = merchName
