
import  urllib

import  pymongo

from    ..util  import  lazy
from    dbi     import  DBI

class MongoDBI ( DBI ) :

    def __init__( self, username, password, hostname, dbname ) :
        self.username = username
        self.password = password
        self.hostname = hostname
        self.dbname   = dbname

    @lazy
    def database( self ) :
        return self.client[ self.dbname ]

    @lazy
    def client( self ) :
        return pymongo.MongoClient( self.uri )

    @lazy
    def uri( self ) :
        return "mongodb://{}:{}@{}/{}".format( self.username, urllib.quote_plus( self.password ), self.hostname, self.dbname )
