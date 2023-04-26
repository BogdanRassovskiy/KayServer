class inCar_cashInCar:
    changed = "1"
    removed = "0"
    #
    driver = "driver"
    cash = "cash"
    term = "term"
    per = "per"
    on_day = "on_day"
    merchName = "0"
    def __init__(self,
        driver,
        cash,
        term,
        per,
        on_day,
        merchName,
        ):
        self.driver = driver
        self.cash = cash
        self.term = term
        self.per = per
        self.on_day = on_day
        self.merchName = merchName
