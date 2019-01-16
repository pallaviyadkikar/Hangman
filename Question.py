class Question:
    def __init__(self):
        self.__qid=None
        self.__qname=None
        self.__lvl=None
        self.__category=None

    def get_qid(self):
        return self.__qid


    def get_qname(self):
        return self.__qname


    def get_lvl(self):
        return self.__lvl


    def get_category(self):
        return self.__category


    def set_qid(self, value):
        self.__qid = value


    def set_qname(self, value):
        self.__qname = value


    def set_lvl(self, value):
        self.__lvl = value


    def set_category(self, value):
        self.__category = value