class Card(object):
    def __init__(self, id):
        self.id = id
        self.image_path = str(id) + ".jpg"
        self.active = True