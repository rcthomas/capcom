
"""Use astropy to extract FITS header metadata for database storage.

Header of each HDU in FITS file is parsed using `astropy.io.fits` module.
Verification option is "fix" by default.  COMMENT and HISTORY cards are parsed
by `astropy` unless ignored.

Metadata for given FITS file is represented as list of dictionaries.  Header
keywords become keys of these dictionaries.  Original ordering of cards with
different header keywords is not captured.

Repeated appearances of given keyword are handled by making the corresponding
dictionary value into list of values.  If keyword appears only once, its value
is merely scalar, not single-element list.  Ordering of cards with same keyword
is captured, but users should not depend on this.

Each dictionary includes (zero-indexed) `position` of corresponding header in
source FITS file and `path` to that file.  The extracted metadata itself is
stored in a `header` entry.  File paths may be absolute or relative, but it is
strongly suggested that they be made relative to some root directory or
directories, so if a root directory changes, the path field does not need to be
updated.  Handling root directories and file paths relative to them is
documented in the `__call__` method of the `AstropyScraper` class.

Extracted metadata should be in the form of standard Python containers and
simple Python values.  These should be transformable into JSON, YAML, etc.  for
ingestion into a database or storage in files on disk.  The general expectation
is that FITS header metadata will be stored in a MongoDB instance for use by
`capcom` when constructing configuration and task files.

"""

import  os

from    astropy.io  import  fits

from    scraper     import  Scraper

class AstropyScraper ( Scraper ) :
    """Extract FITS header metadata from files on local disk."""

    def __init__( self, omit_comment = False, omit_history = False, omit_keywords = list(), verification = "fix" ) :
        """Initialize FITS header metadata extractor.

        Args:
            omit_comment (bool): Ignore COMMENT cards.
            omit_history (bool): Ignore HISTORY cards.
            omit_keywords (List[str]): List of header keywords to ignore.
            verification (str): Verification to option for `astropy.io.fits.`
                Default is "fix."

        """

        self.omit_comment  = omit_comment
        self.omit_history  = omit_history
        self.omit_keywords = omit_keywords + [ "COMMENT", "HISTORY" ]
        self.verification  = verification

    def __call__( self, path, root = "" ) :
        """Extract metadata from a FITS file on local disk.

        Args:
            path (str): Path to FITS file.
            root (Optional[str]): Root path to prepend to `path` but
                not to include in the metadata entry itself.

        Returns:
            List[Dict]: List of extracted metadata dictionaries.  Each dictionary
                has keys `position`, `path`, and `header`.  
                
            Value `position` is the zero-indexed position of the corresponding
            HDU.

            Value `path` is a (probably relative) path to the source FITS file
            for the metadata.  Does not include any `root` prefix.

            Value `header` contains the extracted header metadata dictionary
            itself.

        """

        with fits.open( os.path.join( root, path ), "readonly" ) as hdulist :
            return self._hdulist( path, hdulist )

    def _hdulist( self, path, hdulist ) :
        hdulist.verify( self.verification )
        metadata = list()
        for position, hdu in enumerate( hdulist ) :
            metadata.append( dict( position = position, path = path, header = self._hdu( hdu ) ) )
        return metadata

    def _hdu( self, hdu ) :
        metadata = dict()
        header = hdu.header
        self._header_entries( metadata, header )
        self._header_comment( metadata, header )
        self._header_history( metadata, header )
        return metadata

    def _header_entries( self, metadata, header ) :
        for keyword in header :
            if keyword in self.omit_keywords :
                continue
            self._header_entry( metadata, header, keyword )

    def _header_entry( self, metadata, header, keyword ) :
        if keyword in metadata :
            if type( metadata[ keyword ] ) is not list :
                metadata[ keyword ] = [ metadata[ keyword ] ]
            metadata[ keyword ].append( header[ keyword ] )
        else :
            metadata[ keyword ] = header[ keyword ]

    def _header_comment( self, metadata, header ) :
        if not self.omit_comment and "COMMENT" in header :
            metadata[ "COMMENT" ] = "{}".format( header[ "COMMENT" ] )

    def _header_history( self, metadata, header ) :
        if not self.omit_history and "HISTORY" in header :
            metadata[ "HISTORY" ] = "{}".format( header[ "HISTORY" ] )
