
import  os

from    ..      import  util.lazy   as lazy
from    mongo   import  MongoDBI

class CosmoImageDBI ( MongoDBI ) :

    @classmethod
    def read_only( cls ) :
        return CosmoImageDBI()

    @classmethod
    def read_write( cls ) :
        username = os.environ[ "CDR_MONGODB_RW_USER" ]
        password = os.environ[ "CDR_MONGODB_RW_PASS" ]
        return CosmoImageDBI( username, password )

    def __init__( self, username = None, password = None, hostname = None ) :
        username = username or os.environ[ "CDR_MONGODB_RO_USER" ]
        password = password or os.environ[ "CDR_MONGODB_RO_PASS" ]
        hostname = hostname or os.environ[ "CDR_MONGODB_HOST"    ]
        dbname   = "cosmo_image_metadata"
        super( CosmoImageDBI, self ).__init__( username, password, hostname, dbname )

    @lazy
    def decals( self ) :
        # ensure indexing...
        return self.database.decals

    @lazy
    def bass( self ) :
        # ensure indexing...
        return self.database.bass
