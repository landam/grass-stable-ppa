'''Wrapper for raster3d.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_g3d.7.0.svn /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h -o raster3d.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError, "unhashable type (it is mutable)"
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0
    
    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)
        
        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj
        
        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj
        
        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))


# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]
    
    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)
        
        for path in paths:
            if os.path.exists(path):
                return self.load(path)
        
        raise ImportError,"%s not found." % libname
    
    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError,e
    
    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        
        else:
            for path in self.getplatformpaths(libname):
                yield path
            
            path = ctypes.util.find_library(libname)
            if path: yield path
    
    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]
    
    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]
        
        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)
    
    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:
        
        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']
        
        dirs = []
        
        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        
        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)
        
        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None
    
    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path
                    
                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache
    
    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll"]
    
    def load(self, path):
        return _WindowsLibrary(path)
    
    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["grass_g3d.7.0.svn"] = load_library("grass_g3d.7.0.svn")

# 1 libraries
# End libraries

# No modules

NULL = None # <built-in>

DCELL = c_double # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 403

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 206
class struct_FPRange(Structure):
    pass

struct_FPRange.__slots__ = [
    'min',
    'max',
    'first_time',
]
struct_FPRange._fields_ = [
    ('min', DCELL),
    ('max', DCELL),
    ('first_time', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 63
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'north',
    'south',
    'east',
    'west',
    'top',
    'bottom',
    'rows',
    'cols',
    'depths',
    'ns_res',
    'ew_res',
    'tb_res',
    'proj',
    'zone',
]
struct_anon_25._fields_ = [
    ('north', c_double),
    ('south', c_double),
    ('east', c_double),
    ('west', c_double),
    ('top', c_double),
    ('bottom', c_double),
    ('rows', c_int),
    ('cols', c_int),
    ('depths', c_int),
    ('ns_res', c_double),
    ('ew_res', c_double),
    ('tb_res', c_double),
    ('proj', c_int),
    ('zone', c_int),
]

RASTER3D_Region = struct_anon_25 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 63

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 73
class struct_RASTER3D_Map(Structure):
    pass

resample_fn = CFUNCTYPE(UNCHECKED(None), POINTER(struct_RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 69

struct_RASTER3D_Map.__slots__ = [
    'fileName',
    'tempName',
    'mapset',
    'operation',
    'region',
    'window',
    'resampleFun',
    'unit',
    'tileX',
    'tileY',
    'tileZ',
    'nx',
    'ny',
    'nz',
    'data_fd',
    'type',
    'precision',
    'compression',
    'useLzw',
    'useRle',
    'useXdr',
    'offset',
    'indexOffset',
    'indexLongNbytes',
    'indexNbytesUsed',
    'fileEndPtr',
    'hasIndex',
    'index',
    'tileLength',
    'typeIntern',
    'data',
    'currentIndex',
    'useCache',
    'cache',
    'cacheFD',
    'cacheFileName',
    'cachePosLast',
    'range',
    'numLengthExtern',
    'numLengthIntern',
    'clipX',
    'clipY',
    'clipZ',
    'tileXY',
    'tileSize',
    'nxy',
    'nTiles',
    'useMask',
]
struct_RASTER3D_Map._fields_ = [
    ('fileName', String),
    ('tempName', String),
    ('mapset', String),
    ('operation', c_int),
    ('region', RASTER3D_Region),
    ('window', RASTER3D_Region),
    ('resampleFun', POINTER(resample_fn)),
    ('unit', String),
    ('tileX', c_int),
    ('tileY', c_int),
    ('tileZ', c_int),
    ('nx', c_int),
    ('ny', c_int),
    ('nz', c_int),
    ('data_fd', c_int),
    ('type', c_int),
    ('precision', c_int),
    ('compression', c_int),
    ('useLzw', c_int),
    ('useRle', c_int),
    ('useXdr', c_int),
    ('offset', c_int),
    ('indexOffset', c_long),
    ('indexLongNbytes', c_int),
    ('indexNbytesUsed', c_int),
    ('fileEndPtr', c_int),
    ('hasIndex', c_int),
    ('index', POINTER(c_long)),
    ('tileLength', POINTER(c_int)),
    ('typeIntern', c_int),
    ('data', String),
    ('currentIndex', c_int),
    ('useCache', c_int),
    ('cache', POINTER(None)),
    ('cacheFD', c_int),
    ('cacheFileName', String),
    ('cachePosLast', c_long),
    ('range', struct_FPRange),
    ('numLengthExtern', c_int),
    ('numLengthIntern', c_int),
    ('clipX', c_int),
    ('clipY', c_int),
    ('clipZ', c_int),
    ('tileXY', c_int),
    ('tileSize', c_int),
    ('nxy', c_int),
    ('nTiles', c_int),
    ('useMask', c_int),
]

RASTER3D_Map = struct_RASTER3D_Map # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 185

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 220
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'elts',
    'nofElts',
    'eltSize',
    'names',
    'locks',
    'autoLock',
    'nofUnlocked',
    'minUnlocked',
    'next',
    'prev',
    'first',
    'last',
    'eltRemoveFun',
    'eltRemoveFunData',
    'eltLoadFun',
    'eltLoadFunData',
    'hash',
]
struct_anon_26._fields_ = [
    ('elts', String),
    ('nofElts', c_int),
    ('eltSize', c_int),
    ('names', POINTER(c_int)),
    ('locks', String),
    ('autoLock', c_int),
    ('nofUnlocked', c_int),
    ('minUnlocked', c_int),
    ('next', POINTER(c_int)),
    ('prev', POINTER(c_int)),
    ('first', c_int),
    ('last', c_int),
    ('eltRemoveFun', CFUNCTYPE(UNCHECKED(c_int), )),
    ('eltRemoveFunData', POINTER(None)),
    ('eltLoadFun', CFUNCTYPE(UNCHECKED(c_int), )),
    ('eltLoadFunData', POINTER(None)),
    ('hash', POINTER(None)),
]

RASTER3D_cache = struct_anon_26 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 220

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 234
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'nofNames',
    'index',
    'active',
    'lastName',
    'lastIndex',
    'lastIndexActive',
]
struct_anon_27._fields_ = [
    ('nofNames', c_int),
    ('index', POINTER(c_int)),
    ('active', String),
    ('lastName', c_int),
    ('lastIndex', c_int),
    ('lastIndexActive', c_int),
]

Rast3d_cache_hash = struct_anon_27 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 234

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 239
class struct__d_interval(Structure):
    pass

struct__d_interval.__slots__ = [
    'low',
    'high',
    'inf',
    'next',
]
struct__d_interval._fields_ = [
    ('low', c_double),
    ('high', c_double),
    ('inf', c_int),
    ('next', POINTER(struct__d_interval)),
]

d_Interval = struct__d_interval # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 244

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 249
class struct__d_mask(Structure):
    pass

struct__d_mask.__slots__ = [
    'list',
]
struct__d_mask._fields_ = [
    ('list', POINTER(d_Interval)),
]

d_Mask = struct__d_mask # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 249

write_fn = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), POINTER(None)) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 253

read_fn = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), POINTER(None)) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 254

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 7
try:
    RASTER3D_TILE_SAME_AS_FILE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 8
try:
    RASTER3D_NO_COMPRESSION = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 8
try:
    RASTER3D_COMPRESSION = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 9
try:
    RASTER3D_USE_LZW = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 9
try:
    RASTER3D_NO_LZW = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 10
try:
    RASTER3D_USE_RLE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 10
try:
    RASTER3D_NO_RLE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 11
try:
    RASTER3D_MAX_PRECISION = (-1)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 12
try:
    RASTER3D_NO_CACHE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 12
try:
    RASTER3D_USE_CACHE_DEFAULT = (-1)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 12
try:
    RASTER3D_USE_CACHE_X = (-2)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 12
try:
    RASTER3D_USE_CACHE_Y = (-3)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 12
try:
    RASTER3D_USE_CACHE_Z = (-4)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 12
try:
    RASTER3D_USE_CACHE_XY = (-5)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 12
try:
    RASTER3D_USE_CACHE_XZ = (-6)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 12
try:
    RASTER3D_USE_CACHE_YZ = (-7)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 12
try:
    RASTER3D_USE_CACHE_XYZ = (-8)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 13
try:
    RASTER3D_DEFAULT_WINDOW = NULL
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_DIRECTORY = 'grid3'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_CELL_ELEMENT = 'cell'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_CATS_ELEMENT = 'cats'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_RANGE_ELEMENT = 'range'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_HEADER_ELEMENT = 'cellhd'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_HISTORY_ELEMENT = 'hist'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_COLOR_ELEMENT = 'color'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_COLOR2_DIRECTORY = 'colr2'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_MASK_MAP = 'RASTER3D_MASK'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_WINDOW_ELEMENT = 'WIND3'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_DEFAULT_WINDOW_ELEMENT = 'DEFAULT_WIND3'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_WINDOW_DATABASE = 'windows3d'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 14
try:
    RASTER3D_PERMANENT_MAPSET = 'PERMANENT'
except:
    pass

RASTER3D_Map = struct_RASTER3D_Map # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 73

_d_interval = struct__d_interval # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 239

_d_mask = struct__d_mask # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster3d.h: 249

# No inserted files

