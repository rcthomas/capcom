
"""Parse metadata from FITS files on local disk.

Parsers extract metadata from FITS files and format them into standard
representation for more convenient storage and querying.  Each header-and-data
unit (HDU) of a FITS file is translated into a Python dictionary in a
standardized way.  These dictionaries are stored as individual documents in a
data store like MongoDB, PostgreSQL 9.4+, or some other solution supporting
documents.

"""

class Parser ( object ) :
    """Parser interface."""

    def __call__( self, path ) :
        """Extract metadata from a FITS file on local disk.

        Args:
            path (str): Path to FITS file.

        Returns:
            List[Dict]: List of extracted metadata dictionaries, one per HDU.

        """

        raise NotImplementedError
