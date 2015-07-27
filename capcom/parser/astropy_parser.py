
"""Use astropy to extract FITS header metadata for database storage.

Header of each HDU in FITS file is parsed using `astropy.io.fits`.  COMMENT and
HISTORY cards are parsed as usual by astropy unless the user requests they be
omitted.  Particular keywords may be omitted if desired, but generally this 
option should not be used.  Default verification option is "fix."

Metadata for given FITS file is represented as list of dictionaries.  Header
keywords become keys of these dictionaries.  Original ordering of cards with
different header keywords is not captured.

Repeated appearances of given keyword are handled by making the corresponding
dictionary value into list of values.  If keyword appears only once, its value
is a scalar, not single-element list.  Ordering of cards with same keyword is
captured as a side-effect, but users should not depend on this.

"""

from    astropy.io  import  fits

from    parser      import  Parser

class AstropyParser ( Parser ) :
    """Extract FITS header metadata from files on local disk."""

    def __init__( self, omit_comment = False, omit_history = False, omit_keywords = list(), verification = "fix" ) :
        """Initialize astropy-based FITS header metadata extractor.

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

    def __call__( self, path ) :
        """Extract metadata from a FITS file on local disk.

        Args:
            path (str): Path to FITS file.

        Returns:
            List[Dict]: List of extracted metadata dictionaries.

        """

        with fits.open( path, "readonly" ) as hdulist :
            return self._hdulist( hdulist )

    def _hdulist( self, hdulist ) :
        hdulist.verify( self.verification )
        return [ self._hdu( hdu ) for hdu in hdulist ]

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
