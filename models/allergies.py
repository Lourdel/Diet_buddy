#!/user/bin/python3


from models.basemodel import BaseModel

class Allergies(BaseModel):
    """ Class representing allergies """
    def __init__(self, name=""):
        super().__init__()
        self.name = name
