from .imgcomplete_work import imgcomplete_on_complete
from .cssclass_work import cssclass_on_complete

class Command:

    def __init__(self):
        pass

    def on_complete(self, ed_self):

        res = imgcomplete_on_complete(ed_self)
        if res:
            return res
        res = cssclass_on_complete(ed_self)
        if res:
            return res
