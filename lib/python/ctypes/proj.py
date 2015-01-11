'''Wrapper for gprojects.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_gproj.7.0.svn -I/usr/local/include /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h -o proj.py

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

_libs["grass_gproj.7.0.svn"] = load_library("grass_gproj.7.0.svn")

# 1 libraries
# End libraries

# No modules

projPJ = POINTER(None) # /usr/local/include/proj_api.h: 55

OGRSpatialReferenceH = POINTER(None) # /usr/local/include/ogr_srs_api.h: 252

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 33
class struct_pj_info(Structure):
    pass

struct_pj_info.__slots__ = [
    'pj',
    'meters',
    'zone',
    'proj',
]
struct_pj_info._fields_ = [
    ('pj', projPJ),
    ('meters', c_double),
    ('zone', c_int),
    ('proj', c_char * 100),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 41
class struct_gpj_datum(Structure):
    pass

struct_gpj_datum.__slots__ = [
    'name',
    'longname',
    'ellps',
    'dx',
    'dy',
    'dz',
]
struct_gpj_datum._fields_ = [
    ('name', String),
    ('longname', String),
    ('ellps', String),
    ('dx', c_double),
    ('dy', c_double),
    ('dz', c_double),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 47
class struct_gpj_datum_transform_list(Structure):
    pass

struct_gpj_datum_transform_list.__slots__ = [
    'count',
    'params',
    'where_used',
    'comment',
    'next',
]
struct_gpj_datum_transform_list._fields_ = [
    ('count', c_int),
    ('params', String),
    ('where_used', String),
    ('comment', String),
    ('next', POINTER(struct_gpj_datum_transform_list)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 63
class struct_gpj_ellps(Structure):
    pass

struct_gpj_ellps.__slots__ = [
    'name',
    'longname',
    'a',
    'es',
    'rf',
]
struct_gpj_ellps._fields_ = [
    ('name', String),
    ('longname', String),
    ('a', c_double),
    ('es', c_double),
    ('rf', c_double),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 70
if hasattr(_libs['grass_gproj.7.0.svn'], 'pj_do_proj'):
    pj_do_proj = _libs['grass_gproj.7.0.svn'].pj_do_proj
    pj_do_proj.restype = c_int
    pj_do_proj.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(struct_pj_info), POINTER(struct_pj_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 71
if hasattr(_libs['grass_gproj.7.0.svn'], 'pj_do_transform'):
    pj_do_transform = _libs['grass_gproj.7.0.svn'].pj_do_transform
    pj_do_transform.restype = c_int
    pj_do_transform.argtypes = [c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(struct_pj_info), POINTER(struct_pj_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 75
class struct_Key_Value(Structure):
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 75
if hasattr(_libs['grass_gproj.7.0.svn'], 'pj_get_kv'):
    pj_get_kv = _libs['grass_gproj.7.0.svn'].pj_get_kv
    pj_get_kv.restype = c_int
    pj_get_kv.argtypes = [POINTER(struct_pj_info), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 76
if hasattr(_libs['grass_gproj.7.0.svn'], 'pj_get_string'):
    pj_get_string = _libs['grass_gproj.7.0.svn'].pj_get_string
    pj_get_string.restype = c_int
    pj_get_string.argtypes = [POINTER(struct_pj_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 77
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_get_equivalent_latlong'):
    GPJ_get_equivalent_latlong = _libs['grass_gproj.7.0.svn'].GPJ_get_equivalent_latlong
    GPJ_get_equivalent_latlong.restype = c_int
    GPJ_get_equivalent_latlong.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 78
if hasattr(_libs['grass_gproj.7.0.svn'], 'set_proj_lib'):
    set_proj_lib = _libs['grass_gproj.7.0.svn'].set_proj_lib
    set_proj_lib.restype = ReturnString
    set_proj_lib.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 79
if hasattr(_libs['grass_gproj.7.0.svn'], 'pj_print_proj_params'):
    pj_print_proj_params = _libs['grass_gproj.7.0.svn'].pj_print_proj_params
    pj_print_proj_params.restype = c_int
    pj_print_proj_params.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 83
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_grass_to_wkt'):
    GPJ_grass_to_wkt = _libs['grass_gproj.7.0.svn'].GPJ_grass_to_wkt
    GPJ_grass_to_wkt.restype = ReturnString
    GPJ_grass_to_wkt.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 84
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_grass_to_osr'):
    GPJ_grass_to_osr = _libs['grass_gproj.7.0.svn'].GPJ_grass_to_osr
    GPJ_grass_to_osr.restype = OGRSpatialReferenceH
    GPJ_grass_to_osr.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 85
class struct_Cell_head(Structure):
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 85
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_wkt_to_grass'):
    GPJ_wkt_to_grass = _libs['grass_gproj.7.0.svn'].GPJ_wkt_to_grass
    GPJ_wkt_to_grass.restype = c_int
    GPJ_wkt_to_grass.argtypes = [POINTER(struct_Cell_head), POINTER(POINTER(struct_Key_Value)), POINTER(POINTER(struct_Key_Value)), String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 87
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_osr_to_grass'):
    GPJ_osr_to_grass = _libs['grass_gproj.7.0.svn'].GPJ_osr_to_grass
    GPJ_osr_to_grass.restype = c_int
    GPJ_osr_to_grass.argtypes = [POINTER(struct_Cell_head), POINTER(POINTER(struct_Key_Value)), POINTER(POINTER(struct_Key_Value)), OGRSpatialReferenceH, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 89
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_set_csv_loc'):
    GPJ_set_csv_loc = _libs['grass_gproj.7.0.svn'].GPJ_set_csv_loc
    GPJ_set_csv_loc.restype = ReturnString
    GPJ_set_csv_loc.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 93
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_get_datum_by_name'):
    GPJ_get_datum_by_name = _libs['grass_gproj.7.0.svn'].GPJ_get_datum_by_name
    GPJ_get_datum_by_name.restype = c_int
    GPJ_get_datum_by_name.argtypes = [String, POINTER(struct_gpj_datum)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 94
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_get_default_datum_params_by_name'):
    GPJ_get_default_datum_params_by_name = _libs['grass_gproj.7.0.svn'].GPJ_get_default_datum_params_by_name
    GPJ_get_default_datum_params_by_name.restype = c_int
    GPJ_get_default_datum_params_by_name.argtypes = [String, POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 95
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_get_datum_params'):
    GPJ_get_datum_params = _libs['grass_gproj.7.0.svn'].GPJ_get_datum_params
    GPJ_get_datum_params.restype = c_int
    GPJ_get_datum_params.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 96
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ__get_datum_params'):
    GPJ__get_datum_params = _libs['grass_gproj.7.0.svn'].GPJ__get_datum_params
    GPJ__get_datum_params.restype = c_int
    GPJ__get_datum_params.argtypes = [POINTER(struct_Key_Value), POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 97
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_free_datum'):
    GPJ_free_datum = _libs['grass_gproj.7.0.svn'].GPJ_free_datum
    GPJ_free_datum.restype = None
    GPJ_free_datum.argtypes = [POINTER(struct_gpj_datum)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 98
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_get_datum_transform_by_name'):
    GPJ_get_datum_transform_by_name = _libs['grass_gproj.7.0.svn'].GPJ_get_datum_transform_by_name
    GPJ_get_datum_transform_by_name.restype = POINTER(struct_gpj_datum_transform_list)
    GPJ_get_datum_transform_by_name.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 99
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_free_datum_transform'):
    GPJ_free_datum_transform = _libs['grass_gproj.7.0.svn'].GPJ_free_datum_transform
    GPJ_free_datum_transform.restype = None
    GPJ_free_datum_transform.argtypes = [POINTER(struct_gpj_datum_transform_list)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 102
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_get_ellipsoid_by_name'):
    GPJ_get_ellipsoid_by_name = _libs['grass_gproj.7.0.svn'].GPJ_get_ellipsoid_by_name
    GPJ_get_ellipsoid_by_name.restype = c_int
    GPJ_get_ellipsoid_by_name.argtypes = [String, POINTER(struct_gpj_ellps)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 103
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_get_ellipsoid_params'):
    GPJ_get_ellipsoid_params = _libs['grass_gproj.7.0.svn'].GPJ_get_ellipsoid_params
    GPJ_get_ellipsoid_params.restype = c_int
    GPJ_get_ellipsoid_params.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 104
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ__get_ellipsoid_params'):
    GPJ__get_ellipsoid_params = _libs['grass_gproj.7.0.svn'].GPJ__get_ellipsoid_params
    GPJ__get_ellipsoid_params.restype = c_int
    GPJ__get_ellipsoid_params.argtypes = [POINTER(struct_Key_Value), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 106
if hasattr(_libs['grass_gproj.7.0.svn'], 'GPJ_free_ellps'):
    GPJ_free_ellps = _libs['grass_gproj.7.0.svn'].GPJ_free_ellps
    GPJ_free_ellps.restype = None
    GPJ_free_ellps.argtypes = [POINTER(struct_gpj_ellps)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 113
class struct_anon_44(Structure):
    pass

struct_anon_44.__slots__ = [
    'u',
    'v',
]
struct_anon_44._fields_ = [
    ('u', c_double),
    ('v', c_double),
]

LP = struct_anon_44 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 113

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 115
class struct_DERIVS(Structure):
    pass

struct_DERIVS.__slots__ = [
    'x_l',
    'x_p',
    'y_l',
    'y_p',
]
struct_DERIVS._fields_ = [
    ('x_l', c_double),
    ('x_p', c_double),
    ('y_l', c_double),
    ('y_p', c_double),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 120
class struct_FACTORS(Structure):
    pass

struct_FACTORS.__slots__ = [
    'der',
    'h',
    'k',
    'omega',
    'thetap',
    'conv',
    's',
    'a',
    'b',
    'code',
]
struct_FACTORS._fields_ = [
    ('der', struct_DERIVS),
    ('h', c_double),
    ('k', c_double),
    ('omega', c_double),
    ('thetap', c_double),
    ('conv', c_double),
    ('s', c_double),
    ('a', c_double),
    ('b', c_double),
    ('code', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 130
if hasattr(_libs['grass_gproj.7.0.svn'], 'pj_factors'):
    pj_factors = _libs['grass_gproj.7.0.svn'].pj_factors
    pj_factors.restype = c_int
    pj_factors.argtypes = [LP, POINTER(None), c_double, POINTER(struct_FACTORS)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 27
try:
    ELLIPSOIDTABLE = '/etc/ellipse.table'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 27
try:
    DATUMTABLE = '/etc/datum.table'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 27
try:
    DATUMTRANSFORMTABLE = '/etc/datumtransform.table'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 28
try:
    GRIDDIR = '/etc/nad'
except:
    pass

pj_info = struct_pj_info # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 33

gpj_datum = struct_gpj_datum # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 41

gpj_datum_transform_list = struct_gpj_datum_transform_list # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 47

gpj_ellps = struct_gpj_ellps # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 63

Key_Value = struct_Key_Value # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 75

Cell_head = struct_Cell_head # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 85

DERIVS = struct_DERIVS # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 115

FACTORS = struct_FACTORS # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gprojects.h: 120

# No inserted files

