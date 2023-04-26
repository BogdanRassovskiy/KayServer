class orders_history:
    changed = "1"
    removed = "0"
    #
    data = "data"
    price = "price"
    type = "type"
    getter = "getter"
    driver = "driver"
    date = "date"
    district = "district"
    last_index = "last_index"
    visible = "visible"
    merchName = "0"
    def __init__(self,
        data,
        price,
        type,
        getter,
        driver,
        date,
        district,
        last_index,
        visible,
        merchName,
        ):
        self.data = data
        self.price = price
        self.type = type
        self.getter = getter
        self.driver = driver
        self.date = date
        self.district = district
        self.last_index = last_index
        self.visible = visible
        self.merchName = merchName
