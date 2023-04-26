class orders_drivers:
    changed = "1"
    removed = "0"
    #
    login = "login"
    district = "district"
    name = "name"
    merchName = "0"
    def __init__(self,
        login,
        district,
        name,
        merchName,
        ):
        self.login = login
        self.district = district
        self.name = name
        self.merchName = merchName
