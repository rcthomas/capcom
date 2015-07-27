
class Census ( object ) :

    def __init__( self, selector ) :
        self.selector = selector

    def __call__( self ) :
        raise NotImplementedError
