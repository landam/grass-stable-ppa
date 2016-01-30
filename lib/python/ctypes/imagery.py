'''Wrapper for imagery.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_imagery.7.0.svn /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h -o imagery.py

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

_libs["grass_imagery.7.0.svn"] = load_library("grass_imagery.7.0.svn")

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

CELL = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 402

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 10
class struct_Ref_Color(Structure):
    pass

struct_Ref_Color.__slots__ = [
    'table',
    'index',
    'buf',
    'fd',
    'min',
    'max',
    'n',
]
struct_Ref_Color._fields_ = [
    ('table', POINTER(c_ubyte)),
    ('index', POINTER(c_ubyte)),
    ('buf', POINTER(c_ubyte)),
    ('fd', c_int),
    ('min', CELL),
    ('max', CELL),
    ('n', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 20
class struct_Ref_Files(Structure):
    pass

struct_Ref_Files.__slots__ = [
    'name',
    'mapset',
]
struct_Ref_Files._fields_ = [
    ('name', c_char * 256),
    ('mapset', c_char * 256),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 26
class struct_Ref(Structure):
    pass

struct_Ref.__slots__ = [
    'nfiles',
    'file',
    'red',
    'grn',
    'blu',
]
struct_Ref._fields_ = [
    ('nfiles', c_int),
    ('file', POINTER(struct_Ref_Files)),
    ('red', struct_Ref_Color),
    ('grn', struct_Ref_Color),
    ('blu', struct_Ref_Color),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 33
class struct_Tape_Info(Structure):
    pass

struct_Tape_Info.__slots__ = [
    'title',
    'id',
    'desc',
]
struct_Tape_Info._fields_ = [
    ('title', c_char * 75),
    ('id', (c_char * 75) * 2),
    ('desc', (c_char * 75) * 5),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 40
class struct_Control_Points(Structure):
    pass

struct_Control_Points.__slots__ = [
    'count',
    'e1',
    'n1',
    'e2',
    'n2',
    'status',
]
struct_Control_Points._fields_ = [
    ('count', c_int),
    ('e1', POINTER(c_double)),
    ('n1', POINTER(c_double)),
    ('e2', POINTER(c_double)),
    ('n2', POINTER(c_double)),
    ('status', POINTER(c_int)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 50
class struct_One_Sig(Structure):
    pass

struct_One_Sig.__slots__ = [
    'desc',
    'npoints',
    'mean',
    'var',
    'status',
    'r',
    'g',
    'b',
    'have_color',
]
struct_One_Sig._fields_ = [
    ('desc', c_char * 100),
    ('npoints', c_int),
    ('mean', POINTER(c_double)),
    ('var', POINTER(POINTER(c_double))),
    ('status', c_int),
    ('r', c_float),
    ('g', c_float),
    ('b', c_float),
    ('have_color', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 61
class struct_Signature(Structure):
    pass

struct_Signature.__slots__ = [
    'nbands',
    'nsigs',
    'title',
    'sig',
]
struct_Signature._fields_ = [
    ('nbands', c_int),
    ('nsigs', c_int),
    ('title', c_char * 100),
    ('sig', POINTER(struct_One_Sig)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 69
class struct_SubSig(Structure):
    pass

struct_SubSig.__slots__ = [
    'N',
    'pi',
    'means',
    'R',
    'Rinv',
    'cnst',
    'used',
]
struct_SubSig._fields_ = [
    ('N', c_double),
    ('pi', c_double),
    ('means', POINTER(c_double)),
    ('R', POINTER(POINTER(c_double))),
    ('Rinv', POINTER(POINTER(c_double))),
    ('cnst', c_double),
    ('used', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 80
class struct_ClassData(Structure):
    pass

struct_ClassData.__slots__ = [
    'npixels',
    'count',
    'x',
    'p',
]
struct_ClassData._fields_ = [
    ('npixels', c_int),
    ('count', c_int),
    ('x', POINTER(POINTER(c_double))),
    ('p', POINTER(POINTER(c_double))),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 88
class struct_ClassSig(Structure):
    pass

struct_ClassSig.__slots__ = [
    'classnum',
    'title',
    'used',
    'type',
    'nsubclasses',
    'SubSig',
    'ClassData',
]
struct_ClassSig._fields_ = [
    ('classnum', c_long),
    ('title', String),
    ('used', c_int),
    ('type', c_int),
    ('nsubclasses', c_int),
    ('SubSig', POINTER(struct_SubSig)),
    ('ClassData', struct_ClassData),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 99
class struct_SigSet(Structure):
    pass

struct_SigSet.__slots__ = [
    'nbands',
    'nclasses',
    'title',
    'ClassSig',
]
struct_SigSet._fields_ = [
    ('nbands', c_int),
    ('nclasses', c_int),
    ('title', String),
    ('ClassSig', POINTER(struct_ClassSig)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 5
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_malloc'):
    I_malloc = _libs['grass_imagery.7.0.svn'].I_malloc
    I_malloc.restype = POINTER(None)
    I_malloc.argtypes = [c_size_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 6
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_realloc'):
    I_realloc = _libs['grass_imagery.7.0.svn'].I_realloc
    I_realloc.restype = POINTER(None)
    I_realloc.argtypes = [POINTER(None), c_size_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 7
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_free'):
    I_free = _libs['grass_imagery.7.0.svn'].I_free
    I_free.restype = c_int
    I_free.argtypes = [POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 8
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_alloc_double2'):
    I_alloc_double2 = _libs['grass_imagery.7.0.svn'].I_alloc_double2
    I_alloc_double2.restype = POINTER(POINTER(c_double))
    I_alloc_double2.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 9
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_alloc_int'):
    I_alloc_int = _libs['grass_imagery.7.0.svn'].I_alloc_int
    I_alloc_int.restype = POINTER(c_int)
    I_alloc_int.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 10
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_alloc_int2'):
    I_alloc_int2 = _libs['grass_imagery.7.0.svn'].I_alloc_int2
    I_alloc_int2.restype = POINTER(POINTER(c_int))
    I_alloc_int2.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 11
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_free_int2'):
    I_free_int2 = _libs['grass_imagery.7.0.svn'].I_free_int2
    I_free_int2.restype = c_int
    I_free_int2.argtypes = [POINTER(POINTER(c_int))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 12
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_free_double2'):
    I_free_double2 = _libs['grass_imagery.7.0.svn'].I_free_double2
    I_free_double2.restype = c_int
    I_free_double2.argtypes = [POINTER(POINTER(c_double))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 13
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_alloc_double3'):
    I_alloc_double3 = _libs['grass_imagery.7.0.svn'].I_alloc_double3
    I_alloc_double3.restype = POINTER(POINTER(POINTER(c_double)))
    I_alloc_double3.argtypes = [c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 14
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_free_double3'):
    I_free_double3 = _libs['grass_imagery.7.0.svn'].I_free_double3
    I_free_double3.restype = c_int
    I_free_double3.argtypes = [POINTER(POINTER(POINTER(c_double)))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 17
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_get_to_eol'):
    I_get_to_eol = _libs['grass_imagery.7.0.svn'].I_get_to_eol
    I_get_to_eol.restype = c_int
    I_get_to_eol.argtypes = [String, c_int, POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 20
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_find_group'):
    I_find_group = _libs['grass_imagery.7.0.svn'].I_find_group
    I_find_group.restype = c_int
    I_find_group.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 21
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_find_group_file'):
    I_find_group_file = _libs['grass_imagery.7.0.svn'].I_find_group_file
    I_find_group_file.restype = c_int
    I_find_group_file.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 22
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_find_subgroup'):
    I_find_subgroup = _libs['grass_imagery.7.0.svn'].I_find_subgroup
    I_find_subgroup.restype = c_int
    I_find_subgroup.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 23
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_find_subgroup_file'):
    I_find_subgroup_file = _libs['grass_imagery.7.0.svn'].I_find_subgroup_file
    I_find_subgroup_file.restype = c_int
    I_find_subgroup_file.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 26
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_group_file_new'):
    I_fopen_group_file_new = _libs['grass_imagery.7.0.svn'].I_fopen_group_file_new
    I_fopen_group_file_new.restype = POINTER(FILE)
    I_fopen_group_file_new.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 27
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_group_file_append'):
    I_fopen_group_file_append = _libs['grass_imagery.7.0.svn'].I_fopen_group_file_append
    I_fopen_group_file_append.restype = POINTER(FILE)
    I_fopen_group_file_append.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 28
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_group_file_old'):
    I_fopen_group_file_old = _libs['grass_imagery.7.0.svn'].I_fopen_group_file_old
    I_fopen_group_file_old.restype = POINTER(FILE)
    I_fopen_group_file_old.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 29
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_subgroup_file_new'):
    I_fopen_subgroup_file_new = _libs['grass_imagery.7.0.svn'].I_fopen_subgroup_file_new
    I_fopen_subgroup_file_new.restype = POINTER(FILE)
    I_fopen_subgroup_file_new.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 30
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_subgroup_file_append'):
    I_fopen_subgroup_file_append = _libs['grass_imagery.7.0.svn'].I_fopen_subgroup_file_append
    I_fopen_subgroup_file_append.restype = POINTER(FILE)
    I_fopen_subgroup_file_append.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 31
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_subgroup_file_old'):
    I_fopen_subgroup_file_old = _libs['grass_imagery.7.0.svn'].I_fopen_subgroup_file_old
    I_fopen_subgroup_file_old.restype = POINTER(FILE)
    I_fopen_subgroup_file_old.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 34
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_compute_georef_equations'):
    I_compute_georef_equations = _libs['grass_imagery.7.0.svn'].I_compute_georef_equations
    I_compute_georef_equations.restype = c_int
    I_compute_georef_equations.argtypes = [POINTER(struct_Control_Points), c_double * 3, c_double * 3, c_double * 3, c_double * 3]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 36
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_georef'):
    I_georef = _libs['grass_imagery.7.0.svn'].I_georef
    I_georef.restype = c_int
    I_georef.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), c_double * 3, c_double * 3]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 39
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_get_group'):
    I_get_group = _libs['grass_imagery.7.0.svn'].I_get_group
    I_get_group.restype = c_int
    I_get_group.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 40
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_put_group'):
    I_put_group = _libs['grass_imagery.7.0.svn'].I_put_group
    I_put_group.restype = c_int
    I_put_group.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 41
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_get_subgroup'):
    I_get_subgroup = _libs['grass_imagery.7.0.svn'].I_get_subgroup
    I_get_subgroup.restype = c_int
    I_get_subgroup.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 42
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_put_subgroup'):
    I_put_subgroup = _libs['grass_imagery.7.0.svn'].I_put_subgroup
    I_put_subgroup.restype = c_int
    I_put_subgroup.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 43
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_get_group_ref'):
    I_get_group_ref = _libs['grass_imagery.7.0.svn'].I_get_group_ref
    I_get_group_ref.restype = c_int
    I_get_group_ref.argtypes = [String, POINTER(struct_Ref)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 44
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_get_subgroup_ref'):
    I_get_subgroup_ref = _libs['grass_imagery.7.0.svn'].I_get_subgroup_ref
    I_get_subgroup_ref.restype = c_int
    I_get_subgroup_ref.argtypes = [String, String, POINTER(struct_Ref)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 45
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_init_ref_color_nums'):
    I_init_ref_color_nums = _libs['grass_imagery.7.0.svn'].I_init_ref_color_nums
    I_init_ref_color_nums.restype = c_int
    I_init_ref_color_nums.argtypes = [POINTER(struct_Ref)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 46
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_put_group_ref'):
    I_put_group_ref = _libs['grass_imagery.7.0.svn'].I_put_group_ref
    I_put_group_ref.restype = c_int
    I_put_group_ref.argtypes = [String, POINTER(struct_Ref)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 47
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_put_subgroup_ref'):
    I_put_subgroup_ref = _libs['grass_imagery.7.0.svn'].I_put_subgroup_ref
    I_put_subgroup_ref.restype = c_int
    I_put_subgroup_ref.argtypes = [String, String, POINTER(struct_Ref)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 48
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_add_file_to_group_ref'):
    I_add_file_to_group_ref = _libs['grass_imagery.7.0.svn'].I_add_file_to_group_ref
    I_add_file_to_group_ref.restype = c_int
    I_add_file_to_group_ref.argtypes = [String, String, POINTER(struct_Ref)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 49
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_transfer_group_ref_file'):
    I_transfer_group_ref_file = _libs['grass_imagery.7.0.svn'].I_transfer_group_ref_file
    I_transfer_group_ref_file.restype = c_int
    I_transfer_group_ref_file.argtypes = [POINTER(struct_Ref), c_int, POINTER(struct_Ref)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 50
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_init_group_ref'):
    I_init_group_ref = _libs['grass_imagery.7.0.svn'].I_init_group_ref
    I_init_group_ref.restype = c_int
    I_init_group_ref.argtypes = [POINTER(struct_Ref)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 51
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_free_group_ref'):
    I_free_group_ref = _libs['grass_imagery.7.0.svn'].I_free_group_ref
    I_free_group_ref.restype = c_int
    I_free_group_ref.argtypes = [POINTER(struct_Ref)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 54
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_list_group'):
    I_list_group = _libs['grass_imagery.7.0.svn'].I_list_group
    I_list_group.restype = c_int
    I_list_group.argtypes = [String, POINTER(struct_Ref), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 55
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_list_group_simple'):
    I_list_group_simple = _libs['grass_imagery.7.0.svn'].I_list_group_simple
    I_list_group_simple.restype = c_int
    I_list_group_simple.argtypes = [POINTER(struct_Ref), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 58
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_list_subgroup'):
    I_list_subgroup = _libs['grass_imagery.7.0.svn'].I_list_subgroup
    I_list_subgroup.restype = c_int
    I_list_subgroup.argtypes = [String, String, POINTER(struct_Ref), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 59
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_list_subgroup_simple'):
    I_list_subgroup_simple = _libs['grass_imagery.7.0.svn'].I_list_subgroup_simple
    I_list_subgroup_simple.restype = c_int
    I_list_subgroup_simple.argtypes = [POINTER(struct_Ref), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 62
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_location_info'):
    I_location_info = _libs['grass_imagery.7.0.svn'].I_location_info
    I_location_info.restype = ReturnString
    I_location_info.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 65
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_new_control_point'):
    I_new_control_point = _libs['grass_imagery.7.0.svn'].I_new_control_point
    I_new_control_point.restype = c_int
    I_new_control_point.argtypes = [POINTER(struct_Control_Points), c_double, c_double, c_double, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 67
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_get_control_points'):
    I_get_control_points = _libs['grass_imagery.7.0.svn'].I_get_control_points
    I_get_control_points.restype = c_int
    I_get_control_points.argtypes = [String, POINTER(struct_Control_Points)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 68
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_put_control_points'):
    I_put_control_points = _libs['grass_imagery.7.0.svn'].I_put_control_points
    I_put_control_points.restype = c_int
    I_put_control_points.argtypes = [String, POINTER(struct_Control_Points)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 71
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_group_ref_new'):
    I_fopen_group_ref_new = _libs['grass_imagery.7.0.svn'].I_fopen_group_ref_new
    I_fopen_group_ref_new.restype = POINTER(FILE)
    I_fopen_group_ref_new.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 72
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_group_ref_old'):
    I_fopen_group_ref_old = _libs['grass_imagery.7.0.svn'].I_fopen_group_ref_old
    I_fopen_group_ref_old.restype = POINTER(FILE)
    I_fopen_group_ref_old.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 73
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_subgroup_ref_new'):
    I_fopen_subgroup_ref_new = _libs['grass_imagery.7.0.svn'].I_fopen_subgroup_ref_new
    I_fopen_subgroup_ref_new.restype = POINTER(FILE)
    I_fopen_subgroup_ref_new.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 74
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_subgroup_ref_old'):
    I_fopen_subgroup_ref_old = _libs['grass_imagery.7.0.svn'].I_fopen_subgroup_ref_old
    I_fopen_subgroup_ref_old.restype = POINTER(FILE)
    I_fopen_subgroup_ref_old.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 77
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_init_signatures'):
    I_init_signatures = _libs['grass_imagery.7.0.svn'].I_init_signatures
    I_init_signatures.restype = c_int
    I_init_signatures.argtypes = [POINTER(struct_Signature), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 78
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_new_signature'):
    I_new_signature = _libs['grass_imagery.7.0.svn'].I_new_signature
    I_new_signature.restype = c_int
    I_new_signature.argtypes = [POINTER(struct_Signature)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 79
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_free_signatures'):
    I_free_signatures = _libs['grass_imagery.7.0.svn'].I_free_signatures
    I_free_signatures.restype = c_int
    I_free_signatures.argtypes = [POINTER(struct_Signature)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 80
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_read_one_signature'):
    I_read_one_signature = _libs['grass_imagery.7.0.svn'].I_read_one_signature
    I_read_one_signature.restype = c_int
    I_read_one_signature.argtypes = [POINTER(FILE), POINTER(struct_Signature)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 81
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_read_signatures'):
    I_read_signatures = _libs['grass_imagery.7.0.svn'].I_read_signatures
    I_read_signatures.restype = c_int
    I_read_signatures.argtypes = [POINTER(FILE), POINTER(struct_Signature)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 82
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_write_signatures'):
    I_write_signatures = _libs['grass_imagery.7.0.svn'].I_write_signatures
    I_write_signatures.restype = c_int
    I_write_signatures.argtypes = [POINTER(FILE), POINTER(struct_Signature)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 85
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_signature_file_new'):
    I_fopen_signature_file_new = _libs['grass_imagery.7.0.svn'].I_fopen_signature_file_new
    I_fopen_signature_file_new.restype = POINTER(FILE)
    I_fopen_signature_file_new.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 86
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_signature_file_old'):
    I_fopen_signature_file_old = _libs['grass_imagery.7.0.svn'].I_fopen_signature_file_old
    I_fopen_signature_file_old.restype = POINTER(FILE)
    I_fopen_signature_file_old.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 89
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_SigSetNClasses'):
    I_SigSetNClasses = _libs['grass_imagery.7.0.svn'].I_SigSetNClasses
    I_SigSetNClasses.restype = c_int
    I_SigSetNClasses.argtypes = [POINTER(struct_SigSet)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 90
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_AllocClassData'):
    I_AllocClassData = _libs['grass_imagery.7.0.svn'].I_AllocClassData
    I_AllocClassData.restype = POINTER(struct_ClassData)
    I_AllocClassData.argtypes = [POINTER(struct_SigSet), POINTER(struct_ClassSig), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 91
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_InitSigSet'):
    I_InitSigSet = _libs['grass_imagery.7.0.svn'].I_InitSigSet
    I_InitSigSet.restype = c_int
    I_InitSigSet.argtypes = [POINTER(struct_SigSet)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 92
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_SigSetNBands'):
    I_SigSetNBands = _libs['grass_imagery.7.0.svn'].I_SigSetNBands
    I_SigSetNBands.restype = c_int
    I_SigSetNBands.argtypes = [POINTER(struct_SigSet), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 93
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_NewClassSig'):
    I_NewClassSig = _libs['grass_imagery.7.0.svn'].I_NewClassSig
    I_NewClassSig.restype = POINTER(struct_ClassSig)
    I_NewClassSig.argtypes = [POINTER(struct_SigSet)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 94
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_NewSubSig'):
    I_NewSubSig = _libs['grass_imagery.7.0.svn'].I_NewSubSig
    I_NewSubSig.restype = POINTER(struct_SubSig)
    I_NewSubSig.argtypes = [POINTER(struct_SigSet), POINTER(struct_ClassSig)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 95
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_ReadSigSet'):
    I_ReadSigSet = _libs['grass_imagery.7.0.svn'].I_ReadSigSet
    I_ReadSigSet.restype = c_int
    I_ReadSigSet.argtypes = [POINTER(FILE), POINTER(struct_SigSet)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 96
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_SetSigTitle'):
    I_SetSigTitle = _libs['grass_imagery.7.0.svn'].I_SetSigTitle
    I_SetSigTitle.restype = c_int
    I_SetSigTitle.argtypes = [POINTER(struct_SigSet), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 97
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_GetSigTitle'):
    I_GetSigTitle = _libs['grass_imagery.7.0.svn'].I_GetSigTitle
    I_GetSigTitle.restype = ReturnString
    I_GetSigTitle.argtypes = [POINTER(struct_SigSet)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 98
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_SetClassTitle'):
    I_SetClassTitle = _libs['grass_imagery.7.0.svn'].I_SetClassTitle
    I_SetClassTitle.restype = c_int
    I_SetClassTitle.argtypes = [POINTER(struct_ClassSig), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 99
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_GetClassTitle'):
    I_GetClassTitle = _libs['grass_imagery.7.0.svn'].I_GetClassTitle
    I_GetClassTitle.restype = ReturnString
    I_GetClassTitle.argtypes = [POINTER(struct_ClassSig)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 100
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_WriteSigSet'):
    I_WriteSigSet = _libs['grass_imagery.7.0.svn'].I_WriteSigSet
    I_WriteSigSet.restype = c_int
    I_WriteSigSet.argtypes = [POINTER(FILE), POINTER(struct_SigSet)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 103
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_sigset_file_new'):
    I_fopen_sigset_file_new = _libs['grass_imagery.7.0.svn'].I_fopen_sigset_file_new
    I_fopen_sigset_file_new.restype = POINTER(FILE)
    I_fopen_sigset_file_new.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 104
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_fopen_sigset_file_old'):
    I_fopen_sigset_file_old = _libs['grass_imagery.7.0.svn'].I_fopen_sigset_file_old
    I_fopen_sigset_file_old.restype = POINTER(FILE)
    I_fopen_sigset_file_old.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 107
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_get_target'):
    I_get_target = _libs['grass_imagery.7.0.svn'].I_get_target
    I_get_target.restype = c_int
    I_get_target.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 108
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_put_target'):
    I_put_target = _libs['grass_imagery.7.0.svn'].I_put_target
    I_put_target.restype = c_int
    I_put_target.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 111
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_get_group_title'):
    I_get_group_title = _libs['grass_imagery.7.0.svn'].I_get_group_title
    I_get_group_title.restype = c_int
    I_get_group_title.argtypes = [String, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 112
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_put_group_title'):
    I_put_group_title = _libs['grass_imagery.7.0.svn'].I_put_group_title
    I_put_group_title.restype = c_int
    I_put_group_title.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 115
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_variance'):
    I_variance = _libs['grass_imagery.7.0.svn'].I_variance
    I_variance.restype = c_double
    I_variance.argtypes = [c_double, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagedefs.h: 116
if hasattr(_libs['grass_imagery.7.0.svn'], 'I_stddev'):
    I_stddev = _libs['grass_imagery.7.0.svn'].I_stddev
    I_stddev.restype = c_double
    I_stddev.argtypes = [c_double, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 78
try:
    GNAME_MAX = 256
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 8
try:
    INAME_LEN = GNAME_MAX
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 106
try:
    SIGNATURE_TYPE_MIXED = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 107
try:
    GROUPFILE = 'CURGROUP'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 107
try:
    SUBGROUPFILE = 'CURSUBGROUP'
except:
    pass

Ref_Color = struct_Ref_Color # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 10

Ref_Files = struct_Ref_Files # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 20

Ref = struct_Ref # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 26

Tape_Info = struct_Tape_Info # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 33

Control_Points = struct_Control_Points # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 40

One_Sig = struct_One_Sig # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 50

Signature = struct_Signature # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 61

SubSig = struct_SubSig # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 69

ClassData = struct_ClassData # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 80

ClassSig = struct_ClassSig # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 88

SigSet = struct_SigSet # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/imagery.h: 99

# No inserted files

