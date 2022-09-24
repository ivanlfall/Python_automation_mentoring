class BasePage(object):
    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BasePage, cls).__new__(cls)
        return cls.instance