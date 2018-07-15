from .imgcomplete_work import imgcomplete_on_complete
from cudatext import *

    
class Command:
    
    def __init__(self):
        pass
        
    def config(self):
        pass
        
    def on_complete(self, ed_self):
        return imgcomplete_on_complete(ed_self)
        
        
