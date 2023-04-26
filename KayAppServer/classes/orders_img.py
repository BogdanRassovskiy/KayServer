class orders_img:
    changed = "0"
    removed = "0"
    #
    type = "type"
    _id = "_id"
    place = "place"
    merchName = "0"
    def __init__(self,
        type,
        _id,
        place,
        merchName,
        ):
        self.type = type
        self._id = _id
        self.place = place
        self.merchName = merchName
