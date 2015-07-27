
import  os

from    census  import  Census

class WalkCensus ( Census ) :

    def __init__( self, selector, rootdirs ) :
        super( WalkCensus, self ).__init__( selector )
        self.rootdirs = rootdirs

    def __call__( self ) :
        return sorted( [ self._rootdir( rootdir ) for rootdir in self.rootdirs ] )

    def _rootdir( self, rootdir ) :
        tuples = list()
        for dirpath, dirnames, filenames in os.walk( rootdir ) :
            paths     = [ os.path.join( dirpath, filename ) for filename in filenames ]
            selected  = [ path for path in paths if self.selector( path ) ]
            tuples   += [ ( path, os.path.relpath( path, rootdir ) ) for path in selected ]
        return tuples
