
import  os

from    ..util  import  lazy
from    mongo   import  MongoDBI

class CosmoImageMetadata ( MongoDBI ) :

    @classmethod
    def read_only( cls ) :
        return CosmoImageMetadata()

    @classmethod
    def read_write( cls ) :
        username = os.environ[ "MONGODB_CIM_RW_USER" ]
        password = os.environ[ "MONGODB_CIM_RW_PASS" ]
        return CosmoImageMetadata( username, password )

    def __init__( self, username = None, password = None, hostname = None ) :
        username = username or os.environ[ "MONGODB_CIM_RO_USER" ]
        password = password or os.environ[ "MONGODB_CIM_RO_PASS" ]
        hostname = hostname or os.environ[ "MONGODB_HOST"        ]
        dbname   = os.environ[ "MONGODB_CIM" ]
        super( CosmoImageMetadata, self ).__init__( username, password, hostname, dbname )

    @lazy
    def decam_public( self ) :
        self.database.decam_public.ensure_index( [ ( "relpath", 1 ), ( "position", 1 ) ], unique = True )
        return self.database.decam_public
