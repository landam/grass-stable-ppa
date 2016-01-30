'''Wrapper for gis.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -lgrass_gis.7.0.svn /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h -o grass.py

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

_libs["grass_gis.7.0.svn"] = load_library("grass_gis.7.0.svn")

# 1 libraries
# End libraries

# No modules

__off_t = c_long # /usr/include/bits/types.h: 141

__off64_t = c_long # /usr/include/bits/types.h: 142

# /usr/include/libio.h: 271
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE # /usr/include/stdio.h: 49

_IO_lock_t = None # /usr/include/libio.h: 180

# /usr/include/libio.h: 186
class struct__IO_marker(Structure):
    pass

struct__IO_marker.__slots__ = [
    '_next',
    '_sbuf',
    '_pos',
]
struct__IO_marker._fields_ = [
    ('_next', POINTER(struct__IO_marker)),
    ('_sbuf', POINTER(struct__IO_FILE)),
    ('_pos', c_int),
]

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '__pad1',
    '__pad2',
    '__pad3',
    '__pad4',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', POINTER(None)),
    ('__pad2', POINTER(None)),
    ('__pad3', POINTER(None)),
    ('__pad4', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * (((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t))),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/config.h: 314
class struct_stat(Structure):
    pass

STRUCT_STAT = struct_stat # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/config.h: 314

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 25
class struct_DateTime(Structure):
    pass

struct_DateTime.__slots__ = [
    'mode',
    '_from',
    'to',
    'fracsec',
    'year',
    'month',
    'day',
    'hour',
    'minute',
    'second',
    'positive',
    'tz',
]
struct_DateTime._fields_ = [
    ('mode', c_int),
    ('_from', c_int),
    ('to', c_int),
    ('fracsec', c_int),
    ('year', c_int),
    ('month', c_int),
    ('day', c_int),
    ('hour', c_int),
    ('minute', c_int),
    ('second', c_double),
    ('positive', c_int),
    ('tz', c_int),
]

DateTime = struct_DateTime # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 25

enum_anon_6 = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_DB_WHERE = 0 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_DB_TABLE = (G_OPT_DB_WHERE + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_DB_DRIVER = (G_OPT_DB_TABLE + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_DB_DATABASE = (G_OPT_DB_DRIVER + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_DB_SCHEMA = (G_OPT_DB_DATABASE + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_DB_COLUMN = (G_OPT_DB_SCHEMA + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_DB_COLUMNS = (G_OPT_DB_COLUMN + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_I_GROUP = (G_OPT_DB_COLUMNS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_I_SUBGROUP = (G_OPT_I_GROUP + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R_INPUT = (G_OPT_I_SUBGROUP + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R_INPUTS = (G_OPT_R_INPUT + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R_OUTPUT = (G_OPT_R_INPUTS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R_MAP = (G_OPT_R_OUTPUT + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R_MAPS = (G_OPT_R_MAP + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R_BASE = (G_OPT_R_MAPS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R_COVER = (G_OPT_R_BASE + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R_ELEV = (G_OPT_R_COVER + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R_ELEVS = (G_OPT_R_ELEV + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R3_INPUT = (G_OPT_R_ELEVS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R3_INPUTS = (G_OPT_R3_INPUT + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R3_OUTPUT = (G_OPT_R3_INPUTS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R3_MAP = (G_OPT_R3_OUTPUT + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_R3_MAPS = (G_OPT_R3_MAP + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_INPUT = (G_OPT_R3_MAPS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_INPUTS = (G_OPT_V_INPUT + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_OUTPUT = (G_OPT_V_INPUTS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_MAP = (G_OPT_V_OUTPUT + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_MAPS = (G_OPT_V_MAP + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_TYPE = (G_OPT_V_MAPS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V3_TYPE = (G_OPT_V_TYPE + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_FIELD = (G_OPT_V3_TYPE + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_FIELD_ALL = (G_OPT_V_FIELD + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_CAT = (G_OPT_V_FIELD_ALL + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_CATS = (G_OPT_V_CAT + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_ID = (G_OPT_V_CATS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_V_IDS = (G_OPT_V_ID + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_F_INPUT = (G_OPT_V_IDS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_F_OUTPUT = (G_OPT_F_INPUT + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_F_SEP = (G_OPT_F_OUTPUT + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_C_FG = (G_OPT_F_SEP + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_C_BG = (G_OPT_C_FG + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_M_UNITS = (G_OPT_C_BG + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_M_DATATYPE = (G_OPT_M_UNITS + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

G_OPT_M_MAPSET = (G_OPT_M_DATATYPE + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

STD_OPT = enum_anon_6 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 216

enum_anon_7 = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_RASTER = 1 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_RASTER3D = 2 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_VECTOR = 3 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_OLDVECTOR = 4 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_ASCIIVECTOR = 5 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_ICON = 6 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_LABEL = 7 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_SITE = 8 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_REGION = 9 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_REGION3D = 10 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_GROUP = 11 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

G_ELEMENT_3DVIEW = 12 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 239

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 257
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 284
class struct_G_3dview(Structure):
    pass

struct_G_3dview.__slots__ = [
    'pgm_id',
    'from_to',
    'fov',
    'twist',
    'exag',
    'mesh_freq',
    'poly_freq',
    'display_type',
    'lightson',
    'dozero',
    'colorgrid',
    'shading',
    'fringe',
    'surfonly',
    'doavg',
    'grid_col',
    'bg_col',
    'other_col',
    'lightpos',
    'lightcol',
    'ambient',
    'shine',
    'vwin',
]
struct_G_3dview._fields_ = [
    ('pgm_id', c_char * 40),
    ('from_to', (c_float * 3) * 2),
    ('fov', c_float),
    ('twist', c_float),
    ('exag', c_float),
    ('mesh_freq', c_int),
    ('poly_freq', c_int),
    ('display_type', c_int),
    ('lightson', c_int),
    ('dozero', c_int),
    ('colorgrid', c_int),
    ('shading', c_int),
    ('fringe', c_int),
    ('surfonly', c_int),
    ('doavg', c_int),
    ('grid_col', c_char * 40),
    ('bg_col', c_char * 40),
    ('other_col', c_char * 40),
    ('lightpos', c_float * 4),
    ('lightcol', c_float * 3),
    ('ambient', c_float),
    ('shine', c_float),
    ('vwin', struct_Cell_head),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 311
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 319
class struct_Option(Structure):
    pass

struct_Option.__slots__ = [
    'key',
    'type',
    'required',
    'multiple',
    'options',
    'opts',
    'key_desc',
    'label',
    'description',
    'descriptions',
    'descs',
    'answer',
    '_def',
    'answers',
    'next_opt',
    'gisprompt',
    'guisection',
    'guidependency',
    'checker',
    'count',
]
struct_Option._fields_ = [
    ('key', String),
    ('type', c_int),
    ('required', c_int),
    ('multiple', c_int),
    ('options', String),
    ('opts', POINTER(POINTER(c_char))),
    ('key_desc', String),
    ('label', String),
    ('description', String),
    ('descriptions', String),
    ('descs', POINTER(POINTER(c_char))),
    ('answer', String),
    ('_def', String),
    ('answers', POINTER(POINTER(c_char))),
    ('next_opt', POINTER(struct_Option)),
    ('gisprompt', String),
    ('guisection', String),
    ('guidependency', String),
    ('checker', CFUNCTYPE(UNCHECKED(c_int), )),
    ('count', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 350
class struct_Flag(Structure):
    pass

struct_Flag.__slots__ = [
    'key',
    'answer',
    'suppress_required',
    'label',
    'description',
    'guisection',
    'next_flag',
]
struct_Flag._fields_ = [
    ('key', c_char),
    ('answer', c_char),
    ('suppress_required', c_char),
    ('label', String),
    ('description', String),
    ('guisection', String),
    ('next_flag', POINTER(struct_Flag)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 361
class struct_GModule(Structure):
    pass

struct_GModule.__slots__ = [
    'label',
    'description',
    'keywords',
    'overwrite',
    'verbose',
]
struct_GModule._fields_ = [
    ('label', String),
    ('description', String),
    ('keywords', POINTER(POINTER(c_char))),
    ('overwrite', c_int),
    ('verbose', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 371
class struct_TimeStamp(Structure):
    pass

struct_TimeStamp.__slots__ = [
    'dt',
    'count',
]
struct_TimeStamp._fields_ = [
    ('dt', DateTime * 2),
    ('count', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 377
class struct_Counter(Structure):
    pass

struct_Counter.__slots__ = [
    'value',
]
struct_Counter._fields_ = [
    ('value', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 381
class struct_Popen(Structure):
    pass

struct_Popen.__slots__ = [
    'fp',
    'pid',
]
struct_Popen._fields_ = [
    ('fp', POINTER(FILE)),
    ('pid', c_int),
]

off_t = __off64_t # /usr/include/sys/types.h: 90

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 54
if hasattr(_libs['grass_gis.7.0.svn'], 'G_adjust_Cell_head'):
    G_adjust_Cell_head = _libs['grass_gis.7.0.svn'].G_adjust_Cell_head
    G_adjust_Cell_head.restype = None
    G_adjust_Cell_head.argtypes = [POINTER(struct_Cell_head), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 55
if hasattr(_libs['grass_gis.7.0.svn'], 'G_adjust_Cell_head3'):
    G_adjust_Cell_head3 = _libs['grass_gis.7.0.svn'].G_adjust_Cell_head3
    G_adjust_Cell_head3.restype = None
    G_adjust_Cell_head3.argtypes = [POINTER(struct_Cell_head), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 61
if hasattr(_libs['grass_gis.7.0.svn'], 'G__malloc'):
    G__malloc = _libs['grass_gis.7.0.svn'].G__malloc
    G__malloc.restype = POINTER(None)
    G__malloc.argtypes = [String, c_int, c_size_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 62
if hasattr(_libs['grass_gis.7.0.svn'], 'G__calloc'):
    G__calloc = _libs['grass_gis.7.0.svn'].G__calloc
    G__calloc.restype = POINTER(None)
    G__calloc.argtypes = [String, c_int, c_size_t, c_size_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 63
if hasattr(_libs['grass_gis.7.0.svn'], 'G__realloc'):
    G__realloc = _libs['grass_gis.7.0.svn'].G__realloc
    G__realloc.restype = POINTER(None)
    G__realloc.argtypes = [String, c_int, POINTER(None), c_size_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 64
if hasattr(_libs['grass_gis.7.0.svn'], 'G_free'):
    G_free = _libs['grass_gis.7.0.svn'].G_free
    G_free.restype = None
    G_free.argtypes = [POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 80
if hasattr(_libs['grass_gis.7.0.svn'], 'G_begin_cell_area_calculations'):
    G_begin_cell_area_calculations = _libs['grass_gis.7.0.svn'].G_begin_cell_area_calculations
    G_begin_cell_area_calculations.restype = c_int
    G_begin_cell_area_calculations.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 81
if hasattr(_libs['grass_gis.7.0.svn'], 'G_area_of_cell_at_row'):
    G_area_of_cell_at_row = _libs['grass_gis.7.0.svn'].G_area_of_cell_at_row
    G_area_of_cell_at_row.restype = c_double
    G_area_of_cell_at_row.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 82
if hasattr(_libs['grass_gis.7.0.svn'], 'G_begin_polygon_area_calculations'):
    G_begin_polygon_area_calculations = _libs['grass_gis.7.0.svn'].G_begin_polygon_area_calculations
    G_begin_polygon_area_calculations.restype = c_int
    G_begin_polygon_area_calculations.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 83
if hasattr(_libs['grass_gis.7.0.svn'], 'G_area_of_polygon'):
    G_area_of_polygon = _libs['grass_gis.7.0.svn'].G_area_of_polygon
    G_area_of_polygon.restype = c_double
    G_area_of_polygon.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 86
if hasattr(_libs['grass_gis.7.0.svn'], 'G_begin_zone_area_on_ellipsoid'):
    G_begin_zone_area_on_ellipsoid = _libs['grass_gis.7.0.svn'].G_begin_zone_area_on_ellipsoid
    G_begin_zone_area_on_ellipsoid.restype = None
    G_begin_zone_area_on_ellipsoid.argtypes = [c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 87
if hasattr(_libs['grass_gis.7.0.svn'], 'G_darea0_on_ellipsoid'):
    G_darea0_on_ellipsoid = _libs['grass_gis.7.0.svn'].G_darea0_on_ellipsoid
    G_darea0_on_ellipsoid.restype = c_double
    G_darea0_on_ellipsoid.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 88
if hasattr(_libs['grass_gis.7.0.svn'], 'G_area_for_zone_on_ellipsoid'):
    G_area_for_zone_on_ellipsoid = _libs['grass_gis.7.0.svn'].G_area_for_zone_on_ellipsoid
    G_area_for_zone_on_ellipsoid.restype = c_double
    G_area_for_zone_on_ellipsoid.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 91
if hasattr(_libs['grass_gis.7.0.svn'], 'G_begin_ellipsoid_polygon_area'):
    G_begin_ellipsoid_polygon_area = _libs['grass_gis.7.0.svn'].G_begin_ellipsoid_polygon_area
    G_begin_ellipsoid_polygon_area.restype = None
    G_begin_ellipsoid_polygon_area.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 92
if hasattr(_libs['grass_gis.7.0.svn'], 'G_ellipsoid_polygon_area'):
    G_ellipsoid_polygon_area = _libs['grass_gis.7.0.svn'].G_ellipsoid_polygon_area
    G_ellipsoid_polygon_area.restype = c_double
    G_ellipsoid_polygon_area.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 95
if hasattr(_libs['grass_gis.7.0.svn'], 'G_planimetric_polygon_area'):
    G_planimetric_polygon_area = _libs['grass_gis.7.0.svn'].G_planimetric_polygon_area
    G_planimetric_polygon_area.restype = c_double
    G_planimetric_polygon_area.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 98
if hasattr(_libs['grass_gis.7.0.svn'], 'G_begin_zone_area_on_sphere'):
    G_begin_zone_area_on_sphere = _libs['grass_gis.7.0.svn'].G_begin_zone_area_on_sphere
    G_begin_zone_area_on_sphere.restype = None
    G_begin_zone_area_on_sphere.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 99
if hasattr(_libs['grass_gis.7.0.svn'], 'G_darea0_on_sphere'):
    G_darea0_on_sphere = _libs['grass_gis.7.0.svn'].G_darea0_on_sphere
    G_darea0_on_sphere.restype = c_double
    G_darea0_on_sphere.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 100
if hasattr(_libs['grass_gis.7.0.svn'], 'G_area_for_zone_on_sphere'):
    G_area_for_zone_on_sphere = _libs['grass_gis.7.0.svn'].G_area_for_zone_on_sphere
    G_area_for_zone_on_sphere.restype = c_double
    G_area_for_zone_on_sphere.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 103
if hasattr(_libs['grass_gis.7.0.svn'], 'G_ascii_check'):
    G_ascii_check = _libs['grass_gis.7.0.svn'].G_ascii_check
    G_ascii_check.restype = None
    G_ascii_check.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 115
if hasattr(_libs['grass_gis.7.0.svn'], 'G_vasprintf'):
    G_vasprintf = _libs['grass_gis.7.0.svn'].G_vasprintf
    G_vasprintf.restype = c_int
    G_vasprintf.argtypes = [POINTER(POINTER(c_char)), String, c_void_p]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 116
if hasattr(_libs['grass_gis.7.0.svn'], 'G_asprintf'):
    _func = _libs['grass_gis.7.0.svn'].G_asprintf
    _restype = c_int
    _argtypes = [POINTER(POINTER(c_char)), String]
    G_asprintf = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 120
if hasattr(_libs['grass_gis.7.0.svn'], 'G_basename'):
    G_basename = _libs['grass_gis.7.0.svn'].G_basename
    G_basename.restype = ReturnString
    G_basename.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 123
if hasattr(_libs['grass_gis.7.0.svn'], 'G_bresenham_line'):
    G_bresenham_line = _libs['grass_gis.7.0.svn'].G_bresenham_line
    G_bresenham_line.restype = None
    G_bresenham_line.argtypes = [c_int, c_int, c_int, c_int, CFUNCTYPE(UNCHECKED(c_int), c_int, c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 126
if hasattr(_libs['grass_gis.7.0.svn'], 'G_clicker'):
    G_clicker = _libs['grass_gis.7.0.svn'].G_clicker
    G_clicker.restype = None
    G_clicker.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 129
if hasattr(_libs['grass_gis.7.0.svn'], 'G_num_standard_colors'):
    G_num_standard_colors = _libs['grass_gis.7.0.svn'].G_num_standard_colors
    G_num_standard_colors.restype = c_int
    G_num_standard_colors.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 132
if hasattr(_libs['grass_gis.7.0.svn'], 'G_insert_commas'):
    G_insert_commas = _libs['grass_gis.7.0.svn'].G_insert_commas
    G_insert_commas.restype = c_int
    G_insert_commas.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 133
if hasattr(_libs['grass_gis.7.0.svn'], 'G_remove_commas'):
    G_remove_commas = _libs['grass_gis.7.0.svn'].G_remove_commas
    G_remove_commas.restype = None
    G_remove_commas.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 136
if hasattr(_libs['grass_gis.7.0.svn'], 'G_recursive_copy'):
    G_recursive_copy = _libs['grass_gis.7.0.svn'].G_recursive_copy
    G_recursive_copy.restype = c_int
    G_recursive_copy.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 139
if hasattr(_libs['grass_gis.7.0.svn'], 'G_copy_file'):
    G_copy_file = _libs['grass_gis.7.0.svn'].G_copy_file
    G_copy_file.restype = c_int
    G_copy_file.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 142
if hasattr(_libs['grass_gis.7.0.svn'], 'G_is_initialized'):
    G_is_initialized = _libs['grass_gis.7.0.svn'].G_is_initialized
    G_is_initialized.restype = c_int
    G_is_initialized.argtypes = [POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 143
if hasattr(_libs['grass_gis.7.0.svn'], 'G_initialize_done'):
    G_initialize_done = _libs['grass_gis.7.0.svn'].G_initialize_done
    G_initialize_done.restype = None
    G_initialize_done.argtypes = [POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 144
if hasattr(_libs['grass_gis.7.0.svn'], 'G_init_counter'):
    G_init_counter = _libs['grass_gis.7.0.svn'].G_init_counter
    G_init_counter.restype = None
    G_init_counter.argtypes = [POINTER(struct_Counter), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 145
if hasattr(_libs['grass_gis.7.0.svn'], 'G_counter_next'):
    G_counter_next = _libs['grass_gis.7.0.svn'].G_counter_next
    G_counter_next.restype = c_int
    G_counter_next.argtypes = [POINTER(struct_Counter)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 148
if hasattr(_libs['grass_gis.7.0.svn'], 'G_date'):
    G_date = _libs['grass_gis.7.0.svn'].G_date
    G_date.restype = ReturnString
    G_date.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 151
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_datum_by_name'):
    G_get_datum_by_name = _libs['grass_gis.7.0.svn'].G_get_datum_by_name
    G_get_datum_by_name.restype = c_int
    G_get_datum_by_name.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 152
if hasattr(_libs['grass_gis.7.0.svn'], 'G_datum_name'):
    G_datum_name = _libs['grass_gis.7.0.svn'].G_datum_name
    G_datum_name.restype = ReturnString
    G_datum_name.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 153
if hasattr(_libs['grass_gis.7.0.svn'], 'G_datum_description'):
    G_datum_description = _libs['grass_gis.7.0.svn'].G_datum_description
    G_datum_description.restype = ReturnString
    G_datum_description.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 154
if hasattr(_libs['grass_gis.7.0.svn'], 'G_datum_ellipsoid'):
    G_datum_ellipsoid = _libs['grass_gis.7.0.svn'].G_datum_ellipsoid
    G_datum_ellipsoid.restype = ReturnString
    G_datum_ellipsoid.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 155
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_datumparams_from_projinfo'):
    G_get_datumparams_from_projinfo = _libs['grass_gis.7.0.svn'].G_get_datumparams_from_projinfo
    G_get_datumparams_from_projinfo.restype = c_int
    G_get_datumparams_from_projinfo.argtypes = [POINTER(struct_Key_Value), String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 156
if hasattr(_libs['grass_gis.7.0.svn'], 'G_read_datum_table'):
    G_read_datum_table = _libs['grass_gis.7.0.svn'].G_read_datum_table
    G_read_datum_table.restype = None
    G_read_datum_table.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 160
if hasattr(_libs['grass_gis.7.0.svn'], 'G_init_debug'):
    G_init_debug = _libs['grass_gis.7.0.svn'].G_init_debug
    G_init_debug.restype = None
    G_init_debug.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 161
if hasattr(_libs['grass_gis.7.0.svn'], 'G_debug'):
    _func = _libs['grass_gis.7.0.svn'].G_debug
    _restype = c_int
    _argtypes = [c_int, String]
    G_debug = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 164
if hasattr(_libs['grass_gis.7.0.svn'], 'G_begin_distance_calculations'):
    G_begin_distance_calculations = _libs['grass_gis.7.0.svn'].G_begin_distance_calculations
    G_begin_distance_calculations.restype = c_int
    G_begin_distance_calculations.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 165
if hasattr(_libs['grass_gis.7.0.svn'], 'G_distance'):
    G_distance = _libs['grass_gis.7.0.svn'].G_distance
    G_distance.restype = c_double
    G_distance.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 166
if hasattr(_libs['grass_gis.7.0.svn'], 'G_distance_between_line_segments'):
    G_distance_between_line_segments = _libs['grass_gis.7.0.svn'].G_distance_between_line_segments
    G_distance_between_line_segments.restype = c_double
    G_distance_between_line_segments.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 168
if hasattr(_libs['grass_gis.7.0.svn'], 'G_distance_point_to_line_segment'):
    G_distance_point_to_line_segment = _libs['grass_gis.7.0.svn'].G_distance_point_to_line_segment
    G_distance_point_to_line_segment.restype = c_double
    G_distance_point_to_line_segment.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 172
if hasattr(_libs['grass_gis.7.0.svn'], 'G_done_msg'):
    _func = _libs['grass_gis.7.0.svn'].G_done_msg
    _restype = None
    _argtypes = [String]
    G_done_msg = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 175
if hasattr(_libs['grass_gis.7.0.svn'], 'G_is_little_endian'):
    G_is_little_endian = _libs['grass_gis.7.0.svn'].G_is_little_endian
    G_is_little_endian.restype = c_int
    G_is_little_endian.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 178
if hasattr(_libs['grass_gis.7.0.svn'], 'G_init_env'):
    G_init_env = _libs['grass_gis.7.0.svn'].G_init_env
    G_init_env.restype = None
    G_init_env.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 179
if hasattr(_libs['grass_gis.7.0.svn'], 'G_getenv'):
    G_getenv = _libs['grass_gis.7.0.svn'].G_getenv
    G_getenv.restype = ReturnString
    G_getenv.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 180
if hasattr(_libs['grass_gis.7.0.svn'], 'G_getenv2'):
    G_getenv2 = _libs['grass_gis.7.0.svn'].G_getenv2
    G_getenv2.restype = ReturnString
    G_getenv2.argtypes = [String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 181
if hasattr(_libs['grass_gis.7.0.svn'], 'G__getenv'):
    G__getenv = _libs['grass_gis.7.0.svn'].G__getenv
    G__getenv.restype = ReturnString
    G__getenv.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 182
if hasattr(_libs['grass_gis.7.0.svn'], 'G__getenv2'):
    G__getenv2 = _libs['grass_gis.7.0.svn'].G__getenv2
    G__getenv2.restype = ReturnString
    G__getenv2.argtypes = [String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 183
if hasattr(_libs['grass_gis.7.0.svn'], 'G_setenv'):
    G_setenv = _libs['grass_gis.7.0.svn'].G_setenv
    G_setenv.restype = None
    G_setenv.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 184
if hasattr(_libs['grass_gis.7.0.svn'], 'G_setenv2'):
    G_setenv2 = _libs['grass_gis.7.0.svn'].G_setenv2
    G_setenv2.restype = None
    G_setenv2.argtypes = [String, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 185
if hasattr(_libs['grass_gis.7.0.svn'], 'G__setenv'):
    G__setenv = _libs['grass_gis.7.0.svn'].G__setenv
    G__setenv.restype = None
    G__setenv.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 186
if hasattr(_libs['grass_gis.7.0.svn'], 'G__setenv2'):
    G__setenv2 = _libs['grass_gis.7.0.svn'].G__setenv2
    G__setenv2.restype = None
    G__setenv2.argtypes = [String, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 187
if hasattr(_libs['grass_gis.7.0.svn'], 'G_unsetenv'):
    G_unsetenv = _libs['grass_gis.7.0.svn'].G_unsetenv
    G_unsetenv.restype = None
    G_unsetenv.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 188
if hasattr(_libs['grass_gis.7.0.svn'], 'G_unsetenv2'):
    G_unsetenv2 = _libs['grass_gis.7.0.svn'].G_unsetenv2
    G_unsetenv2.restype = None
    G_unsetenv2.argtypes = [String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 189
if hasattr(_libs['grass_gis.7.0.svn'], 'G__write_env'):
    G__write_env = _libs['grass_gis.7.0.svn'].G__write_env
    G__write_env.restype = None
    G__write_env.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 190
if hasattr(_libs['grass_gis.7.0.svn'], 'G__env_name'):
    G__env_name = _libs['grass_gis.7.0.svn'].G__env_name
    G__env_name.restype = ReturnString
    G__env_name.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 191
if hasattr(_libs['grass_gis.7.0.svn'], 'G__read_env'):
    G__read_env = _libs['grass_gis.7.0.svn'].G__read_env
    G__read_env.restype = None
    G__read_env.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 192
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_gisrc_mode'):
    G_set_gisrc_mode = _libs['grass_gis.7.0.svn'].G_set_gisrc_mode
    G_set_gisrc_mode.restype = None
    G_set_gisrc_mode.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 193
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_gisrc_mode'):
    G_get_gisrc_mode = _libs['grass_gis.7.0.svn'].G_get_gisrc_mode
    G_get_gisrc_mode.restype = c_int
    G_get_gisrc_mode.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 194
if hasattr(_libs['grass_gis.7.0.svn'], 'G__create_alt_env'):
    G__create_alt_env = _libs['grass_gis.7.0.svn'].G__create_alt_env
    G__create_alt_env.restype = None
    G__create_alt_env.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 195
if hasattr(_libs['grass_gis.7.0.svn'], 'G__switch_env'):
    G__switch_env = _libs['grass_gis.7.0.svn'].G__switch_env
    G__switch_env.restype = None
    G__switch_env.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 198
if hasattr(_libs['grass_gis.7.0.svn'], 'G_info_format'):
    G_info_format = _libs['grass_gis.7.0.svn'].G_info_format
    G_info_format.restype = c_int
    G_info_format.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 199
if hasattr(_libs['grass_gis.7.0.svn'], 'G_message'):
    _func = _libs['grass_gis.7.0.svn'].G_message
    _restype = None
    _argtypes = [String]
    G_message = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 200
if hasattr(_libs['grass_gis.7.0.svn'], 'G_verbose_message'):
    _func = _libs['grass_gis.7.0.svn'].G_verbose_message
    _restype = None
    _argtypes = [String]
    G_verbose_message = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 202
if hasattr(_libs['grass_gis.7.0.svn'], 'G_important_message'):
    _func = _libs['grass_gis.7.0.svn'].G_important_message
    _restype = None
    _argtypes = [String]
    G_important_message = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 204
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fatal_error'):
    _func = _libs['grass_gis.7.0.svn'].G_fatal_error
    _restype = None
    _argtypes = [String]
    G_fatal_error = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 206
if hasattr(_libs['grass_gis.7.0.svn'], 'G_warning'):
    _func = _libs['grass_gis.7.0.svn'].G_warning
    _restype = None
    _argtypes = [String]
    G_warning = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 207
if hasattr(_libs['grass_gis.7.0.svn'], 'G_suppress_warnings'):
    G_suppress_warnings = _libs['grass_gis.7.0.svn'].G_suppress_warnings
    G_suppress_warnings.restype = c_int
    G_suppress_warnings.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 208
if hasattr(_libs['grass_gis.7.0.svn'], 'G_sleep_on_error'):
    G_sleep_on_error = _libs['grass_gis.7.0.svn'].G_sleep_on_error
    G_sleep_on_error.restype = c_int
    G_sleep_on_error.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 209
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_error_routine'):
    G_set_error_routine = _libs['grass_gis.7.0.svn'].G_set_error_routine
    G_set_error_routine.restype = None
    G_set_error_routine.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String, c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 210
if hasattr(_libs['grass_gis.7.0.svn'], 'G_unset_error_routine'):
    G_unset_error_routine = _libs['grass_gis.7.0.svn'].G_unset_error_routine
    G_unset_error_routine.restype = None
    G_unset_error_routine.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 211
if hasattr(_libs['grass_gis.7.0.svn'], 'G_init_logging'):
    G_init_logging = _libs['grass_gis.7.0.svn'].G_init_logging
    G_init_logging.restype = None
    G_init_logging.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 214
if hasattr(_libs['grass_gis.7.0.svn'], 'G_file_name'):
    G_file_name = _libs['grass_gis.7.0.svn'].G_file_name
    G_file_name.restype = ReturnString
    G_file_name.argtypes = [String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 215
if hasattr(_libs['grass_gis.7.0.svn'], 'G_file_name_misc'):
    G_file_name_misc = _libs['grass_gis.7.0.svn'].G_file_name_misc
    G_file_name_misc.restype = ReturnString
    G_file_name_misc.argtypes = [String, String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 219
if hasattr(_libs['grass_gis.7.0.svn'], 'G_find_raster'):
    G_find_raster = _libs['grass_gis.7.0.svn'].G_find_raster
    G_find_raster.restype = ReturnString
    G_find_raster.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 220
if hasattr(_libs['grass_gis.7.0.svn'], 'G_find_raster2'):
    G_find_raster2 = _libs['grass_gis.7.0.svn'].G_find_raster2
    G_find_raster2.restype = ReturnString
    G_find_raster2.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 223
if hasattr(_libs['grass_gis.7.0.svn'], 'G_find_file'):
    G_find_file = _libs['grass_gis.7.0.svn'].G_find_file
    G_find_file.restype = ReturnString
    G_find_file.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 224
if hasattr(_libs['grass_gis.7.0.svn'], 'G_find_file2'):
    G_find_file2 = _libs['grass_gis.7.0.svn'].G_find_file2
    G_find_file2.restype = ReturnString
    G_find_file2.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 225
if hasattr(_libs['grass_gis.7.0.svn'], 'G_find_file_misc'):
    G_find_file_misc = _libs['grass_gis.7.0.svn'].G_find_file_misc
    G_find_file_misc.restype = ReturnString
    G_find_file_misc.argtypes = [String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 226
if hasattr(_libs['grass_gis.7.0.svn'], 'G_find_file2_misc'):
    G_find_file2_misc = _libs['grass_gis.7.0.svn'].G_find_file2_misc
    G_find_file2_misc.restype = ReturnString
    G_find_file2_misc.argtypes = [String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 230
if hasattr(_libs['grass_gis.7.0.svn'], 'G_find_etc'):
    G_find_etc = _libs['grass_gis.7.0.svn'].G_find_etc
    G_find_etc.restype = ReturnString
    G_find_etc.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 233
if hasattr(_libs['grass_gis.7.0.svn'], 'G_find_vector'):
    G_find_vector = _libs['grass_gis.7.0.svn'].G_find_vector
    G_find_vector.restype = ReturnString
    G_find_vector.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 234
if hasattr(_libs['grass_gis.7.0.svn'], 'G_find_vector2'):
    G_find_vector2 = _libs['grass_gis.7.0.svn'].G_find_vector2
    G_find_vector2.restype = ReturnString
    G_find_vector2.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 237
if hasattr(_libs['grass_gis.7.0.svn'], 'G_zlib_compress'):
    G_zlib_compress = _libs['grass_gis.7.0.svn'].G_zlib_compress
    G_zlib_compress.restype = c_int
    G_zlib_compress.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 238
if hasattr(_libs['grass_gis.7.0.svn'], 'G_zlib_expand'):
    G_zlib_expand = _libs['grass_gis.7.0.svn'].G_zlib_expand
    G_zlib_expand.restype = c_int
    G_zlib_expand.argtypes = [POINTER(c_ubyte), c_int, POINTER(c_ubyte), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 239
if hasattr(_libs['grass_gis.7.0.svn'], 'G_zlib_write'):
    G_zlib_write = _libs['grass_gis.7.0.svn'].G_zlib_write
    G_zlib_write.restype = c_int
    G_zlib_write.argtypes = [c_int, POINTER(c_ubyte), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 240
if hasattr(_libs['grass_gis.7.0.svn'], 'G_zlib_read'):
    G_zlib_read = _libs['grass_gis.7.0.svn'].G_zlib_read
    G_zlib_read.restype = c_int
    G_zlib_read.argtypes = [c_int, c_int, POINTER(c_ubyte), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 241
if hasattr(_libs['grass_gis.7.0.svn'], 'G_zlib_write_noCompress'):
    G_zlib_write_noCompress = _libs['grass_gis.7.0.svn'].G_zlib_write_noCompress
    G_zlib_write_noCompress.restype = c_int
    G_zlib_write_noCompress.argtypes = [c_int, POINTER(c_ubyte), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 244
if hasattr(_libs['grass_gis.7.0.svn'], 'G_begin_geodesic_equation'):
    G_begin_geodesic_equation = _libs['grass_gis.7.0.svn'].G_begin_geodesic_equation
    G_begin_geodesic_equation.restype = c_int
    G_begin_geodesic_equation.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 245
if hasattr(_libs['grass_gis.7.0.svn'], 'G_geodesic_lat_from_lon'):
    G_geodesic_lat_from_lon = _libs['grass_gis.7.0.svn'].G_geodesic_lat_from_lon
    G_geodesic_lat_from_lon.restype = c_double
    G_geodesic_lat_from_lon.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 248
if hasattr(_libs['grass_gis.7.0.svn'], 'G_begin_geodesic_distance'):
    G_begin_geodesic_distance = _libs['grass_gis.7.0.svn'].G_begin_geodesic_distance
    G_begin_geodesic_distance.restype = None
    G_begin_geodesic_distance.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 249
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_geodesic_distance_lat1'):
    G_set_geodesic_distance_lat1 = _libs['grass_gis.7.0.svn'].G_set_geodesic_distance_lat1
    G_set_geodesic_distance_lat1.restype = None
    G_set_geodesic_distance_lat1.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 250
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_geodesic_distance_lat2'):
    G_set_geodesic_distance_lat2 = _libs['grass_gis.7.0.svn'].G_set_geodesic_distance_lat2
    G_set_geodesic_distance_lat2.restype = None
    G_set_geodesic_distance_lat2.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 251
if hasattr(_libs['grass_gis.7.0.svn'], 'G_geodesic_distance_lon_to_lon'):
    G_geodesic_distance_lon_to_lon = _libs['grass_gis.7.0.svn'].G_geodesic_distance_lon_to_lon
    G_geodesic_distance_lon_to_lon.restype = c_double
    G_geodesic_distance_lon_to_lon.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 252
if hasattr(_libs['grass_gis.7.0.svn'], 'G_geodesic_distance'):
    G_geodesic_distance = _libs['grass_gis.7.0.svn'].G_geodesic_distance
    G_geodesic_distance.restype = c_double
    G_geodesic_distance.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 255
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_ellipsoid_parameters'):
    G_get_ellipsoid_parameters = _libs['grass_gis.7.0.svn'].G_get_ellipsoid_parameters
    G_get_ellipsoid_parameters.restype = c_int
    G_get_ellipsoid_parameters.argtypes = [POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 256
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_spheroid_by_name'):
    G_get_spheroid_by_name = _libs['grass_gis.7.0.svn'].G_get_spheroid_by_name
    G_get_spheroid_by_name.restype = c_int
    G_get_spheroid_by_name.argtypes = [String, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 257
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_ellipsoid_by_name'):
    G_get_ellipsoid_by_name = _libs['grass_gis.7.0.svn'].G_get_ellipsoid_by_name
    G_get_ellipsoid_by_name.restype = c_int
    G_get_ellipsoid_by_name.argtypes = [String, POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 258
if hasattr(_libs['grass_gis.7.0.svn'], 'G_ellipsoid_name'):
    G_ellipsoid_name = _libs['grass_gis.7.0.svn'].G_ellipsoid_name
    G_ellipsoid_name.restype = ReturnString
    G_ellipsoid_name.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 259
if hasattr(_libs['grass_gis.7.0.svn'], 'G_ellipsoid_description'):
    G_ellipsoid_description = _libs['grass_gis.7.0.svn'].G_ellipsoid_description
    G_ellipsoid_description.restype = ReturnString
    G_ellipsoid_description.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 260
if hasattr(_libs['grass_gis.7.0.svn'], 'G_read_ellipsoid_table'):
    G_read_ellipsoid_table = _libs['grass_gis.7.0.svn'].G_read_ellipsoid_table
    G_read_ellipsoid_table.restype = c_int
    G_read_ellipsoid_table.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 263
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_projunits'):
    G_get_projunits = _libs['grass_gis.7.0.svn'].G_get_projunits
    G_get_projunits.restype = POINTER(struct_Key_Value)
    G_get_projunits.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 264
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_projinfo'):
    G_get_projinfo = _libs['grass_gis.7.0.svn'].G_get_projinfo
    G_get_projinfo.restype = POINTER(struct_Key_Value)
    G_get_projinfo.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 267
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_window'):
    G_get_window = _libs['grass_gis.7.0.svn'].G_get_window
    G_get_window.restype = None
    G_get_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 268
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_default_window'):
    G_get_default_window = _libs['grass_gis.7.0.svn'].G_get_default_window
    G_get_default_window.restype = None
    G_get_default_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 269
if hasattr(_libs['grass_gis.7.0.svn'], 'G__get_window'):
    G__get_window = _libs['grass_gis.7.0.svn'].G__get_window
    G__get_window.restype = None
    G__get_window.argtypes = [POINTER(struct_Cell_head), String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 273
if hasattr(_libs['grass_gis.7.0.svn'], 'G_getl'):
    G_getl = _libs['grass_gis.7.0.svn'].G_getl
    G_getl.restype = c_int
    G_getl.argtypes = [String, c_int, POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 274
if hasattr(_libs['grass_gis.7.0.svn'], 'G_getl2'):
    G_getl2 = _libs['grass_gis.7.0.svn'].G_getl2
    G_getl2.restype = c_int
    G_getl2.argtypes = [String, c_int, POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 277
if hasattr(_libs['grass_gis.7.0.svn'], 'G_gisbase'):
    G_gisbase = _libs['grass_gis.7.0.svn'].G_gisbase
    G_gisbase.restype = ReturnString
    G_gisbase.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 280
if hasattr(_libs['grass_gis.7.0.svn'], 'G_gisdbase'):
    G_gisdbase = _libs['grass_gis.7.0.svn'].G_gisdbase
    G_gisdbase.restype = ReturnString
    G_gisdbase.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 283
if hasattr(_libs['grass_gis.7.0.svn'], 'G__gisinit'):
    G__gisinit = _libs['grass_gis.7.0.svn'].G__gisinit
    G__gisinit.restype = None
    G__gisinit.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 284
if hasattr(_libs['grass_gis.7.0.svn'], 'G__no_gisinit'):
    G__no_gisinit = _libs['grass_gis.7.0.svn'].G__no_gisinit
    G__no_gisinit.restype = None
    G__no_gisinit.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 285
if hasattr(_libs['grass_gis.7.0.svn'], 'G__check_gisinit'):
    G__check_gisinit = _libs['grass_gis.7.0.svn'].G__check_gisinit
    G__check_gisinit.restype = None
    G__check_gisinit.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 286
if hasattr(_libs['grass_gis.7.0.svn'], 'G_init_all'):
    G_init_all = _libs['grass_gis.7.0.svn'].G_init_all
    G_init_all.restype = None
    G_init_all.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 289
if hasattr(_libs['grass_gis.7.0.svn'], 'G_add_error_handler'):
    G_add_error_handler = _libs['grass_gis.7.0.svn'].G_add_error_handler
    G_add_error_handler.restype = None
    G_add_error_handler.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 290
if hasattr(_libs['grass_gis.7.0.svn'], 'G_remove_error_handler'):
    G_remove_error_handler = _libs['grass_gis.7.0.svn'].G_remove_error_handler
    G_remove_error_handler.restype = None
    G_remove_error_handler.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 291
if hasattr(_libs['grass_gis.7.0.svn'], 'G__call_error_handlers'):
    G__call_error_handlers = _libs['grass_gis.7.0.svn'].G__call_error_handlers
    G__call_error_handlers.restype = None
    G__call_error_handlers.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 294
if hasattr(_libs['grass_gis.7.0.svn'], 'G_home'):
    G_home = _libs['grass_gis.7.0.svn'].G_home
    G_home.restype = ReturnString
    G_home.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 295
if hasattr(_libs['grass_gis.7.0.svn'], 'G__home'):
    G__home = _libs['grass_gis.7.0.svn'].G__home
    G__home.restype = ReturnString
    G__home.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 298
if hasattr(_libs['grass_gis.7.0.svn'], 'G_intersect_line_segments'):
    G_intersect_line_segments = _libs['grass_gis.7.0.svn'].G_intersect_line_segments
    G_intersect_line_segments.restype = c_int
    G_intersect_line_segments.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 303
if hasattr(_libs['grass_gis.7.0.svn'], 'G_is_gisbase'):
    G_is_gisbase = _libs['grass_gis.7.0.svn'].G_is_gisbase
    G_is_gisbase.restype = c_int
    G_is_gisbase.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 304
if hasattr(_libs['grass_gis.7.0.svn'], 'G_is_location'):
    G_is_location = _libs['grass_gis.7.0.svn'].G_is_location
    G_is_location.restype = c_int
    G_is_location.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 305
if hasattr(_libs['grass_gis.7.0.svn'], 'G_is_mapset'):
    G_is_mapset = _libs['grass_gis.7.0.svn'].G_is_mapset
    G_is_mapset.restype = c_int
    G_is_mapset.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 308
if hasattr(_libs['grass_gis.7.0.svn'], 'G_create_key_value'):
    G_create_key_value = _libs['grass_gis.7.0.svn'].G_create_key_value
    G_create_key_value.restype = POINTER(struct_Key_Value)
    G_create_key_value.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 309
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_key_value'):
    G_set_key_value = _libs['grass_gis.7.0.svn'].G_set_key_value
    G_set_key_value.restype = None
    G_set_key_value.argtypes = [String, String, POINTER(struct_Key_Value)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 310
if hasattr(_libs['grass_gis.7.0.svn'], 'G_find_key_value'):
    G_find_key_value = _libs['grass_gis.7.0.svn'].G_find_key_value
    G_find_key_value.restype = ReturnString
    G_find_key_value.argtypes = [String, POINTER(struct_Key_Value)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 311
if hasattr(_libs['grass_gis.7.0.svn'], 'G_free_key_value'):
    G_free_key_value = _libs['grass_gis.7.0.svn'].G_free_key_value
    G_free_key_value.restype = None
    G_free_key_value.argtypes = [POINTER(struct_Key_Value)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 314
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fwrite_key_value'):
    G_fwrite_key_value = _libs['grass_gis.7.0.svn'].G_fwrite_key_value
    G_fwrite_key_value.restype = c_int
    G_fwrite_key_value.argtypes = [POINTER(FILE), POINTER(struct_Key_Value)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 315
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fread_key_value'):
    G_fread_key_value = _libs['grass_gis.7.0.svn'].G_fread_key_value
    G_fread_key_value.restype = POINTER(struct_Key_Value)
    G_fread_key_value.argtypes = [POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 318
if hasattr(_libs['grass_gis.7.0.svn'], 'G_write_key_value_file'):
    G_write_key_value_file = _libs['grass_gis.7.0.svn'].G_write_key_value_file
    G_write_key_value_file.restype = None
    G_write_key_value_file.argtypes = [String, POINTER(struct_Key_Value)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 319
if hasattr(_libs['grass_gis.7.0.svn'], 'G_read_key_value_file'):
    G_read_key_value_file = _libs['grass_gis.7.0.svn'].G_read_key_value_file
    G_read_key_value_file.restype = POINTER(struct_Key_Value)
    G_read_key_value_file.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 322
if hasattr(_libs['grass_gis.7.0.svn'], 'G_update_key_value_file'):
    G_update_key_value_file = _libs['grass_gis.7.0.svn'].G_update_key_value_file
    G_update_key_value_file.restype = None
    G_update_key_value_file.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 323
if hasattr(_libs['grass_gis.7.0.svn'], 'G_lookup_key_value_from_file'):
    G_lookup_key_value_from_file = _libs['grass_gis.7.0.svn'].G_lookup_key_value_from_file
    G_lookup_key_value_from_file.restype = c_int
    G_lookup_key_value_from_file.argtypes = [String, String, POINTER(c_char), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 326
if hasattr(_libs['grass_gis.7.0.svn'], 'G_legal_filename'):
    G_legal_filename = _libs['grass_gis.7.0.svn'].G_legal_filename
    G_legal_filename.restype = c_int
    G_legal_filename.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 327
if hasattr(_libs['grass_gis.7.0.svn'], 'G_check_input_output_name'):
    G_check_input_output_name = _libs['grass_gis.7.0.svn'].G_check_input_output_name
    G_check_input_output_name.restype = c_int
    G_check_input_output_name.argtypes = [String, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 330
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_distance_to_line_tolerance'):
    G_set_distance_to_line_tolerance = _libs['grass_gis.7.0.svn'].G_set_distance_to_line_tolerance
    G_set_distance_to_line_tolerance.restype = None
    G_set_distance_to_line_tolerance.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 331
if hasattr(_libs['grass_gis.7.0.svn'], 'G_distance2_point_to_line'):
    G_distance2_point_to_line = _libs['grass_gis.7.0.svn'].G_distance2_point_to_line
    G_distance2_point_to_line.restype = c_double
    G_distance2_point_to_line.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 335
if hasattr(_libs['grass_gis.7.0.svn'], 'G_list_element'):
    G_list_element = _libs['grass_gis.7.0.svn'].G_list_element
    G_list_element.restype = None
    G_list_element.argtypes = [String, String, String, CFUNCTYPE(UNCHECKED(c_int), String, String, String)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 337
if hasattr(_libs['grass_gis.7.0.svn'], 'G_list'):
    G_list = _libs['grass_gis.7.0.svn'].G_list
    G_list.restype = POINTER(POINTER(c_char))
    G_list.argtypes = [c_int, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 338
if hasattr(_libs['grass_gis.7.0.svn'], 'G_free_list'):
    G_free_list = _libs['grass_gis.7.0.svn'].G_free_list
    G_free_list.restype = None
    G_free_list.argtypes = [POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 341
if hasattr(_libs['grass_gis.7.0.svn'], 'G_lat_format'):
    G_lat_format = _libs['grass_gis.7.0.svn'].G_lat_format
    G_lat_format.restype = None
    G_lat_format.argtypes = [c_double, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 342
if hasattr(_libs['grass_gis.7.0.svn'], 'G_lat_format_string'):
    G_lat_format_string = _libs['grass_gis.7.0.svn'].G_lat_format_string
    G_lat_format_string.restype = ReturnString
    G_lat_format_string.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 343
if hasattr(_libs['grass_gis.7.0.svn'], 'G_lon_format'):
    G_lon_format = _libs['grass_gis.7.0.svn'].G_lon_format
    G_lon_format.restype = None
    G_lon_format.argtypes = [c_double, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 344
if hasattr(_libs['grass_gis.7.0.svn'], 'G_lon_format_string'):
    G_lon_format_string = _libs['grass_gis.7.0.svn'].G_lon_format_string
    G_lon_format_string.restype = ReturnString
    G_lon_format_string.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 345
if hasattr(_libs['grass_gis.7.0.svn'], 'G_llres_format'):
    G_llres_format = _libs['grass_gis.7.0.svn'].G_llres_format
    G_llres_format.restype = None
    G_llres_format.argtypes = [c_double, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 346
if hasattr(_libs['grass_gis.7.0.svn'], 'G_llres_format_string'):
    G_llres_format_string = _libs['grass_gis.7.0.svn'].G_llres_format_string
    G_llres_format_string.restype = ReturnString
    G_llres_format_string.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 347
if hasattr(_libs['grass_gis.7.0.svn'], 'G_lat_parts'):
    G_lat_parts = _libs['grass_gis.7.0.svn'].G_lat_parts
    G_lat_parts.restype = None
    G_lat_parts.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_double), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 348
if hasattr(_libs['grass_gis.7.0.svn'], 'G_lon_parts'):
    G_lon_parts = _libs['grass_gis.7.0.svn'].G_lon_parts
    G_lon_parts.restype = None
    G_lon_parts.argtypes = [c_double, POINTER(c_int), POINTER(c_int), POINTER(c_double), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 351
if hasattr(_libs['grass_gis.7.0.svn'], 'G_lat_scan'):
    G_lat_scan = _libs['grass_gis.7.0.svn'].G_lat_scan
    G_lat_scan.restype = c_int
    G_lat_scan.argtypes = [String, POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 352
if hasattr(_libs['grass_gis.7.0.svn'], 'G_lon_scan'):
    G_lon_scan = _libs['grass_gis.7.0.svn'].G_lon_scan
    G_lon_scan.restype = c_int
    G_lon_scan.argtypes = [String, POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 353
if hasattr(_libs['grass_gis.7.0.svn'], 'G_llres_scan'):
    G_llres_scan = _libs['grass_gis.7.0.svn'].G_llres_scan
    G_llres_scan.restype = c_int
    G_llres_scan.argtypes = [String, POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 356
if hasattr(_libs['grass_gis.7.0.svn'], 'G_location'):
    G_location = _libs['grass_gis.7.0.svn'].G_location
    G_location.restype = ReturnString
    G_location.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 357
if hasattr(_libs['grass_gis.7.0.svn'], 'G_location_path'):
    G_location_path = _libs['grass_gis.7.0.svn'].G_location_path
    G_location_path.restype = ReturnString
    G_location_path.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 358
if hasattr(_libs['grass_gis.7.0.svn'], 'G__location_path'):
    G__location_path = _libs['grass_gis.7.0.svn'].G__location_path
    G__location_path.restype = ReturnString
    G__location_path.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 361
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_ls_filter'):
    G_set_ls_filter = _libs['grass_gis.7.0.svn'].G_set_ls_filter
    G_set_ls_filter.restype = None
    G_set_ls_filter.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String, POINTER(None)), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 362
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_ls_exclude_filter'):
    G_set_ls_exclude_filter = _libs['grass_gis.7.0.svn'].G_set_ls_exclude_filter
    G_set_ls_exclude_filter.restype = None
    G_set_ls_exclude_filter.argtypes = [CFUNCTYPE(UNCHECKED(c_int), String, POINTER(None)), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 363
if hasattr(_libs['grass_gis.7.0.svn'], 'G__ls'):
    G__ls = _libs['grass_gis.7.0.svn'].G__ls
    G__ls.restype = POINTER(POINTER(c_char))
    G__ls.argtypes = [String, POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 364
if hasattr(_libs['grass_gis.7.0.svn'], 'G_ls'):
    G_ls = _libs['grass_gis.7.0.svn'].G_ls
    G_ls.restype = None
    G_ls.argtypes = [String, POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 365
if hasattr(_libs['grass_gis.7.0.svn'], 'G_ls_format'):
    G_ls_format = _libs['grass_gis.7.0.svn'].G_ls_format
    G_ls_format.restype = None
    G_ls_format.argtypes = [POINTER(POINTER(c_char)), c_int, c_int, POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 369
if hasattr(_libs['grass_gis.7.0.svn'], 'G_ls_regex_filter'):
    G_ls_regex_filter = _libs['grass_gis.7.0.svn'].G_ls_regex_filter
    G_ls_regex_filter.restype = POINTER(None)
    G_ls_regex_filter.argtypes = [String, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 370
if hasattr(_libs['grass_gis.7.0.svn'], 'G_ls_glob_filter'):
    G_ls_glob_filter = _libs['grass_gis.7.0.svn'].G_ls_glob_filter
    G_ls_glob_filter.restype = POINTER(None)
    G_ls_glob_filter.argtypes = [String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 371
if hasattr(_libs['grass_gis.7.0.svn'], 'G_free_ls_filter'):
    G_free_ls_filter = _libs['grass_gis.7.0.svn'].G_free_ls_filter
    G_free_ls_filter.restype = None
    G_free_ls_filter.argtypes = [POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 375
if hasattr(_libs['grass_gis.7.0.svn'], 'G__machine_name'):
    G__machine_name = _libs['grass_gis.7.0.svn'].G__machine_name
    G__machine_name.restype = ReturnString
    G__machine_name.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 378
if hasattr(_libs['grass_gis.7.0.svn'], 'G__make_location'):
    G__make_location = _libs['grass_gis.7.0.svn'].G__make_location
    G__make_location.restype = c_int
    G__make_location.argtypes = [String, POINTER(struct_Cell_head), POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 380
if hasattr(_libs['grass_gis.7.0.svn'], 'G_make_location'):
    G_make_location = _libs['grass_gis.7.0.svn'].G_make_location
    G_make_location.restype = c_int
    G_make_location.argtypes = [String, POINTER(struct_Cell_head), POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 382
if hasattr(_libs['grass_gis.7.0.svn'], 'G_compare_projections'):
    G_compare_projections = _libs['grass_gis.7.0.svn'].G_compare_projections
    G_compare_projections.restype = c_int
    G_compare_projections.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 386
if hasattr(_libs['grass_gis.7.0.svn'], 'G__make_mapset'):
    G__make_mapset = _libs['grass_gis.7.0.svn'].G__make_mapset
    G__make_mapset.restype = c_int
    G__make_mapset.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 388
if hasattr(_libs['grass_gis.7.0.svn'], 'G_make_mapset'):
    G_make_mapset = _libs['grass_gis.7.0.svn'].G_make_mapset
    G_make_mapset.restype = c_int
    G_make_mapset.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 392
if hasattr(_libs['grass_gis.7.0.svn'], 'G_tolcase'):
    G_tolcase = _libs['grass_gis.7.0.svn'].G_tolcase
    G_tolcase.restype = ReturnString
    G_tolcase.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 393
if hasattr(_libs['grass_gis.7.0.svn'], 'G_toucase'):
    G_toucase = _libs['grass_gis.7.0.svn'].G_toucase
    G_toucase.restype = ReturnString
    G_toucase.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 396
if hasattr(_libs['grass_gis.7.0.svn'], 'G_mapset'):
    G_mapset = _libs['grass_gis.7.0.svn'].G_mapset
    G_mapset.restype = ReturnString
    G_mapset.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 397
if hasattr(_libs['grass_gis.7.0.svn'], 'G__mapset'):
    G__mapset = _libs['grass_gis.7.0.svn'].G__mapset
    G__mapset.restype = ReturnString
    G__mapset.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 400
if hasattr(_libs['grass_gis.7.0.svn'], 'G__make_mapset_element'):
    G__make_mapset_element = _libs['grass_gis.7.0.svn'].G__make_mapset_element
    G__make_mapset_element.restype = c_int
    G__make_mapset_element.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 401
if hasattr(_libs['grass_gis.7.0.svn'], 'G__make_mapset_element_misc'):
    G__make_mapset_element_misc = _libs['grass_gis.7.0.svn'].G__make_mapset_element_misc
    G__make_mapset_element_misc.restype = c_int
    G__make_mapset_element_misc.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 402
if hasattr(_libs['grass_gis.7.0.svn'], 'G__mapset_permissions'):
    G__mapset_permissions = _libs['grass_gis.7.0.svn'].G__mapset_permissions
    G__mapset_permissions.restype = c_int
    G__mapset_permissions.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 403
if hasattr(_libs['grass_gis.7.0.svn'], 'G__mapset_permissions2'):
    G__mapset_permissions2 = _libs['grass_gis.7.0.svn'].G__mapset_permissions2
    G__mapset_permissions2.restype = c_int
    G__mapset_permissions2.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 406
if hasattr(_libs['grass_gis.7.0.svn'], 'G__mapset_name'):
    G__mapset_name = _libs['grass_gis.7.0.svn'].G__mapset_name
    G__mapset_name.restype = ReturnString
    G__mapset_name.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 407
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_list_of_mapsets'):
    G_get_list_of_mapsets = _libs['grass_gis.7.0.svn'].G_get_list_of_mapsets
    G_get_list_of_mapsets.restype = None
    G_get_list_of_mapsets.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 408
if hasattr(_libs['grass_gis.7.0.svn'], 'G__create_alt_search_path'):
    G__create_alt_search_path = _libs['grass_gis.7.0.svn'].G__create_alt_search_path
    G__create_alt_search_path.restype = None
    G__create_alt_search_path.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 409
if hasattr(_libs['grass_gis.7.0.svn'], 'G__switch_search_path'):
    G__switch_search_path = _libs['grass_gis.7.0.svn'].G__switch_search_path
    G__switch_search_path.restype = None
    G__switch_search_path.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 410
if hasattr(_libs['grass_gis.7.0.svn'], 'G_reset_mapsets'):
    G_reset_mapsets = _libs['grass_gis.7.0.svn'].G_reset_mapsets
    G_reset_mapsets.restype = None
    G_reset_mapsets.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 411
if hasattr(_libs['grass_gis.7.0.svn'], 'G_available_mapsets'):
    G_available_mapsets = _libs['grass_gis.7.0.svn'].G_available_mapsets
    G_available_mapsets.restype = POINTER(POINTER(c_char))
    G_available_mapsets.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 412
if hasattr(_libs['grass_gis.7.0.svn'], 'G_add_mapset_to_search_path'):
    G_add_mapset_to_search_path = _libs['grass_gis.7.0.svn'].G_add_mapset_to_search_path
    G_add_mapset_to_search_path.restype = None
    G_add_mapset_to_search_path.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 413
if hasattr(_libs['grass_gis.7.0.svn'], 'G_is_mapset_in_search_path'):
    G_is_mapset_in_search_path = _libs['grass_gis.7.0.svn'].G_is_mapset_in_search_path
    G_is_mapset_in_search_path.restype = c_int
    G_is_mapset_in_search_path.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 416
if hasattr(_libs['grass_gis.7.0.svn'], 'G_myname'):
    G_myname = _libs['grass_gis.7.0.svn'].G_myname
    G_myname.restype = ReturnString
    G_myname.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 419
if hasattr(_libs['grass_gis.7.0.svn'], 'G_color_values'):
    G_color_values = _libs['grass_gis.7.0.svn'].G_color_values
    G_color_values.restype = c_int
    G_color_values.argtypes = [String, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 420
if hasattr(_libs['grass_gis.7.0.svn'], 'G_color_name'):
    G_color_name = _libs['grass_gis.7.0.svn'].G_color_name
    G_color_name.restype = ReturnString
    G_color_name.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 423
if hasattr(_libs['grass_gis.7.0.svn'], 'G_newlines_to_spaces'):
    G_newlines_to_spaces = _libs['grass_gis.7.0.svn'].G_newlines_to_spaces
    G_newlines_to_spaces.restype = None
    G_newlines_to_spaces.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 426
if hasattr(_libs['grass_gis.7.0.svn'], 'G_name_is_fully_qualified'):
    G_name_is_fully_qualified = _libs['grass_gis.7.0.svn'].G_name_is_fully_qualified
    G_name_is_fully_qualified.restype = c_int
    G_name_is_fully_qualified.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 427
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fully_qualified_name'):
    G_fully_qualified_name = _libs['grass_gis.7.0.svn'].G_fully_qualified_name
    G_fully_qualified_name.restype = ReturnString
    G_fully_qualified_name.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 428
if hasattr(_libs['grass_gis.7.0.svn'], 'G_unqualified_name'):
    G_unqualified_name = _libs['grass_gis.7.0.svn'].G_unqualified_name
    G_unqualified_name.restype = c_int
    G_unqualified_name.argtypes = [String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 431
if hasattr(_libs['grass_gis.7.0.svn'], 'G_open_new'):
    G_open_new = _libs['grass_gis.7.0.svn'].G_open_new
    G_open_new.restype = c_int
    G_open_new.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 432
if hasattr(_libs['grass_gis.7.0.svn'], 'G_open_old'):
    G_open_old = _libs['grass_gis.7.0.svn'].G_open_old
    G_open_old.restype = c_int
    G_open_old.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 433
if hasattr(_libs['grass_gis.7.0.svn'], 'G_open_update'):
    G_open_update = _libs['grass_gis.7.0.svn'].G_open_update
    G_open_update.restype = c_int
    G_open_update.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 434
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fopen_new'):
    G_fopen_new = _libs['grass_gis.7.0.svn'].G_fopen_new
    G_fopen_new.restype = POINTER(FILE)
    G_fopen_new.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 435
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fopen_old'):
    G_fopen_old = _libs['grass_gis.7.0.svn'].G_fopen_old
    G_fopen_old.restype = POINTER(FILE)
    G_fopen_old.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 436
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fopen_append'):
    G_fopen_append = _libs['grass_gis.7.0.svn'].G_fopen_append
    G_fopen_append.restype = POINTER(FILE)
    G_fopen_append.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 437
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fopen_modify'):
    G_fopen_modify = _libs['grass_gis.7.0.svn'].G_fopen_modify
    G_fopen_modify.restype = POINTER(FILE)
    G_fopen_modify.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 440
if hasattr(_libs['grass_gis.7.0.svn'], 'G_open_new_misc'):
    G_open_new_misc = _libs['grass_gis.7.0.svn'].G_open_new_misc
    G_open_new_misc.restype = c_int
    G_open_new_misc.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 441
if hasattr(_libs['grass_gis.7.0.svn'], 'G_open_old_misc'):
    G_open_old_misc = _libs['grass_gis.7.0.svn'].G_open_old_misc
    G_open_old_misc.restype = c_int
    G_open_old_misc.argtypes = [String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 442
if hasattr(_libs['grass_gis.7.0.svn'], 'G_open_update_misc'):
    G_open_update_misc = _libs['grass_gis.7.0.svn'].G_open_update_misc
    G_open_update_misc.restype = c_int
    G_open_update_misc.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 443
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fopen_new_misc'):
    G_fopen_new_misc = _libs['grass_gis.7.0.svn'].G_fopen_new_misc
    G_fopen_new_misc.restype = POINTER(FILE)
    G_fopen_new_misc.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 444
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fopen_old_misc'):
    G_fopen_old_misc = _libs['grass_gis.7.0.svn'].G_fopen_old_misc
    G_fopen_old_misc.restype = POINTER(FILE)
    G_fopen_old_misc.argtypes = [String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 446
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fopen_append_misc'):
    G_fopen_append_misc = _libs['grass_gis.7.0.svn'].G_fopen_append_misc
    G_fopen_append_misc.restype = POINTER(FILE)
    G_fopen_append_misc.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 447
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fopen_modify_misc'):
    G_fopen_modify_misc = _libs['grass_gis.7.0.svn'].G_fopen_modify_misc
    G_fopen_modify_misc.restype = POINTER(FILE)
    G_fopen_modify_misc.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 450
if hasattr(_libs['grass_gis.7.0.svn'], 'G_check_overwrite'):
    G_check_overwrite = _libs['grass_gis.7.0.svn'].G_check_overwrite
    G_check_overwrite.restype = c_int
    G_check_overwrite.argtypes = [c_int, POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 453
if hasattr(_libs['grass_gis.7.0.svn'], 'G_open_pager'):
    G_open_pager = _libs['grass_gis.7.0.svn'].G_open_pager
    G_open_pager.restype = POINTER(FILE)
    G_open_pager.argtypes = [POINTER(struct_Popen)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 454
if hasattr(_libs['grass_gis.7.0.svn'], 'G_close_pager'):
    G_close_pager = _libs['grass_gis.7.0.svn'].G_close_pager
    G_close_pager.restype = None
    G_close_pager.argtypes = [POINTER(struct_Popen)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 455
if hasattr(_libs['grass_gis.7.0.svn'], 'G_open_mail'):
    G_open_mail = _libs['grass_gis.7.0.svn'].G_open_mail
    G_open_mail.restype = POINTER(FILE)
    G_open_mail.argtypes = [POINTER(struct_Popen)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 456
if hasattr(_libs['grass_gis.7.0.svn'], 'G_close_mail'):
    G_close_mail = _libs['grass_gis.7.0.svn'].G_close_mail
    G_close_mail.restype = None
    G_close_mail.argtypes = [POINTER(struct_Popen)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 459
if hasattr(_libs['grass_gis.7.0.svn'], 'G_disable_interactive'):
    G_disable_interactive = _libs['grass_gis.7.0.svn'].G_disable_interactive
    G_disable_interactive.restype = None
    G_disable_interactive.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 460
if hasattr(_libs['grass_gis.7.0.svn'], 'G_define_module'):
    G_define_module = _libs['grass_gis.7.0.svn'].G_define_module
    G_define_module.restype = POINTER(struct_GModule)
    G_define_module.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 461
if hasattr(_libs['grass_gis.7.0.svn'], 'G_define_flag'):
    G_define_flag = _libs['grass_gis.7.0.svn'].G_define_flag
    G_define_flag.restype = POINTER(struct_Flag)
    G_define_flag.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 462
if hasattr(_libs['grass_gis.7.0.svn'], 'G_define_option'):
    G_define_option = _libs['grass_gis.7.0.svn'].G_define_option
    G_define_option.restype = POINTER(struct_Option)
    G_define_option.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 463
if hasattr(_libs['grass_gis.7.0.svn'], 'G_define_standard_option'):
    G_define_standard_option = _libs['grass_gis.7.0.svn'].G_define_standard_option
    G_define_standard_option.restype = POINTER(struct_Option)
    G_define_standard_option.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 464
if hasattr(_libs['grass_gis.7.0.svn'], 'G_parser'):
    G_parser = _libs['grass_gis.7.0.svn'].G_parser
    G_parser.restype = c_int
    G_parser.argtypes = [c_int, POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 465
if hasattr(_libs['grass_gis.7.0.svn'], 'G_usage'):
    G_usage = _libs['grass_gis.7.0.svn'].G_usage
    G_usage.restype = None
    G_usage.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 466
if hasattr(_libs['grass_gis.7.0.svn'], 'G_recreate_command'):
    G_recreate_command = _libs['grass_gis.7.0.svn'].G_recreate_command
    G_recreate_command.restype = ReturnString
    G_recreate_command.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 467
if hasattr(_libs['grass_gis.7.0.svn'], 'G_add_keyword'):
    G_add_keyword = _libs['grass_gis.7.0.svn'].G_add_keyword
    G_add_keyword.restype = None
    G_add_keyword.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 468
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_keywords'):
    G_set_keywords = _libs['grass_gis.7.0.svn'].G_set_keywords
    G_set_keywords.restype = None
    G_set_keywords.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 469
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_overwrite'):
    G_get_overwrite = _libs['grass_gis.7.0.svn'].G_get_overwrite
    G_get_overwrite.restype = c_int
    G_get_overwrite.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 472
if hasattr(_libs['grass_gis.7.0.svn'], 'G_mkdir'):
    G_mkdir = _libs['grass_gis.7.0.svn'].G_mkdir
    G_mkdir.restype = c_int
    G_mkdir.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 473
if hasattr(_libs['grass_gis.7.0.svn'], 'G_is_dirsep'):
    G_is_dirsep = _libs['grass_gis.7.0.svn'].G_is_dirsep
    G_is_dirsep.restype = c_int
    G_is_dirsep.argtypes = [c_char]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 474
if hasattr(_libs['grass_gis.7.0.svn'], 'G_is_absolute_path'):
    G_is_absolute_path = _libs['grass_gis.7.0.svn'].G_is_absolute_path
    G_is_absolute_path.restype = c_int
    G_is_absolute_path.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 475
if hasattr(_libs['grass_gis.7.0.svn'], 'G_convert_dirseps_to_host'):
    G_convert_dirseps_to_host = _libs['grass_gis.7.0.svn'].G_convert_dirseps_to_host
    G_convert_dirseps_to_host.restype = ReturnString
    G_convert_dirseps_to_host.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 476
if hasattr(_libs['grass_gis.7.0.svn'], 'G_convert_dirseps_from_host'):
    G_convert_dirseps_from_host = _libs['grass_gis.7.0.svn'].G_convert_dirseps_from_host
    G_convert_dirseps_from_host.restype = ReturnString
    G_convert_dirseps_from_host.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 477
if hasattr(_libs['grass_gis.7.0.svn'], 'G_lstat'):
    G_lstat = _libs['grass_gis.7.0.svn'].G_lstat
    G_lstat.restype = c_int
    G_lstat.argtypes = [String, POINTER(STRUCT_STAT)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 478
if hasattr(_libs['grass_gis.7.0.svn'], 'G_stat'):
    G_stat = _libs['grass_gis.7.0.svn'].G_stat
    G_stat.restype = c_int
    G_stat.argtypes = [String, POINTER(STRUCT_STAT)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 481
if hasattr(_libs['grass_gis.7.0.svn'], 'G_percent'):
    G_percent = _libs['grass_gis.7.0.svn'].G_percent
    G_percent.restype = None
    G_percent.argtypes = [c_long, c_long, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 482
if hasattr(_libs['grass_gis.7.0.svn'], 'G_percent_reset'):
    G_percent_reset = _libs['grass_gis.7.0.svn'].G_percent_reset
    G_percent_reset.restype = None
    G_percent_reset.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 483
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_percent_routine'):
    G_set_percent_routine = _libs['grass_gis.7.0.svn'].G_set_percent_routine
    G_set_percent_routine.restype = None
    G_set_percent_routine.argtypes = [CFUNCTYPE(UNCHECKED(c_int), c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 484
if hasattr(_libs['grass_gis.7.0.svn'], 'G_unset_percent_routine'):
    G_unset_percent_routine = _libs['grass_gis.7.0.svn'].G_unset_percent_routine
    G_unset_percent_routine.restype = None
    G_unset_percent_routine.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 487
if hasattr(_libs['grass_gis.7.0.svn'], 'G_popen_clear'):
    G_popen_clear = _libs['grass_gis.7.0.svn'].G_popen_clear
    G_popen_clear.restype = None
    G_popen_clear.argtypes = [POINTER(struct_Popen)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 488
if hasattr(_libs['grass_gis.7.0.svn'], 'G_popen_write'):
    G_popen_write = _libs['grass_gis.7.0.svn'].G_popen_write
    G_popen_write.restype = POINTER(FILE)
    G_popen_write.argtypes = [POINTER(struct_Popen), String, POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 489
if hasattr(_libs['grass_gis.7.0.svn'], 'G_popen_read'):
    G_popen_read = _libs['grass_gis.7.0.svn'].G_popen_read
    G_popen_read.restype = POINTER(FILE)
    G_popen_read.argtypes = [POINTER(struct_Popen), String, POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 490
if hasattr(_libs['grass_gis.7.0.svn'], 'G_popen_close'):
    G_popen_close = _libs['grass_gis.7.0.svn'].G_popen_close
    G_popen_close.restype = None
    G_popen_close.argtypes = [POINTER(struct_Popen)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 493
if hasattr(_libs['grass_gis.7.0.svn'], 'G_setup_plot'):
    G_setup_plot = _libs['grass_gis.7.0.svn'].G_setup_plot
    G_setup_plot.restype = None
    G_setup_plot.argtypes = [c_double, c_double, c_double, c_double, CFUNCTYPE(UNCHECKED(c_int), c_int, c_int), CFUNCTYPE(UNCHECKED(c_int), c_int, c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 495
if hasattr(_libs['grass_gis.7.0.svn'], 'G_setup_fill'):
    G_setup_fill = _libs['grass_gis.7.0.svn'].G_setup_fill
    G_setup_fill.restype = None
    G_setup_fill.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 496
if hasattr(_libs['grass_gis.7.0.svn'], 'G_plot_where_xy'):
    G_plot_where_xy = _libs['grass_gis.7.0.svn'].G_plot_where_xy
    G_plot_where_xy.restype = None
    G_plot_where_xy.argtypes = [c_double, c_double, POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 497
if hasattr(_libs['grass_gis.7.0.svn'], 'G_plot_where_en'):
    G_plot_where_en = _libs['grass_gis.7.0.svn'].G_plot_where_en
    G_plot_where_en.restype = None
    G_plot_where_en.argtypes = [c_int, c_int, POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 498
if hasattr(_libs['grass_gis.7.0.svn'], 'G_plot_point'):
    G_plot_point = _libs['grass_gis.7.0.svn'].G_plot_point
    G_plot_point.restype = None
    G_plot_point.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 499
if hasattr(_libs['grass_gis.7.0.svn'], 'G_plot_line'):
    G_plot_line = _libs['grass_gis.7.0.svn'].G_plot_line
    G_plot_line.restype = None
    G_plot_line.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 500
if hasattr(_libs['grass_gis.7.0.svn'], 'G_plot_line2'):
    G_plot_line2 = _libs['grass_gis.7.0.svn'].G_plot_line2
    G_plot_line2.restype = None
    G_plot_line2.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 501
if hasattr(_libs['grass_gis.7.0.svn'], 'G_plot_polygon'):
    G_plot_polygon = _libs['grass_gis.7.0.svn'].G_plot_polygon
    G_plot_polygon.restype = c_int
    G_plot_polygon.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 502
if hasattr(_libs['grass_gis.7.0.svn'], 'G_plot_area'):
    G_plot_area = _libs['grass_gis.7.0.svn'].G_plot_area
    G_plot_area.restype = c_int
    G_plot_area.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 503
if hasattr(_libs['grass_gis.7.0.svn'], 'G_plot_fx'):
    G_plot_fx = _libs['grass_gis.7.0.svn'].G_plot_fx
    G_plot_fx.restype = None
    G_plot_fx.argtypes = [CFUNCTYPE(UNCHECKED(c_double), c_double), c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 506
if hasattr(_libs['grass_gis.7.0.svn'], 'G_pole_in_polygon'):
    G_pole_in_polygon = _libs['grass_gis.7.0.svn'].G_pole_in_polygon
    G_pole_in_polygon.restype = c_int
    G_pole_in_polygon.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 509
if hasattr(_libs['grass_gis.7.0.svn'], 'G_program_name'):
    G_program_name = _libs['grass_gis.7.0.svn'].G_program_name
    G_program_name.restype = ReturnString
    G_program_name.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 510
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_program_name'):
    G_set_program_name = _libs['grass_gis.7.0.svn'].G_set_program_name
    G_set_program_name.restype = None
    G_set_program_name.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 513
if hasattr(_libs['grass_gis.7.0.svn'], 'G_projection'):
    G_projection = _libs['grass_gis.7.0.svn'].G_projection
    G_projection.restype = c_int
    G_projection.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 516
if hasattr(_libs['grass_gis.7.0.svn'], 'G__projection_units'):
    G__projection_units = _libs['grass_gis.7.0.svn'].G__projection_units
    G__projection_units.restype = c_int
    G__projection_units.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 517
if hasattr(_libs['grass_gis.7.0.svn'], 'G__projection_name'):
    G__projection_name = _libs['grass_gis.7.0.svn'].G__projection_name
    G__projection_name.restype = ReturnString
    G__projection_name.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 520
if hasattr(_libs['grass_gis.7.0.svn'], 'G_database_unit_name'):
    G_database_unit_name = _libs['grass_gis.7.0.svn'].G_database_unit_name
    G_database_unit_name.restype = ReturnString
    G_database_unit_name.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 521
if hasattr(_libs['grass_gis.7.0.svn'], 'G_database_projection_name'):
    G_database_projection_name = _libs['grass_gis.7.0.svn'].G_database_projection_name
    G_database_projection_name.restype = ReturnString
    G_database_projection_name.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 522
if hasattr(_libs['grass_gis.7.0.svn'], 'G_database_datum_name'):
    G_database_datum_name = _libs['grass_gis.7.0.svn'].G_database_datum_name
    G_database_datum_name.restype = ReturnString
    G_database_datum_name.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 523
if hasattr(_libs['grass_gis.7.0.svn'], 'G_database_ellipse_name'):
    G_database_ellipse_name = _libs['grass_gis.7.0.svn'].G_database_ellipse_name
    G_database_ellipse_name.restype = ReturnString
    G_database_ellipse_name.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 524
if hasattr(_libs['grass_gis.7.0.svn'], 'G_database_units_to_meters_factor'):
    G_database_units_to_meters_factor = _libs['grass_gis.7.0.svn'].G_database_units_to_meters_factor
    G_database_units_to_meters_factor.restype = c_double
    G_database_units_to_meters_factor.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 527
if hasattr(_libs['grass_gis.7.0.svn'], 'G_put_window'):
    G_put_window = _libs['grass_gis.7.0.svn'].G_put_window
    G_put_window.restype = c_int
    G_put_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 528
if hasattr(_libs['grass_gis.7.0.svn'], 'G__put_window'):
    G__put_window = _libs['grass_gis.7.0.svn'].G__put_window
    G__put_window.restype = c_int
    G__put_window.argtypes = [POINTER(struct_Cell_head), String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 531
if hasattr(_libs['grass_gis.7.0.svn'], 'G_putenv'):
    G_putenv = _libs['grass_gis.7.0.svn'].G_putenv
    G_putenv.restype = None
    G_putenv.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 534
if hasattr(_libs['grass_gis.7.0.svn'], 'G_meridional_radius_of_curvature'):
    G_meridional_radius_of_curvature = _libs['grass_gis.7.0.svn'].G_meridional_radius_of_curvature
    G_meridional_radius_of_curvature.restype = c_double
    G_meridional_radius_of_curvature.argtypes = [c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 535
if hasattr(_libs['grass_gis.7.0.svn'], 'G_transverse_radius_of_curvature'):
    G_transverse_radius_of_curvature = _libs['grass_gis.7.0.svn'].G_transverse_radius_of_curvature
    G_transverse_radius_of_curvature.restype = c_double
    G_transverse_radius_of_curvature.argtypes = [c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 536
if hasattr(_libs['grass_gis.7.0.svn'], 'G_radius_of_conformal_tangent_sphere'):
    G_radius_of_conformal_tangent_sphere = _libs['grass_gis.7.0.svn'].G_radius_of_conformal_tangent_sphere
    G_radius_of_conformal_tangent_sphere.restype = c_double
    G_radius_of_conformal_tangent_sphere.argtypes = [c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 539
if hasattr(_libs['grass_gis.7.0.svn'], 'G__read_Cell_head'):
    G__read_Cell_head = _libs['grass_gis.7.0.svn'].G__read_Cell_head
    G__read_Cell_head.restype = None
    G__read_Cell_head.argtypes = [POINTER(FILE), POINTER(struct_Cell_head), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 540
if hasattr(_libs['grass_gis.7.0.svn'], 'G__read_Cell_head_array'):
    G__read_Cell_head_array = _libs['grass_gis.7.0.svn'].G__read_Cell_head_array
    G__read_Cell_head_array.restype = None
    G__read_Cell_head_array.argtypes = [POINTER(POINTER(c_char)), POINTER(struct_Cell_head), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 543
if hasattr(_libs['grass_gis.7.0.svn'], 'G_remove'):
    G_remove = _libs['grass_gis.7.0.svn'].G_remove
    G_remove.restype = c_int
    G_remove.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 544
if hasattr(_libs['grass_gis.7.0.svn'], 'G_remove_misc'):
    G_remove_misc = _libs['grass_gis.7.0.svn'].G_remove_misc
    G_remove_misc.restype = c_int
    G_remove_misc.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 547
if hasattr(_libs['grass_gis.7.0.svn'], 'G_rename_file'):
    G_rename_file = _libs['grass_gis.7.0.svn'].G_rename_file
    G_rename_file.restype = c_int
    G_rename_file.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 548
if hasattr(_libs['grass_gis.7.0.svn'], 'G_rename'):
    G_rename = _libs['grass_gis.7.0.svn'].G_rename
    G_rename.restype = c_int
    G_rename.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 551
if hasattr(_libs['grass_gis.7.0.svn'], 'G_begin_rhumbline_equation'):
    G_begin_rhumbline_equation = _libs['grass_gis.7.0.svn'].G_begin_rhumbline_equation
    G_begin_rhumbline_equation.restype = c_int
    G_begin_rhumbline_equation.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 552
if hasattr(_libs['grass_gis.7.0.svn'], 'G_rhumbline_lat_from_lon'):
    G_rhumbline_lat_from_lon = _libs['grass_gis.7.0.svn'].G_rhumbline_lat_from_lon
    G_rhumbline_lat_from_lon.restype = c_double
    G_rhumbline_lat_from_lon.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 555
if hasattr(_libs['grass_gis.7.0.svn'], 'G_rotate_around_point'):
    G_rotate_around_point = _libs['grass_gis.7.0.svn'].G_rotate_around_point
    G_rotate_around_point.restype = None
    G_rotate_around_point.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 556
if hasattr(_libs['grass_gis.7.0.svn'], 'G_rotate_around_point_int'):
    G_rotate_around_point_int = _libs['grass_gis.7.0.svn'].G_rotate_around_point_int
    G_rotate_around_point_int.restype = None
    G_rotate_around_point_int.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 559
if hasattr(_libs['grass_gis.7.0.svn'], 'G_ftell'):
    G_ftell = _libs['grass_gis.7.0.svn'].G_ftell
    G_ftell.restype = off_t
    G_ftell.argtypes = [POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 560
if hasattr(_libs['grass_gis.7.0.svn'], 'G_fseek'):
    G_fseek = _libs['grass_gis.7.0.svn'].G_fseek
    G_fseek.restype = None
    G_fseek.argtypes = [POINTER(FILE), off_t, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 563
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_set_window'):
    G_get_set_window = _libs['grass_gis.7.0.svn'].G_get_set_window
    G_get_set_window.restype = None
    G_get_set_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 564
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_window'):
    G_set_window = _libs['grass_gis.7.0.svn'].G_set_window
    G_set_window.restype = None
    G_set_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 567
if hasattr(_libs['grass_gis.7.0.svn'], 'G_shortest_way'):
    G_shortest_way = _libs['grass_gis.7.0.svn'].G_shortest_way
    G_shortest_way.restype = None
    G_shortest_way.argtypes = [POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 570
if hasattr(_libs['grass_gis.7.0.svn'], 'G_sleep'):
    G_sleep = _libs['grass_gis.7.0.svn'].G_sleep
    G_sleep.restype = None
    G_sleep.argtypes = [c_uint]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 573
if hasattr(_libs['grass_gis.7.0.svn'], 'G_snprintf'):
    _func = _libs['grass_gis.7.0.svn'].G_snprintf
    _restype = c_int
    _argtypes = [String, c_size_t, String]
    G_snprintf = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 577
if hasattr(_libs['grass_gis.7.0.svn'], 'G_strcasecmp'):
    G_strcasecmp = _libs['grass_gis.7.0.svn'].G_strcasecmp
    G_strcasecmp.restype = c_int
    G_strcasecmp.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 578
if hasattr(_libs['grass_gis.7.0.svn'], 'G_store'):
    G_store = _libs['grass_gis.7.0.svn'].G_store
    G_store.restype = ReturnString
    G_store.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 579
if hasattr(_libs['grass_gis.7.0.svn'], 'G_strchg'):
    G_strchg = _libs['grass_gis.7.0.svn'].G_strchg
    G_strchg.restype = ReturnString
    G_strchg.argtypes = [String, c_char, c_char]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 580
if hasattr(_libs['grass_gis.7.0.svn'], 'G_str_replace'):
    G_str_replace = _libs['grass_gis.7.0.svn'].G_str_replace
    G_str_replace.restype = ReturnString
    G_str_replace.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 581
if hasattr(_libs['grass_gis.7.0.svn'], 'G_strip'):
    G_strip = _libs['grass_gis.7.0.svn'].G_strip
    G_strip.restype = None
    G_strip.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 582
if hasattr(_libs['grass_gis.7.0.svn'], 'G_chop'):
    G_chop = _libs['grass_gis.7.0.svn'].G_chop
    G_chop.restype = ReturnString
    G_chop.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 583
if hasattr(_libs['grass_gis.7.0.svn'], 'G_str_to_upper'):
    G_str_to_upper = _libs['grass_gis.7.0.svn'].G_str_to_upper
    G_str_to_upper.restype = None
    G_str_to_upper.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 584
if hasattr(_libs['grass_gis.7.0.svn'], 'G_str_to_lower'):
    G_str_to_lower = _libs['grass_gis.7.0.svn'].G_str_to_lower
    G_str_to_lower.restype = None
    G_str_to_lower.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 585
if hasattr(_libs['grass_gis.7.0.svn'], 'G_str_to_sql'):
    G_str_to_sql = _libs['grass_gis.7.0.svn'].G_str_to_sql
    G_str_to_sql.restype = c_int
    G_str_to_sql.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 586
if hasattr(_libs['grass_gis.7.0.svn'], 'G_squeeze'):
    G_squeeze = _libs['grass_gis.7.0.svn'].G_squeeze
    G_squeeze.restype = ReturnString
    G_squeeze.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 589
if hasattr(_libs['grass_gis.7.0.svn'], 'G_init_tempfile'):
    G_init_tempfile = _libs['grass_gis.7.0.svn'].G_init_tempfile
    G_init_tempfile.restype = None
    G_init_tempfile.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 590
if hasattr(_libs['grass_gis.7.0.svn'], 'G_tempfile'):
    G_tempfile = _libs['grass_gis.7.0.svn'].G_tempfile
    G_tempfile.restype = ReturnString
    G_tempfile.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 591
if hasattr(_libs['grass_gis.7.0.svn'], 'G__tempfile'):
    G__tempfile = _libs['grass_gis.7.0.svn'].G__tempfile
    G__tempfile.restype = ReturnString
    G__tempfile.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 592
if hasattr(_libs['grass_gis.7.0.svn'], 'G__temp_element'):
    G__temp_element = _libs['grass_gis.7.0.svn'].G__temp_element
    G__temp_element.restype = None
    G__temp_element.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 595
if hasattr(_libs['grass_gis.7.0.svn'], 'G_init_timestamp'):
    G_init_timestamp = _libs['grass_gis.7.0.svn'].G_init_timestamp
    G_init_timestamp.restype = None
    G_init_timestamp.argtypes = [POINTER(struct_TimeStamp)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 596
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_timestamp'):
    G_set_timestamp = _libs['grass_gis.7.0.svn'].G_set_timestamp
    G_set_timestamp.restype = None
    G_set_timestamp.argtypes = [POINTER(struct_TimeStamp), POINTER(struct_DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 597
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_timestamp_range'):
    G_set_timestamp_range = _libs['grass_gis.7.0.svn'].G_set_timestamp_range
    G_set_timestamp_range.restype = None
    G_set_timestamp_range.argtypes = [POINTER(struct_TimeStamp), POINTER(struct_DateTime), POINTER(struct_DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 599
if hasattr(_libs['grass_gis.7.0.svn'], 'G__read_timestamp'):
    G__read_timestamp = _libs['grass_gis.7.0.svn'].G__read_timestamp
    G__read_timestamp.restype = c_int
    G__read_timestamp.argtypes = [POINTER(FILE), POINTER(struct_TimeStamp)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 600
if hasattr(_libs['grass_gis.7.0.svn'], 'G__write_timestamp'):
    G__write_timestamp = _libs['grass_gis.7.0.svn'].G__write_timestamp
    G__write_timestamp.restype = c_int
    G__write_timestamp.argtypes = [POINTER(FILE), POINTER(struct_TimeStamp)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 601
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_timestamps'):
    G_get_timestamps = _libs['grass_gis.7.0.svn'].G_get_timestamps
    G_get_timestamps.restype = None
    G_get_timestamps.argtypes = [POINTER(struct_TimeStamp), POINTER(struct_DateTime), POINTER(struct_DateTime), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 602
if hasattr(_libs['grass_gis.7.0.svn'], 'G_read_raster_timestamp'):
    G_read_raster_timestamp = _libs['grass_gis.7.0.svn'].G_read_raster_timestamp
    G_read_raster_timestamp.restype = c_int
    G_read_raster_timestamp.argtypes = [String, String, POINTER(struct_TimeStamp)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 603
if hasattr(_libs['grass_gis.7.0.svn'], 'G_read_vector_timestamp'):
    G_read_vector_timestamp = _libs['grass_gis.7.0.svn'].G_read_vector_timestamp
    G_read_vector_timestamp.restype = c_int
    G_read_vector_timestamp.argtypes = [String, String, POINTER(struct_TimeStamp)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 604
if hasattr(_libs['grass_gis.7.0.svn'], 'G_write_raster_timestamp'):
    G_write_raster_timestamp = _libs['grass_gis.7.0.svn'].G_write_raster_timestamp
    G_write_raster_timestamp.restype = c_int
    G_write_raster_timestamp.argtypes = [String, POINTER(struct_TimeStamp)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 605
if hasattr(_libs['grass_gis.7.0.svn'], 'G_write_vector_timestamp'):
    G_write_vector_timestamp = _libs['grass_gis.7.0.svn'].G_write_vector_timestamp
    G_write_vector_timestamp.restype = c_int
    G_write_vector_timestamp.argtypes = [String, POINTER(struct_TimeStamp)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 606
if hasattr(_libs['grass_gis.7.0.svn'], 'G_format_timestamp'):
    G_format_timestamp = _libs['grass_gis.7.0.svn'].G_format_timestamp
    G_format_timestamp.restype = c_int
    G_format_timestamp.argtypes = [POINTER(struct_TimeStamp), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 607
if hasattr(_libs['grass_gis.7.0.svn'], 'G_scan_timestamp'):
    G_scan_timestamp = _libs['grass_gis.7.0.svn'].G_scan_timestamp
    G_scan_timestamp.restype = c_int
    G_scan_timestamp.argtypes = [POINTER(struct_TimeStamp), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 608
if hasattr(_libs['grass_gis.7.0.svn'], 'G_remove_raster_timestamp'):
    G_remove_raster_timestamp = _libs['grass_gis.7.0.svn'].G_remove_raster_timestamp
    G_remove_raster_timestamp.restype = c_int
    G_remove_raster_timestamp.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 609
if hasattr(_libs['grass_gis.7.0.svn'], 'G_remove_vector_timestamp'):
    G_remove_vector_timestamp = _libs['grass_gis.7.0.svn'].G_remove_vector_timestamp
    G_remove_vector_timestamp.restype = c_int
    G_remove_vector_timestamp.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 610
if hasattr(_libs['grass_gis.7.0.svn'], 'G_read_grid3_timestamp'):
    G_read_grid3_timestamp = _libs['grass_gis.7.0.svn'].G_read_grid3_timestamp
    G_read_grid3_timestamp.restype = c_int
    G_read_grid3_timestamp.argtypes = [String, String, POINTER(struct_TimeStamp)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 611
if hasattr(_libs['grass_gis.7.0.svn'], 'G_remove_grid3_timestamp'):
    G_remove_grid3_timestamp = _libs['grass_gis.7.0.svn'].G_remove_grid3_timestamp
    G_remove_grid3_timestamp.restype = c_int
    G_remove_grid3_timestamp.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 612
if hasattr(_libs['grass_gis.7.0.svn'], 'G_write_grid3_timestamp'):
    G_write_grid3_timestamp = _libs['grass_gis.7.0.svn'].G_write_grid3_timestamp
    G_write_grid3_timestamp.restype = c_int
    G_write_grid3_timestamp.argtypes = [String, POINTER(struct_TimeStamp)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 615
if hasattr(_libs['grass_gis.7.0.svn'], 'G_tokenize'):
    G_tokenize = _libs['grass_gis.7.0.svn'].G_tokenize
    G_tokenize.restype = POINTER(POINTER(c_char))
    G_tokenize.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 616
if hasattr(_libs['grass_gis.7.0.svn'], 'G_number_of_tokens'):
    G_number_of_tokens = _libs['grass_gis.7.0.svn'].G_number_of_tokens
    G_number_of_tokens.restype = c_int
    G_number_of_tokens.argtypes = [POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 617
if hasattr(_libs['grass_gis.7.0.svn'], 'G_free_tokens'):
    G_free_tokens = _libs['grass_gis.7.0.svn'].G_free_tokens
    G_free_tokens.restype = None
    G_free_tokens.argtypes = [POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 620
if hasattr(_libs['grass_gis.7.0.svn'], 'G_trim_decimal'):
    G_trim_decimal = _libs['grass_gis.7.0.svn'].G_trim_decimal
    G_trim_decimal.restype = None
    G_trim_decimal.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 623
if hasattr(_libs['grass_gis.7.0.svn'], 'G_units_to_meters_factor'):
    G_units_to_meters_factor = _libs['grass_gis.7.0.svn'].G_units_to_meters_factor
    G_units_to_meters_factor.restype = c_double
    G_units_to_meters_factor.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 624
if hasattr(_libs['grass_gis.7.0.svn'], 'G_units_to_meters_factor_sq'):
    G_units_to_meters_factor_sq = _libs['grass_gis.7.0.svn'].G_units_to_meters_factor_sq
    G_units_to_meters_factor_sq.restype = c_double
    G_units_to_meters_factor_sq.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 625
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_units_name'):
    G_get_units_name = _libs['grass_gis.7.0.svn'].G_get_units_name
    G_get_units_name.restype = ReturnString
    G_get_units_name.argtypes = [c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 626
if hasattr(_libs['grass_gis.7.0.svn'], 'G_units'):
    G_units = _libs['grass_gis.7.0.svn'].G_units
    G_units.restype = c_int
    G_units.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 630
if hasattr(_libs['grass_gis.7.0.svn'], 'G_rc_path'):
    G_rc_path = _libs['grass_gis.7.0.svn'].G_rc_path
    G_rc_path.restype = ReturnString
    G_rc_path.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 634
if hasattr(_libs['grass_gis.7.0.svn'], 'G_verbose'):
    G_verbose = _libs['grass_gis.7.0.svn'].G_verbose
    G_verbose.restype = c_int
    G_verbose.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 635
if hasattr(_libs['grass_gis.7.0.svn'], 'G_verbose_min'):
    G_verbose_min = _libs['grass_gis.7.0.svn'].G_verbose_min
    G_verbose_min.restype = c_int
    G_verbose_min.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 636
if hasattr(_libs['grass_gis.7.0.svn'], 'G_verbose_std'):
    G_verbose_std = _libs['grass_gis.7.0.svn'].G_verbose_std
    G_verbose_std.restype = c_int
    G_verbose_std.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 637
if hasattr(_libs['grass_gis.7.0.svn'], 'G_verbose_max'):
    G_verbose_max = _libs['grass_gis.7.0.svn'].G_verbose_max
    G_verbose_max.restype = c_int
    G_verbose_max.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 638
if hasattr(_libs['grass_gis.7.0.svn'], 'G_set_verbose'):
    G_set_verbose = _libs['grass_gis.7.0.svn'].G_set_verbose
    G_set_verbose.restype = c_int
    G_set_verbose.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 641
if hasattr(_libs['grass_gis.7.0.svn'], 'G_3dview_warning'):
    G_3dview_warning = _libs['grass_gis.7.0.svn'].G_3dview_warning
    G_3dview_warning.restype = None
    G_3dview_warning.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 642
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_3dview_defaults'):
    G_get_3dview_defaults = _libs['grass_gis.7.0.svn'].G_get_3dview_defaults
    G_get_3dview_defaults.restype = c_int
    G_get_3dview_defaults.argtypes = [POINTER(struct_G_3dview), POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 643
if hasattr(_libs['grass_gis.7.0.svn'], 'G_put_3dview'):
    G_put_3dview = _libs['grass_gis.7.0.svn'].G_put_3dview
    G_put_3dview.restype = c_int
    G_put_3dview.argtypes = [String, String, POINTER(struct_G_3dview), POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 645
if hasattr(_libs['grass_gis.7.0.svn'], 'G_get_3dview'):
    G_get_3dview = _libs['grass_gis.7.0.svn'].G_get_3dview
    G_get_3dview.restype = c_int
    G_get_3dview.argtypes = [String, String, POINTER(struct_G_3dview)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 648
if hasattr(_libs['grass_gis.7.0.svn'], 'G_whoami'):
    G_whoami = _libs['grass_gis.7.0.svn'].G_whoami
    G_whoami.restype = ReturnString
    G_whoami.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 651
if hasattr(_libs['grass_gis.7.0.svn'], 'G_adjust_window_to_box'):
    G_adjust_window_to_box = _libs['grass_gis.7.0.svn'].G_adjust_window_to_box
    G_adjust_window_to_box.restype = None
    G_adjust_window_to_box.argtypes = [POINTER(struct_Cell_head), POINTER(struct_Cell_head), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 655
if hasattr(_libs['grass_gis.7.0.svn'], 'G_format_northing'):
    G_format_northing = _libs['grass_gis.7.0.svn'].G_format_northing
    G_format_northing.restype = None
    G_format_northing.argtypes = [c_double, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 656
if hasattr(_libs['grass_gis.7.0.svn'], 'G_format_easting'):
    G_format_easting = _libs['grass_gis.7.0.svn'].G_format_easting
    G_format_easting.restype = None
    G_format_easting.argtypes = [c_double, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 657
if hasattr(_libs['grass_gis.7.0.svn'], 'G_format_resolution'):
    G_format_resolution = _libs['grass_gis.7.0.svn'].G_format_resolution
    G_format_resolution.restype = None
    G_format_resolution.argtypes = [c_double, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 660
if hasattr(_libs['grass_gis.7.0.svn'], 'G_point_in_region'):
    G_point_in_region = _libs['grass_gis.7.0.svn'].G_point_in_region
    G_point_in_region.restype = c_int
    G_point_in_region.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 661
if hasattr(_libs['grass_gis.7.0.svn'], 'G_point_in_window'):
    G_point_in_window = _libs['grass_gis.7.0.svn'].G_point_in_window
    G_point_in_window.restype = c_int
    G_point_in_window.argtypes = [c_double, c_double, POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 664
if hasattr(_libs['grass_gis.7.0.svn'], 'G_limit_east'):
    G_limit_east = _libs['grass_gis.7.0.svn'].G_limit_east
    G_limit_east.restype = c_int
    G_limit_east.argtypes = [POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 665
if hasattr(_libs['grass_gis.7.0.svn'], 'G_limit_west'):
    G_limit_west = _libs['grass_gis.7.0.svn'].G_limit_west
    G_limit_west.restype = c_int
    G_limit_west.argtypes = [POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 666
if hasattr(_libs['grass_gis.7.0.svn'], 'G_limit_north'):
    G_limit_north = _libs['grass_gis.7.0.svn'].G_limit_north
    G_limit_north.restype = c_int
    G_limit_north.argtypes = [POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 667
if hasattr(_libs['grass_gis.7.0.svn'], 'G_limit_south'):
    G_limit_south = _libs['grass_gis.7.0.svn'].G_limit_south
    G_limit_south.restype = c_int
    G_limit_south.argtypes = [POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 670
if hasattr(_libs['grass_gis.7.0.svn'], 'G_window_overlap'):
    G_window_overlap = _libs['grass_gis.7.0.svn'].G_window_overlap
    G_window_overlap.restype = c_int
    G_window_overlap.argtypes = [POINTER(struct_Cell_head), c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 672
if hasattr(_libs['grass_gis.7.0.svn'], 'G_window_percentage_overlap'):
    G_window_percentage_overlap = _libs['grass_gis.7.0.svn'].G_window_percentage_overlap
    G_window_percentage_overlap.restype = c_double
    G_window_percentage_overlap.argtypes = [POINTER(struct_Cell_head), c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 676
if hasattr(_libs['grass_gis.7.0.svn'], 'G_scan_northing'):
    G_scan_northing = _libs['grass_gis.7.0.svn'].G_scan_northing
    G_scan_northing.restype = c_int
    G_scan_northing.argtypes = [String, POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 677
if hasattr(_libs['grass_gis.7.0.svn'], 'G_scan_easting'):
    G_scan_easting = _libs['grass_gis.7.0.svn'].G_scan_easting
    G_scan_easting.restype = c_int
    G_scan_easting.argtypes = [String, POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 678
if hasattr(_libs['grass_gis.7.0.svn'], 'G_scan_resolution'):
    G_scan_resolution = _libs['grass_gis.7.0.svn'].G_scan_resolution
    G_scan_resolution.restype = c_int
    G_scan_resolution.argtypes = [String, POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 681
if hasattr(_libs['grass_gis.7.0.svn'], 'G_adjust_east_longitude'):
    G_adjust_east_longitude = _libs['grass_gis.7.0.svn'].G_adjust_east_longitude
    G_adjust_east_longitude.restype = c_double
    G_adjust_east_longitude.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 682
if hasattr(_libs['grass_gis.7.0.svn'], 'G_adjust_easting'):
    G_adjust_easting = _libs['grass_gis.7.0.svn'].G_adjust_easting
    G_adjust_easting.restype = c_double
    G_adjust_easting.argtypes = [c_double, POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 683
if hasattr(_libs['grass_gis.7.0.svn'], 'G__init_window'):
    G__init_window = _libs['grass_gis.7.0.svn'].G__init_window
    G__init_window.restype = None
    G__init_window.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 686
if hasattr(_libs['grass_gis.7.0.svn'], 'G_begin_execute'):
    G_begin_execute = _libs['grass_gis.7.0.svn'].G_begin_execute
    G_begin_execute.restype = None
    G_begin_execute.argtypes = [CFUNCTYPE(UNCHECKED(None), POINTER(None)), POINTER(None), POINTER(POINTER(None)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 687
if hasattr(_libs['grass_gis.7.0.svn'], 'G_end_execute'):
    G_end_execute = _libs['grass_gis.7.0.svn'].G_end_execute
    G_end_execute.restype = None
    G_end_execute.argtypes = [POINTER(POINTER(None))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 688
if hasattr(_libs['grass_gis.7.0.svn'], 'G_init_workers'):
    G_init_workers = _libs['grass_gis.7.0.svn'].G_init_workers
    G_init_workers.restype = None
    G_init_workers.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 689
if hasattr(_libs['grass_gis.7.0.svn'], 'G_finish_workers'):
    G_finish_workers = _libs['grass_gis.7.0.svn'].G_finish_workers
    G_finish_workers.restype = None
    G_finish_workers.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 692
if hasattr(_libs['grass_gis.7.0.svn'], 'G__write_Cell_head'):
    G__write_Cell_head = _libs['grass_gis.7.0.svn'].G__write_Cell_head
    G__write_Cell_head.restype = None
    G__write_Cell_head.argtypes = [POINTER(FILE), POINTER(struct_Cell_head), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 693
if hasattr(_libs['grass_gis.7.0.svn'], 'G__write_Cell_head3'):
    G__write_Cell_head3 = _libs['grass_gis.7.0.svn'].G__write_Cell_head3
    G__write_Cell_head3.restype = None
    G__write_Cell_head3.argtypes = [POINTER(FILE), POINTER(struct_Cell_head), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 696
if hasattr(_libs['grass_gis.7.0.svn'], 'G_write_zeros'):
    G_write_zeros = _libs['grass_gis.7.0.svn'].G_write_zeros
    G_write_zeros.restype = None
    G_write_zeros.argtypes = [c_int, c_size_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 699
if hasattr(_libs['grass_gis.7.0.svn'], 'G_zero'):
    G_zero = _libs['grass_gis.7.0.svn'].G_zero
    G_zero.restype = None
    G_zero.argtypes = [POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 702
if hasattr(_libs['grass_gis.7.0.svn'], 'G_zone'):
    G_zone = _libs['grass_gis.7.0.svn'].G_zone
    G_zone.restype = c_int
    G_zone.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 40
try:
    GIS_H_VERSION = '$Revision: 45093 $'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 40
try:
    GIS_H_DATE = '$Date: 2011-01-20 13:10:50 +0100 (Thu, 20 Jan 2011) $'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 41
def G_gisinit(pgm):
    return (G__gisinit (GIS_H_VERSION, pgm))

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 41
try:
    G_no_gisinit = (G__no_gisinit (GIS_H_VERSION))
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 44
try:
    TRUE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 47
try:
    FALSE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 50
try:
    PRI_OFF_T = 'lld'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 54
try:
    NEWLINE = '\\n'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 58
try:
    U_UNKNOWN = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 58
try:
    U_ACRES = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 58
try:
    U_HECTARES = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 58
try:
    U_KILOMETERS = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 58
try:
    U_METERS = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 58
try:
    U_MILES = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 58
try:
    U_FEET = 6
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 58
try:
    U_RADIANS = 7
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 58
try:
    U_DEGREES = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 59
try:
    PROJECTION_XY = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 59
try:
    PROJECTION_UTM = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 59
try:
    PROJECTION_SP = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 59
try:
    PROJECTION_LL = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 59
try:
    PROJECTION_OTHER = 99
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 60
try:
    PROJECTION_FILE = 'PROJ_INFO'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 60
try:
    UNIT_FILE = 'PROJ_UNITS'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 61
try:
    CONFIG_DIR = '.grass7'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 64
try:
    M_PI = 3.1415926535897931
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 66
try:
    M_PI_2 = 1.5707963267948966
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 68
try:
    M_PI_4 = 0.78539816339744828
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 70
try:
    GRASS_EPSILON = 1.0000000000000001e-15
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 72
try:
    G_VAR_GISRC = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 72
try:
    G_VAR_MAPSET = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 74
try:
    G_GISRC_MODE_FILE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 74
try:
    G_GISRC_MODE_MEMORY = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 76
try:
    TYPE_INTEGER = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 76
try:
    TYPE_DOUBLE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 76
try:
    TYPE_STRING = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 76
try:
    YES = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 76
try:
    NO = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 78
try:
    GNAME_MAX = 256
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 78
try:
    GMAPSET_MAX = 256
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 79
try:
    GPATH_MAX = 4096
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 92
def deserialize_int32_le(buf):
    return (((((buf [0]) << 0) | ((buf [1]) << 8)) | ((buf [2]) << 16)) | ((buf [3]) << 24))

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 104
def deserialize_int32_be(buf):
    return (((((buf [0]) << 24) | ((buf [1]) << 16)) | ((buf [2]) << 8)) | ((buf [3]) << 0))

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 109
try:
    GRASS_DIRSEP = '/'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 113
try:
    HOST_DIRSEP = '/'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 113
try:
    G_DEV_NULL = '/dev/null'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 170
try:
    G_INFO_FORMAT_STANDARD = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 170
try:
    G_INFO_FORMAT_GUI = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 170
try:
    G_INFO_FORMAT_SILENT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 170
try:
    G_INFO_FORMAT_PLAIN = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 172
try:
    G_ICON_CROSS = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 172
try:
    G_ICON_BOX = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 172
try:
    G_ICON_ARROW = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 174
try:
    DEFAULT_FG_COLOR = 'black'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 174
try:
    DEFAULT_BG_COLOR = 'white'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 176
try:
    GR_FATAL_EXIT = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 176
try:
    GR_FATAL_PRINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 176
try:
    GR_FATAL_RETURN = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 45
def G__alloca(n):
    return (G_malloc (n))

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 45
def G__freea(p):
    return (G_free (p))

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 58
def G_incr_void_ptr(ptr, size):
    return (ptr + size)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 74
def G_malloc(n):
    return (G__malloc ('<ctypesgen>', 0, n))

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 74
def G_calloc(m, n):
    return (G__calloc ('<ctypesgen>', 0, m, n))

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gisdefs.h: 74
def G_realloc(p, n):
    return (G__realloc ('<ctypesgen>', 0, p, n))

Cell_head = struct_Cell_head # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 257

G_3dview = struct_G_3dview # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 284

Key_Value = struct_Key_Value # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 311

Option = struct_Option # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 319

Flag = struct_Flag # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 350

GModule = struct_GModule # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 361

TimeStamp = struct_TimeStamp # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 371

Counter = struct_Counter # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 377

Popen = struct_Popen # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 381

# No inserted files

