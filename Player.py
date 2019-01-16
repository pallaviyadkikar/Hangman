classass Player:
    def __init__(self):
        self.__pname=None
        self.__category=None
        self.__points=None
        self.__city=None

    def get_city(self):
        return self.__city


    def set_city(self, value):
        self.__city = value


    def get_pname(self):
        return self.__pname


    def get_category(self):
        return self.__category


    def get_points(self):
        return self.__points


    def set_pname(self, value):
        self.__pname = value


    def set_category(self, value):
        self.__category = value


    def set_points(self, value):
        self.__points = value