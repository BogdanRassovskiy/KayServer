class orders_categories:
    changed = "1"
    removed = "0"
    #
    cat_id = "cat_id"
    id = "id"
    name = "name"
    work = "work"
    img = "img"
    name2 = "name2"
    merchName = "0"
    def __init__(self,
        cat_id,
        id,
        name,
        work,
        img,
        name2,
        merchName,
        ):
        self.cat_id = cat_id
        self.id = id
        self.name = name
        self.work = work
        self.img = img
        self.name2 = name2
        self.merchName = merchName
