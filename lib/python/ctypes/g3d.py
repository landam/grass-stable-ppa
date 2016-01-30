'''Wrapper for G3d.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_g3d.7.0.svn /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h -o g3d.py

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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 271
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 325
class struct_Key_Value(Structure):
    pass

struct_Key_Value.__slots__ = [
    'nitems',
    'nalloc',
    'key',
    'value',
]
struct_Key_Value._fields_ = [
    ('nitems', c_int),
    ('nalloc', c_int),
    ('key', POINTER(POINTER(c_char))),
    ('value', POINTER(POINTER(c_char))),
]

CELL = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 400

DCELL = c_double # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 401

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 404
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 412
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 424
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 434
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 419
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 446
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 73
class struct_Quant_table(Structure):
    pass

struct_Quant_table.__slots__ = [
    'dLow',
    'dHigh',
    'cLow',
    'cHigh',
]
struct_Quant_table._fields_ = [
    ('dLow', DCELL),
    ('dHigh', DCELL),
    ('cLow', CELL),
    ('cHigh', CELL),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 106
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'vals',
    'rules',
    'nalloc',
    'active',
    'inf_dmin',
    'inf_dmax',
    'inf_min',
    'inf_max',
]
struct_anon_23._fields_ = [
    ('vals', POINTER(DCELL)),
    ('rules', POINTER(POINTER(struct_Quant_table))),
    ('nalloc', c_int),
    ('active', c_int),
    ('inf_dmin', DCELL),
    ('inf_dmax', DCELL),
    ('inf_min', CELL),
    ('inf_max', CELL),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 81
class struct_Quant(Structure):
    pass

struct_Quant.__slots__ = [
    'truncate_only',
    'round_only',
    'defaultDRuleSet',
    'defaultCRuleSet',
    'infiniteLeftSet',
    'infiniteRightSet',
    'cRangeSet',
    'maxNofRules',
    'nofRules',
    'defaultDMin',
    'defaultDMax',
    'defaultCMin',
    'defaultCMax',
    'infiniteDLeft',
    'infiniteDRight',
    'infiniteCLeft',
    'infiniteCRight',
    'dMin',
    'dMax',
    'cMin',
    'cMax',
    'table',
    'fp_lookup',
]
struct_Quant._fields_ = [
    ('truncate_only', c_int),
    ('round_only', c_int),
    ('defaultDRuleSet', c_int),
    ('defaultCRuleSet', c_int),
    ('infiniteLeftSet', c_int),
    ('infiniteRightSet', c_int),
    ('cRangeSet', c_int),
    ('maxNofRules', c_int),
    ('nofRules', c_int),
    ('defaultDMin', DCELL),
    ('defaultDMax', DCELL),
    ('defaultCMin', CELL),
    ('defaultCMax', CELL),
    ('infiniteDLeft', DCELL),
    ('infiniteDRight', DCELL),
    ('infiniteCLeft', CELL),
    ('infiniteCRight', CELL),
    ('dMin', DCELL),
    ('dMax', DCELL),
    ('cMin', CELL),
    ('cMax', CELL),
    ('table', POINTER(struct_Quant_table)),
    ('fp_lookup', struct_anon_23),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 124
class struct_Categories(Structure):
    pass

struct_Categories.__slots__ = [
    'ncats',
    'num',
    'title',
    'fmt',
    'm1',
    'a1',
    'm2',
    'a2',
    'q',
    'labels',
    'marks',
    'nalloc',
    'last_marked_rule',
]
struct_Categories._fields_ = [
    ('ncats', CELL),
    ('num', CELL),
    ('title', String),
    ('fmt', String),
    ('m1', c_float),
    ('a1', c_float),
    ('m2', c_float),
    ('a2', c_float),
    ('q', struct_Quant),
    ('labels', POINTER(POINTER(c_char))),
    ('marks', POINTER(c_int)),
    ('nalloc', c_int),
    ('last_marked_rule', c_int),
]

HIST_MAPID = 0 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 150

HIST_TITLE = (HIST_MAPID + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 150

HIST_MAPSET = (HIST_TITLE + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 150

HIST_CREATOR = (HIST_MAPSET + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 150

HIST_MAPTYPE = (HIST_CREATOR + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 150

HIST_DATSRC_1 = (HIST_MAPTYPE + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 150

HIST_DATSRC_2 = (HIST_DATSRC_1 + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 150

HIST_KEYWRD = (HIST_DATSRC_2 + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 150

HIST_NUM_FIELDS = (HIST_KEYWRD + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 150

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 164
class struct_History(Structure):
    pass

struct_History.__slots__ = [
    'fields',
    'nlines',
    'lines',
]
struct_History._fields_ = [
    ('fields', POINTER(c_char) * HIST_NUM_FIELDS),
    ('nlines', c_int),
    ('lines', POINTER(POINTER(c_char))),
]

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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 63
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

G3D_Region = struct_anon_25 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 63

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 73
class struct_G3D_Map(Structure):
    pass

resample_fn = CFUNCTYPE(UNCHECKED(None), POINTER(struct_G3D_Map), c_int, c_int, c_int, POINTER(None), c_int) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 69

struct_G3D_Map.__slots__ = [
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
struct_G3D_Map._fields_ = [
    ('fileName', String),
    ('tempName', String),
    ('mapset', String),
    ('operation', c_int),
    ('region', G3D_Region),
    ('window', G3D_Region),
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

G3D_Map = struct_G3D_Map # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 185

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 220
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

G3D_cache = struct_anon_26 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 220

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 234
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

G3d_cache_hash = struct_anon_27 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 234

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 239
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

d_Interval = struct__d_interval # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 244

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 249
class struct__d_mask(Structure):
    pass

struct__d_mask.__slots__ = [
    'list',
]
struct__d_mask._fields_ = [
    ('list', POINTER(d_Interval)),
]

d_Mask = struct__d_mask # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 249

write_fn = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), POINTER(None)) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 253

read_fn = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), POINTER(None)) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 254

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 259
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_reset'):
    G3d_cache_reset = _libs['grass_g3d.7.0.svn'].G3d_cache_reset
    G3d_cache_reset.restype = None
    G3d_cache_reset.argtypes = [POINTER(G3D_cache)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 260
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_dispose'):
    G3d_cache_dispose = _libs['grass_g3d.7.0.svn'].G3d_cache_dispose
    G3d_cache_dispose.restype = None
    G3d_cache_dispose.argtypes = [POINTER(G3D_cache)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 261
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_new'):
    G3d_cache_new = _libs['grass_g3d.7.0.svn'].G3d_cache_new
    G3d_cache_new.restype = POINTER(None)
    G3d_cache_new.argtypes = [c_int, c_int, c_int, POINTER(write_fn), POINTER(None), POINTER(read_fn), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 262
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_set_removeFun'):
    G3d_cache_set_removeFun = _libs['grass_g3d.7.0.svn'].G3d_cache_set_removeFun
    G3d_cache_set_removeFun.restype = None
    G3d_cache_set_removeFun.argtypes = [POINTER(G3D_cache), POINTER(write_fn), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 263
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_set_loadFun'):
    G3d_cache_set_loadFun = _libs['grass_g3d.7.0.svn'].G3d_cache_set_loadFun
    G3d_cache_set_loadFun.restype = None
    G3d_cache_set_loadFun.argtypes = [POINTER(G3D_cache), POINTER(read_fn), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 264
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_new_read'):
    G3d_cache_new_read = _libs['grass_g3d.7.0.svn'].G3d_cache_new_read
    G3d_cache_new_read.restype = POINTER(None)
    G3d_cache_new_read.argtypes = [c_int, c_int, c_int, POINTER(read_fn), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 265
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_lock'):
    G3d_cache_lock = _libs['grass_g3d.7.0.svn'].G3d_cache_lock
    G3d_cache_lock.restype = c_int
    G3d_cache_lock.argtypes = [POINTER(G3D_cache), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 266
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_lock_intern'):
    G3d_cache_lock_intern = _libs['grass_g3d.7.0.svn'].G3d_cache_lock_intern
    G3d_cache_lock_intern.restype = None
    G3d_cache_lock_intern.argtypes = [POINTER(G3D_cache), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 267
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_unlock'):
    G3d_cache_unlock = _libs['grass_g3d.7.0.svn'].G3d_cache_unlock
    G3d_cache_unlock.restype = c_int
    G3d_cache_unlock.argtypes = [POINTER(G3D_cache), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 268
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_unlock_all'):
    G3d_cache_unlock_all = _libs['grass_g3d.7.0.svn'].G3d_cache_unlock_all
    G3d_cache_unlock_all.restype = c_int
    G3d_cache_unlock_all.argtypes = [POINTER(G3D_cache)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 269
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_lock_all'):
    G3d_cache_lock_all = _libs['grass_g3d.7.0.svn'].G3d_cache_lock_all
    G3d_cache_lock_all.restype = c_int
    G3d_cache_lock_all.argtypes = [POINTER(G3D_cache)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 270
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_autolock_on'):
    G3d_cache_autolock_on = _libs['grass_g3d.7.0.svn'].G3d_cache_autolock_on
    G3d_cache_autolock_on.restype = None
    G3d_cache_autolock_on.argtypes = [POINTER(G3D_cache)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 271
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_autolock_off'):
    G3d_cache_autolock_off = _libs['grass_g3d.7.0.svn'].G3d_cache_autolock_off
    G3d_cache_autolock_off.restype = None
    G3d_cache_autolock_off.argtypes = [POINTER(G3D_cache)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 272
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_set_minUnlock'):
    G3d_cache_set_minUnlock = _libs['grass_g3d.7.0.svn'].G3d_cache_set_minUnlock
    G3d_cache_set_minUnlock.restype = None
    G3d_cache_set_minUnlock.argtypes = [POINTER(G3D_cache), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 273
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_remove_elt'):
    G3d_cache_remove_elt = _libs['grass_g3d.7.0.svn'].G3d_cache_remove_elt
    G3d_cache_remove_elt.restype = c_int
    G3d_cache_remove_elt.argtypes = [POINTER(G3D_cache), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 274
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_flush'):
    G3d_cache_flush = _libs['grass_g3d.7.0.svn'].G3d_cache_flush
    G3d_cache_flush.restype = c_int
    G3d_cache_flush.argtypes = [POINTER(G3D_cache), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 275
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_remove_all'):
    G3d_cache_remove_all = _libs['grass_g3d.7.0.svn'].G3d_cache_remove_all
    G3d_cache_remove_all.restype = c_int
    G3d_cache_remove_all.argtypes = [POINTER(G3D_cache)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 276
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_flush_all'):
    G3d_cache_flush_all = _libs['grass_g3d.7.0.svn'].G3d_cache_flush_all
    G3d_cache_flush_all.restype = c_int
    G3d_cache_flush_all.argtypes = [POINTER(G3D_cache)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 277
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_elt_ptr'):
    G3d_cache_elt_ptr = _libs['grass_g3d.7.0.svn'].G3d_cache_elt_ptr
    G3d_cache_elt_ptr.restype = POINTER(None)
    G3d_cache_elt_ptr.argtypes = [POINTER(G3D_cache), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 278
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_load'):
    G3d_cache_load = _libs['grass_g3d.7.0.svn'].G3d_cache_load
    G3d_cache_load.restype = c_int
    G3d_cache_load.argtypes = [POINTER(G3D_cache), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 279
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_get_elt'):
    G3d_cache_get_elt = _libs['grass_g3d.7.0.svn'].G3d_cache_get_elt
    G3d_cache_get_elt.restype = c_int
    G3d_cache_get_elt.argtypes = [POINTER(G3D_cache), c_int, POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 280
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_put_elt'):
    G3d_cache_put_elt = _libs['grass_g3d.7.0.svn'].G3d_cache_put_elt
    G3d_cache_put_elt.restype = c_int
    G3d_cache_put_elt.argtypes = [POINTER(G3D_cache), c_int, POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 283
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_hash_reset'):
    G3d_cache_hash_reset = _libs['grass_g3d.7.0.svn'].G3d_cache_hash_reset
    G3d_cache_hash_reset.restype = None
    G3d_cache_hash_reset.argtypes = [POINTER(G3d_cache_hash)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 284
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_hash_dispose'):
    G3d_cache_hash_dispose = _libs['grass_g3d.7.0.svn'].G3d_cache_hash_dispose
    G3d_cache_hash_dispose.restype = None
    G3d_cache_hash_dispose.argtypes = [POINTER(G3d_cache_hash)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 285
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_hash_new'):
    G3d_cache_hash_new = _libs['grass_g3d.7.0.svn'].G3d_cache_hash_new
    G3d_cache_hash_new.restype = POINTER(None)
    G3d_cache_hash_new.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 286
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_hash_remove_name'):
    G3d_cache_hash_remove_name = _libs['grass_g3d.7.0.svn'].G3d_cache_hash_remove_name
    G3d_cache_hash_remove_name.restype = None
    G3d_cache_hash_remove_name.argtypes = [POINTER(G3d_cache_hash), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 287
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_hash_load_name'):
    G3d_cache_hash_load_name = _libs['grass_g3d.7.0.svn'].G3d_cache_hash_load_name
    G3d_cache_hash_load_name.restype = None
    G3d_cache_hash_load_name.argtypes = [POINTER(G3d_cache_hash), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 288
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cache_hash_name2index'):
    G3d_cache_hash_name2index = _libs['grass_g3d.7.0.svn'].G3d_cache_hash_name2index
    G3d_cache_hash_name2index.restype = c_int
    G3d_cache_hash_name2index.argtypes = [POINTER(G3d_cache_hash), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 291
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_changePrecision'):
    G3d_changePrecision = _libs['grass_g3d.7.0.svn'].G3d_changePrecision
    G3d_changePrecision.restype = None
    G3d_changePrecision.argtypes = [POINTER(None), c_int, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 294
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_changeType'):
    G3d_changeType = _libs['grass_g3d.7.0.svn'].G3d_changeType
    G3d_changeType.restype = None
    G3d_changeType.argtypes = [POINTER(None), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 297
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_compareFiles'):
    G3d_compareFiles = _libs['grass_g3d.7.0.svn'].G3d_compareFiles
    G3d_compareFiles.restype = None
    G3d_compareFiles.argtypes = [String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 300
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_filename'):
    G3d_filename = _libs['grass_g3d.7.0.svn'].G3d_filename
    G3d_filename.restype = None
    G3d_filename.argtypes = [String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 303
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_find_grid3'):
    G_find_grid3 = _libs['grass_g3d.7.0.svn'].G_find_grid3
    G_find_grid3.restype = ReturnString
    G_find_grid3.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 306
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_fpcompress_printBinary'):
    G_fpcompress_printBinary = _libs['grass_g3d.7.0.svn'].G_fpcompress_printBinary
    G_fpcompress_printBinary.restype = None
    G_fpcompress_printBinary.argtypes = [String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 307
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_fpcompress_dissectXdrDouble'):
    G_fpcompress_dissectXdrDouble = _libs['grass_g3d.7.0.svn'].G_fpcompress_dissectXdrDouble
    G_fpcompress_dissectXdrDouble.restype = None
    G_fpcompress_dissectXdrDouble.argtypes = [POINTER(c_ubyte)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 308
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_fpcompress_writeXdrNums'):
    G_fpcompress_writeXdrNums = _libs['grass_g3d.7.0.svn'].G_fpcompress_writeXdrNums
    G_fpcompress_writeXdrNums.restype = c_int
    G_fpcompress_writeXdrNums.argtypes = [c_int, String, c_int, c_int, String, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 309
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_fpcompress_writeXdrFloats'):
    G_fpcompress_writeXdrFloats = _libs['grass_g3d.7.0.svn'].G_fpcompress_writeXdrFloats
    G_fpcompress_writeXdrFloats.restype = c_int
    G_fpcompress_writeXdrFloats.argtypes = [c_int, String, c_int, c_int, String, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 310
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_fpcompress_writeXdrDouble'):
    G_fpcompress_writeXdrDouble = _libs['grass_g3d.7.0.svn'].G_fpcompress_writeXdrDouble
    G_fpcompress_writeXdrDouble.restype = c_int
    G_fpcompress_writeXdrDouble.argtypes = [c_int, String, c_int, c_int, String, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 311
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_fpcompress_readXdrNums'):
    G_fpcompress_readXdrNums = _libs['grass_g3d.7.0.svn'].G_fpcompress_readXdrNums
    G_fpcompress_readXdrNums.restype = c_int
    G_fpcompress_readXdrNums.argtypes = [c_int, String, c_int, c_int, c_int, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 312
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_fpcompress_readXdrFloats'):
    G_fpcompress_readXdrFloats = _libs['grass_g3d.7.0.svn'].G_fpcompress_readXdrFloats
    G_fpcompress_readXdrFloats.restype = c_int
    G_fpcompress_readXdrFloats.argtypes = [c_int, String, c_int, c_int, c_int, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 313
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_fpcompress_readXdrDoubles'):
    G_fpcompress_readXdrDoubles = _libs['grass_g3d.7.0.svn'].G_fpcompress_readXdrDoubles
    G_fpcompress_readXdrDoubles.restype = c_int
    G_fpcompress_readXdrDoubles.argtypes = [c_int, String, c_int, c_int, c_int, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 316
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_malloc'):
    G3d_malloc = _libs['grass_g3d.7.0.svn'].G3d_malloc
    G3d_malloc.restype = POINTER(None)
    G3d_malloc.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 317
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_realloc'):
    G3d_realloc = _libs['grass_g3d.7.0.svn'].G3d_realloc
    G3d_realloc.restype = POINTER(None)
    G3d_realloc.argtypes = [POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 318
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_free'):
    G3d_free = _libs['grass_g3d.7.0.svn'].G3d_free
    G3d_free.restype = None
    G3d_free.argtypes = [POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 321
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_initCache'):
    G3d_initCache = _libs['grass_g3d.7.0.svn'].G3d_initCache
    G3d_initCache.restype = c_int
    G3d_initCache.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 322
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_disposeCache'):
    G3d_disposeCache = _libs['grass_g3d.7.0.svn'].G3d_disposeCache
    G3d_disposeCache.restype = c_int
    G3d_disposeCache.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 323
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_flushAllTiles'):
    G3d_flushAllTiles = _libs['grass_g3d.7.0.svn'].G3d_flushAllTiles
    G3d_flushAllTiles.restype = c_int
    G3d_flushAllTiles.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 326
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_writeCats'):
    G3d_writeCats = _libs['grass_g3d.7.0.svn'].G3d_writeCats
    G3d_writeCats.restype = c_int
    G3d_writeCats.argtypes = [String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 327
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readCats'):
    G3d_readCats = _libs['grass_g3d.7.0.svn'].G3d_readCats
    G3d_readCats.restype = c_int
    G3d_readCats.argtypes = [String, String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 330
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_closeCell'):
    G3d_closeCell = _libs['grass_g3d.7.0.svn'].G3d_closeCell
    G3d_closeCell.restype = c_int
    G3d_closeCell.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 333
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_removeColor'):
    G3d_removeColor = _libs['grass_g3d.7.0.svn'].G3d_removeColor
    G3d_removeColor.restype = c_int
    G3d_removeColor.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 334
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readColors'):
    G3d_readColors = _libs['grass_g3d.7.0.svn'].G3d_readColors
    G3d_readColors.restype = c_int
    G3d_readColors.argtypes = [String, String, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 335
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_writeColors'):
    G3d_writeColors = _libs['grass_g3d.7.0.svn'].G3d_writeColors
    G3d_writeColors.restype = c_int
    G3d_writeColors.argtypes = [String, String, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 338
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setCompressionMode'):
    G3d_setCompressionMode = _libs['grass_g3d.7.0.svn'].G3d_setCompressionMode
    G3d_setCompressionMode.restype = None
    G3d_setCompressionMode.argtypes = [c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 339
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getCompressionMode'):
    G3d_getCompressionMode = _libs['grass_g3d.7.0.svn'].G3d_getCompressionMode
    G3d_getCompressionMode.restype = None
    G3d_getCompressionMode.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 340
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setCacheSize'):
    G3d_setCacheSize = _libs['grass_g3d.7.0.svn'].G3d_setCacheSize
    G3d_setCacheSize.restype = None
    G3d_setCacheSize.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 341
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getCacheSize'):
    G3d_getCacheSize = _libs['grass_g3d.7.0.svn'].G3d_getCacheSize
    G3d_getCacheSize.restype = c_int
    G3d_getCacheSize.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 342
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setCacheLimit'):
    G3d_setCacheLimit = _libs['grass_g3d.7.0.svn'].G3d_setCacheLimit
    G3d_setCacheLimit.restype = None
    G3d_setCacheLimit.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 343
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getCacheLimit'):
    G3d_getCacheLimit = _libs['grass_g3d.7.0.svn'].G3d_getCacheLimit
    G3d_getCacheLimit.restype = c_int
    G3d_getCacheLimit.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 344
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setFileType'):
    G3d_setFileType = _libs['grass_g3d.7.0.svn'].G3d_setFileType
    G3d_setFileType.restype = None
    G3d_setFileType.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 345
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getFileType'):
    G3d_getFileType = _libs['grass_g3d.7.0.svn'].G3d_getFileType
    G3d_getFileType.restype = c_int
    G3d_getFileType.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 346
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setTileDimension'):
    G3d_setTileDimension = _libs['grass_g3d.7.0.svn'].G3d_setTileDimension
    G3d_setTileDimension.restype = None
    G3d_setTileDimension.argtypes = [c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 347
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getTileDimension'):
    G3d_getTileDimension = _libs['grass_g3d.7.0.svn'].G3d_getTileDimension
    G3d_getTileDimension.restype = None
    G3d_getTileDimension.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 348
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setErrorFun'):
    G3d_setErrorFun = _libs['grass_g3d.7.0.svn'].G3d_setErrorFun
    G3d_setErrorFun.restype = None
    G3d_setErrorFun.argtypes = [CFUNCTYPE(UNCHECKED(None), String)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 349
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setUnit'):
    G3d_setUnit = _libs['grass_g3d.7.0.svn'].G3d_setUnit
    G3d_setUnit.restype = None
    G3d_setUnit.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 350
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_initDefaults'):
    G3d_initDefaults = _libs['grass_g3d.7.0.svn'].G3d_initDefaults
    G3d_initDefaults.restype = None
    G3d_initDefaults.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 353
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_writeDoubles'):
    G3d_writeDoubles = _libs['grass_g3d.7.0.svn'].G3d_writeDoubles
    G3d_writeDoubles.restype = c_int
    G3d_writeDoubles.argtypes = [c_int, c_int, POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 354
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readDoubles'):
    G3d_readDoubles = _libs['grass_g3d.7.0.svn'].G3d_readDoubles
    G3d_readDoubles.restype = c_int
    G3d_readDoubles.argtypes = [c_int, c_int, POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 357
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_skipError'):
    G3d_skipError = _libs['grass_g3d.7.0.svn'].G3d_skipError
    G3d_skipError.restype = None
    G3d_skipError.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 358
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_printError'):
    G3d_printError = _libs['grass_g3d.7.0.svn'].G3d_printError
    G3d_printError.restype = None
    G3d_printError.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 359
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_fatalError'):
    _func = _libs['grass_g3d.7.0.svn'].G3d_fatalError
    _restype = None
    _argtypes = [String]
    G3d_fatalError = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 361
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_fatalError_noargs'):
    G3d_fatalError_noargs = _libs['grass_g3d.7.0.svn'].G3d_fatalError_noargs
    G3d_fatalError_noargs.restype = None
    G3d_fatalError_noargs.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 362
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_error'):
    _func = _libs['grass_g3d.7.0.svn'].G3d_error
    _restype = None
    _argtypes = [String]
    G3d_error = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 365
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_isXdrNullNum'):
    G3d_isXdrNullNum = _libs['grass_g3d.7.0.svn'].G3d_isXdrNullNum
    G3d_isXdrNullNum.restype = c_int
    G3d_isXdrNullNum.argtypes = [POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 366
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_isXdrNullFloat'):
    G3d_isXdrNullFloat = _libs['grass_g3d.7.0.svn'].G3d_isXdrNullFloat
    G3d_isXdrNullFloat.restype = c_int
    G3d_isXdrNullFloat.argtypes = [POINTER(c_float)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 367
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_isXdrNullDouble'):
    G3d_isXdrNullDouble = _libs['grass_g3d.7.0.svn'].G3d_isXdrNullDouble
    G3d_isXdrNullDouble.restype = c_int
    G3d_isXdrNullDouble.argtypes = [POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 368
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setXdrNullNum'):
    G3d_setXdrNullNum = _libs['grass_g3d.7.0.svn'].G3d_setXdrNullNum
    G3d_setXdrNullNum.restype = None
    G3d_setXdrNullNum.argtypes = [POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 369
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setXdrNullDouble'):
    G3d_setXdrNullDouble = _libs['grass_g3d.7.0.svn'].G3d_setXdrNullDouble
    G3d_setXdrNullDouble.restype = None
    G3d_setXdrNullDouble.argtypes = [POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 370
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setXdrNullFloat'):
    G3d_setXdrNullFloat = _libs['grass_g3d.7.0.svn'].G3d_setXdrNullFloat
    G3d_setXdrNullFloat.restype = None
    G3d_setXdrNullFloat.argtypes = [POINTER(c_float)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 371
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_initFpXdr'):
    G3d_initFpXdr = _libs['grass_g3d.7.0.svn'].G3d_initFpXdr
    G3d_initFpXdr.restype = c_int
    G3d_initFpXdr.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 372
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_initCopyToXdr'):
    G3d_initCopyToXdr = _libs['grass_g3d.7.0.svn'].G3d_initCopyToXdr
    G3d_initCopyToXdr.restype = c_int
    G3d_initCopyToXdr.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 373
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_copyToXdr'):
    G3d_copyToXdr = _libs['grass_g3d.7.0.svn'].G3d_copyToXdr
    G3d_copyToXdr.restype = c_int
    G3d_copyToXdr.argtypes = [POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 374
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_initCopyFromXdr'):
    G3d_initCopyFromXdr = _libs['grass_g3d.7.0.svn'].G3d_initCopyFromXdr
    G3d_initCopyFromXdr.restype = c_int
    G3d_initCopyFromXdr.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 375
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_copyFromXdr'):
    G3d_copyFromXdr = _libs['grass_g3d.7.0.svn'].G3d_copyFromXdr
    G3d_copyFromXdr.restype = c_int
    G3d_copyFromXdr.argtypes = [c_int, POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 378
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_writeHistory'):
    G3d_writeHistory = _libs['grass_g3d.7.0.svn'].G3d_writeHistory
    G3d_writeHistory.restype = c_int
    G3d_writeHistory.argtypes = [String, POINTER(struct_History)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 379
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readHistory'):
    G3d_readHistory = _libs['grass_g3d.7.0.svn'].G3d_readHistory
    G3d_readHistory.restype = c_int
    G3d_readHistory.argtypes = [String, String, POINTER(struct_History)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 382
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_writeInts'):
    G3d_writeInts = _libs['grass_g3d.7.0.svn'].G3d_writeInts
    G3d_writeInts.restype = c_int
    G3d_writeInts.argtypes = [c_int, c_int, POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 383
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readInts'):
    G3d_readInts = _libs['grass_g3d.7.0.svn'].G3d_readInts
    G3d_readInts.restype = c_int
    G3d_readInts.argtypes = [c_int, c_int, POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 386
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_keyGetInt'):
    G3d_keyGetInt = _libs['grass_g3d.7.0.svn'].G3d_keyGetInt
    G3d_keyGetInt.restype = c_int
    G3d_keyGetInt.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 387
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_keyGetDouble'):
    G3d_keyGetDouble = _libs['grass_g3d.7.0.svn'].G3d_keyGetDouble
    G3d_keyGetDouble.restype = c_int
    G3d_keyGetDouble.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 388
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_keyGetString'):
    G3d_keyGetString = _libs['grass_g3d.7.0.svn'].G3d_keyGetString
    G3d_keyGetString.restype = c_int
    G3d_keyGetString.argtypes = [POINTER(struct_Key_Value), String, POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 389
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_keyGetValue'):
    G3d_keyGetValue = _libs['grass_g3d.7.0.svn'].G3d_keyGetValue
    G3d_keyGetValue.restype = c_int
    G3d_keyGetValue.argtypes = [POINTER(struct_Key_Value), String, String, String, c_int, c_int, POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 391
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_keySetInt'):
    G3d_keySetInt = _libs['grass_g3d.7.0.svn'].G3d_keySetInt
    G3d_keySetInt.restype = c_int
    G3d_keySetInt.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 392
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_keySetDouble'):
    G3d_keySetDouble = _libs['grass_g3d.7.0.svn'].G3d_keySetDouble
    G3d_keySetDouble.restype = c_int
    G3d_keySetDouble.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 393
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_keySetString'):
    G3d_keySetString = _libs['grass_g3d.7.0.svn'].G3d_keySetString
    G3d_keySetString.restype = c_int
    G3d_keySetString.argtypes = [POINTER(struct_Key_Value), String, POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 394
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_keySetValue'):
    G3d_keySetValue = _libs['grass_g3d.7.0.svn'].G3d_keySetValue
    G3d_keySetValue.restype = c_int
    G3d_keySetValue.argtypes = [POINTER(struct_Key_Value), String, String, String, c_int, c_int, POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 397
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_longEncode'):
    G3d_longEncode = _libs['grass_g3d.7.0.svn'].G3d_longEncode
    G3d_longEncode.restype = c_int
    G3d_longEncode.argtypes = [POINTER(c_long), POINTER(c_ubyte), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 398
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_longDecode'):
    G3d_longDecode = _libs['grass_g3d.7.0.svn'].G3d_longDecode
    G3d_longDecode.restype = None
    G3d_longDecode.argtypes = [POINTER(c_ubyte), POINTER(c_long), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 401
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_makeMapsetMapDirectory'):
    G3d_makeMapsetMapDirectory = _libs['grass_g3d.7.0.svn'].G3d_makeMapsetMapDirectory
    G3d_makeMapsetMapDirectory.restype = None
    G3d_makeMapsetMapDirectory.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 404
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskClose'):
    G3d_maskClose = _libs['grass_g3d.7.0.svn'].G3d_maskClose
    G3d_maskClose.restype = c_int
    G3d_maskClose.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 405
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskFileExists'):
    G3d_maskFileExists = _libs['grass_g3d.7.0.svn'].G3d_maskFileExists
    G3d_maskFileExists.restype = c_int
    G3d_maskFileExists.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 406
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskOpenOld'):
    G3d_maskOpenOld = _libs['grass_g3d.7.0.svn'].G3d_maskOpenOld
    G3d_maskOpenOld.restype = c_int
    G3d_maskOpenOld.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 407
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskReopen'):
    G3d_maskReopen = _libs['grass_g3d.7.0.svn'].G3d_maskReopen
    G3d_maskReopen.restype = c_int
    G3d_maskReopen.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 408
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_isMasked'):
    G3d_isMasked = _libs['grass_g3d.7.0.svn'].G3d_isMasked
    G3d_isMasked.restype = c_int
    G3d_isMasked.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 409
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskNum'):
    G3d_maskNum = _libs['grass_g3d.7.0.svn'].G3d_maskNum
    G3d_maskNum.restype = None
    G3d_maskNum.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 410
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskFloat'):
    G3d_maskFloat = _libs['grass_g3d.7.0.svn'].G3d_maskFloat
    G3d_maskFloat.restype = None
    G3d_maskFloat.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, POINTER(c_float)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 411
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskDouble'):
    G3d_maskDouble = _libs['grass_g3d.7.0.svn'].G3d_maskDouble
    G3d_maskDouble.restype = None
    G3d_maskDouble.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 412
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskTile'):
    G3d_maskTile = _libs['grass_g3d.7.0.svn'].G3d_maskTile
    G3d_maskTile.restype = None
    G3d_maskTile.argtypes = [POINTER(G3D_Map), c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 413
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskOn'):
    G3d_maskOn = _libs['grass_g3d.7.0.svn'].G3d_maskOn
    G3d_maskOn.restype = None
    G3d_maskOn.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 414
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskOff'):
    G3d_maskOff = _libs['grass_g3d.7.0.svn'].G3d_maskOff
    G3d_maskOff.restype = None
    G3d_maskOff.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 415
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskIsOn'):
    G3d_maskIsOn = _libs['grass_g3d.7.0.svn'].G3d_maskIsOn
    G3d_maskIsOn.restype = c_int
    G3d_maskIsOn.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 416
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskIsOff'):
    G3d_maskIsOff = _libs['grass_g3d.7.0.svn'].G3d_maskIsOff
    G3d_maskIsOff.restype = c_int
    G3d_maskIsOff.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 417
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskFile'):
    G3d_maskFile = _libs['grass_g3d.7.0.svn'].G3d_maskFile
    G3d_maskFile.restype = ReturnString
    G3d_maskFile.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 418
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_maskMapExists'):
    G3d_maskMapExists = _libs['grass_g3d.7.0.svn'].G3d_maskMapExists
    G3d_maskMapExists.restype = c_int
    G3d_maskMapExists.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 421
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_mask_d_select'):
    G3d_mask_d_select = _libs['grass_g3d.7.0.svn'].G3d_mask_d_select
    G3d_mask_d_select.restype = c_int
    G3d_mask_d_select.argtypes = [POINTER(DCELL), POINTER(d_Mask)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 422
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_mask_match_d_interval'):
    G3d_mask_match_d_interval = _libs['grass_g3d.7.0.svn'].G3d_mask_match_d_interval
    G3d_mask_match_d_interval.restype = DCELL
    G3d_mask_match_d_interval.argtypes = [DCELL, POINTER(d_Interval)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 423
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_parse_vallist'):
    G3d_parse_vallist = _libs['grass_g3d.7.0.svn'].G3d_parse_vallist
    G3d_parse_vallist.restype = None
    G3d_parse_vallist.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(d_Mask))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 426
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_g3dType2cellType'):
    G3d_g3dType2cellType = _libs['grass_g3d.7.0.svn'].G3d_g3dType2cellType
    G3d_g3dType2cellType.restype = c_int
    G3d_g3dType2cellType.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 427
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_copyFloat2Double'):
    G3d_copyFloat2Double = _libs['grass_g3d.7.0.svn'].G3d_copyFloat2Double
    G3d_copyFloat2Double.restype = None
    G3d_copyFloat2Double.argtypes = [POINTER(c_float), c_int, POINTER(c_double), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 428
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_copyDouble2Float'):
    G3d_copyDouble2Float = _libs['grass_g3d.7.0.svn'].G3d_copyDouble2Float
    G3d_copyDouble2Float.restype = None
    G3d_copyDouble2Float.argtypes = [POINTER(c_double), c_int, POINTER(c_float), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 429
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_copyValues'):
    G3d_copyValues = _libs['grass_g3d.7.0.svn'].G3d_copyValues
    G3d_copyValues.restype = None
    G3d_copyValues.argtypes = [POINTER(None), c_int, c_int, POINTER(None), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 430
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_length'):
    G3d_length = _libs['grass_g3d.7.0.svn'].G3d_length
    G3d_length.restype = c_int
    G3d_length.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 431
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_externLength'):
    G3d_externLength = _libs['grass_g3d.7.0.svn'].G3d_externLength
    G3d_externLength.restype = c_int
    G3d_externLength.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 434
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_isNullValueNum'):
    G3d_isNullValueNum = _libs['grass_g3d.7.0.svn'].G3d_isNullValueNum
    G3d_isNullValueNum.restype = c_int
    G3d_isNullValueNum.argtypes = [POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 435
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setNullValue'):
    G3d_setNullValue = _libs['grass_g3d.7.0.svn'].G3d_setNullValue
    G3d_setNullValue.restype = None
    G3d_setNullValue.argtypes = [POINTER(None), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 438
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_openNewParam'):
    G3d_openNewParam = _libs['grass_g3d.7.0.svn'].G3d_openNewParam
    G3d_openNewParam.restype = POINTER(None)
    G3d_openNewParam.argtypes = [String, c_int, c_int, POINTER(G3D_Region), c_int, c_int, c_int, c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 440
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_openCellOldNoHeader'):
    G3d_openCellOldNoHeader = _libs['grass_g3d.7.0.svn'].G3d_openCellOldNoHeader
    G3d_openCellOldNoHeader.restype = POINTER(None)
    G3d_openCellOldNoHeader.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 441
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_openCellOld'):
    G3d_openCellOld = _libs['grass_g3d.7.0.svn'].G3d_openCellOld
    G3d_openCellOld.restype = POINTER(None)
    G3d_openCellOld.argtypes = [String, String, POINTER(G3D_Region), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 442
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_openCellNew'):
    G3d_openCellNew = _libs['grass_g3d.7.0.svn'].G3d_openCellNew
    G3d_openCellNew.restype = POINTER(None)
    G3d_openCellNew.argtypes = [String, c_int, c_int, POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 443
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_openNewOptTileSize'):
    G3d_openNewOptTileSize = _libs['grass_g3d.7.0.svn'].G3d_openNewOptTileSize
    G3d_openNewOptTileSize.restype = POINTER(None)
    G3d_openNewOptTileSize.argtypes = [String, c_int, POINTER(G3D_Region), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 446
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setStandard3dInputParams'):
    G3d_setStandard3dInputParams = _libs['grass_g3d.7.0.svn'].G3d_setStandard3dInputParams
    G3d_setStandard3dInputParams.restype = None
    G3d_setStandard3dInputParams.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 447
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getStandard3dParams'):
    G3d_getStandard3dParams = _libs['grass_g3d.7.0.svn'].G3d_getStandard3dParams
    G3d_getStandard3dParams.restype = c_int
    G3d_getStandard3dParams.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 449
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setWindowParams'):
    G3d_setWindowParams = _libs['grass_g3d.7.0.svn'].G3d_setWindowParams
    G3d_setWindowParams.restype = None
    G3d_setWindowParams.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 450
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getWindowParams'):
    G3d_getWindowParams = _libs['grass_g3d.7.0.svn'].G3d_getWindowParams
    G3d_getWindowParams.restype = ReturnString
    G3d_getWindowParams.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 453
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_range_updateFromTile'):
    G3d_range_updateFromTile = _libs['grass_g3d.7.0.svn'].G3d_range_updateFromTile
    G3d_range_updateFromTile.restype = None
    G3d_range_updateFromTile.argtypes = [POINTER(G3D_Map), POINTER(None), c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 455
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readRange'):
    G3d_readRange = _libs['grass_g3d.7.0.svn'].G3d_readRange
    G3d_readRange.restype = c_int
    G3d_readRange.argtypes = [String, String, POINTER(struct_FPRange)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 456
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_range_load'):
    G3d_range_load = _libs['grass_g3d.7.0.svn'].G3d_range_load
    G3d_range_load.restype = c_int
    G3d_range_load.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 457
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_range_min_max'):
    G3d_range_min_max = _libs['grass_g3d.7.0.svn'].G3d_range_min_max
    G3d_range_min_max.restype = None
    G3d_range_min_max.argtypes = [POINTER(G3D_Map), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 458
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_range_write'):
    G3d_range_write = _libs['grass_g3d.7.0.svn'].G3d_range_write
    G3d_range_write.restype = c_int
    G3d_range_write.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 459
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_range_init'):
    G3d_range_init = _libs['grass_g3d.7.0.svn'].G3d_range_init
    G3d_range_init.restype = c_int
    G3d_range_init.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 462
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getRegionValue'):
    G3d_getRegionValue = _libs['grass_g3d.7.0.svn'].G3d_getRegionValue
    G3d_getRegionValue.restype = None
    G3d_getRegionValue.argtypes = [POINTER(G3D_Map), c_double, c_double, c_double, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 463
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_adjustRegion'):
    G3d_adjustRegion = _libs['grass_g3d.7.0.svn'].G3d_adjustRegion
    G3d_adjustRegion.restype = None
    G3d_adjustRegion.argtypes = [POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 464
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_regionCopy'):
    G3d_regionCopy = _libs['grass_g3d.7.0.svn'].G3d_regionCopy
    G3d_regionCopy.restype = None
    G3d_regionCopy.argtypes = [POINTER(G3D_Region), POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 465
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_incorporate2dRegion'):
    G3d_incorporate2dRegion = _libs['grass_g3d.7.0.svn'].G3d_incorporate2dRegion
    G3d_incorporate2dRegion.restype = None
    G3d_incorporate2dRegion.argtypes = [POINTER(struct_Cell_head), POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 466
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_regionFromToCellHead'):
    G3d_regionFromToCellHead = _libs['grass_g3d.7.0.svn'].G3d_regionFromToCellHead
    G3d_regionFromToCellHead.restype = None
    G3d_regionFromToCellHead.argtypes = [POINTER(struct_Cell_head), POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 467
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_adjustRegionRes'):
    G3d_adjustRegionRes = _libs['grass_g3d.7.0.svn'].G3d_adjustRegionRes
    G3d_adjustRegionRes.restype = None
    G3d_adjustRegionRes.argtypes = [POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 468
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_extract2dRegion'):
    G3d_extract2dRegion = _libs['grass_g3d.7.0.svn'].G3d_extract2dRegion
    G3d_extract2dRegion.restype = None
    G3d_extract2dRegion.argtypes = [POINTER(G3D_Region), POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 469
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_regionToCellHead'):
    G3d_regionToCellHead = _libs['grass_g3d.7.0.svn'].G3d_regionToCellHead
    G3d_regionToCellHead.restype = None
    G3d_regionToCellHead.argtypes = [POINTER(G3D_Region), POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 470
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readRegionMap'):
    G3d_readRegionMap = _libs['grass_g3d.7.0.svn'].G3d_readRegionMap
    G3d_readRegionMap.restype = c_int
    G3d_readRegionMap.argtypes = [String, String, POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 471
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_isValidLocation'):
    G3d_isValidLocation = _libs['grass_g3d.7.0.svn'].G3d_isValidLocation
    G3d_isValidLocation.restype = c_int
    G3d_isValidLocation.argtypes = [POINTER(G3D_Region), c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 472
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_location2coord'):
    G3d_location2coord = _libs['grass_g3d.7.0.svn'].G3d_location2coord
    G3d_location2coord.restype = None
    G3d_location2coord.argtypes = [POINTER(G3D_Region), c_double, c_double, c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 473
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_location2coord2'):
    G3d_location2coord2 = _libs['grass_g3d.7.0.svn'].G3d_location2coord2
    G3d_location2coord2.restype = None
    G3d_location2coord2.argtypes = [POINTER(G3D_Region), c_double, c_double, c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 474
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_coord2location'):
    G3d_coord2location = _libs['grass_g3d.7.0.svn'].G3d_coord2location
    G3d_coord2location.restype = None
    G3d_coord2location.argtypes = [POINTER(G3D_Region), c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 476
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_nearestNeighbor'):
    G3d_nearestNeighbor = _libs['grass_g3d.7.0.svn'].G3d_nearestNeighbor
    G3d_nearestNeighbor.restype = None
    G3d_nearestNeighbor.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 477
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setResamplingFun'):
    G3d_setResamplingFun = _libs['grass_g3d.7.0.svn'].G3d_setResamplingFun
    G3d_setResamplingFun.restype = None
    G3d_setResamplingFun.argtypes = [POINTER(G3D_Map), CFUNCTYPE(UNCHECKED(None), )]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 478
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getResamplingFun'):
    G3d_getResamplingFun = _libs['grass_g3d.7.0.svn'].G3d_getResamplingFun
    G3d_getResamplingFun.restype = None
    G3d_getResamplingFun.argtypes = [POINTER(G3D_Map), POINTER(CFUNCTYPE(UNCHECKED(None), ))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 479
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getNearestNeighborFunPtr'):
    G3d_getNearestNeighborFunPtr = _libs['grass_g3d.7.0.svn'].G3d_getNearestNeighborFunPtr
    G3d_getNearestNeighborFunPtr.restype = None
    G3d_getNearestNeighborFunPtr.argtypes = [POINTER(CFUNCTYPE(UNCHECKED(None), ))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 482
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getVolumeA'):
    G3d_getVolumeA = _libs['grass_g3d.7.0.svn'].G3d_getVolumeA
    G3d_getVolumeA.restype = None
    G3d_getVolumeA.argtypes = [POINTER(None), (((c_double * 3) * 2) * 2) * 2, c_int, c_int, c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 483
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getVolume'):
    G3d_getVolume = _libs['grass_g3d.7.0.svn'].G3d_getVolume
    G3d_getVolume.restype = None
    G3d_getVolume.argtypes = [POINTER(None), c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 486
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getAlignedVolume'):
    G3d_getAlignedVolume = _libs['grass_g3d.7.0.svn'].G3d_getAlignedVolume
    G3d_getAlignedVolume.restype = None
    G3d_getAlignedVolume.argtypes = [POINTER(None), c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 488
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_makeAlignedVolumeFile'):
    G3d_makeAlignedVolumeFile = _libs['grass_g3d.7.0.svn'].G3d_makeAlignedVolumeFile
    G3d_makeAlignedVolumeFile.restype = None
    G3d_makeAlignedVolumeFile.argtypes = [POINTER(None), String, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 491
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getValue'):
    G3d_getValue = _libs['grass_g3d.7.0.svn'].G3d_getValue
    G3d_getValue.restype = None
    G3d_getValue.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 492
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getFloat'):
    G3d_getFloat = _libs['grass_g3d.7.0.svn'].G3d_getFloat
    G3d_getFloat.restype = c_float
    G3d_getFloat.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 493
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getDouble'):
    G3d_getDouble = _libs['grass_g3d.7.0.svn'].G3d_getDouble
    G3d_getDouble.restype = c_double
    G3d_getDouble.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 494
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getWindowValue'):
    G3d_getWindowValue = _libs['grass_g3d.7.0.svn'].G3d_getWindowValue
    G3d_getWindowValue.restype = None
    G3d_getWindowValue.argtypes = [POINTER(G3D_Map), c_double, c_double, c_double, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 497
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_windowPtr'):
    G3d_windowPtr = _libs['grass_g3d.7.0.svn'].G3d_windowPtr
    G3d_windowPtr.restype = POINTER(G3D_Region)
    G3d_windowPtr.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 498
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setWindow'):
    G3d_setWindow = _libs['grass_g3d.7.0.svn'].G3d_setWindow
    G3d_setWindow.restype = None
    G3d_setWindow.argtypes = [POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 499
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setWindowMap'):
    G3d_setWindowMap = _libs['grass_g3d.7.0.svn'].G3d_setWindowMap
    G3d_setWindowMap.restype = None
    G3d_setWindowMap.argtypes = [POINTER(G3D_Map), POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 500
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getWindow'):
    G3d_getWindow = _libs['grass_g3d.7.0.svn'].G3d_getWindow
    G3d_getWindow.restype = None
    G3d_getWindow.argtypes = [POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 503
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_useWindowParams'):
    G3d_useWindowParams = _libs['grass_g3d.7.0.svn'].G3d_useWindowParams
    G3d_useWindowParams.restype = None
    G3d_useWindowParams.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 504
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readWindow'):
    G3d_readWindow = _libs['grass_g3d.7.0.svn'].G3d_readWindow
    G3d_readWindow.restype = c_int
    G3d_readWindow.argtypes = [POINTER(G3D_Region), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 508
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getBlockNocache'):
    G3d_getBlockNocache = _libs['grass_g3d.7.0.svn'].G3d_getBlockNocache
    G3d_getBlockNocache.restype = None
    G3d_getBlockNocache.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, c_int, c_int, c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 510
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getBlock'):
    G3d_getBlock = _libs['grass_g3d.7.0.svn'].G3d_getBlock
    G3d_getBlock.restype = None
    G3d_getBlock.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, c_int, c_int, c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 513
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readHeader'):
    G3d_readHeader = _libs['grass_g3d.7.0.svn'].G3d_readHeader
    G3d_readHeader.restype = c_int
    G3d_readHeader.argtypes = [POINTER(G3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 517
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_writeHeader'):
    G3d_writeHeader = _libs['grass_g3d.7.0.svn'].G3d_writeHeader
    G3d_writeHeader.restype = c_int
    G3d_writeHeader.argtypes = [POINTER(G3D_Map), c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_double, c_double, c_double, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 521
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_cacheSizeEncode'):
    G3d_cacheSizeEncode = _libs['grass_g3d.7.0.svn'].G3d_cacheSizeEncode
    G3d_cacheSizeEncode.restype = c_int
    G3d_cacheSizeEncode.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 522
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d__computeCacheSize'):
    G3d__computeCacheSize = _libs['grass_g3d.7.0.svn'].G3d__computeCacheSize
    G3d__computeCacheSize.restype = c_int
    G3d__computeCacheSize.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 523
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_fillHeader'):
    G3d_fillHeader = _libs['grass_g3d.7.0.svn'].G3d_fillHeader
    G3d_fillHeader.restype = c_int
    G3d_fillHeader.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_double, c_double, c_double, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 528
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getCoordsMap'):
    G3d_getCoordsMap = _libs['grass_g3d.7.0.svn'].G3d_getCoordsMap
    G3d_getCoordsMap.restype = None
    G3d_getCoordsMap.argtypes = [POINTER(G3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 529
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getCoordsMapWindow'):
    G3d_getCoordsMapWindow = _libs['grass_g3d.7.0.svn'].G3d_getCoordsMapWindow
    G3d_getCoordsMapWindow.restype = None
    G3d_getCoordsMapWindow.argtypes = [POINTER(G3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 530
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getNofTilesMap'):
    G3d_getNofTilesMap = _libs['grass_g3d.7.0.svn'].G3d_getNofTilesMap
    G3d_getNofTilesMap.restype = None
    G3d_getNofTilesMap.argtypes = [POINTER(G3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 531
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getRegionMap'):
    G3d_getRegionMap = _libs['grass_g3d.7.0.svn'].G3d_getRegionMap
    G3d_getRegionMap.restype = None
    G3d_getRegionMap.argtypes = [POINTER(G3D_Map), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 533
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getWindowMap'):
    G3d_getWindowMap = _libs['grass_g3d.7.0.svn'].G3d_getWindowMap
    G3d_getWindowMap.restype = None
    G3d_getWindowMap.argtypes = [POINTER(G3D_Map), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 535
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getTileDimensionsMap'):
    G3d_getTileDimensionsMap = _libs['grass_g3d.7.0.svn'].G3d_getTileDimensionsMap
    G3d_getTileDimensionsMap.restype = None
    G3d_getTileDimensionsMap.argtypes = [POINTER(G3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 536
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_tileTypeMap'):
    G3d_tileTypeMap = _libs['grass_g3d.7.0.svn'].G3d_tileTypeMap
    G3d_tileTypeMap.restype = c_int
    G3d_tileTypeMap.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 537
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_fileTypeMap'):
    G3d_fileTypeMap = _libs['grass_g3d.7.0.svn'].G3d_fileTypeMap
    G3d_fileTypeMap.restype = c_int
    G3d_fileTypeMap.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 538
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_tilePrecisionMap'):
    G3d_tilePrecisionMap = _libs['grass_g3d.7.0.svn'].G3d_tilePrecisionMap
    G3d_tilePrecisionMap.restype = c_int
    G3d_tilePrecisionMap.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 539
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_tileUseCacheMap'):
    G3d_tileUseCacheMap = _libs['grass_g3d.7.0.svn'].G3d_tileUseCacheMap
    G3d_tileUseCacheMap.restype = c_int
    G3d_tileUseCacheMap.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 540
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_printHeader'):
    G3d_printHeader = _libs['grass_g3d.7.0.svn'].G3d_printHeader
    G3d_printHeader.restype = None
    G3d_printHeader.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 541
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getRegionStructMap'):
    G3d_getRegionStructMap = _libs['grass_g3d.7.0.svn'].G3d_getRegionStructMap
    G3d_getRegionStructMap.restype = None
    G3d_getRegionStructMap.argtypes = [POINTER(G3D_Map), POINTER(G3D_Region)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 544
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_flushIndex'):
    G3d_flushIndex = _libs['grass_g3d.7.0.svn'].G3d_flushIndex
    G3d_flushIndex.restype = c_int
    G3d_flushIndex.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 545
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_initIndex'):
    G3d_initIndex = _libs['grass_g3d.7.0.svn'].G3d_initIndex
    G3d_initIndex.restype = c_int
    G3d_initIndex.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 548
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_retile'):
    G3d_retile = _libs['grass_g3d.7.0.svn'].G3d_retile
    G3d_retile.restype = None
    G3d_retile.argtypes = [POINTER(None), String, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 551
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_rle_count_only'):
    G_rle_count_only = _libs['grass_g3d.7.0.svn'].G_rle_count_only
    G_rle_count_only.restype = c_int
    G_rle_count_only.argtypes = [String, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 552
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_rle_encode'):
    G_rle_encode = _libs['grass_g3d.7.0.svn'].G_rle_encode
    G_rle_encode.restype = None
    G_rle_encode.argtypes = [String, String, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 553
if hasattr(_libs['grass_g3d.7.0.svn'], 'G_rle_decode'):
    G_rle_decode = _libs['grass_g3d.7.0.svn'].G_rle_decode
    G_rle_decode.restype = None
    G_rle_decode.argtypes = [String, String, c_int, c_int, POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 556
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_allocTilesType'):
    G3d_allocTilesType = _libs['grass_g3d.7.0.svn'].G3d_allocTilesType
    G3d_allocTilesType.restype = POINTER(None)
    G3d_allocTilesType.argtypes = [POINTER(G3D_Map), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 557
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_allocTiles'):
    G3d_allocTiles = _libs['grass_g3d.7.0.svn'].G3d_allocTiles
    G3d_allocTiles.restype = POINTER(None)
    G3d_allocTiles.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 558
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_freeTiles'):
    G3d_freeTiles = _libs['grass_g3d.7.0.svn'].G3d_freeTiles
    G3d_freeTiles.restype = None
    G3d_freeTiles.argtypes = [POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 561
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getTilePtr'):
    G3d_getTilePtr = _libs['grass_g3d.7.0.svn'].G3d_getTilePtr
    G3d_getTilePtr.restype = POINTER(None)
    G3d_getTilePtr.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 562
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_tileLoad'):
    G3d_tileLoad = _libs['grass_g3d.7.0.svn'].G3d_tileLoad
    G3d_tileLoad.restype = c_int
    G3d_tileLoad.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 563
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d__removeTile'):
    G3d__removeTile = _libs['grass_g3d.7.0.svn'].G3d__removeTile
    G3d__removeTile.restype = c_int
    G3d__removeTile.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 564
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getFloatRegion'):
    G3d_getFloatRegion = _libs['grass_g3d.7.0.svn'].G3d_getFloatRegion
    G3d_getFloatRegion.restype = c_float
    G3d_getFloatRegion.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 565
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getDoubleRegion'):
    G3d_getDoubleRegion = _libs['grass_g3d.7.0.svn'].G3d_getDoubleRegion
    G3d_getDoubleRegion.restype = c_double
    G3d_getDoubleRegion.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 566
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_getValueRegion'):
    G3d_getValueRegion = _libs['grass_g3d.7.0.svn'].G3d_getValueRegion
    G3d_getValueRegion.restype = None
    G3d_getValueRegion.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 569
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_computeOptimalTileDimension'):
    G3d_computeOptimalTileDimension = _libs['grass_g3d.7.0.svn'].G3d_computeOptimalTileDimension
    G3d_computeOptimalTileDimension.restype = None
    G3d_computeOptimalTileDimension.argtypes = [POINTER(G3D_Region), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 570
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_tileIndex2tile'):
    G3d_tileIndex2tile = _libs['grass_g3d.7.0.svn'].G3d_tileIndex2tile
    G3d_tileIndex2tile.restype = None
    G3d_tileIndex2tile.argtypes = [POINTER(G3D_Map), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 571
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_tile2tileIndex'):
    G3d_tile2tileIndex = _libs['grass_g3d.7.0.svn'].G3d_tile2tileIndex
    G3d_tile2tileIndex.restype = c_int
    G3d_tile2tileIndex.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 572
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_tileCoordOrigin'):
    G3d_tileCoordOrigin = _libs['grass_g3d.7.0.svn'].G3d_tileCoordOrigin
    G3d_tileCoordOrigin.restype = None
    G3d_tileCoordOrigin.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 573
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_tileIndexOrigin'):
    G3d_tileIndexOrigin = _libs['grass_g3d.7.0.svn'].G3d_tileIndexOrigin
    G3d_tileIndexOrigin.restype = None
    G3d_tileIndexOrigin.argtypes = [POINTER(G3D_Map), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 574
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_coord2tileCoord'):
    G3d_coord2tileCoord = _libs['grass_g3d.7.0.svn'].G3d_coord2tileCoord
    G3d_coord2tileCoord.restype = None
    G3d_coord2tileCoord.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 576
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_coord2tileIndex'):
    G3d_coord2tileIndex = _libs['grass_g3d.7.0.svn'].G3d_coord2tileIndex
    G3d_coord2tileIndex.restype = None
    G3d_coord2tileIndex.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 577
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_coordInRange'):
    G3d_coordInRange = _libs['grass_g3d.7.0.svn'].G3d_coordInRange
    G3d_coordInRange.restype = c_int
    G3d_coordInRange.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 578
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_tileIndexInRange'):
    G3d_tileIndexInRange = _libs['grass_g3d.7.0.svn'].G3d_tileIndexInRange
    G3d_tileIndexInRange.restype = c_int
    G3d_tileIndexInRange.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 579
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_tileInRange'):
    G3d_tileInRange = _libs['grass_g3d.7.0.svn'].G3d_tileInRange
    G3d_tileInRange.restype = c_int
    G3d_tileInRange.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 580
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_computeClippedTileDimensions'):
    G3d_computeClippedTileDimensions = _libs['grass_g3d.7.0.svn'].G3d_computeClippedTileDimensions
    G3d_computeClippedTileDimensions.restype = c_int
    G3d_computeClippedTileDimensions.argtypes = [POINTER(G3D_Map), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 584
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setNullTileType'):
    G3d_setNullTileType = _libs['grass_g3d.7.0.svn'].G3d_setNullTileType
    G3d_setNullTileType.restype = None
    G3d_setNullTileType.argtypes = [POINTER(G3D_Map), POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 585
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_setNullTile'):
    G3d_setNullTile = _libs['grass_g3d.7.0.svn'].G3d_setNullTile
    G3d_setNullTile.restype = None
    G3d_setNullTile.argtypes = [POINTER(G3D_Map), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 588
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readTile'):
    G3d_readTile = _libs['grass_g3d.7.0.svn'].G3d_readTile
    G3d_readTile.restype = c_int
    G3d_readTile.argtypes = [POINTER(G3D_Map), c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 589
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readTileFloat'):
    G3d_readTileFloat = _libs['grass_g3d.7.0.svn'].G3d_readTileFloat
    G3d_readTileFloat.restype = c_int
    G3d_readTileFloat.argtypes = [POINTER(G3D_Map), c_int, POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 590
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_readTileDouble'):
    G3d_readTileDouble = _libs['grass_g3d.7.0.svn'].G3d_readTileDouble
    G3d_readTileDouble.restype = c_int
    G3d_readTileDouble.argtypes = [POINTER(G3D_Map), c_int, POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 591
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_lockTile'):
    G3d_lockTile = _libs['grass_g3d.7.0.svn'].G3d_lockTile
    G3d_lockTile.restype = c_int
    G3d_lockTile.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 592
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_unlockTile'):
    G3d_unlockTile = _libs['grass_g3d.7.0.svn'].G3d_unlockTile
    G3d_unlockTile.restype = c_int
    G3d_unlockTile.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 593
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_unlockAll'):
    G3d_unlockAll = _libs['grass_g3d.7.0.svn'].G3d_unlockAll
    G3d_unlockAll.restype = c_int
    G3d_unlockAll.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 594
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_autolockOn'):
    G3d_autolockOn = _libs['grass_g3d.7.0.svn'].G3d_autolockOn
    G3d_autolockOn.restype = None
    G3d_autolockOn.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 595
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_autolockOff'):
    G3d_autolockOff = _libs['grass_g3d.7.0.svn'].G3d_autolockOff
    G3d_autolockOff.restype = None
    G3d_autolockOff.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 596
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_minUnlocked'):
    G3d_minUnlocked = _libs['grass_g3d.7.0.svn'].G3d_minUnlocked
    G3d_minUnlocked.restype = None
    G3d_minUnlocked.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 597
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_beginCycle'):
    G3d_beginCycle = _libs['grass_g3d.7.0.svn'].G3d_beginCycle
    G3d_beginCycle.restype = c_int
    G3d_beginCycle.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 598
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_endCycle'):
    G3d_endCycle = _libs['grass_g3d.7.0.svn'].G3d_endCycle
    G3d_endCycle.restype = c_int
    G3d_endCycle.argtypes = [POINTER(G3D_Map)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 601
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_writeTile'):
    G3d_writeTile = _libs['grass_g3d.7.0.svn'].G3d_writeTile
    G3d_writeTile.restype = c_int
    G3d_writeTile.argtypes = [POINTER(G3D_Map), c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 602
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_writeTileFloat'):
    G3d_writeTileFloat = _libs['grass_g3d.7.0.svn'].G3d_writeTileFloat
    G3d_writeTileFloat.restype = c_int
    G3d_writeTileFloat.argtypes = [POINTER(G3D_Map), c_int, POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 603
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_writeTileDouble'):
    G3d_writeTileDouble = _libs['grass_g3d.7.0.svn'].G3d_writeTileDouble
    G3d_writeTileDouble.restype = c_int
    G3d_writeTileDouble.argtypes = [POINTER(G3D_Map), c_int, POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 604
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_flushTile'):
    G3d_flushTile = _libs['grass_g3d.7.0.svn'].G3d_flushTile
    G3d_flushTile.restype = c_int
    G3d_flushTile.argtypes = [POINTER(G3D_Map), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 605
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_flushTileCube'):
    G3d_flushTileCube = _libs['grass_g3d.7.0.svn'].G3d_flushTileCube
    G3d_flushTileCube.restype = c_int
    G3d_flushTileCube.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 606
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_flushTilesInCube'):
    G3d_flushTilesInCube = _libs['grass_g3d.7.0.svn'].G3d_flushTilesInCube
    G3d_flushTilesInCube.restype = c_int
    G3d_flushTilesInCube.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 607
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_putFloat'):
    G3d_putFloat = _libs['grass_g3d.7.0.svn'].G3d_putFloat
    G3d_putFloat.restype = c_int
    G3d_putFloat.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, c_float]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 608
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_putDouble'):
    G3d_putDouble = _libs['grass_g3d.7.0.svn'].G3d_putDouble
    G3d_putDouble.restype = c_int
    G3d_putDouble.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 609
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_putValue'):
    G3d_putValue = _libs['grass_g3d.7.0.svn'].G3d_putValue
    G3d_putValue.restype = c_int
    G3d_putValue.argtypes = [POINTER(G3D_Map), c_int, c_int, c_int, POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 612
if hasattr(_libs['grass_g3d.7.0.svn'], 'G3d_writeAscii'):
    G3d_writeAscii = _libs['grass_g3d.7.0.svn'].G3d_writeAscii
    G3d_writeAscii.restype = None
    G3d_writeAscii.argtypes = [POINTER(None), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 7
try:
    G3D_TILE_SAME_AS_FILE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 8
try:
    G3D_NO_COMPRESSION = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 8
try:
    G3D_COMPRESSION = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 9
try:
    G3D_USE_LZW = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 9
try:
    G3D_NO_LZW = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 10
try:
    G3D_USE_RLE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 10
try:
    G3D_NO_RLE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 11
try:
    G3D_MAX_PRECISION = (-1)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 12
try:
    G3D_NO_CACHE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 12
try:
    G3D_USE_CACHE_DEFAULT = (-1)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 12
try:
    G3D_USE_CACHE_X = (-2)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 12
try:
    G3D_USE_CACHE_Y = (-3)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 12
try:
    G3D_USE_CACHE_Z = (-4)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 12
try:
    G3D_USE_CACHE_XY = (-5)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 12
try:
    G3D_USE_CACHE_XZ = (-6)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 12
try:
    G3D_USE_CACHE_YZ = (-7)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 12
try:
    G3D_USE_CACHE_XYZ = (-8)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 13
try:
    G3D_DEFAULT_WINDOW = NULL
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_DIRECTORY = 'grid3'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_CELL_ELEMENT = 'cell'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_CATS_ELEMENT = 'cats'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_RANGE_ELEMENT = 'range'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_HEADER_ELEMENT = 'cellhd'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_HISTORY_ELEMENT = 'hist'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_COLOR_ELEMENT = 'color'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_COLOR2_DIRECTORY = 'colr2'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_MASK_MAP = 'G3D_MASK'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_WINDOW_ELEMENT = 'WIND3'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_DEFAULT_WINDOW_ELEMENT = 'DEFAULT_WIND3'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_WINDOW_DATABASE = 'windows3d'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 14
try:
    G3D_PERMANENT_MAPSET = 'PERMANENT'
except:
    pass

G3D_Map = struct_G3D_Map # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 73

_d_interval = struct__d_interval # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 239

_d_mask = struct__d_mask # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/G3d.h: 249

# No inserted files

