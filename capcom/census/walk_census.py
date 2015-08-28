
import  os

from    census  import  Census

class WalkCensus ( Census ) :

    def __init__( self, selector, rootdirs, memoize = False ) :
        super( WalkCensus, self ).__init__( selector )
        self.rootdirs  = rootdirs
        self.memoize   = memoize
        if self.memoize :
            self()

    def __call__( self ) :
        if self.memoize :
            try :
                return self._census
            except AttributeError :
                self._census = sorted( self._rootdirs() )
                return self._census
        else :
            return sorted( self._rootdirs() )

    def _rootdirs( self ) :
        tuples = list()
        for rootdir in self.rootdirs :
            tuples += self._rootdir( rootdir )
        return tuples

    def _rootdir( self, rootdir ) :
        tuples = list()
        for dirpath, dirnames, filenames in os.walk( rootdir ) :
            print rootdir, dirpath, len( tuples )
            paths     = [ os.path.join( dirpath, filename ) for filename in filenames ]
            selected  = [ path for path in paths if self.selector( path ) ]
            tuples   += [ ( path, os.path.relpath( path, rootdir ) ) for path in selected ]
        return tuples
