
from    selector    import  Selector

class EndingSelector ( Selector ) :

    def __init__( self, ending = ".fits" ) :
        self.ending = ending

    def __call__( self, path ) :
        return path.endswith( self.ending )
