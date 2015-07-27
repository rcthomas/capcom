
import  os

class Selector ( object ) :

    def __call__( self, path ) :
        """Returns true if a path is a file that should be scraped."""

        raise NotImplementedError
