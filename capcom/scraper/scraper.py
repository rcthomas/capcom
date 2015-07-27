
class Scraper ( object ) :

    def __init__( self, census, parser ) :
        self.census = census
        self.parser = parser

    def __call__( self ) :
        raise NotImplementedError
