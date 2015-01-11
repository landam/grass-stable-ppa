'''Wrapper for dbmi.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_dbmiclient.7.0.svn -lgrass_dbmibase.7.0.svn /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h -o dbmi.py

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

_libs["grass_dbmiclient.7.0.svn"] = load_library("grass_dbmiclient.7.0.svn")
_libs["grass_dbmibase.7.0.svn"] = load_library("grass_dbmibase.7.0.svn")

# 2 libraries
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

dbAddress = POINTER(None) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 140

dbToken = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 141

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 147
class struct__db_string(Structure):
    pass

struct__db_string.__slots__ = [
    'string',
    'nalloc',
]
struct__db_string._fields_ = [
    ('string', String),
    ('nalloc', c_int),
]

dbString = struct__db_string # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 147

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 149
class struct__dbmscap(Structure):
    pass

struct__dbmscap.__slots__ = [
    'driverName',
    'startup',
    'comment',
    'next',
]
struct__dbmscap._fields_ = [
    ('driverName', c_char * 256),
    ('startup', c_char * 256),
    ('comment', c_char * 256),
    ('next', POINTER(struct__dbmscap)),
]

dbDbmscap = struct__dbmscap # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 155

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 162
class struct__db_dirent(Structure):
    pass

struct__db_dirent.__slots__ = [
    'name',
    'isdir',
    'perm',
]
struct__db_dirent._fields_ = [
    ('name', dbString),
    ('isdir', c_int),
    ('perm', c_int),
]

dbDirent = struct__db_dirent # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 162

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 169
class struct__db_driver(Structure):
    pass

struct__db_driver.__slots__ = [
    'dbmscap',
    'send',
    'recv',
    'pid',
]
struct__db_driver._fields_ = [
    ('dbmscap', dbDbmscap),
    ('send', POINTER(FILE)),
    ('recv', POINTER(FILE)),
    ('pid', c_int),
]

dbDriver = struct__db_driver # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 169

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 176
class struct__db_handle(Structure):
    pass

struct__db_handle.__slots__ = [
    'dbName',
    'dbSchema',
]
struct__db_handle._fields_ = [
    ('dbName', dbString),
    ('dbSchema', dbString),
]

dbHandle = struct__db_handle # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 176

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 187
class struct__db_date_time(Structure):
    pass

struct__db_date_time.__slots__ = [
    'current',
    'year',
    'month',
    'day',
    'hour',
    'minute',
    'seconds',
]
struct__db_date_time._fields_ = [
    ('current', c_char),
    ('year', c_int),
    ('month', c_int),
    ('day', c_int),
    ('hour', c_int),
    ('minute', c_int),
    ('seconds', c_double),
]

dbDateTime = struct__db_date_time # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 187

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 196
class struct__db_value(Structure):
    pass

struct__db_value.__slots__ = [
    'isNull',
    'i',
    'd',
    's',
    't',
]
struct__db_value._fields_ = [
    ('isNull', c_char),
    ('i', c_int),
    ('d', c_double),
    ('s', dbString),
    ('t', dbDateTime),
]

dbValue = struct__db_value # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 196

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 214
class struct__db_column(Structure):
    pass

struct__db_column.__slots__ = [
    'columnName',
    'description',
    'sqlDataType',
    'hostDataType',
    'value',
    'dataLen',
    'precision',
    'scale',
    'nullAllowed',
    'hasDefaultValue',
    'useDefaultValue',
    'defaultValue',
    'select',
    'update',
]
struct__db_column._fields_ = [
    ('columnName', dbString),
    ('description', dbString),
    ('sqlDataType', c_int),
    ('hostDataType', c_int),
    ('value', dbValue),
    ('dataLen', c_int),
    ('precision', c_int),
    ('scale', c_int),
    ('nullAllowed', c_char),
    ('hasDefaultValue', c_char),
    ('useDefaultValue', c_char),
    ('defaultValue', dbValue),
    ('select', c_int),
    ('update', c_int),
]

dbColumn = struct__db_column # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 214

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 224
class struct__db_table(Structure):
    pass

struct__db_table.__slots__ = [
    'tableName',
    'description',
    'numColumns',
    'columns',
    'priv_insert',
    'priv_delete',
]
struct__db_table._fields_ = [
    ('tableName', dbString),
    ('description', dbString),
    ('numColumns', c_int),
    ('columns', POINTER(dbColumn)),
    ('priv_insert', c_int),
    ('priv_delete', c_int),
]

dbTable = struct__db_table # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 224

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 234
class struct__db_cursor(Structure):
    pass

struct__db_cursor.__slots__ = [
    'token',
    'driver',
    'table',
    'column_flags',
    'type',
    'mode',
]
struct__db_cursor._fields_ = [
    ('token', dbToken),
    ('driver', POINTER(dbDriver)),
    ('table', POINTER(dbTable)),
    ('column_flags', POINTER(c_short)),
    ('type', c_int),
    ('mode', c_int),
]

dbCursor = struct__db_cursor # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 234

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 243
class struct__db_index(Structure):
    pass

struct__db_index.__slots__ = [
    'indexName',
    'tableName',
    'numColumns',
    'columnNames',
    'unique',
]
struct__db_index._fields_ = [
    ('indexName', dbString),
    ('tableName', dbString),
    ('numColumns', c_int),
    ('columnNames', POINTER(dbString)),
    ('unique', c_char),
]

dbIndex = struct__db_index # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 243

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 252
class struct__db_driver_state(Structure):
    pass

struct__db_driver_state.__slots__ = [
    'dbname',
    'dbschema',
    'open',
    'ncursors',
    'cursor_list',
]
struct__db_driver_state._fields_ = [
    ('dbname', String),
    ('dbschema', String),
    ('open', c_int),
    ('ncursors', c_int),
    ('cursor_list', POINTER(POINTER(dbCursor))),
]

dbDriverState = struct__db_driver_state # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 252

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 259
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'cat',
    'val',
]
struct_anon_23._fields_ = [
    ('cat', c_int),
    ('val', c_int),
]

dbCatValI = struct_anon_23 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 259

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 266
class union_anon_24(Union):
    pass

union_anon_24.__slots__ = [
    'i',
    'd',
    's',
    't',
]
union_anon_24._fields_ = [
    ('i', c_int),
    ('d', c_double),
    ('s', POINTER(dbString)),
    ('t', POINTER(dbDateTime)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 277
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'cat',
    'isNull',
    'val',
]
struct_anon_25._fields_ = [
    ('cat', c_int),
    ('isNull', c_int),
    ('val', union_anon_24),
]

dbCatVal = struct_anon_25 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 277

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 286
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'n_values',
    'alloc',
    'ctype',
    'value',
]
struct_anon_26._fields_ = [
    ('n_values', c_int),
    ('alloc', c_int),
    ('ctype', c_int),
    ('value', POINTER(dbCatVal)),
]

dbCatValArray = struct_anon_26 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 286

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 300
class struct__db_connection(Structure):
    pass

struct__db_connection.__slots__ = [
    'driverName',
    'databaseName',
    'schemaName',
    'location',
    'user',
    'password',
    'keycol',
    'group',
]
struct__db_connection._fields_ = [
    ('driverName', String),
    ('databaseName', String),
    ('schemaName', String),
    ('location', String),
    ('user', String),
    ('password', String),
    ('keycol', String),
    ('group', String),
]

dbConnection = struct__db_connection # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 300

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 312
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'count',
    'alloc',
    'table',
    'key',
    'cat',
    'where',
    'label',
]
struct_anon_27._fields_ = [
    ('count', c_int),
    ('alloc', c_int),
    ('table', String),
    ('key', String),
    ('cat', POINTER(c_int)),
    ('where', POINTER(POINTER(c_char))),
    ('label', POINTER(POINTER(c_char))),
]

dbRclsRule = struct_anon_27 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 312

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 4
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_Cstring_to_lowercase'):
    db_Cstring_to_lowercase = _libs['grass_dbmiclient.7.0.svn'].db_Cstring_to_lowercase
    db_Cstring_to_lowercase.restype = None
    db_Cstring_to_lowercase.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 5
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_Cstring_to_uppercase'):
    db_Cstring_to_uppercase = _libs['grass_dbmiclient.7.0.svn'].db_Cstring_to_uppercase
    db_Cstring_to_uppercase.restype = None
    db_Cstring_to_uppercase.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 6
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_add_column'):
    db_add_column = _libs['grass_dbmiclient.7.0.svn'].db_add_column
    db_add_column.restype = c_int
    db_add_column.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 7
for _lib in _libs.values():
    if hasattr(_lib, 'db__add_cursor_to_driver_state'):
        db__add_cursor_to_driver_state = _lib.db__add_cursor_to_driver_state
        db__add_cursor_to_driver_state.restype = None
        db__add_cursor_to_driver_state.argtypes = [POINTER(dbCursor)]
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 8
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_alloc_cursor_column_flags'):
    db_alloc_cursor_column_flags = _libs['grass_dbmiclient.7.0.svn'].db_alloc_cursor_column_flags
    db_alloc_cursor_column_flags.restype = c_int
    db_alloc_cursor_column_flags.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 9
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_alloc_cursor_table'):
    db_alloc_cursor_table = _libs['grass_dbmiclient.7.0.svn'].db_alloc_cursor_table
    db_alloc_cursor_table.restype = c_int
    db_alloc_cursor_table.argtypes = [POINTER(dbCursor), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 10
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_append_table_column'):
    db_append_table_column = _libs['grass_dbmiclient.7.0.svn'].db_append_table_column
    db_append_table_column.restype = c_int
    db_append_table_column.argtypes = [POINTER(dbTable), POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 11
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_alloc_dirent_array'):
    db_alloc_dirent_array = _libs['grass_dbmiclient.7.0.svn'].db_alloc_dirent_array
    db_alloc_dirent_array.restype = POINTER(dbDirent)
    db_alloc_dirent_array.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 12
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_alloc_handle_array'):
    db_alloc_handle_array = _libs['grass_dbmiclient.7.0.svn'].db_alloc_handle_array
    db_alloc_handle_array.restype = POINTER(dbHandle)
    db_alloc_handle_array.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 13
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_alloc_index_array'):
    db_alloc_index_array = _libs['grass_dbmiclient.7.0.svn'].db_alloc_index_array
    db_alloc_index_array.restype = POINTER(dbIndex)
    db_alloc_index_array.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 14
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_alloc_index_columns'):
    db_alloc_index_columns = _libs['grass_dbmiclient.7.0.svn'].db_alloc_index_columns
    db_alloc_index_columns.restype = c_int
    db_alloc_index_columns.argtypes = [POINTER(dbIndex), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 15
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_alloc_string_array'):
    db_alloc_string_array = _libs['grass_dbmiclient.7.0.svn'].db_alloc_string_array
    db_alloc_string_array.restype = POINTER(dbString)
    db_alloc_string_array.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 16
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_alloc_table'):
    db_alloc_table = _libs['grass_dbmiclient.7.0.svn'].db_alloc_table
    db_alloc_table.restype = POINTER(dbTable)
    db_alloc_table.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 17
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_append_string'):
    db_append_string = _libs['grass_dbmiclient.7.0.svn'].db_append_string
    db_append_string.restype = c_int
    db_append_string.argtypes = [POINTER(dbString), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 18
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_auto_print_errors'):
    db_auto_print_errors = _libs['grass_dbmiclient.7.0.svn'].db_auto_print_errors
    db_auto_print_errors.restype = None
    db_auto_print_errors.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 19
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_auto_print_protocol_errors'):
    db_auto_print_protocol_errors = _libs['grass_dbmiclient.7.0.svn'].db_auto_print_protocol_errors
    db_auto_print_protocol_errors.restype = None
    db_auto_print_protocol_errors.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 20
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_bind_update'):
    db_bind_update = _libs['grass_dbmiclient.7.0.svn'].db_bind_update
    db_bind_update.restype = c_int
    db_bind_update.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 21
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_calloc'):
    db_calloc = _libs['grass_dbmiclient.7.0.svn'].db_calloc
    db_calloc.restype = POINTER(None)
    db_calloc.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 22
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_CatValArray_alloc'):
    db_CatValArray_alloc = _libs['grass_dbmiclient.7.0.svn'].db_CatValArray_alloc
    db_CatValArray_alloc.restype = c_int
    db_CatValArray_alloc.argtypes = [POINTER(dbCatValArray), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 23
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_CatValArray_realloc'):
    db_CatValArray_realloc = _libs['grass_dbmiclient.7.0.svn'].db_CatValArray_realloc
    db_CatValArray_realloc.restype = c_int
    db_CatValArray_realloc.argtypes = [POINTER(dbCatValArray), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 24
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_CatValArray_free'):
    db_CatValArray_free = _libs['grass_dbmiclient.7.0.svn'].db_CatValArray_free
    db_CatValArray_free.restype = None
    db_CatValArray_free.argtypes = [POINTER(dbCatValArray)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 25
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_CatValArray_init'):
    db_CatValArray_init = _libs['grass_dbmiclient.7.0.svn'].db_CatValArray_init
    db_CatValArray_init.restype = None
    db_CatValArray_init.argtypes = [POINTER(dbCatValArray)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 26
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_CatValArray_sort'):
    db_CatValArray_sort = _libs['grass_dbmiclient.7.0.svn'].db_CatValArray_sort
    db_CatValArray_sort.restype = None
    db_CatValArray_sort.argtypes = [POINTER(dbCatValArray)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 27
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_CatValArray_sort_by_value'):
    db_CatValArray_sort_by_value = _libs['grass_dbmiclient.7.0.svn'].db_CatValArray_sort_by_value
    db_CatValArray_sort_by_value.restype = c_int
    db_CatValArray_sort_by_value.argtypes = [POINTER(dbCatValArray)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 28
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_CatValArray_get_value'):
    db_CatValArray_get_value = _libs['grass_dbmiclient.7.0.svn'].db_CatValArray_get_value
    db_CatValArray_get_value.restype = c_int
    db_CatValArray_get_value.argtypes = [POINTER(dbCatValArray), c_int, POINTER(POINTER(dbCatVal))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 29
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_CatValArray_get_value_int'):
    db_CatValArray_get_value_int = _libs['grass_dbmiclient.7.0.svn'].db_CatValArray_get_value_int
    db_CatValArray_get_value_int.restype = c_int
    db_CatValArray_get_value_int.argtypes = [POINTER(dbCatValArray), c_int, POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 30
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_CatValArray_get_value_double'):
    db_CatValArray_get_value_double = _libs['grass_dbmiclient.7.0.svn'].db_CatValArray_get_value_double
    db_CatValArray_get_value_double.restype = c_int
    db_CatValArray_get_value_double.argtypes = [POINTER(dbCatValArray), c_int, POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 32
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_char_to_lowercase'):
    db_char_to_lowercase = _libs['grass_dbmiclient.7.0.svn'].db_char_to_lowercase
    db_char_to_lowercase.restype = None
    db_char_to_lowercase.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 33
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_char_to_uppercase'):
    db_char_to_uppercase = _libs['grass_dbmiclient.7.0.svn'].db_char_to_uppercase
    db_char_to_uppercase.restype = None
    db_char_to_uppercase.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 34
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_clear_error'):
    db_clear_error = _libs['grass_dbmiclient.7.0.svn'].db_clear_error
    db_clear_error.restype = None
    db_clear_error.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 35
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_clone_table'):
    db_clone_table = _libs['grass_dbmiclient.7.0.svn'].db_clone_table
    db_clone_table.restype = POINTER(dbTable)
    db_clone_table.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 36
for _lib in _libs.values():
    if hasattr(_lib, 'db__close_all_cursors'):
        db__close_all_cursors = _lib.db__close_all_cursors
        db__close_all_cursors.restype = None
        db__close_all_cursors.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 37
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_close_cursor'):
    db_close_cursor = _libs['grass_dbmiclient.7.0.svn'].db_close_cursor
    db_close_cursor.restype = c_int
    db_close_cursor.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 38
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_close_database'):
    db_close_database = _libs['grass_dbmiclient.7.0.svn'].db_close_database
    db_close_database.restype = c_int
    db_close_database.argtypes = [POINTER(dbDriver)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 39
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_close_database_shutdown_driver'):
    db_close_database_shutdown_driver = _libs['grass_dbmiclient.7.0.svn'].db_close_database_shutdown_driver
    db_close_database_shutdown_driver.restype = c_int
    db_close_database_shutdown_driver.argtypes = [POINTER(dbDriver)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 40
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_column_sqltype'):
    db_column_sqltype = _libs['grass_dbmiclient.7.0.svn'].db_column_sqltype
    db_column_sqltype.restype = c_int
    db_column_sqltype.argtypes = [POINTER(dbDriver), String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 41
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_column_Ctype'):
    db_column_Ctype = _libs['grass_dbmiclient.7.0.svn'].db_column_Ctype
    db_column_Ctype.restype = c_int
    db_column_Ctype.argtypes = [POINTER(dbDriver), String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 42
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_convert_Cstring_to_column_default_value'):
    db_convert_Cstring_to_column_default_value = _libs['grass_dbmiclient.7.0.svn'].db_convert_Cstring_to_column_default_value
    db_convert_Cstring_to_column_default_value.restype = c_int
    db_convert_Cstring_to_column_default_value.argtypes = [String, POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 44
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_convert_Cstring_to_column_value'):
    db_convert_Cstring_to_column_value = _libs['grass_dbmiclient.7.0.svn'].db_convert_Cstring_to_column_value
    db_convert_Cstring_to_column_value.restype = c_int
    db_convert_Cstring_to_column_value.argtypes = [String, POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 46
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_convert_Cstring_to_value'):
    db_convert_Cstring_to_value = _libs['grass_dbmiclient.7.0.svn'].db_convert_Cstring_to_value
    db_convert_Cstring_to_value.restype = c_int
    db_convert_Cstring_to_value.argtypes = [String, c_int, POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 48
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_convert_Cstring_to_value_datetime'):
    db_convert_Cstring_to_value_datetime = _libs['grass_dbmiclient.7.0.svn'].db_convert_Cstring_to_value_datetime
    db_convert_Cstring_to_value_datetime.restype = c_int
    db_convert_Cstring_to_value_datetime.argtypes = [String, c_int, POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 50
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_convert_column_default_value_to_string'):
    db_convert_column_default_value_to_string = _libs['grass_dbmiclient.7.0.svn'].db_convert_column_default_value_to_string
    db_convert_column_default_value_to_string.restype = c_int
    db_convert_column_default_value_to_string.argtypes = [POINTER(dbColumn), POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 52
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_convert_column_value_to_string'):
    db_convert_column_value_to_string = _libs['grass_dbmiclient.7.0.svn'].db_convert_column_value_to_string
    db_convert_column_value_to_string.restype = c_int
    db_convert_column_value_to_string.argtypes = [POINTER(dbColumn), POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 53
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_convert_value_datetime_into_string'):
    db_convert_value_datetime_into_string = _libs['grass_dbmiclient.7.0.svn'].db_convert_value_datetime_into_string
    db_convert_value_datetime_into_string.restype = c_int
    db_convert_value_datetime_into_string.argtypes = [POINTER(dbValue), c_int, POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 55
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_convert_value_to_string'):
    db_convert_value_to_string = _libs['grass_dbmiclient.7.0.svn'].db_convert_value_to_string
    db_convert_value_to_string.restype = c_int
    db_convert_value_to_string.argtypes = [POINTER(dbValue), c_int, POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 57
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_copy_column'):
    db_copy_column = _libs['grass_dbmiclient.7.0.svn'].db_copy_column
    db_copy_column.restype = POINTER(dbColumn)
    db_copy_column.argtypes = [POINTER(dbColumn), POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 58
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_copy_dbmscap_entry'):
    db_copy_dbmscap_entry = _libs['grass_dbmiclient.7.0.svn'].db_copy_dbmscap_entry
    db_copy_dbmscap_entry.restype = None
    db_copy_dbmscap_entry.argtypes = [POINTER(dbDbmscap), POINTER(dbDbmscap)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 59
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_copy_string'):
    db_copy_string = _libs['grass_dbmiclient.7.0.svn'].db_copy_string
    db_copy_string.restype = c_int
    db_copy_string.argtypes = [POINTER(dbString), POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 60
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_table_to_sql'):
    db_table_to_sql = _libs['grass_dbmiclient.7.0.svn'].db_table_to_sql
    db_table_to_sql.restype = c_int
    db_table_to_sql.argtypes = [POINTER(dbTable), POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 61
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_copy_table'):
    db_copy_table = _libs['grass_dbmiclient.7.0.svn'].db_copy_table
    db_copy_table.restype = c_int
    db_copy_table.argtypes = [String, String, String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 63
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_copy_table_where'):
    db_copy_table_where = _libs['grass_dbmiclient.7.0.svn'].db_copy_table_where
    db_copy_table_where.restype = c_int
    db_copy_table_where.argtypes = [String, String, String, String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 66
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_copy_table_select'):
    db_copy_table_select = _libs['grass_dbmiclient.7.0.svn'].db_copy_table_select
    db_copy_table_select.restype = c_int
    db_copy_table_select.argtypes = [String, String, String, String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 69
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_copy_table_by_ints'):
    db_copy_table_by_ints = _libs['grass_dbmiclient.7.0.svn'].db_copy_table_by_ints
    db_copy_table_by_ints.restype = c_int
    db_copy_table_by_ints.argtypes = [String, String, String, String, String, String, String, POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 72
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_copy_value'):
    db_copy_value = _libs['grass_dbmiclient.7.0.svn'].db_copy_value
    db_copy_value.restype = None
    db_copy_value.argtypes = [POINTER(dbValue), POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 73
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_create_database'):
    db_create_database = _libs['grass_dbmiclient.7.0.svn'].db_create_database
    db_create_database.restype = c_int
    db_create_database.argtypes = [POINTER(dbDriver), POINTER(dbHandle)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 74
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_create_index'):
    db_create_index = _libs['grass_dbmiclient.7.0.svn'].db_create_index
    db_create_index.restype = c_int
    db_create_index.argtypes = [POINTER(dbDriver), POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 75
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_create_index2'):
    db_create_index2 = _libs['grass_dbmiclient.7.0.svn'].db_create_index2
    db_create_index2.restype = c_int
    db_create_index2.argtypes = [POINTER(dbDriver), String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 77
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_create_table'):
    db_create_table = _libs['grass_dbmiclient.7.0.svn'].db_create_table
    db_create_table.restype = c_int
    db_create_table.argtypes = [POINTER(dbDriver), POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 78
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_add_column'):
        db_d_add_column = _lib.db_d_add_column
        db_d_add_column.restype = c_int
        db_d_add_column.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 79
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_bind_update'):
        db_d_bind_update = _lib.db_d_bind_update
        db_d_bind_update.restype = c_int
        db_d_bind_update.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 80
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_dbmscap_filename'):
    db_dbmscap_filename = _libs['grass_dbmiclient.7.0.svn'].db_dbmscap_filename
    db_dbmscap_filename.restype = ReturnString
    db_dbmscap_filename.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 81
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_close_cursor'):
        db_d_close_cursor = _lib.db_d_close_cursor
        db_d_close_cursor.restype = c_int
        db_d_close_cursor.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 82
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_close_database'):
        db_d_close_database = _lib.db_d_close_database
        db_d_close_database.restype = c_int
        db_d_close_database.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 83
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_create_database'):
        db_d_create_database = _lib.db_d_create_database
        db_d_create_database.restype = c_int
        db_d_create_database.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 84
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_create_index'):
        db_d_create_index = _lib.db_d_create_index
        db_d_create_index.restype = c_int
        db_d_create_index.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 85
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_create_table'):
        db_d_create_table = _lib.db_d_create_table
        db_d_create_table.restype = c_int
        db_d_create_table.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 86
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_delete'):
        db_d_delete = _lib.db_d_delete
        db_d_delete.restype = c_int
        db_d_delete.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 87
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_delete_database'):
        db_d_delete_database = _lib.db_d_delete_database
        db_d_delete_database.restype = c_int
        db_d_delete_database.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 88
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_describe_table'):
        db_d_describe_table = _lib.db_d_describe_table
        db_d_describe_table.restype = c_int
        db_d_describe_table.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 89
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_drop_column'):
        db_d_drop_column = _lib.db_d_drop_column
        db_d_drop_column.restype = c_int
        db_d_drop_column.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 90
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_drop_index'):
        db_d_drop_index = _lib.db_d_drop_index
        db_d_drop_index.restype = c_int
        db_d_drop_index.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 91
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_drop_table'):
        db_d_drop_table = _lib.db_d_drop_table
        db_d_drop_table.restype = c_int
        db_d_drop_table.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 92
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_debug'):
    db_debug = _libs['grass_dbmiclient.7.0.svn'].db_debug
    db_debug.restype = None
    db_debug.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 93
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_debug_off'):
    db_debug_off = _libs['grass_dbmiclient.7.0.svn'].db_debug_off
    db_debug_off.restype = None
    db_debug_off.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 94
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_debug_on'):
    db_debug_on = _libs['grass_dbmiclient.7.0.svn'].db_debug_on
    db_debug_on.restype = None
    db_debug_on.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 95
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_delete'):
    db_delete = _libs['grass_dbmiclient.7.0.svn'].db_delete
    db_delete.restype = c_int
    db_delete.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 96
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_delete_database'):
    db_delete_database = _libs['grass_dbmiclient.7.0.svn'].db_delete_database
    db_delete_database.restype = c_int
    db_delete_database.argtypes = [POINTER(dbDriver), POINTER(dbHandle)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 97
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_delete_table'):
    db_delete_table = _libs['grass_dbmiclient.7.0.svn'].db_delete_table
    db_delete_table.restype = c_int
    db_delete_table.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 98
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_describe_table'):
    db_describe_table = _libs['grass_dbmiclient.7.0.svn'].db_describe_table
    db_describe_table.restype = c_int
    db_describe_table.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(POINTER(dbTable))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 99
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_execute_immediate'):
        db_d_execute_immediate = _lib.db_d_execute_immediate
        db_d_execute_immediate.restype = c_int
        db_d_execute_immediate.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 100
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_begin_transaction'):
        db_d_begin_transaction = _lib.db_d_begin_transaction
        db_d_begin_transaction.restype = c_int
        db_d_begin_transaction.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 101
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_commit_transaction'):
        db_d_commit_transaction = _lib.db_d_commit_transaction
        db_d_commit_transaction.restype = c_int
        db_d_commit_transaction.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 102
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_fetch'):
        db_d_fetch = _lib.db_d_fetch
        db_d_fetch.restype = c_int
        db_d_fetch.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 103
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_find_database'):
        db_d_find_database = _lib.db_d_find_database
        db_d_find_database.restype = c_int
        db_d_find_database.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 104
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_get_num_rows'):
        db_d_get_num_rows = _lib.db_d_get_num_rows
        db_d_get_num_rows.restype = c_int
        db_d_get_num_rows.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 105
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_grant_on_table'):
        db_d_grant_on_table = _lib.db_d_grant_on_table
        db_d_grant_on_table.restype = c_int
        db_d_grant_on_table.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 106
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_insert'):
        db_d_insert = _lib.db_d_insert
        db_d_insert.restype = c_int
        db_d_insert.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 107
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_dirent'):
    db_dirent = _libs['grass_dbmiclient.7.0.svn'].db_dirent
    db_dirent.restype = POINTER(dbDirent)
    db_dirent.argtypes = [String, POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 108
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_list_databases'):
        db_d_list_databases = _lib.db_d_list_databases
        db_d_list_databases.restype = c_int
        db_d_list_databases.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 109
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_list_indexes'):
        db_d_list_indexes = _lib.db_d_list_indexes
        db_d_list_indexes.restype = c_int
        db_d_list_indexes.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 110
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_list_tables'):
        db_d_list_tables = _lib.db_d_list_tables
        db_d_list_tables.restype = c_int
        db_d_list_tables.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 111
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_open_database'):
        db_d_open_database = _lib.db_d_open_database
        db_d_open_database.restype = c_int
        db_d_open_database.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 112
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_open_insert_cursor'):
        db_d_open_insert_cursor = _lib.db_d_open_insert_cursor
        db_d_open_insert_cursor.restype = c_int
        db_d_open_insert_cursor.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 113
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_open_select_cursor'):
        db_d_open_select_cursor = _lib.db_d_open_select_cursor
        db_d_open_select_cursor.restype = c_int
        db_d_open_select_cursor.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 114
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_open_update_cursor'):
        db_d_open_update_cursor = _lib.db_d_open_update_cursor
        db_d_open_update_cursor.restype = c_int
        db_d_open_update_cursor.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 115
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_double_quote_string'):
    db_double_quote_string = _libs['grass_dbmiclient.7.0.svn'].db_double_quote_string
    db_double_quote_string.restype = None
    db_double_quote_string.argtypes = [POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 116
for _lib in _libs.values():
    if hasattr(_lib, 'db_driver'):
        db_driver = _lib.db_driver
        db_driver.restype = c_int
        db_driver.argtypes = [c_int, POINTER(POINTER(c_char))]
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 118
for _lib in _libs.values():
    if hasattr(_lib, 'db_driver_mkdir'):
        db_driver_mkdir = _lib.db_driver_mkdir
        db_driver_mkdir.restype = c_int
        db_driver_mkdir.argtypes = [String, c_int, c_int]
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 119
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_drop_column'):
    db_drop_column = _libs['grass_dbmiclient.7.0.svn'].db_drop_column
    db_drop_column.restype = c_int
    db_drop_column.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 121
for _lib in _libs.values():
    if hasattr(_lib, 'db__drop_cursor_from_driver_state'):
        db__drop_cursor_from_driver_state = _lib.db__drop_cursor_from_driver_state
        db__drop_cursor_from_driver_state.restype = None
        db__drop_cursor_from_driver_state.argtypes = [POINTER(dbCursor)]
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 122
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_drop_index'):
    db_drop_index = _libs['grass_dbmiclient.7.0.svn'].db_drop_index
    db_drop_index.restype = c_int
    db_drop_index.argtypes = [POINTER(dbDriver), POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 123
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_drop_table'):
    db_drop_table = _libs['grass_dbmiclient.7.0.svn'].db_drop_table
    db_drop_table.restype = c_int
    db_drop_table.argtypes = [POINTER(dbDriver), POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 124
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_drop_token'):
    db_drop_token = _libs['grass_dbmiclient.7.0.svn'].db_drop_token
    db_drop_token.restype = None
    db_drop_token.argtypes = [dbToken]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 125
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_update'):
        db_d_update = _lib.db_d_update
        db_d_update.restype = c_int
        db_d_update.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 126
for _lib in _libs.values():
    if hasattr(_lib, 'db_d_version'):
        db_d_version = _lib.db_d_version
        db_d_version.restype = c_int
        db_d_version.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 127
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_enlarge_string'):
    db_enlarge_string = _libs['grass_dbmiclient.7.0.svn'].db_enlarge_string
    db_enlarge_string.restype = c_int
    db_enlarge_string.argtypes = [POINTER(dbString), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 128
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_error'):
    db_error = _libs['grass_dbmiclient.7.0.svn'].db_error
    db_error.restype = None
    db_error.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 129
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_execute_immediate'):
    db_execute_immediate = _libs['grass_dbmiclient.7.0.svn'].db_execute_immediate
    db_execute_immediate.restype = c_int
    db_execute_immediate.argtypes = [POINTER(dbDriver), POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 130
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_begin_transaction'):
    db_begin_transaction = _libs['grass_dbmiclient.7.0.svn'].db_begin_transaction
    db_begin_transaction.restype = c_int
    db_begin_transaction.argtypes = [POINTER(dbDriver)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 131
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_commit_transaction'):
    db_commit_transaction = _libs['grass_dbmiclient.7.0.svn'].db_commit_transaction
    db_commit_transaction.restype = c_int
    db_commit_transaction.argtypes = [POINTER(dbDriver)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 132
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_fetch'):
    db_fetch = _libs['grass_dbmiclient.7.0.svn'].db_fetch
    db_fetch.restype = c_int
    db_fetch.argtypes = [POINTER(dbCursor), c_int, POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 133
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_find_database'):
    db_find_database = _libs['grass_dbmiclient.7.0.svn'].db_find_database
    db_find_database.restype = c_int
    db_find_database.argtypes = [POINTER(dbDriver), POINTER(dbHandle), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 134
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_find_token'):
    db_find_token = _libs['grass_dbmiclient.7.0.svn'].db_find_token
    db_find_token.restype = dbAddress
    db_find_token.argtypes = [dbToken]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 135
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free'):
    db_free = _libs['grass_dbmiclient.7.0.svn'].db_free
    db_free.restype = None
    db_free.argtypes = [POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 136
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_column'):
    db_free_column = _libs['grass_dbmiclient.7.0.svn'].db_free_column
    db_free_column.restype = None
    db_free_column.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 137
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_cursor'):
    db_free_cursor = _libs['grass_dbmiclient.7.0.svn'].db_free_cursor
    db_free_cursor.restype = None
    db_free_cursor.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 138
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_cursor_column_flags'):
    db_free_cursor_column_flags = _libs['grass_dbmiclient.7.0.svn'].db_free_cursor_column_flags
    db_free_cursor_column_flags.restype = None
    db_free_cursor_column_flags.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 139
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_dbmscap'):
    db_free_dbmscap = _libs['grass_dbmiclient.7.0.svn'].db_free_dbmscap
    db_free_dbmscap.restype = None
    db_free_dbmscap.argtypes = [POINTER(dbDbmscap)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 140
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_dirent_array'):
    db_free_dirent_array = _libs['grass_dbmiclient.7.0.svn'].db_free_dirent_array
    db_free_dirent_array.restype = None
    db_free_dirent_array.argtypes = [POINTER(dbDirent), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 141
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_handle'):
    db_free_handle = _libs['grass_dbmiclient.7.0.svn'].db_free_handle
    db_free_handle.restype = None
    db_free_handle.argtypes = [POINTER(dbHandle)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 142
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_handle_array'):
    db_free_handle_array = _libs['grass_dbmiclient.7.0.svn'].db_free_handle_array
    db_free_handle_array.restype = None
    db_free_handle_array.argtypes = [POINTER(dbHandle), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 143
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_index'):
    db_free_index = _libs['grass_dbmiclient.7.0.svn'].db_free_index
    db_free_index.restype = None
    db_free_index.argtypes = [POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 144
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_index_array'):
    db_free_index_array = _libs['grass_dbmiclient.7.0.svn'].db_free_index_array
    db_free_index_array.restype = None
    db_free_index_array.argtypes = [POINTER(dbIndex), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 145
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_string'):
    db_free_string = _libs['grass_dbmiclient.7.0.svn'].db_free_string
    db_free_string.restype = None
    db_free_string.argtypes = [POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 146
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_string_array'):
    db_free_string_array = _libs['grass_dbmiclient.7.0.svn'].db_free_string_array
    db_free_string_array.restype = None
    db_free_string_array.argtypes = [POINTER(dbString), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 147
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_free_table'):
    db_free_table = _libs['grass_dbmiclient.7.0.svn'].db_free_table
    db_free_table.restype = None
    db_free_table.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 148
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column'):
    db_get_column = _libs['grass_dbmiclient.7.0.svn'].db_get_column
    db_get_column.restype = c_int
    db_get_column.argtypes = [POINTER(dbDriver), String, String, POINTER(POINTER(dbColumn))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 150
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_default_value'):
    db_get_column_default_value = _libs['grass_dbmiclient.7.0.svn'].db_get_column_default_value
    db_get_column_default_value.restype = POINTER(dbValue)
    db_get_column_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 151
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_description'):
    db_get_column_description = _libs['grass_dbmiclient.7.0.svn'].db_get_column_description
    db_get_column_description.restype = ReturnString
    db_get_column_description.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 152
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_host_type'):
    db_get_column_host_type = _libs['grass_dbmiclient.7.0.svn'].db_get_column_host_type
    db_get_column_host_type.restype = c_int
    db_get_column_host_type.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 153
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_length'):
    db_get_column_length = _libs['grass_dbmiclient.7.0.svn'].db_get_column_length
    db_get_column_length.restype = c_int
    db_get_column_length.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 154
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_name'):
    db_get_column_name = _libs['grass_dbmiclient.7.0.svn'].db_get_column_name
    db_get_column_name.restype = ReturnString
    db_get_column_name.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 155
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_precision'):
    db_get_column_precision = _libs['grass_dbmiclient.7.0.svn'].db_get_column_precision
    db_get_column_precision.restype = c_int
    db_get_column_precision.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 156
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_scale'):
    db_get_column_scale = _libs['grass_dbmiclient.7.0.svn'].db_get_column_scale
    db_get_column_scale.restype = c_int
    db_get_column_scale.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 157
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_select_priv'):
    db_get_column_select_priv = _libs['grass_dbmiclient.7.0.svn'].db_get_column_select_priv
    db_get_column_select_priv.restype = c_int
    db_get_column_select_priv.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 158
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_sqltype'):
    db_get_column_sqltype = _libs['grass_dbmiclient.7.0.svn'].db_get_column_sqltype
    db_get_column_sqltype.restype = c_int
    db_get_column_sqltype.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 159
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_update_priv'):
    db_get_column_update_priv = _libs['grass_dbmiclient.7.0.svn'].db_get_column_update_priv
    db_get_column_update_priv.restype = c_int
    db_get_column_update_priv.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 160
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_column_value'):
    db_get_column_value = _libs['grass_dbmiclient.7.0.svn'].db_get_column_value
    db_get_column_value.restype = POINTER(dbValue)
    db_get_column_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 161
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_connection'):
    db_get_connection = _libs['grass_dbmiclient.7.0.svn'].db_get_connection
    db_get_connection.restype = c_int
    db_get_connection.argtypes = [POINTER(dbConnection)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 162
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_cursor_number_of_columns'):
    db_get_cursor_number_of_columns = _libs['grass_dbmiclient.7.0.svn'].db_get_cursor_number_of_columns
    db_get_cursor_number_of_columns.restype = c_int
    db_get_cursor_number_of_columns.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 163
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_cursor_table'):
    db_get_cursor_table = _libs['grass_dbmiclient.7.0.svn'].db_get_cursor_table
    db_get_cursor_table.restype = POINTER(dbTable)
    db_get_cursor_table.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 164
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_cursor_token'):
    db_get_cursor_token = _libs['grass_dbmiclient.7.0.svn'].db_get_cursor_token
    db_get_cursor_token.restype = dbToken
    db_get_cursor_token.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 165
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_default_driver_name'):
    db_get_default_driver_name = _libs['grass_dbmiclient.7.0.svn'].db_get_default_driver_name
    db_get_default_driver_name.restype = ReturnString
    db_get_default_driver_name.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 166
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_default_database_name'):
    db_get_default_database_name = _libs['grass_dbmiclient.7.0.svn'].db_get_default_database_name
    db_get_default_database_name.restype = ReturnString
    db_get_default_database_name.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 167
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_default_schema_name'):
    db_get_default_schema_name = _libs['grass_dbmiclient.7.0.svn'].db_get_default_schema_name
    db_get_default_schema_name.restype = ReturnString
    db_get_default_schema_name.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 168
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_default_group_name'):
    db_get_default_group_name = _libs['grass_dbmiclient.7.0.svn'].db_get_default_group_name
    db_get_default_group_name.restype = ReturnString
    db_get_default_group_name.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 169
for _lib in _libs.values():
    if hasattr(_lib, 'db__get_driver_state'):
        db__get_driver_state = _lib.db__get_driver_state
        db__get_driver_state.restype = POINTER(dbDriverState)
        db__get_driver_state.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 170
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_error_code'):
    db_get_error_code = _libs['grass_dbmiclient.7.0.svn'].db_get_error_code
    db_get_error_code.restype = c_int
    db_get_error_code.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 171
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_error_msg'):
    db_get_error_msg = _libs['grass_dbmiclient.7.0.svn'].db_get_error_msg
    db_get_error_msg.restype = ReturnString
    db_get_error_msg.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 172
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_error_who'):
    db_get_error_who = _libs['grass_dbmiclient.7.0.svn'].db_get_error_who
    db_get_error_who.restype = ReturnString
    db_get_error_who.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 173
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_handle_dbname'):
    db_get_handle_dbname = _libs['grass_dbmiclient.7.0.svn'].db_get_handle_dbname
    db_get_handle_dbname.restype = ReturnString
    db_get_handle_dbname.argtypes = [POINTER(dbHandle)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 174
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_handle_dbschema'):
    db_get_handle_dbschema = _libs['grass_dbmiclient.7.0.svn'].db_get_handle_dbschema
    db_get_handle_dbschema.restype = ReturnString
    db_get_handle_dbschema.argtypes = [POINTER(dbHandle)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 175
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_index_column_name'):
    db_get_index_column_name = _libs['grass_dbmiclient.7.0.svn'].db_get_index_column_name
    db_get_index_column_name.restype = ReturnString
    db_get_index_column_name.argtypes = [POINTER(dbIndex), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 176
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_index_name'):
    db_get_index_name = _libs['grass_dbmiclient.7.0.svn'].db_get_index_name
    db_get_index_name.restype = ReturnString
    db_get_index_name.argtypes = [POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 177
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_index_number_of_columns'):
    db_get_index_number_of_columns = _libs['grass_dbmiclient.7.0.svn'].db_get_index_number_of_columns
    db_get_index_number_of_columns.restype = c_int
    db_get_index_number_of_columns.argtypes = [POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 178
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_index_table_name'):
    db_get_index_table_name = _libs['grass_dbmiclient.7.0.svn'].db_get_index_table_name
    db_get_index_table_name.restype = ReturnString
    db_get_index_table_name.argtypes = [POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 179
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_num_rows'):
    db_get_num_rows = _libs['grass_dbmiclient.7.0.svn'].db_get_num_rows
    db_get_num_rows.restype = c_int
    db_get_num_rows.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 180
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_string'):
    db_get_string = _libs['grass_dbmiclient.7.0.svn'].db_get_string
    db_get_string.restype = ReturnString
    db_get_string.argtypes = [POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 181
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_table_column'):
    db_get_table_column = _libs['grass_dbmiclient.7.0.svn'].db_get_table_column
    db_get_table_column.restype = POINTER(dbColumn)
    db_get_table_column.argtypes = [POINTER(dbTable), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 182
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_table_column_by_name'):
    db_get_table_column_by_name = _libs['grass_dbmiclient.7.0.svn'].db_get_table_column_by_name
    db_get_table_column_by_name.restype = POINTER(dbColumn)
    db_get_table_column_by_name.argtypes = [POINTER(dbTable), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 183
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_table_delete_priv'):
    db_get_table_delete_priv = _libs['grass_dbmiclient.7.0.svn'].db_get_table_delete_priv
    db_get_table_delete_priv.restype = c_int
    db_get_table_delete_priv.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 184
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_table_description'):
    db_get_table_description = _libs['grass_dbmiclient.7.0.svn'].db_get_table_description
    db_get_table_description.restype = ReturnString
    db_get_table_description.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 185
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_table_insert_priv'):
    db_get_table_insert_priv = _libs['grass_dbmiclient.7.0.svn'].db_get_table_insert_priv
    db_get_table_insert_priv.restype = c_int
    db_get_table_insert_priv.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 186
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_table_name'):
    db_get_table_name = _libs['grass_dbmiclient.7.0.svn'].db_get_table_name
    db_get_table_name.restype = ReturnString
    db_get_table_name.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 187
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_table_number_of_columns'):
    db_get_table_number_of_columns = _libs['grass_dbmiclient.7.0.svn'].db_get_table_number_of_columns
    db_get_table_number_of_columns.restype = c_int
    db_get_table_number_of_columns.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 188
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_table_number_of_rows'):
    db_get_table_number_of_rows = _libs['grass_dbmiclient.7.0.svn'].db_get_table_number_of_rows
    db_get_table_number_of_rows.restype = c_int
    db_get_table_number_of_rows.argtypes = [POINTER(dbDriver), POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 189
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_table_select_priv'):
    db_get_table_select_priv = _libs['grass_dbmiclient.7.0.svn'].db_get_table_select_priv
    db_get_table_select_priv.restype = c_int
    db_get_table_select_priv.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 190
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_table_update_priv'):
    db_get_table_update_priv = _libs['grass_dbmiclient.7.0.svn'].db_get_table_update_priv
    db_get_table_update_priv.restype = c_int
    db_get_table_update_priv.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 191
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_value_as_double'):
    db_get_value_as_double = _libs['grass_dbmiclient.7.0.svn'].db_get_value_as_double
    db_get_value_as_double.restype = c_double
    db_get_value_as_double.argtypes = [POINTER(dbValue), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 192
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_value_day'):
    db_get_value_day = _libs['grass_dbmiclient.7.0.svn'].db_get_value_day
    db_get_value_day.restype = c_int
    db_get_value_day.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 193
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_value_double'):
    db_get_value_double = _libs['grass_dbmiclient.7.0.svn'].db_get_value_double
    db_get_value_double.restype = c_double
    db_get_value_double.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 194
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_value_hour'):
    db_get_value_hour = _libs['grass_dbmiclient.7.0.svn'].db_get_value_hour
    db_get_value_hour.restype = c_int
    db_get_value_hour.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 195
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_value_int'):
    db_get_value_int = _libs['grass_dbmiclient.7.0.svn'].db_get_value_int
    db_get_value_int.restype = c_int
    db_get_value_int.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 196
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_value_minute'):
    db_get_value_minute = _libs['grass_dbmiclient.7.0.svn'].db_get_value_minute
    db_get_value_minute.restype = c_int
    db_get_value_minute.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 197
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_value_month'):
    db_get_value_month = _libs['grass_dbmiclient.7.0.svn'].db_get_value_month
    db_get_value_month.restype = c_int
    db_get_value_month.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 198
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_value_seconds'):
    db_get_value_seconds = _libs['grass_dbmiclient.7.0.svn'].db_get_value_seconds
    db_get_value_seconds.restype = c_double
    db_get_value_seconds.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 199
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_value_string'):
    db_get_value_string = _libs['grass_dbmiclient.7.0.svn'].db_get_value_string
    db_get_value_string.restype = ReturnString
    db_get_value_string.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 200
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_value_year'):
    db_get_value_year = _libs['grass_dbmiclient.7.0.svn'].db_get_value_year
    db_get_value_year.restype = c_int
    db_get_value_year.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 201
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_grant_on_table'):
    db_grant_on_table = _libs['grass_dbmiclient.7.0.svn'].db_grant_on_table
    db_grant_on_table.restype = c_int
    db_grant_on_table.argtypes = [POINTER(dbDriver), String, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 203
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_has_dbms'):
    db_has_dbms = _libs['grass_dbmiclient.7.0.svn'].db_has_dbms
    db_has_dbms.restype = c_int
    db_has_dbms.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 204
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_init_column'):
    db_init_column = _libs['grass_dbmiclient.7.0.svn'].db_init_column
    db_init_column.restype = None
    db_init_column.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 205
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_init_cursor'):
    db_init_cursor = _libs['grass_dbmiclient.7.0.svn'].db_init_cursor
    db_init_cursor.restype = None
    db_init_cursor.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 206
for _lib in _libs.values():
    if hasattr(_lib, 'db__init_driver_state'):
        db__init_driver_state = _lib.db__init_driver_state
        db__init_driver_state.restype = None
        db__init_driver_state.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 207
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_init_handle'):
    db_init_handle = _libs['grass_dbmiclient.7.0.svn'].db_init_handle
    db_init_handle.restype = None
    db_init_handle.argtypes = [POINTER(dbHandle)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 208
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_init_index'):
    db_init_index = _libs['grass_dbmiclient.7.0.svn'].db_init_index
    db_init_index.restype = None
    db_init_index.argtypes = [POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 209
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_init_string'):
    db_init_string = _libs['grass_dbmiclient.7.0.svn'].db_init_string
    db_init_string.restype = None
    db_init_string.argtypes = [POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 210
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_init_table'):
    db_init_table = _libs['grass_dbmiclient.7.0.svn'].db_init_table
    db_init_table.restype = None
    db_init_table.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 211
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_insert'):
    db_insert = _libs['grass_dbmiclient.7.0.svn'].db_insert
    db_insert.restype = c_int
    db_insert.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 212
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_interval_range'):
    db_interval_range = _libs['grass_dbmiclient.7.0.svn'].db_interval_range
    db_interval_range.restype = None
    db_interval_range.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 213
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_isdir'):
    db_isdir = _libs['grass_dbmiclient.7.0.svn'].db_isdir
    db_isdir.restype = c_int
    db_isdir.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 214
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_legal_tablename'):
    db_legal_tablename = _libs['grass_dbmiclient.7.0.svn'].db_legal_tablename
    db_legal_tablename.restype = c_int
    db_legal_tablename.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 215
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_list_databases'):
    db_list_databases = _libs['grass_dbmiclient.7.0.svn'].db_list_databases
    db_list_databases.restype = c_int
    db_list_databases.argtypes = [POINTER(dbDriver), POINTER(dbString), c_int, POINTER(POINTER(dbHandle)), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 217
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_list_drivers'):
    db_list_drivers = _libs['grass_dbmiclient.7.0.svn'].db_list_drivers
    db_list_drivers.restype = ReturnString
    db_list_drivers.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 218
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_list_indexes'):
    db_list_indexes = _libs['grass_dbmiclient.7.0.svn'].db_list_indexes
    db_list_indexes.restype = c_int
    db_list_indexes.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(POINTER(dbIndex)), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 220
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_list_tables'):
    db_list_tables = _libs['grass_dbmiclient.7.0.svn'].db_list_tables
    db_list_tables.restype = c_int
    db_list_tables.argtypes = [POINTER(dbDriver), POINTER(POINTER(dbString)), POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 222
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_malloc'):
    db_malloc = _libs['grass_dbmiclient.7.0.svn'].db_malloc
    db_malloc.restype = POINTER(None)
    db_malloc.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 223
for _lib in _libs.values():
    if hasattr(_lib, 'db__mark_database_closed'):
        db__mark_database_closed = _lib.db__mark_database_closed
        db__mark_database_closed.restype = None
        db__mark_database_closed.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 224
for _lib in _libs.values():
    if hasattr(_lib, 'db__mark_database_open'):
        db__mark_database_open = _lib.db__mark_database_open
        db__mark_database_open.restype = None
        db__mark_database_open.argtypes = [String, String]
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 225
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_memory_error'):
    db_memory_error = _libs['grass_dbmiclient.7.0.svn'].db_memory_error
    db_memory_error.restype = None
    db_memory_error.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 226
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_new_token'):
    db_new_token = _libs['grass_dbmiclient.7.0.svn'].db_new_token
    db_new_token.restype = dbToken
    db_new_token.argtypes = [dbAddress]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 227
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_nocase_compare'):
    db_nocase_compare = _libs['grass_dbmiclient.7.0.svn'].db_nocase_compare
    db_nocase_compare.restype = c_int
    db_nocase_compare.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 228
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_noproc_error'):
    db_noproc_error = _libs['grass_dbmiclient.7.0.svn'].db_noproc_error
    db_noproc_error.restype = None
    db_noproc_error.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 229
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_open_database'):
    db_open_database = _libs['grass_dbmiclient.7.0.svn'].db_open_database
    db_open_database.restype = c_int
    db_open_database.argtypes = [POINTER(dbDriver), POINTER(dbHandle)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 230
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_open_insert_cursor'):
    db_open_insert_cursor = _libs['grass_dbmiclient.7.0.svn'].db_open_insert_cursor
    db_open_insert_cursor.restype = c_int
    db_open_insert_cursor.argtypes = [POINTER(dbDriver), POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 231
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_open_select_cursor'):
    db_open_select_cursor = _libs['grass_dbmiclient.7.0.svn'].db_open_select_cursor
    db_open_select_cursor.restype = c_int
    db_open_select_cursor.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(dbCursor), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 233
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_open_update_cursor'):
    db_open_update_cursor = _libs['grass_dbmiclient.7.0.svn'].db_open_update_cursor
    db_open_update_cursor.restype = c_int
    db_open_update_cursor.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(dbString), POINTER(dbCursor), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 235
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_print_column_definition'):
    db_print_column_definition = _libs['grass_dbmiclient.7.0.svn'].db_print_column_definition
    db_print_column_definition.restype = None
    db_print_column_definition.argtypes = [POINTER(FILE), POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 236
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_print_error'):
    db_print_error = _libs['grass_dbmiclient.7.0.svn'].db_print_error
    db_print_error.restype = None
    db_print_error.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 237
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_print_index'):
    db_print_index = _libs['grass_dbmiclient.7.0.svn'].db_print_index
    db_print_index.restype = None
    db_print_index.argtypes = [POINTER(FILE), POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 238
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_print_table_definition'):
    db_print_table_definition = _libs['grass_dbmiclient.7.0.svn'].db_print_table_definition
    db_print_table_definition.restype = None
    db_print_table_definition.argtypes = [POINTER(FILE), POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 239
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_procedure_not_implemented'):
    db_procedure_not_implemented = _libs['grass_dbmiclient.7.0.svn'].db_procedure_not_implemented
    db_procedure_not_implemented.restype = None
    db_procedure_not_implemented.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 240
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_protocol_error'):
    db_protocol_error = _libs['grass_dbmiclient.7.0.svn'].db_protocol_error
    db_protocol_error.restype = None
    db_protocol_error.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 241
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_read_dbmscap'):
    db_read_dbmscap = _libs['grass_dbmiclient.7.0.svn'].db_read_dbmscap
    db_read_dbmscap.restype = POINTER(dbDbmscap)
    db_read_dbmscap.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 242
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_realloc'):
    db_realloc = _libs['grass_dbmiclient.7.0.svn'].db_realloc
    db_realloc.restype = POINTER(None)
    db_realloc.argtypes = [POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 243
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_char'):
    db__recv_char = _libs['grass_dbmiclient.7.0.svn'].db__recv_char
    db__recv_char.restype = c_int
    db__recv_char.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 244
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_column_default_value'):
    db__recv_column_default_value = _libs['grass_dbmiclient.7.0.svn'].db__recv_column_default_value
    db__recv_column_default_value.restype = c_int
    db__recv_column_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 245
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_column_definition'):
    db__recv_column_definition = _libs['grass_dbmiclient.7.0.svn'].db__recv_column_definition
    db__recv_column_definition.restype = c_int
    db__recv_column_definition.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 246
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_column_value'):
    db__recv_column_value = _libs['grass_dbmiclient.7.0.svn'].db__recv_column_value
    db__recv_column_value.restype = c_int
    db__recv_column_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 247
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_datetime'):
    db__recv_datetime = _libs['grass_dbmiclient.7.0.svn'].db__recv_datetime
    db__recv_datetime.restype = c_int
    db__recv_datetime.argtypes = [POINTER(dbDateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 248
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_double'):
    db__recv_double = _libs['grass_dbmiclient.7.0.svn'].db__recv_double
    db__recv_double.restype = c_int
    db__recv_double.argtypes = [POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 249
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_double_array'):
    db__recv_double_array = _libs['grass_dbmiclient.7.0.svn'].db__recv_double_array
    db__recv_double_array.restype = c_int
    db__recv_double_array.argtypes = [POINTER(POINTER(c_double)), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 250
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_float'):
    db__recv_float = _libs['grass_dbmiclient.7.0.svn'].db__recv_float
    db__recv_float.restype = c_int
    db__recv_float.argtypes = [POINTER(c_float)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 251
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_float_array'):
    db__recv_float_array = _libs['grass_dbmiclient.7.0.svn'].db__recv_float_array
    db__recv_float_array.restype = c_int
    db__recv_float_array.argtypes = [POINTER(POINTER(c_float)), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 252
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_handle'):
    db__recv_handle = _libs['grass_dbmiclient.7.0.svn'].db__recv_handle
    db__recv_handle.restype = c_int
    db__recv_handle.argtypes = [POINTER(dbHandle)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 253
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_index'):
    db__recv_index = _libs['grass_dbmiclient.7.0.svn'].db__recv_index
    db__recv_index.restype = c_int
    db__recv_index.argtypes = [POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 254
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_index_array'):
    db__recv_index_array = _libs['grass_dbmiclient.7.0.svn'].db__recv_index_array
    db__recv_index_array.restype = c_int
    db__recv_index_array.argtypes = [POINTER(POINTER(dbIndex)), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 255
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_int'):
    db__recv_int = _libs['grass_dbmiclient.7.0.svn'].db__recv_int
    db__recv_int.restype = c_int
    db__recv_int.argtypes = [POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 256
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_int_array'):
    db__recv_int_array = _libs['grass_dbmiclient.7.0.svn'].db__recv_int_array
    db__recv_int_array.restype = c_int
    db__recv_int_array.argtypes = [POINTER(POINTER(c_int)), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 257
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_procnum'):
    db__recv_procnum = _libs['grass_dbmiclient.7.0.svn'].db__recv_procnum
    db__recv_procnum.restype = c_int
    db__recv_procnum.argtypes = [POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 258
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_return_code'):
    db__recv_return_code = _libs['grass_dbmiclient.7.0.svn'].db__recv_return_code
    db__recv_return_code.restype = c_int
    db__recv_return_code.argtypes = [POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 259
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_short'):
    db__recv_short = _libs['grass_dbmiclient.7.0.svn'].db__recv_short
    db__recv_short.restype = c_int
    db__recv_short.argtypes = [POINTER(c_short)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 260
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_short_array'):
    db__recv_short_array = _libs['grass_dbmiclient.7.0.svn'].db__recv_short_array
    db__recv_short_array.restype = c_int
    db__recv_short_array.argtypes = [POINTER(POINTER(c_short)), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 261
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_string'):
    db__recv_string = _libs['grass_dbmiclient.7.0.svn'].db__recv_string
    db__recv_string.restype = c_int
    db__recv_string.argtypes = [POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 262
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_string_array'):
    db__recv_string_array = _libs['grass_dbmiclient.7.0.svn'].db__recv_string_array
    db__recv_string_array.restype = c_int
    db__recv_string_array.argtypes = [POINTER(POINTER(dbString)), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 263
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_table_data'):
    db__recv_table_data = _libs['grass_dbmiclient.7.0.svn'].db__recv_table_data
    db__recv_table_data.restype = c_int
    db__recv_table_data.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 264
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_table_definition'):
    db__recv_table_definition = _libs['grass_dbmiclient.7.0.svn'].db__recv_table_definition
    db__recv_table_definition.restype = c_int
    db__recv_table_definition.argtypes = [POINTER(POINTER(dbTable))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 265
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_token'):
    db__recv_token = _libs['grass_dbmiclient.7.0.svn'].db__recv_token
    db__recv_token.restype = c_int
    db__recv_token.argtypes = [POINTER(dbToken)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 266
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__recv_value'):
    db__recv_value = _libs['grass_dbmiclient.7.0.svn'].db__recv_value
    db__recv_value.restype = c_int
    db__recv_value.argtypes = [POINTER(dbValue), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 267
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_Cstring'):
    db__send_Cstring = _libs['grass_dbmiclient.7.0.svn'].db__send_Cstring
    db__send_Cstring.restype = c_int
    db__send_Cstring.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 268
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_char'):
    db__send_char = _libs['grass_dbmiclient.7.0.svn'].db__send_char
    db__send_char.restype = c_int
    db__send_char.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 269
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_column_default_value'):
    db__send_column_default_value = _libs['grass_dbmiclient.7.0.svn'].db__send_column_default_value
    db__send_column_default_value.restype = c_int
    db__send_column_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 270
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_column_definition'):
    db__send_column_definition = _libs['grass_dbmiclient.7.0.svn'].db__send_column_definition
    db__send_column_definition.restype = c_int
    db__send_column_definition.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 271
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_column_value'):
    db__send_column_value = _libs['grass_dbmiclient.7.0.svn'].db__send_column_value
    db__send_column_value.restype = c_int
    db__send_column_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 272
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_datetime'):
    db__send_datetime = _libs['grass_dbmiclient.7.0.svn'].db__send_datetime
    db__send_datetime.restype = c_int
    db__send_datetime.argtypes = [POINTER(dbDateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 273
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_double'):
    db__send_double = _libs['grass_dbmiclient.7.0.svn'].db__send_double
    db__send_double.restype = c_int
    db__send_double.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 274
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_double_array'):
    db__send_double_array = _libs['grass_dbmiclient.7.0.svn'].db__send_double_array
    db__send_double_array.restype = c_int
    db__send_double_array.argtypes = [POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 275
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_failure'):
    db__send_failure = _libs['grass_dbmiclient.7.0.svn'].db__send_failure
    db__send_failure.restype = c_int
    db__send_failure.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 276
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_float'):
    db__send_float = _libs['grass_dbmiclient.7.0.svn'].db__send_float
    db__send_float.restype = c_int
    db__send_float.argtypes = [c_float]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 277
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_float_array'):
    db__send_float_array = _libs['grass_dbmiclient.7.0.svn'].db__send_float_array
    db__send_float_array.restype = c_int
    db__send_float_array.argtypes = [POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 278
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_handle'):
    db__send_handle = _libs['grass_dbmiclient.7.0.svn'].db__send_handle
    db__send_handle.restype = c_int
    db__send_handle.argtypes = [POINTER(dbHandle)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 279
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_index'):
    db__send_index = _libs['grass_dbmiclient.7.0.svn'].db__send_index
    db__send_index.restype = c_int
    db__send_index.argtypes = [POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 280
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_index_array'):
    db__send_index_array = _libs['grass_dbmiclient.7.0.svn'].db__send_index_array
    db__send_index_array.restype = c_int
    db__send_index_array.argtypes = [POINTER(dbIndex), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 281
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_int'):
    db__send_int = _libs['grass_dbmiclient.7.0.svn'].db__send_int
    db__send_int.restype = c_int
    db__send_int.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 282
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_int_array'):
    db__send_int_array = _libs['grass_dbmiclient.7.0.svn'].db__send_int_array
    db__send_int_array.restype = c_int
    db__send_int_array.argtypes = [POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 283
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_procedure_not_implemented'):
    db__send_procedure_not_implemented = _libs['grass_dbmiclient.7.0.svn'].db__send_procedure_not_implemented
    db__send_procedure_not_implemented.restype = c_int
    db__send_procedure_not_implemented.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 284
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_procedure_ok'):
    db__send_procedure_ok = _libs['grass_dbmiclient.7.0.svn'].db__send_procedure_ok
    db__send_procedure_ok.restype = c_int
    db__send_procedure_ok.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 285
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_short'):
    db__send_short = _libs['grass_dbmiclient.7.0.svn'].db__send_short
    db__send_short.restype = c_int
    db__send_short.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 286
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_short_array'):
    db__send_short_array = _libs['grass_dbmiclient.7.0.svn'].db__send_short_array
    db__send_short_array.restype = c_int
    db__send_short_array.argtypes = [POINTER(c_short), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 287
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_string'):
    db__send_string = _libs['grass_dbmiclient.7.0.svn'].db__send_string
    db__send_string.restype = c_int
    db__send_string.argtypes = [POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 288
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_string_array'):
    db__send_string_array = _libs['grass_dbmiclient.7.0.svn'].db__send_string_array
    db__send_string_array.restype = c_int
    db__send_string_array.argtypes = [POINTER(dbString), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 289
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_success'):
    db__send_success = _libs['grass_dbmiclient.7.0.svn'].db__send_success
    db__send_success.restype = c_int
    db__send_success.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 290
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_table_data'):
    db__send_table_data = _libs['grass_dbmiclient.7.0.svn'].db__send_table_data
    db__send_table_data.restype = c_int
    db__send_table_data.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 291
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_table_definition'):
    db__send_table_definition = _libs['grass_dbmiclient.7.0.svn'].db__send_table_definition
    db__send_table_definition.restype = c_int
    db__send_table_definition.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 292
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_token'):
    db__send_token = _libs['grass_dbmiclient.7.0.svn'].db__send_token
    db__send_token.restype = c_int
    db__send_token.argtypes = [POINTER(dbToken)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 293
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__send_value'):
    db__send_value = _libs['grass_dbmiclient.7.0.svn'].db__send_value
    db__send_value.restype = c_int
    db__send_value.argtypes = [POINTER(dbValue), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 294
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_select_CatValArray'):
    db_select_CatValArray = _libs['grass_dbmiclient.7.0.svn'].db_select_CatValArray
    db_select_CatValArray.restype = c_int
    db_select_CatValArray.argtypes = [POINTER(dbDriver), String, String, String, String, POINTER(dbCatValArray)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 297
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_select_int'):
    db_select_int = _libs['grass_dbmiclient.7.0.svn'].db_select_int
    db_select_int.restype = c_int
    db_select_int.argtypes = [POINTER(dbDriver), String, String, String, POINTER(POINTER(c_int))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 299
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_select_value'):
    db_select_value = _libs['grass_dbmiclient.7.0.svn'].db_select_value
    db_select_value.restype = c_int
    db_select_value.argtypes = [POINTER(dbDriver), String, String, c_int, String, POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 301
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_description'):
    db_set_column_description = _libs['grass_dbmiclient.7.0.svn'].db_set_column_description
    db_set_column_description.restype = c_int
    db_set_column_description.argtypes = [POINTER(dbColumn), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 302
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_has_defined_default_value'):
    db_set_column_has_defined_default_value = _libs['grass_dbmiclient.7.0.svn'].db_set_column_has_defined_default_value
    db_set_column_has_defined_default_value.restype = None
    db_set_column_has_defined_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 303
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_has_undefined_default_value'):
    db_set_column_has_undefined_default_value = _libs['grass_dbmiclient.7.0.svn'].db_set_column_has_undefined_default_value
    db_set_column_has_undefined_default_value.restype = None
    db_set_column_has_undefined_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 304
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_host_type'):
    db_set_column_host_type = _libs['grass_dbmiclient.7.0.svn'].db_set_column_host_type
    db_set_column_host_type.restype = None
    db_set_column_host_type.argtypes = [POINTER(dbColumn), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 305
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_length'):
    db_set_column_length = _libs['grass_dbmiclient.7.0.svn'].db_set_column_length
    db_set_column_length.restype = None
    db_set_column_length.argtypes = [POINTER(dbColumn), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 306
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_name'):
    db_set_column_name = _libs['grass_dbmiclient.7.0.svn'].db_set_column_name
    db_set_column_name.restype = c_int
    db_set_column_name.argtypes = [POINTER(dbColumn), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 307
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_null_allowed'):
    db_set_column_null_allowed = _libs['grass_dbmiclient.7.0.svn'].db_set_column_null_allowed
    db_set_column_null_allowed.restype = None
    db_set_column_null_allowed.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 308
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_precision'):
    db_set_column_precision = _libs['grass_dbmiclient.7.0.svn'].db_set_column_precision
    db_set_column_precision.restype = None
    db_set_column_precision.argtypes = [POINTER(dbColumn), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 309
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_scale'):
    db_set_column_scale = _libs['grass_dbmiclient.7.0.svn'].db_set_column_scale
    db_set_column_scale.restype = None
    db_set_column_scale.argtypes = [POINTER(dbColumn), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 310
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_select_priv_granted'):
    db_set_column_select_priv_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_column_select_priv_granted
    db_set_column_select_priv_granted.restype = None
    db_set_column_select_priv_granted.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 311
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_select_priv_not_granted'):
    db_set_column_select_priv_not_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_column_select_priv_not_granted
    db_set_column_select_priv_not_granted.restype = None
    db_set_column_select_priv_not_granted.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 312
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_sqltype'):
    db_set_column_sqltype = _libs['grass_dbmiclient.7.0.svn'].db_set_column_sqltype
    db_set_column_sqltype.restype = None
    db_set_column_sqltype.argtypes = [POINTER(dbColumn), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 313
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_update_priv_granted'):
    db_set_column_update_priv_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_column_update_priv_granted
    db_set_column_update_priv_granted.restype = None
    db_set_column_update_priv_granted.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 314
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_update_priv_not_granted'):
    db_set_column_update_priv_not_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_column_update_priv_not_granted
    db_set_column_update_priv_not_granted.restype = None
    db_set_column_update_priv_not_granted.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 315
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_column_use_default_value'):
    db_set_column_use_default_value = _libs['grass_dbmiclient.7.0.svn'].db_set_column_use_default_value
    db_set_column_use_default_value.restype = None
    db_set_column_use_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 316
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_connection'):
    db_set_connection = _libs['grass_dbmiclient.7.0.svn'].db_set_connection
    db_set_connection.restype = c_int
    db_set_connection.argtypes = [POINTER(dbConnection)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 317
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_cursor_column_flag'):
    db_set_cursor_column_flag = _libs['grass_dbmiclient.7.0.svn'].db_set_cursor_column_flag
    db_set_cursor_column_flag.restype = None
    db_set_cursor_column_flag.argtypes = [POINTER(dbCursor), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 318
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_cursor_column_for_update'):
    db_set_cursor_column_for_update = _libs['grass_dbmiclient.7.0.svn'].db_set_cursor_column_for_update
    db_set_cursor_column_for_update.restype = None
    db_set_cursor_column_for_update.argtypes = [POINTER(dbCursor), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 319
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_cursor_mode'):
    db_set_cursor_mode = _libs['grass_dbmiclient.7.0.svn'].db_set_cursor_mode
    db_set_cursor_mode.restype = None
    db_set_cursor_mode.argtypes = [POINTER(dbCursor), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 320
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_cursor_mode_insensitive'):
    db_set_cursor_mode_insensitive = _libs['grass_dbmiclient.7.0.svn'].db_set_cursor_mode_insensitive
    db_set_cursor_mode_insensitive.restype = None
    db_set_cursor_mode_insensitive.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 321
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_cursor_mode_scroll'):
    db_set_cursor_mode_scroll = _libs['grass_dbmiclient.7.0.svn'].db_set_cursor_mode_scroll
    db_set_cursor_mode_scroll.restype = None
    db_set_cursor_mode_scroll.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 322
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_cursor_table'):
    db_set_cursor_table = _libs['grass_dbmiclient.7.0.svn'].db_set_cursor_table
    db_set_cursor_table.restype = None
    db_set_cursor_table.argtypes = [POINTER(dbCursor), POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 323
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_cursor_token'):
    db_set_cursor_token = _libs['grass_dbmiclient.7.0.svn'].db_set_cursor_token
    db_set_cursor_token.restype = None
    db_set_cursor_token.argtypes = [POINTER(dbCursor), dbToken]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 324
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_cursor_type_insert'):
    db_set_cursor_type_insert = _libs['grass_dbmiclient.7.0.svn'].db_set_cursor_type_insert
    db_set_cursor_type_insert.restype = None
    db_set_cursor_type_insert.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 325
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_cursor_type_readonly'):
    db_set_cursor_type_readonly = _libs['grass_dbmiclient.7.0.svn'].db_set_cursor_type_readonly
    db_set_cursor_type_readonly.restype = None
    db_set_cursor_type_readonly.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 326
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_cursor_type_update'):
    db_set_cursor_type_update = _libs['grass_dbmiclient.7.0.svn'].db_set_cursor_type_update
    db_set_cursor_type_update.restype = None
    db_set_cursor_type_update.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 327
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_default_connection'):
    db_set_default_connection = _libs['grass_dbmiclient.7.0.svn'].db_set_default_connection
    db_set_default_connection.restype = c_int
    db_set_default_connection.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 328
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_error_who'):
    db_set_error_who = _libs['grass_dbmiclient.7.0.svn'].db_set_error_who
    db_set_error_who.restype = None
    db_set_error_who.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 329
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_handle'):
    db_set_handle = _libs['grass_dbmiclient.7.0.svn'].db_set_handle
    db_set_handle.restype = c_int
    db_set_handle.argtypes = [POINTER(dbHandle), String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 330
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_index_column_name'):
    db_set_index_column_name = _libs['grass_dbmiclient.7.0.svn'].db_set_index_column_name
    db_set_index_column_name.restype = c_int
    db_set_index_column_name.argtypes = [POINTER(dbIndex), c_int, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 332
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_index_name'):
    db_set_index_name = _libs['grass_dbmiclient.7.0.svn'].db_set_index_name
    db_set_index_name.restype = c_int
    db_set_index_name.argtypes = [POINTER(dbIndex), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 333
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_index_table_name'):
    db_set_index_table_name = _libs['grass_dbmiclient.7.0.svn'].db_set_index_table_name
    db_set_index_table_name.restype = c_int
    db_set_index_table_name.argtypes = [POINTER(dbIndex), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 334
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_index_type_non_unique'):
    db_set_index_type_non_unique = _libs['grass_dbmiclient.7.0.svn'].db_set_index_type_non_unique
    db_set_index_type_non_unique.restype = c_int
    db_set_index_type_non_unique.argtypes = [POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 335
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_index_type_unique'):
    db_set_index_type_unique = _libs['grass_dbmiclient.7.0.svn'].db_set_index_type_unique
    db_set_index_type_unique.restype = c_int
    db_set_index_type_unique.argtypes = [POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 336
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__set_protocol_fds'):
    db__set_protocol_fds = _libs['grass_dbmiclient.7.0.svn'].db__set_protocol_fds
    db__set_protocol_fds.restype = None
    db__set_protocol_fds.argtypes = [POINTER(FILE), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 337
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_string'):
    db_set_string = _libs['grass_dbmiclient.7.0.svn'].db_set_string
    db_set_string.restype = c_int
    db_set_string.argtypes = [POINTER(dbString), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 338
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_string_no_copy'):
    db_set_string_no_copy = _libs['grass_dbmiclient.7.0.svn'].db_set_string_no_copy
    db_set_string_no_copy.restype = c_int
    db_set_string_no_copy.argtypes = [POINTER(dbString), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 339
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_column'):
    db_set_table_column = _libs['grass_dbmiclient.7.0.svn'].db_set_table_column
    db_set_table_column.restype = c_int
    db_set_table_column.argtypes = [POINTER(dbTable), c_int, POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 340
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_delete_priv_granted'):
    db_set_table_delete_priv_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_table_delete_priv_granted
    db_set_table_delete_priv_granted.restype = None
    db_set_table_delete_priv_granted.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 341
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_delete_priv_not_granted'):
    db_set_table_delete_priv_not_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_table_delete_priv_not_granted
    db_set_table_delete_priv_not_granted.restype = None
    db_set_table_delete_priv_not_granted.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 342
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_description'):
    db_set_table_description = _libs['grass_dbmiclient.7.0.svn'].db_set_table_description
    db_set_table_description.restype = c_int
    db_set_table_description.argtypes = [POINTER(dbTable), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 343
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_insert_priv_granted'):
    db_set_table_insert_priv_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_table_insert_priv_granted
    db_set_table_insert_priv_granted.restype = None
    db_set_table_insert_priv_granted.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 344
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_insert_priv_not_granted'):
    db_set_table_insert_priv_not_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_table_insert_priv_not_granted
    db_set_table_insert_priv_not_granted.restype = None
    db_set_table_insert_priv_not_granted.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 345
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_name'):
    db_set_table_name = _libs['grass_dbmiclient.7.0.svn'].db_set_table_name
    db_set_table_name.restype = c_int
    db_set_table_name.argtypes = [POINTER(dbTable), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 346
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_select_priv_granted'):
    db_set_table_select_priv_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_table_select_priv_granted
    db_set_table_select_priv_granted.restype = None
    db_set_table_select_priv_granted.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 347
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_select_priv_not_granted'):
    db_set_table_select_priv_not_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_table_select_priv_not_granted
    db_set_table_select_priv_not_granted.restype = None
    db_set_table_select_priv_not_granted.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 348
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_update_priv_granted'):
    db_set_table_update_priv_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_table_update_priv_granted
    db_set_table_update_priv_granted.restype = None
    db_set_table_update_priv_granted.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 349
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_table_update_priv_not_granted'):
    db_set_table_update_priv_not_granted = _libs['grass_dbmiclient.7.0.svn'].db_set_table_update_priv_not_granted
    db_set_table_update_priv_not_granted.restype = None
    db_set_table_update_priv_not_granted.argtypes = [POINTER(dbTable)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 350
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_datetime_current'):
    db_set_value_datetime_current = _libs['grass_dbmiclient.7.0.svn'].db_set_value_datetime_current
    db_set_value_datetime_current.restype = None
    db_set_value_datetime_current.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 351
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_datetime_not_current'):
    db_set_value_datetime_not_current = _libs['grass_dbmiclient.7.0.svn'].db_set_value_datetime_not_current
    db_set_value_datetime_not_current.restype = None
    db_set_value_datetime_not_current.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 352
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_day'):
    db_set_value_day = _libs['grass_dbmiclient.7.0.svn'].db_set_value_day
    db_set_value_day.restype = None
    db_set_value_day.argtypes = [POINTER(dbValue), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 353
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_double'):
    db_set_value_double = _libs['grass_dbmiclient.7.0.svn'].db_set_value_double
    db_set_value_double.restype = None
    db_set_value_double.argtypes = [POINTER(dbValue), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 354
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_hour'):
    db_set_value_hour = _libs['grass_dbmiclient.7.0.svn'].db_set_value_hour
    db_set_value_hour.restype = None
    db_set_value_hour.argtypes = [POINTER(dbValue), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 355
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_int'):
    db_set_value_int = _libs['grass_dbmiclient.7.0.svn'].db_set_value_int
    db_set_value_int.restype = None
    db_set_value_int.argtypes = [POINTER(dbValue), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 356
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_minute'):
    db_set_value_minute = _libs['grass_dbmiclient.7.0.svn'].db_set_value_minute
    db_set_value_minute.restype = None
    db_set_value_minute.argtypes = [POINTER(dbValue), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 357
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_month'):
    db_set_value_month = _libs['grass_dbmiclient.7.0.svn'].db_set_value_month
    db_set_value_month.restype = None
    db_set_value_month.argtypes = [POINTER(dbValue), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 358
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_not_null'):
    db_set_value_not_null = _libs['grass_dbmiclient.7.0.svn'].db_set_value_not_null
    db_set_value_not_null.restype = None
    db_set_value_not_null.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 359
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_null'):
    db_set_value_null = _libs['grass_dbmiclient.7.0.svn'].db_set_value_null
    db_set_value_null.restype = None
    db_set_value_null.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 360
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_seconds'):
    db_set_value_seconds = _libs['grass_dbmiclient.7.0.svn'].db_set_value_seconds
    db_set_value_seconds.restype = None
    db_set_value_seconds.argtypes = [POINTER(dbValue), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 361
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_string'):
    db_set_value_string = _libs['grass_dbmiclient.7.0.svn'].db_set_value_string
    db_set_value_string.restype = c_int
    db_set_value_string.argtypes = [POINTER(dbValue), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 362
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_value_year'):
    db_set_value_year = _libs['grass_dbmiclient.7.0.svn'].db_set_value_year
    db_set_value_year.restype = None
    db_set_value_year.argtypes = [POINTER(dbValue), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 363
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_shutdown_driver'):
    db_shutdown_driver = _libs['grass_dbmiclient.7.0.svn'].db_shutdown_driver
    db_shutdown_driver.restype = c_int
    db_shutdown_driver.argtypes = [POINTER(dbDriver)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 364
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_sqltype_name'):
    db_sqltype_name = _libs['grass_dbmiclient.7.0.svn'].db_sqltype_name
    db_sqltype_name.restype = ReturnString
    db_sqltype_name.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 365
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_sqltype_to_Ctype'):
    db_sqltype_to_Ctype = _libs['grass_dbmiclient.7.0.svn'].db_sqltype_to_Ctype
    db_sqltype_to_Ctype.restype = c_int
    db_sqltype_to_Ctype.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 366
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_start_driver'):
    db_start_driver = _libs['grass_dbmiclient.7.0.svn'].db_start_driver
    db_start_driver.restype = POINTER(dbDriver)
    db_start_driver.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 367
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_start_driver_open_database'):
    db_start_driver_open_database = _libs['grass_dbmiclient.7.0.svn'].db_start_driver_open_database
    db_start_driver_open_database.restype = POINTER(dbDriver)
    db_start_driver_open_database.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 368
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db__start_procedure_call'):
    db__start_procedure_call = _libs['grass_dbmiclient.7.0.svn'].db__start_procedure_call
    db__start_procedure_call.restype = c_int
    db__start_procedure_call.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 369
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_store'):
    db_store = _libs['grass_dbmiclient.7.0.svn'].db_store
    db_store.restype = ReturnString
    db_store.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 370
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_strip'):
    db_strip = _libs['grass_dbmiclient.7.0.svn'].db_strip
    db_strip.restype = None
    db_strip.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 371
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_syserror'):
    db_syserror = _libs['grass_dbmiclient.7.0.svn'].db_syserror
    db_syserror.restype = None
    db_syserror.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 372
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_table_exists'):
    db_table_exists = _libs['grass_dbmiclient.7.0.svn'].db_table_exists
    db_table_exists.restype = c_int
    db_table_exists.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 374
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_column_has_default_value'):
    db_test_column_has_default_value = _libs['grass_dbmiclient.7.0.svn'].db_test_column_has_default_value
    db_test_column_has_default_value.restype = c_int
    db_test_column_has_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 375
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_column_has_defined_default_value'):
    db_test_column_has_defined_default_value = _libs['grass_dbmiclient.7.0.svn'].db_test_column_has_defined_default_value
    db_test_column_has_defined_default_value.restype = c_int
    db_test_column_has_defined_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 376
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_column_has_undefined_default_value'):
    db_test_column_has_undefined_default_value = _libs['grass_dbmiclient.7.0.svn'].db_test_column_has_undefined_default_value
    db_test_column_has_undefined_default_value.restype = c_int
    db_test_column_has_undefined_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 377
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_column_null_allowed'):
    db_test_column_null_allowed = _libs['grass_dbmiclient.7.0.svn'].db_test_column_null_allowed
    db_test_column_null_allowed.restype = c_int
    db_test_column_null_allowed.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 378
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_column_use_default_value'):
    db_test_column_use_default_value = _libs['grass_dbmiclient.7.0.svn'].db_test_column_use_default_value
    db_test_column_use_default_value.restype = c_int
    db_test_column_use_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 379
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_cursor_any_column_flag'):
    db_test_cursor_any_column_flag = _libs['grass_dbmiclient.7.0.svn'].db_test_cursor_any_column_flag
    db_test_cursor_any_column_flag.restype = c_int
    db_test_cursor_any_column_flag.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 380
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_cursor_any_column_for_update'):
    db_test_cursor_any_column_for_update = _libs['grass_dbmiclient.7.0.svn'].db_test_cursor_any_column_for_update
    db_test_cursor_any_column_for_update.restype = c_int
    db_test_cursor_any_column_for_update.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 381
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_cursor_column_flag'):
    db_test_cursor_column_flag = _libs['grass_dbmiclient.7.0.svn'].db_test_cursor_column_flag
    db_test_cursor_column_flag.restype = c_int
    db_test_cursor_column_flag.argtypes = [POINTER(dbCursor), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 382
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_cursor_column_for_update'):
    db_test_cursor_column_for_update = _libs['grass_dbmiclient.7.0.svn'].db_test_cursor_column_for_update
    db_test_cursor_column_for_update.restype = c_int
    db_test_cursor_column_for_update.argtypes = [POINTER(dbCursor), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 383
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_cursor_mode_insensitive'):
    db_test_cursor_mode_insensitive = _libs['grass_dbmiclient.7.0.svn'].db_test_cursor_mode_insensitive
    db_test_cursor_mode_insensitive.restype = c_int
    db_test_cursor_mode_insensitive.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 384
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_cursor_mode_scroll'):
    db_test_cursor_mode_scroll = _libs['grass_dbmiclient.7.0.svn'].db_test_cursor_mode_scroll
    db_test_cursor_mode_scroll.restype = c_int
    db_test_cursor_mode_scroll.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 385
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_cursor_type_fetch'):
    db_test_cursor_type_fetch = _libs['grass_dbmiclient.7.0.svn'].db_test_cursor_type_fetch
    db_test_cursor_type_fetch.restype = c_int
    db_test_cursor_type_fetch.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 386
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_cursor_type_insert'):
    db_test_cursor_type_insert = _libs['grass_dbmiclient.7.0.svn'].db_test_cursor_type_insert
    db_test_cursor_type_insert.restype = c_int
    db_test_cursor_type_insert.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 387
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_cursor_type_update'):
    db_test_cursor_type_update = _libs['grass_dbmiclient.7.0.svn'].db_test_cursor_type_update
    db_test_cursor_type_update.restype = c_int
    db_test_cursor_type_update.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 388
for _lib in _libs.values():
    if hasattr(_lib, 'db__test_database_open'):
        db__test_database_open = _lib.db__test_database_open
        db__test_database_open.restype = c_int
        db__test_database_open.argtypes = []
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 389
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_index_type_unique'):
    db_test_index_type_unique = _libs['grass_dbmiclient.7.0.svn'].db_test_index_type_unique
    db_test_index_type_unique.restype = c_int
    db_test_index_type_unique.argtypes = [POINTER(dbIndex)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 390
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_value_datetime_current'):
    db_test_value_datetime_current = _libs['grass_dbmiclient.7.0.svn'].db_test_value_datetime_current
    db_test_value_datetime_current.restype = c_int
    db_test_value_datetime_current.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 391
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_test_value_isnull'):
    db_test_value_isnull = _libs['grass_dbmiclient.7.0.svn'].db_test_value_isnull
    db_test_value_isnull.restype = c_int
    db_test_value_isnull.argtypes = [POINTER(dbValue)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 392
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_unset_column_has_default_value'):
    db_unset_column_has_default_value = _libs['grass_dbmiclient.7.0.svn'].db_unset_column_has_default_value
    db_unset_column_has_default_value.restype = None
    db_unset_column_has_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 393
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_unset_column_null_allowed'):
    db_unset_column_null_allowed = _libs['grass_dbmiclient.7.0.svn'].db_unset_column_null_allowed
    db_unset_column_null_allowed.restype = None
    db_unset_column_null_allowed.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 394
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_unset_column_use_default_value'):
    db_unset_column_use_default_value = _libs['grass_dbmiclient.7.0.svn'].db_unset_column_use_default_value
    db_unset_column_use_default_value.restype = None
    db_unset_column_use_default_value.argtypes = [POINTER(dbColumn)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 395
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_unset_cursor_column_flag'):
    db_unset_cursor_column_flag = _libs['grass_dbmiclient.7.0.svn'].db_unset_cursor_column_flag
    db_unset_cursor_column_flag.restype = None
    db_unset_cursor_column_flag.argtypes = [POINTER(dbCursor), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 396
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_unset_cursor_column_for_update'):
    db_unset_cursor_column_for_update = _libs['grass_dbmiclient.7.0.svn'].db_unset_cursor_column_for_update
    db_unset_cursor_column_for_update.restype = None
    db_unset_cursor_column_for_update.argtypes = [POINTER(dbCursor), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 397
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_unset_cursor_mode'):
    db_unset_cursor_mode = _libs['grass_dbmiclient.7.0.svn'].db_unset_cursor_mode
    db_unset_cursor_mode.restype = None
    db_unset_cursor_mode.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 398
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_unset_cursor_mode_insensitive'):
    db_unset_cursor_mode_insensitive = _libs['grass_dbmiclient.7.0.svn'].db_unset_cursor_mode_insensitive
    db_unset_cursor_mode_insensitive.restype = None
    db_unset_cursor_mode_insensitive.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 399
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_unset_cursor_mode_scroll'):
    db_unset_cursor_mode_scroll = _libs['grass_dbmiclient.7.0.svn'].db_unset_cursor_mode_scroll
    db_unset_cursor_mode_scroll.restype = None
    db_unset_cursor_mode_scroll.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 400
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_update'):
    db_update = _libs['grass_dbmiclient.7.0.svn'].db_update
    db_update.restype = c_int
    db_update.argtypes = [POINTER(dbCursor)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 401
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_gversion'):
    db_gversion = _libs['grass_dbmiclient.7.0.svn'].db_gversion
    db_gversion.restype = c_int
    db_gversion.argtypes = [POINTER(dbDriver), POINTER(dbString), POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 403
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_whoami'):
    db_whoami = _libs['grass_dbmiclient.7.0.svn'].db_whoami
    db_whoami.restype = ReturnString
    db_whoami.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 404
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_zero'):
    db_zero = _libs['grass_dbmiclient.7.0.svn'].db_zero
    db_zero.restype = None
    db_zero.argtypes = [POINTER(None), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 405
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_zero_string'):
    db_zero_string = _libs['grass_dbmiclient.7.0.svn'].db_zero_string
    db_zero_string.restype = None
    db_zero_string.argtypes = [POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 406
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_sizeof_string'):
    db_sizeof_string = _libs['grass_dbmiclient.7.0.svn'].db_sizeof_string
    db_sizeof_string.restype = c_uint
    db_sizeof_string.argtypes = [POINTER(dbString)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 407
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_set_login'):
    db_set_login = _libs['grass_dbmiclient.7.0.svn'].db_set_login
    db_set_login.restype = c_int
    db_set_login.argtypes = [String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmidefs.h: 408
if hasattr(_libs['grass_dbmiclient.7.0.svn'], 'db_get_login'):
    db_get_login = _libs['grass_dbmiclient.7.0.svn'].db_get_login
    db_get_login.restype = c_int
    db_get_login.argtypes = [String, String, POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 18
try:
    DB_VERSION = '0'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 19
try:
    DB_DEFAULT_DRIVER = 'sqlite'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 21
try:
    DB_PROC_VERSION = 999
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 22
try:
    DB_PROC_CLOSE_DATABASE = 101
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 22
try:
    DB_PROC_CREATE_DATABASE = 102
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 22
try:
    DB_PROC_DELETE_DATABASE = 103
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 22
try:
    DB_PROC_FIND_DATABASE = 104
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 22
try:
    DB_PROC_LIST_DATABASES = 105
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 22
try:
    DB_PROC_OPEN_DATABASE = 106
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 22
try:
    DB_PROC_SHUTDOWN_DRIVER = 107
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_CLOSE_CURSOR = 201
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_DELETE = 202
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_FETCH = 203
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_INSERT = 204
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_OPEN_INSERT_CURSOR = 205
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_OPEN_SELECT_CURSOR = 206
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_OPEN_UPDATE_CURSOR = 207
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_UPDATE = 208
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_ROWS = 209
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_BIND_UPDATE = 220
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 23
try:
    DB_PROC_BIND_INSERT = 221
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 24
try:
    DB_PROC_EXECUTE_IMMEDIATE = 301
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 24
try:
    DB_PROC_BEGIN_TRANSACTION = 302
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 24
try:
    DB_PROC_COMMIT_TRANSACTION = 303
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 25
try:
    DB_PROC_CREATE_TABLE = 401
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 25
try:
    DB_PROC_DESCRIBE_TABLE = 402
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 25
try:
    DB_PROC_DROP_TABLE = 403
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 25
try:
    DB_PROC_LIST_TABLES = 404
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 25
try:
    DB_PROC_ADD_COLUMN = 405
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 25
try:
    DB_PROC_DROP_COLUMN = 406
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 25
try:
    DB_PROC_GRANT_ON_TABLE = 407
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 26
try:
    DB_PROC_CREATE_INDEX = 701
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 26
try:
    DB_PROC_LIST_INDEXES = 702
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 26
try:
    DB_PROC_DROP_INDEX = 703
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 28
try:
    DB_PERM_R = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 28
try:
    DB_PERM_W = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 28
try:
    DB_PERM_X = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 30
try:
    DB_OK = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 30
try:
    DB_FAILED = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 30
try:
    DB_NOPROC = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 30
try:
    DB_MEMORY_ERR = (-1)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 30
try:
    DB_PROTOCOL_ERR = (-2)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 30
try:
    DB_EOF = (-1)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 32
try:
    DB_SQL_TYPE_UNKNOWN = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_CHARACTER = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_SMALLINT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_INTEGER = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_REAL = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_DOUBLE_PRECISION = 6
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_DECIMAL = 7
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_NUMERIC = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_DATE = 9
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_TIME = 10
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_TIMESTAMP = 11
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_INTERVAL = 12
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 33
try:
    DB_SQL_TYPE_TEXT = 13
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 34
try:
    DB_SQL_TYPE_SERIAL = 21
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 36
try:
    DB_YEAR = 16384
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 36
try:
    DB_MONTH = 8192
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 36
try:
    DB_DAY = 4096
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 36
try:
    DB_HOUR = 2048
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 36
try:
    DB_MINUTE = 1024
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 36
try:
    DB_SECOND = 512
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 36
try:
    DB_FRACTION = 256
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 36
try:
    DB_DATETIME_MASK = 65280
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 38
try:
    DB_C_TYPE_STRING = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 38
try:
    DB_C_TYPE_INT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 38
try:
    DB_C_TYPE_DOUBLE = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 38
try:
    DB_C_TYPE_DATETIME = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 40
try:
    DB_CURRENT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 40
try:
    DB_NEXT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 40
try:
    DB_PREVIOUS = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 40
try:
    DB_FIRST = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 40
try:
    DB_LAST = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 42
try:
    DB_READONLY = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 42
try:
    DB_INSERT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 42
try:
    DB_UPDATE = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 42
try:
    DB_SEQUENTIAL = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 42
try:
    DB_SCROLL = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 42
try:
    DB_INSENSITIVE = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 44
try:
    DB_GRANTED = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 44
try:
    DB_NOT_GRANTED = (-1)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 46
try:
    DB_PRIV_SELECT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 47
try:
    DB_GROUP = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 47
try:
    DB_PUBLIC = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 49
try:
    DB_DEFINED = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 49
try:
    DB_UNDEFINED = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 51
try:
    DB_SQL_MAX = 4096
except:
    pass

_db_string = struct__db_string # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 147

_dbmscap = struct__dbmscap # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 149

_db_dirent = struct__db_dirent # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 162

_db_driver = struct__db_driver # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 169

_db_handle = struct__db_handle # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 176

_db_date_time = struct__db_date_time # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 187

_db_value = struct__db_value # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 196

_db_column = struct__db_column # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 214

_db_table = struct__db_table # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 224

_db_cursor = struct__db_cursor # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 234

_db_index = struct__db_index # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 243

_db_driver_state = struct__db_driver_state # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 252

_db_connection = struct__db_connection # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dbmi.h: 300

# No inserted files

