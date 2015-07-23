
"""Scrape metadata from FITS files on local disk.

Scrapers are things that pull metadata from FITS files and format them into a
standard representation.  Each HDU of a FITS file should become a Python
dictionary.  These should be stored individually somewhere like a data store.
They should tell you a path to a file on disk where the metadata came from,
possibly a path relative to some kind of root that may change over time.  They
should also tell you what position in the file the source HDU was located.
"""

class Scraper ( object ) :
    """Scraper interface."""

    def __call__( self, path, root = "" ) :
        raise NotImplementedError
