
from    distutils.core  import  setup

# Scripts to install.

scripts = [ 
        ]

# Path to scripts.

scripts = [ "bin/%s" % script for script in scripts ]

# Package and sub-packages.

packages = [ "capcom" ]

# Package setup.  The requirements may be too stringent and older versions
# may be alright.  Haven't checked.

setup(  name            =   "capcom"                                        ,
        version         =   "0.1.0"                                         ,
        description     =   "Coordinate instructions for C3 applications."  ,
        author          =   "R. C. Thomas"                                  ,
        author_email    =   "rcthomas@lbl.gov"                              ,
        url             =   "https://github.com/rcthomas/capcom"            ,
        requires        =   [ "pymongo" ]                                   ,
        packages        =   packages                                        ,
        scripts         =   scripts                                         )
