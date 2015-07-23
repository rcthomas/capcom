
def lazy( func ) :
    attr = "__" + func.__name__
    @property
    def _lazy( obj ) :
        try :
            return getattr( obj, attr )
        except AttributeError :
            setattr( obj, attr, func( obj ) )
            return getattr( obj, attr )
    return _lazy
