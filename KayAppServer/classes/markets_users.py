class markets_users:
    changed = "1"
    removed = "0"
    #
    login = "login"
    adres = "adres"
    inn = "inn"
    phone = "phone"
    varified = "varified"
    district = "district"
    phone2 = "phone2"
    def __init__(self,
        login,
        adres,
        inn,
        phone,
        varified,
        district,
        phone2,
        ):
        self.login = login
        self.adres = adres
        self.inn = inn
        self.phone = phone
        self.varified = varified
        self.district = district
        self.phone2 = phone2
