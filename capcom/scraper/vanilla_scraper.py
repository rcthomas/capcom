
from    scraper import  Scraper

class VanillaScraper ( Scraper ) :

    def __call__( self ) :
        for entry in self.census() :
            yield self._relpath( *entry )

    def _relpath( self, path, relpath ) :
        docs = list()
        for position, header in enumerate( self.parser( path ) ) :
            docs.append( dict( relpath = relpath, position = position, header = header ) )
        return docs
