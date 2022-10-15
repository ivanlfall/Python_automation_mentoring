class BasePage(object):
    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BasePage, cls).__new__(cls)
        return cls.instance

    def __str__(self):
        return self.__class__.__name__
