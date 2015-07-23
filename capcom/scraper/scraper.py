
class Scraper ( object ) :
    """Scraper interface."""

    def __call__( self, path, root = "" ) :
        raise NotImplementedError
