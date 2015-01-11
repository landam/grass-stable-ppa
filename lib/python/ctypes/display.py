'''Wrapper for display.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_display.7.0.svn /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h -o display.py

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

_libs["grass_display.7.0.svn"] = load_library("grass_display.7.0.svn")

# 1 libraries
# End libraries

# No modules

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 273
class struct_Cell_head(Structure):
    pass

struct_Cell_head.__slots__ = [
    'format',
    'compressed',
    'rows',
    'rows3',
    'cols',
    'cols3',
    'depths',
    'proj',
    'zone',
    'ew_res',
    'ew_res3',
    'ns_res',
    'ns_res3',
    'tb_res',
    'north',
    'south',
    'east',
    'west',
    'top',
    'bottom',
]
struct_Cell_head._fields_ = [
    ('format', c_int),
    ('compressed', c_int),
    ('rows', c_int),
    ('rows3', c_int),
    ('cols', c_int),
    ('cols3', c_int),
    ('depths', c_int),
    ('proj', c_int),
    ('zone', c_int),
    ('ew_res', c_double),
    ('ew_res3', c_double),
    ('ns_res', c_double),
    ('ns_res3', c_double),
    ('tb_res', c_double),
    ('north', c_double),
    ('south', c_double),
    ('east', c_double),
    ('west', c_double),
    ('top', c_double),
    ('bottom', c_double),
]

CELL = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 402

DCELL = c_double # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 403

FCELL = c_float # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 404

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 406
class struct__Color_Value_(Structure):
    pass

struct__Color_Value_.__slots__ = [
    'value',
    'red',
    'grn',
    'blu',
]
struct__Color_Value_._fields_ = [
    ('value', DCELL),
    ('red', c_ubyte),
    ('grn', c_ubyte),
    ('blu', c_ubyte),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 414
class struct__Color_Rule_(Structure):
    pass

struct__Color_Rule_.__slots__ = [
    'low',
    'high',
    'next',
    'prev',
]
struct__Color_Rule_._fields_ = [
    ('low', struct__Color_Value_),
    ('high', struct__Color_Value_),
    ('next', POINTER(struct__Color_Rule_)),
    ('prev', POINTER(struct__Color_Rule_)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 426
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'red',
    'grn',
    'blu',
    'set',
    'nalloc',
    'active',
]
struct_anon_8._fields_ = [
    ('red', POINTER(c_ubyte)),
    ('grn', POINTER(c_ubyte)),
    ('blu', POINTER(c_ubyte)),
    ('set', POINTER(c_ubyte)),
    ('nalloc', c_int),
    ('active', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 436
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'vals',
    'rules',
    'nalloc',
    'active',
]
struct_anon_9._fields_ = [
    ('vals', POINTER(DCELL)),
    ('rules', POINTER(POINTER(struct__Color_Rule_))),
    ('nalloc', c_int),
    ('active', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 421
class struct__Color_Info_(Structure):
    pass

struct__Color_Info_.__slots__ = [
    'rules',
    'n_rules',
    'lookup',
    'fp_lookup',
    'min',
    'max',
]
struct__Color_Info_._fields_ = [
    ('rules', POINTER(struct__Color_Rule_)),
    ('n_rules', c_int),
    ('lookup', struct_anon_8),
    ('fp_lookup', struct_anon_9),
    ('min', DCELL),
    ('max', DCELL),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 448
class struct_Colors(Structure):
    pass

struct_Colors.__slots__ = [
    'version',
    'shift',
    'invert',
    'is_float',
    'null_set',
    'null_red',
    'null_grn',
    'null_blu',
    'undef_set',
    'undef_red',
    'undef_grn',
    'undef_blu',
    'fixed',
    'modular',
    'cmin',
    'cmax',
    'organizing',
]
struct_Colors._fields_ = [
    ('version', c_int),
    ('shift', DCELL),
    ('invert', c_int),
    ('is_float', c_int),
    ('null_set', c_int),
    ('null_red', c_ubyte),
    ('null_grn', c_ubyte),
    ('null_blu', c_ubyte),
    ('undef_set', c_int),
    ('undef_red', c_ubyte),
    ('undef_grn', c_ubyte),
    ('undef_blu', c_ubyte),
    ('fixed', struct__Color_Info_),
    ('modular', struct__Color_Info_),
    ('cmin', DCELL),
    ('cmax', DCELL),
    ('organizing', c_int),
]

RASTER_MAP_TYPE = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 22

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 228
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'r',
    'g',
    'b',
    'a',
]
struct_anon_24._fields_ = [
    ('r', c_ubyte),
    ('g', c_ubyte),
    ('b', c_ubyte),
    ('a', c_ubyte),
]

RGBA_Color = struct_anon_24 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 228

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 27
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'color',
    'r',
    'g',
    'b',
    'fr',
    'fg',
    'fb',
]
struct_anon_25._fields_ = [
    ('color', c_int),
    ('r', c_int),
    ('g', c_int),
    ('b', c_int),
    ('fr', c_double),
    ('fg', c_double),
    ('fb', c_double),
]

SYMBCOLOR = struct_anon_25 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 27

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 35
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'count',
    'alloc',
    'x',
    'y',
]
struct_anon_26._fields_ = [
    ('count', c_int),
    ('alloc', c_int),
    ('x', POINTER(c_double)),
    ('y', POINTER(c_double)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 40
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'clock',
    'x',
    'y',
    'r',
    'a1',
    'a2',
]
struct_anon_27._fields_ = [
    ('clock', c_int),
    ('x', c_double),
    ('y', c_double),
    ('r', c_double),
    ('a1', c_double),
    ('a2', c_double),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 33
class union_anon_28(Union):
    pass

union_anon_28.__slots__ = [
    'line',
    'arc',
]
union_anon_28._fields_ = [
    ('line', struct_anon_26),
    ('arc', struct_anon_27),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 46
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'type',
    'coor',
]
struct_anon_29._fields_ = [
    ('type', c_int),
    ('coor', union_anon_28),
]

SYMBEL = struct_anon_29 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 46

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 55
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'count',
    'alloc',
    'elem',
    'scount',
    'salloc',
    'sx',
    'sy',
]
struct_anon_30._fields_ = [
    ('count', c_int),
    ('alloc', c_int),
    ('elem', POINTER(POINTER(SYMBEL))),
    ('scount', c_int),
    ('salloc', c_int),
    ('sx', POINTER(c_int)),
    ('sy', POINTER(c_int)),
]

SYMBCHAIN = struct_anon_30 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 55

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 65
class struct_anon_31(Structure):
    pass

struct_anon_31.__slots__ = [
    'type',
    'color',
    'fcolor',
    'count',
    'alloc',
    'chain',
]
struct_anon_31._fields_ = [
    ('type', c_int),
    ('color', SYMBCOLOR),
    ('fcolor', SYMBCOLOR),
    ('count', c_int),
    ('alloc', c_int),
    ('chain', POINTER(POINTER(SYMBCHAIN))),
]

SYMBPART = struct_anon_31 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 65

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 72
class struct_anon_32(Structure):
    pass

struct_anon_32.__slots__ = [
    'scale',
    'count',
    'alloc',
    'part',
]
struct_anon_32._fields_ = [
    ('scale', c_double),
    ('count', c_int),
    ('alloc', c_int),
    ('part', POINTER(POINTER(SYMBPART))),
]

SYMBOL = struct_anon_32 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/symbol.h: 72

enum_clip_mode = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 8

M_NONE = 0 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 8

M_CULL = (M_NONE + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 8

M_CLIP = (M_CULL + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 8

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 16
if hasattr(_libs['grass_display.7.0.svn'], 'D_update_conversions'):
    D_update_conversions = _libs['grass_display.7.0.svn'].D_update_conversions
    D_update_conversions.restype = None
    D_update_conversions.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 17
if hasattr(_libs['grass_display.7.0.svn'], 'D_fit_d_to_u'):
    D_fit_d_to_u = _libs['grass_display.7.0.svn'].D_fit_d_to_u
    D_fit_d_to_u.restype = None
    D_fit_d_to_u.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 18
if hasattr(_libs['grass_display.7.0.svn'], 'D_fit_u_to_d'):
    D_fit_u_to_d = _libs['grass_display.7.0.svn'].D_fit_u_to_d
    D_fit_u_to_d.restype = None
    D_fit_u_to_d.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 19
if hasattr(_libs['grass_display.7.0.svn'], 'D_show_conversions'):
    D_show_conversions = _libs['grass_display.7.0.svn'].D_show_conversions
    D_show_conversions.restype = None
    D_show_conversions.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 21
if hasattr(_libs['grass_display.7.0.svn'], 'D_do_conversions'):
    D_do_conversions = _libs['grass_display.7.0.svn'].D_do_conversions
    D_do_conversions.restype = None
    D_do_conversions.argtypes = [POINTER(struct_Cell_head), c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 23
if hasattr(_libs['grass_display.7.0.svn'], 'D_is_lat_lon'):
    D_is_lat_lon = _libs['grass_display.7.0.svn'].D_is_lat_lon
    D_is_lat_lon.restype = c_int
    D_is_lat_lon.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 25
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_d_to_a_xconv'):
    D_get_d_to_a_xconv = _libs['grass_display.7.0.svn'].D_get_d_to_a_xconv
    D_get_d_to_a_xconv.restype = c_double
    D_get_d_to_a_xconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 26
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_d_to_a_yconv'):
    D_get_d_to_a_yconv = _libs['grass_display.7.0.svn'].D_get_d_to_a_yconv
    D_get_d_to_a_yconv.restype = c_double
    D_get_d_to_a_yconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 27
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_d_to_u_xconv'):
    D_get_d_to_u_xconv = _libs['grass_display.7.0.svn'].D_get_d_to_u_xconv
    D_get_d_to_u_xconv.restype = c_double
    D_get_d_to_u_xconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 28
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_d_to_u_yconv'):
    D_get_d_to_u_yconv = _libs['grass_display.7.0.svn'].D_get_d_to_u_yconv
    D_get_d_to_u_yconv.restype = c_double
    D_get_d_to_u_yconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 29
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_a_to_u_xconv'):
    D_get_a_to_u_xconv = _libs['grass_display.7.0.svn'].D_get_a_to_u_xconv
    D_get_a_to_u_xconv.restype = c_double
    D_get_a_to_u_xconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 30
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_a_to_u_yconv'):
    D_get_a_to_u_yconv = _libs['grass_display.7.0.svn'].D_get_a_to_u_yconv
    D_get_a_to_u_yconv.restype = c_double
    D_get_a_to_u_yconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 31
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_a_to_d_xconv'):
    D_get_a_to_d_xconv = _libs['grass_display.7.0.svn'].D_get_a_to_d_xconv
    D_get_a_to_d_xconv.restype = c_double
    D_get_a_to_d_xconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 32
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_a_to_d_yconv'):
    D_get_a_to_d_yconv = _libs['grass_display.7.0.svn'].D_get_a_to_d_yconv
    D_get_a_to_d_yconv.restype = c_double
    D_get_a_to_d_yconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 33
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_u_to_d_xconv'):
    D_get_u_to_d_xconv = _libs['grass_display.7.0.svn'].D_get_u_to_d_xconv
    D_get_u_to_d_xconv.restype = c_double
    D_get_u_to_d_xconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 34
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_u_to_d_yconv'):
    D_get_u_to_d_yconv = _libs['grass_display.7.0.svn'].D_get_u_to_d_yconv
    D_get_u_to_d_yconv.restype = c_double
    D_get_u_to_d_yconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 35
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_u_to_a_xconv'):
    D_get_u_to_a_xconv = _libs['grass_display.7.0.svn'].D_get_u_to_a_xconv
    D_get_u_to_a_xconv.restype = c_double
    D_get_u_to_a_xconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 36
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_u_to_a_yconv'):
    D_get_u_to_a_yconv = _libs['grass_display.7.0.svn'].D_get_u_to_a_yconv
    D_get_u_to_a_yconv.restype = c_double
    D_get_u_to_a_yconv.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 38
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_ns_resolution'):
    D_get_ns_resolution = _libs['grass_display.7.0.svn'].D_get_ns_resolution
    D_get_ns_resolution.restype = c_double
    D_get_ns_resolution.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 39
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_ew_resolution'):
    D_get_ew_resolution = _libs['grass_display.7.0.svn'].D_get_ew_resolution
    D_get_ew_resolution.restype = c_double
    D_get_ew_resolution.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 41
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_u_west'):
    D_get_u_west = _libs['grass_display.7.0.svn'].D_get_u_west
    D_get_u_west.restype = c_double
    D_get_u_west.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 42
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_u_east'):
    D_get_u_east = _libs['grass_display.7.0.svn'].D_get_u_east
    D_get_u_east.restype = c_double
    D_get_u_east.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 43
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_u_north'):
    D_get_u_north = _libs['grass_display.7.0.svn'].D_get_u_north
    D_get_u_north.restype = c_double
    D_get_u_north.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 44
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_u_south'):
    D_get_u_south = _libs['grass_display.7.0.svn'].D_get_u_south
    D_get_u_south.restype = c_double
    D_get_u_south.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 45
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_a_west'):
    D_get_a_west = _libs['grass_display.7.0.svn'].D_get_a_west
    D_get_a_west.restype = c_double
    D_get_a_west.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 46
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_a_east'):
    D_get_a_east = _libs['grass_display.7.0.svn'].D_get_a_east
    D_get_a_east.restype = c_double
    D_get_a_east.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 47
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_a_north'):
    D_get_a_north = _libs['grass_display.7.0.svn'].D_get_a_north
    D_get_a_north.restype = c_double
    D_get_a_north.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 48
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_a_south'):
    D_get_a_south = _libs['grass_display.7.0.svn'].D_get_a_south
    D_get_a_south.restype = c_double
    D_get_a_south.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 49
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_d_west'):
    D_get_d_west = _libs['grass_display.7.0.svn'].D_get_d_west
    D_get_d_west.restype = c_double
    D_get_d_west.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 50
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_d_east'):
    D_get_d_east = _libs['grass_display.7.0.svn'].D_get_d_east
    D_get_d_east.restype = c_double
    D_get_d_east.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 51
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_d_north'):
    D_get_d_north = _libs['grass_display.7.0.svn'].D_get_d_north
    D_get_d_north.restype = c_double
    D_get_d_north.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 52
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_d_south'):
    D_get_d_south = _libs['grass_display.7.0.svn'].D_get_d_south
    D_get_d_south.restype = c_double
    D_get_d_south.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 54
if hasattr(_libs['grass_display.7.0.svn'], 'D_set_region'):
    D_set_region = _libs['grass_display.7.0.svn'].D_set_region
    D_set_region.restype = None
    D_set_region.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 55
if hasattr(_libs['grass_display.7.0.svn'], 'D_set_src'):
    D_set_src = _libs['grass_display.7.0.svn'].D_set_src
    D_set_src.restype = None
    D_set_src.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 56
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_src'):
    D_get_src = _libs['grass_display.7.0.svn'].D_get_src
    D_get_src.restype = None
    D_get_src.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 57
if hasattr(_libs['grass_display.7.0.svn'], 'D_set_grid'):
    D_set_grid = _libs['grass_display.7.0.svn'].D_set_grid
    D_set_grid.restype = None
    D_set_grid.argtypes = [c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 58
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_grid'):
    D_get_grid = _libs['grass_display.7.0.svn'].D_get_grid
    D_get_grid.restype = None
    D_get_grid.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 59
if hasattr(_libs['grass_display.7.0.svn'], 'D_set_dst'):
    D_set_dst = _libs['grass_display.7.0.svn'].D_set_dst
    D_set_dst.restype = None
    D_set_dst.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 60
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_dst'):
    D_get_dst = _libs['grass_display.7.0.svn'].D_get_dst
    D_get_dst.restype = None
    D_get_dst.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 62
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_u'):
    D_get_u = _libs['grass_display.7.0.svn'].D_get_u
    D_get_u.restype = None
    D_get_u.argtypes = [(c_double * 2) * 2]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 63
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_a'):
    D_get_a = _libs['grass_display.7.0.svn'].D_get_a
    D_get_a.restype = None
    D_get_a.argtypes = [(c_int * 2) * 2]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 64
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_d'):
    D_get_d = _libs['grass_display.7.0.svn'].D_get_d
    D_get_d.restype = None
    D_get_d.argtypes = [(c_double * 2) * 2]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 66
if hasattr(_libs['grass_display.7.0.svn'], 'D_d_to_a_row'):
    D_d_to_a_row = _libs['grass_display.7.0.svn'].D_d_to_a_row
    D_d_to_a_row.restype = c_double
    D_d_to_a_row.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 67
if hasattr(_libs['grass_display.7.0.svn'], 'D_d_to_a_col'):
    D_d_to_a_col = _libs['grass_display.7.0.svn'].D_d_to_a_col
    D_d_to_a_col.restype = c_double
    D_d_to_a_col.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 68
if hasattr(_libs['grass_display.7.0.svn'], 'D_d_to_u_row'):
    D_d_to_u_row = _libs['grass_display.7.0.svn'].D_d_to_u_row
    D_d_to_u_row.restype = c_double
    D_d_to_u_row.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 69
if hasattr(_libs['grass_display.7.0.svn'], 'D_d_to_u_col'):
    D_d_to_u_col = _libs['grass_display.7.0.svn'].D_d_to_u_col
    D_d_to_u_col.restype = c_double
    D_d_to_u_col.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 70
if hasattr(_libs['grass_display.7.0.svn'], 'D_a_to_u_row'):
    D_a_to_u_row = _libs['grass_display.7.0.svn'].D_a_to_u_row
    D_a_to_u_row.restype = c_double
    D_a_to_u_row.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 71
if hasattr(_libs['grass_display.7.0.svn'], 'D_a_to_u_col'):
    D_a_to_u_col = _libs['grass_display.7.0.svn'].D_a_to_u_col
    D_a_to_u_col.restype = c_double
    D_a_to_u_col.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 72
if hasattr(_libs['grass_display.7.0.svn'], 'D_a_to_d_row'):
    D_a_to_d_row = _libs['grass_display.7.0.svn'].D_a_to_d_row
    D_a_to_d_row.restype = c_double
    D_a_to_d_row.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 73
if hasattr(_libs['grass_display.7.0.svn'], 'D_a_to_d_col'):
    D_a_to_d_col = _libs['grass_display.7.0.svn'].D_a_to_d_col
    D_a_to_d_col.restype = c_double
    D_a_to_d_col.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 74
if hasattr(_libs['grass_display.7.0.svn'], 'D_u_to_d_row'):
    D_u_to_d_row = _libs['grass_display.7.0.svn'].D_u_to_d_row
    D_u_to_d_row.restype = c_double
    D_u_to_d_row.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 75
if hasattr(_libs['grass_display.7.0.svn'], 'D_u_to_d_col'):
    D_u_to_d_col = _libs['grass_display.7.0.svn'].D_u_to_d_col
    D_u_to_d_col.restype = c_double
    D_u_to_d_col.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 76
if hasattr(_libs['grass_display.7.0.svn'], 'D_u_to_a_row'):
    D_u_to_a_row = _libs['grass_display.7.0.svn'].D_u_to_a_row
    D_u_to_a_row.restype = c_double
    D_u_to_a_row.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 77
if hasattr(_libs['grass_display.7.0.svn'], 'D_u_to_a_col'):
    D_u_to_a_col = _libs['grass_display.7.0.svn'].D_u_to_a_col
    D_u_to_a_col.restype = c_double
    D_u_to_a_col.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 81
if hasattr(_libs['grass_display.7.0.svn'], 'D_set_clip'):
    D_set_clip = _libs['grass_display.7.0.svn'].D_set_clip
    D_set_clip.restype = None
    D_set_clip.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 82
if hasattr(_libs['grass_display.7.0.svn'], 'D_clip_to_map'):
    D_clip_to_map = _libs['grass_display.7.0.svn'].D_clip_to_map
    D_clip_to_map.restype = None
    D_clip_to_map.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 83
if hasattr(_libs['grass_display.7.0.svn'], 'D_set_clip_mode'):
    D_set_clip_mode = _libs['grass_display.7.0.svn'].D_set_clip_mode
    D_set_clip_mode.restype = None
    D_set_clip_mode.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 84
if hasattr(_libs['grass_display.7.0.svn'], 'D_set_reduction'):
    D_set_reduction = _libs['grass_display.7.0.svn'].D_set_reduction
    D_set_reduction.restype = None
    D_set_reduction.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 86
if hasattr(_libs['grass_display.7.0.svn'], 'D_line_width'):
    D_line_width = _libs['grass_display.7.0.svn'].D_line_width
    D_line_width.restype = None
    D_line_width.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 87
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_text_box'):
    D_get_text_box = _libs['grass_display.7.0.svn'].D_get_text_box
    D_get_text_box.restype = None
    D_get_text_box.argtypes = [String, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 89
if hasattr(_libs['grass_display.7.0.svn'], 'D_pos_abs'):
    D_pos_abs = _libs['grass_display.7.0.svn'].D_pos_abs
    D_pos_abs.restype = None
    D_pos_abs.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 90
if hasattr(_libs['grass_display.7.0.svn'], 'D_pos_rel'):
    D_pos_rel = _libs['grass_display.7.0.svn'].D_pos_rel
    D_pos_rel.restype = None
    D_pos_rel.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 91
if hasattr(_libs['grass_display.7.0.svn'], 'D_move_abs'):
    D_move_abs = _libs['grass_display.7.0.svn'].D_move_abs
    D_move_abs.restype = None
    D_move_abs.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 92
if hasattr(_libs['grass_display.7.0.svn'], 'D_move_rel'):
    D_move_rel = _libs['grass_display.7.0.svn'].D_move_rel
    D_move_rel.restype = None
    D_move_rel.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 93
if hasattr(_libs['grass_display.7.0.svn'], 'D_cont_abs'):
    D_cont_abs = _libs['grass_display.7.0.svn'].D_cont_abs
    D_cont_abs.restype = None
    D_cont_abs.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 94
if hasattr(_libs['grass_display.7.0.svn'], 'D_cont_rel'):
    D_cont_rel = _libs['grass_display.7.0.svn'].D_cont_rel
    D_cont_rel.restype = None
    D_cont_rel.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 95
if hasattr(_libs['grass_display.7.0.svn'], 'D_line_abs'):
    D_line_abs = _libs['grass_display.7.0.svn'].D_line_abs
    D_line_abs.restype = None
    D_line_abs.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 96
if hasattr(_libs['grass_display.7.0.svn'], 'D_line_rel'):
    D_line_rel = _libs['grass_display.7.0.svn'].D_line_rel
    D_line_rel.restype = None
    D_line_rel.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 97
if hasattr(_libs['grass_display.7.0.svn'], 'D_polydots_abs'):
    D_polydots_abs = _libs['grass_display.7.0.svn'].D_polydots_abs
    D_polydots_abs.restype = None
    D_polydots_abs.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 98
if hasattr(_libs['grass_display.7.0.svn'], 'D_polydots_rel'):
    D_polydots_rel = _libs['grass_display.7.0.svn'].D_polydots_rel
    D_polydots_rel.restype = None
    D_polydots_rel.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 99
if hasattr(_libs['grass_display.7.0.svn'], 'D_polyline_abs'):
    D_polyline_abs = _libs['grass_display.7.0.svn'].D_polyline_abs
    D_polyline_abs.restype = None
    D_polyline_abs.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 100
if hasattr(_libs['grass_display.7.0.svn'], 'D_polyline_rel'):
    D_polyline_rel = _libs['grass_display.7.0.svn'].D_polyline_rel
    D_polyline_rel.restype = None
    D_polyline_rel.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 101
if hasattr(_libs['grass_display.7.0.svn'], 'D_polygon_abs'):
    D_polygon_abs = _libs['grass_display.7.0.svn'].D_polygon_abs
    D_polygon_abs.restype = None
    D_polygon_abs.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 102
if hasattr(_libs['grass_display.7.0.svn'], 'D_polygon_rel'):
    D_polygon_rel = _libs['grass_display.7.0.svn'].D_polygon_rel
    D_polygon_rel.restype = None
    D_polygon_rel.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 103
if hasattr(_libs['grass_display.7.0.svn'], 'D_box_abs'):
    D_box_abs = _libs['grass_display.7.0.svn'].D_box_abs
    D_box_abs.restype = None
    D_box_abs.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 104
if hasattr(_libs['grass_display.7.0.svn'], 'D_box_rel'):
    D_box_rel = _libs['grass_display.7.0.svn'].D_box_rel
    D_box_rel.restype = None
    D_box_rel.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 106
if hasattr(_libs['grass_display.7.0.svn'], 'D_begin'):
    D_begin = _libs['grass_display.7.0.svn'].D_begin
    D_begin.restype = None
    D_begin.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 107
if hasattr(_libs['grass_display.7.0.svn'], 'D_end'):
    D_end = _libs['grass_display.7.0.svn'].D_end
    D_end.restype = None
    D_end.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 108
if hasattr(_libs['grass_display.7.0.svn'], 'D_close'):
    D_close = _libs['grass_display.7.0.svn'].D_close
    D_close.restype = None
    D_close.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 109
if hasattr(_libs['grass_display.7.0.svn'], 'D_stroke'):
    D_stroke = _libs['grass_display.7.0.svn'].D_stroke
    D_stroke.restype = None
    D_stroke.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 110
if hasattr(_libs['grass_display.7.0.svn'], 'D_fill'):
    D_fill = _libs['grass_display.7.0.svn'].D_fill
    D_fill.restype = None
    D_fill.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 111
if hasattr(_libs['grass_display.7.0.svn'], 'D_dots'):
    D_dots = _libs['grass_display.7.0.svn'].D_dots
    D_dots.restype = None
    D_dots.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 114
if hasattr(_libs['grass_display.7.0.svn'], 'D_plot_icon'):
    D_plot_icon = _libs['grass_display.7.0.svn'].D_plot_icon
    D_plot_icon.restype = None
    D_plot_icon.argtypes = [c_double, c_double, c_int, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 117
if hasattr(_libs['grass_display.7.0.svn'], 'D_draw_raster'):
    D_draw_raster = _libs['grass_display.7.0.svn'].D_draw_raster
    D_draw_raster.restype = c_int
    D_draw_raster.argtypes = [c_int, POINTER(None), POINTER(struct_Colors), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 118
if hasattr(_libs['grass_display.7.0.svn'], 'D_draw_d_raster'):
    D_draw_d_raster = _libs['grass_display.7.0.svn'].D_draw_d_raster
    D_draw_d_raster.restype = c_int
    D_draw_d_raster.argtypes = [c_int, POINTER(DCELL), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 119
if hasattr(_libs['grass_display.7.0.svn'], 'D_draw_f_raster'):
    D_draw_f_raster = _libs['grass_display.7.0.svn'].D_draw_f_raster
    D_draw_f_raster.restype = c_int
    D_draw_f_raster.argtypes = [c_int, POINTER(FCELL), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 120
if hasattr(_libs['grass_display.7.0.svn'], 'D_draw_c_raster'):
    D_draw_c_raster = _libs['grass_display.7.0.svn'].D_draw_c_raster
    D_draw_c_raster.restype = c_int
    D_draw_c_raster.argtypes = [c_int, POINTER(CELL), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 121
if hasattr(_libs['grass_display.7.0.svn'], 'D_draw_cell'):
    D_draw_cell = _libs['grass_display.7.0.svn'].D_draw_cell
    D_draw_cell.restype = c_int
    D_draw_cell.argtypes = [c_int, POINTER(CELL), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 122
if hasattr(_libs['grass_display.7.0.svn'], 'D_cell_draw_begin'):
    D_cell_draw_begin = _libs['grass_display.7.0.svn'].D_cell_draw_begin
    D_cell_draw_begin.restype = None
    D_cell_draw_begin.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 123
if hasattr(_libs['grass_display.7.0.svn'], 'D_draw_raster_RGB'):
    D_draw_raster_RGB = _libs['grass_display.7.0.svn'].D_draw_raster_RGB
    D_draw_raster_RGB.restype = c_int
    D_draw_raster_RGB.argtypes = [c_int, POINTER(None), POINTER(None), POINTER(None), POINTER(struct_Colors), POINTER(struct_Colors), POINTER(struct_Colors), RASTER_MAP_TYPE, RASTER_MAP_TYPE, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 126
if hasattr(_libs['grass_display.7.0.svn'], 'D_cell_draw_end'):
    D_cell_draw_end = _libs['grass_display.7.0.svn'].D_cell_draw_end
    D_cell_draw_end.restype = None
    D_cell_draw_end.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 129
if hasattr(_libs['grass_display.7.0.svn'], 'D_set_overlay_mode'):
    D_set_overlay_mode = _libs['grass_display.7.0.svn'].D_set_overlay_mode
    D_set_overlay_mode.restype = c_int
    D_set_overlay_mode.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 130
if hasattr(_libs['grass_display.7.0.svn'], 'D_color'):
    D_color = _libs['grass_display.7.0.svn'].D_color
    D_color.restype = c_int
    D_color.argtypes = [CELL, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 131
if hasattr(_libs['grass_display.7.0.svn'], 'D_c_color'):
    D_c_color = _libs['grass_display.7.0.svn'].D_c_color
    D_c_color.restype = c_int
    D_c_color.argtypes = [CELL, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 132
if hasattr(_libs['grass_display.7.0.svn'], 'D_d_color'):
    D_d_color = _libs['grass_display.7.0.svn'].D_d_color
    D_d_color.restype = c_int
    D_d_color.argtypes = [DCELL, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 133
if hasattr(_libs['grass_display.7.0.svn'], 'D_f_color'):
    D_f_color = _libs['grass_display.7.0.svn'].D_f_color
    D_f_color.restype = c_int
    D_f_color.argtypes = [FCELL, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 134
if hasattr(_libs['grass_display.7.0.svn'], 'D_color_of_type'):
    D_color_of_type = _libs['grass_display.7.0.svn'].D_color_of_type
    D_color_of_type.restype = c_int
    D_color_of_type.argtypes = [POINTER(None), POINTER(struct_Colors), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 137
if hasattr(_libs['grass_display.7.0.svn'], 'D_setup'):
    D_setup = _libs['grass_display.7.0.svn'].D_setup
    D_setup.restype = None
    D_setup.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 138
if hasattr(_libs['grass_display.7.0.svn'], 'D_setup_unity'):
    D_setup_unity = _libs['grass_display.7.0.svn'].D_setup_unity
    D_setup_unity.restype = None
    D_setup_unity.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 139
if hasattr(_libs['grass_display.7.0.svn'], 'D_setup2'):
    D_setup2 = _libs['grass_display.7.0.svn'].D_setup2
    D_setup2.restype = None
    D_setup2.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 142
if hasattr(_libs['grass_display.7.0.svn'], 'D_symbol'):
    D_symbol = _libs['grass_display.7.0.svn'].D_symbol
    D_symbol.restype = None
    D_symbol.argtypes = [POINTER(SYMBOL), c_double, c_double, POINTER(RGBA_Color), POINTER(RGBA_Color)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 144
if hasattr(_libs['grass_display.7.0.svn'], 'D_symbol2'):
    D_symbol2 = _libs['grass_display.7.0.svn'].D_symbol2
    D_symbol2.restype = None
    D_symbol2.argtypes = [POINTER(SYMBOL), c_double, c_double, POINTER(RGBA_Color), POINTER(RGBA_Color)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 148
if hasattr(_libs['grass_display.7.0.svn'], 'D_translate_color'):
    D_translate_color = _libs['grass_display.7.0.svn'].D_translate_color
    D_translate_color.restype = c_int
    D_translate_color.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 149
if hasattr(_libs['grass_display.7.0.svn'], 'D_parse_color'):
    D_parse_color = _libs['grass_display.7.0.svn'].D_parse_color
    D_parse_color.restype = c_int
    D_parse_color.argtypes = [String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 150
if hasattr(_libs['grass_display.7.0.svn'], 'D_use_color'):
    D_use_color = _libs['grass_display.7.0.svn'].D_use_color
    D_use_color.restype = c_int
    D_use_color.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 151
if hasattr(_libs['grass_display.7.0.svn'], 'D_color_number_to_RGB'):
    D_color_number_to_RGB = _libs['grass_display.7.0.svn'].D_color_number_to_RGB
    D_color_number_to_RGB.restype = c_int
    D_color_number_to_RGB.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 152
if hasattr(_libs['grass_display.7.0.svn'], 'D_RGB_color'):
    D_RGB_color = _libs['grass_display.7.0.svn'].D_RGB_color
    D_RGB_color.restype = None
    D_RGB_color.argtypes = [c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 155
if hasattr(_libs['grass_display.7.0.svn'], 'D_erase'):
    D_erase = _libs['grass_display.7.0.svn'].D_erase
    D_erase.restype = None
    D_erase.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 159
if hasattr(_libs['grass_display.7.0.svn'], 'D_open_driver'):
    D_open_driver = _libs['grass_display.7.0.svn'].D_open_driver
    D_open_driver.restype = c_int
    D_open_driver.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 160
if hasattr(_libs['grass_display.7.0.svn'], 'D_close_driver'):
    D_close_driver = _libs['grass_display.7.0.svn'].D_close_driver
    D_close_driver.restype = None
    D_close_driver.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 161
if hasattr(_libs['grass_display.7.0.svn'], 'D_save_command'):
    D_save_command = _libs['grass_display.7.0.svn'].D_save_command
    D_save_command.restype = c_int
    D_save_command.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 163
if hasattr(_libs['grass_display.7.0.svn'], 'D_get_window'):
    D_get_window = _libs['grass_display.7.0.svn'].D_get_window
    D_get_window.restype = None
    D_get_window.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 165
if hasattr(_libs['grass_display.7.0.svn'], 'D__erase'):
    D__erase = _libs['grass_display.7.0.svn'].D__erase
    D__erase.restype = None
    D__erase.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 167
if hasattr(_libs['grass_display.7.0.svn'], 'D_text_size'):
    D_text_size = _libs['grass_display.7.0.svn'].D_text_size
    D_text_size.restype = None
    D_text_size.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 168
if hasattr(_libs['grass_display.7.0.svn'], 'D_text_rotation'):
    D_text_rotation = _libs['grass_display.7.0.svn'].D_text_rotation
    D_text_rotation.restype = None
    D_text_rotation.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 169
if hasattr(_libs['grass_display.7.0.svn'], 'D_text'):
    D_text = _libs['grass_display.7.0.svn'].D_text
    D_text.restype = None
    D_text.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 171
if hasattr(_libs['grass_display.7.0.svn'], 'D_font'):
    D_font = _libs['grass_display.7.0.svn'].D_font
    D_font.restype = None
    D_font.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 172
if hasattr(_libs['grass_display.7.0.svn'], 'D_encoding'):
    D_encoding = _libs['grass_display.7.0.svn'].D_encoding
    D_encoding.restype = None
    D_encoding.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 173
if hasattr(_libs['grass_display.7.0.svn'], 'D_font_list'):
    D_font_list = _libs['grass_display.7.0.svn'].D_font_list
    D_font_list.restype = None
    D_font_list.argtypes = [POINTER(POINTER(POINTER(c_char))), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/display.h: 174
if hasattr(_libs['grass_display.7.0.svn'], 'D_font_info'):
    D_font_info = _libs['grass_display.7.0.svn'].D_font_info
    D_font_info.restype = None
    D_font_info.argtypes = [POINTER(POINTER(POINTER(c_char))), POINTER(c_int)]

# No inserted files

