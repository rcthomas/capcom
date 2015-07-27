
from    scraper import  Scraper

class VanillaScraper ( Scraper ) :

    def __call__( self ) :
        docs = list()
        for path, relpath in self.census() :
            for position, header in enumerate( scraper( path ) ) :
                docs.append( dict( path = relpath, position = position, header = header ) )
        return docs
