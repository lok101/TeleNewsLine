from db.DB_methods import DBController


class Control:
    def __init__(self):
        self.db = DBController()


controller = Control()
