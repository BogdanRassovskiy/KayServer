class myImage:
    changed = "1"
    removed = "0"
    #
    link = "";
    photo = None;
    def __init__(self,
        link,
        photo,
        ):
        self.link = link;
        self.photo = photo;
