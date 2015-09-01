
import  os

from    ..util  import  lazy
from    mongo   import  MongoDBI, MongoRG

class CosmoImageMetadata ( MongoDBI ) :

    @classmethod
    def read_only( cls ) :
        return CosmoImageMetadata( "readonly" )

    @classmethod
    def read_write( cls ) :
        username = os.environ[ "MONGODB_CIM_RW_USER" ]
        password = os.environ[ "MONGODB_CIM_RW_PASS" ]
        return CosmoImageMetadata( "readwrite", username, password )

    def __init__( self, mode, username = None, password = None, hostname = None ) :
        self.mode = mode
        username  = username or os.environ[ "MONGODB_CIM_RO_USER" ]
        password  = password or os.environ[ "MONGODB_CIM_RO_PASS" ]
        hostname  = hostname or os.environ[ "MONGODB_HOST"        ]
        dbname    = os.environ[ "MONGODB_CIM" ]
        super( CosmoImageMetadata, self ).__init__( username, password, hostname, dbname )

    @lazy
    def decam_public( self ) :
        collection = self.database.decam_public
        if self.mode == "readwrite" :
            collection.ensure_index( [ ( "relpath", 1 ), ( "position", 1 ) ], unique = True )
            collection.ensure_index( [ ( "header.DATE-OBS", 1 ) ], sparse = True )
            collection.ensure_index( [ ( "header.OBSTYPE" , 1 ) ], sparse = True )
        return collection

    @lazy
    def bass( self ) :
        collection = self.database.bass
        if self.mode == "readwrite" :
            collection.ensure_index( [ ( "relpath", 1 ), ( "position", 1 ) ], unique = True )
            collection.ensure_index( [ ( "header.DATE-OBS", 1 ) ], sparse = True )
            collection.ensure_index( [ ( "header.OBSTYPE" , 1 ) ], sparse = True )
        return collection

class DECamPublicRG ( MongoRG ) :

    def __init__( self, dbi = None ) :
        self.dbi = dbi or CosmoImageMetadata.read_only()
        super( DECamPublicRG, self ).__init__( self.dbi.decam_public )
