from .imgcomplete_work import imgcomplete_on_complete

class Command:

    def __init__(self):
        pass

    def on_complete(self, ed_self):
        res = imgcomplete_on_complete(ed_self)
        return res
        # todo: add calling of HTML Class Complete
