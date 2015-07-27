
from    selector    import  Selector

class AnySelector ( Selector ) :

    def __call__( self, path ) :
        return True
