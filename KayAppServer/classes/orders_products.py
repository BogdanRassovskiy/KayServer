class orders_products:
    changed = "1"
    removed = "0"
    #
    cat_id = "cat_id"
    id = "id"
    name = "name"
    rev = "rev"
    work = "work"
    img = "img"
    box = "box"
    form = "form"
    visible = "visible"
    ost = "ost"
    name2 = "name2"
    rev2 = "rev2"
    merchName = "0"
    def __init__(self,
        cat_id,
        id,
        name,
        rev,
        work,
        img,
        box,
        form,
        visible,
        ost,
        name2,
        rev2,
        merchName,
        ):
        self.cat_id = cat_id
        self.id = id
        self.name = name
        self.rev = rev
        self.work = work
        self.img = img
        self.box = box
        self.form = form
        self.visible = visible
        self.ost = ost
        self.name2 = name2
        self.rev2 = rev2
        self.merchName = merchName
