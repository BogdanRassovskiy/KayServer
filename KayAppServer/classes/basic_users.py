class basic_users:
    changed = "1"
    removed = "0"
    #
    login = "login"
    pswd = "pswd"
    session = "session"
    merchName = "merchName"
    user_type = "user_type"
    lon = "lon"
    lat = "lat"
    updates = "updates"
    lang = "lang"
    ent = "ent"
    def __init__(self,
        login,
        pswd,
        session,
        merchName,
        user_type,
        lon,
        lat,
        updates,
        lang,
        ent,
        ):
        self.login = login
        self.pswd = pswd
        self.session = session
        self.merchName = merchName
        self.user_type = user_type
        self.lon = lon
        self.lat = lat
        self.updates = updates
        self.lang = lang
        self.ent = ent
