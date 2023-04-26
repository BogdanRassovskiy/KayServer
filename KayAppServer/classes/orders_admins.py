class orders_admins:
    changed = "1"
    removed = "0"
    #
    login = "login"
    level = "level"
    role = "role"
    merchName = "0"
    def __init__(self,
        login,
        level,
        role,
        merchName,
        ):
        self.login = login
        self.level = level
        self.role = role
        self.merchName = merchName
