'''Wrapper for vedit.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_vedit.7.0.svn -I/usr/local/include /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h -o vedit.py

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

_libs["grass_vedit.7.0.svn"] = load_library("grass_vedit.7.0.svn")

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

off_t = __off64_t # /usr/include/sys/types.h: 90

dglByte_t = c_ubyte # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/type.h: 36

dglInt32_t = c_long # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/type.h: 37

dglInt64_t = c_longlong # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/type.h: 38

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/heap.h: 33
class union__dglHeapData(Union):
    pass

union__dglHeapData.__slots__ = [
    'pv',
    'n',
    'un',
    'l',
    'ul',
]
union__dglHeapData._fields_ = [
    ('pv', POINTER(None)),
    ('n', c_int),
    ('un', c_uint),
    ('l', c_long),
    ('ul', c_ulong),
]

dglHeapData_u = union__dglHeapData # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/heap.h: 33

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/heap.h: 42
class struct__dglHeapNode(Structure):
    pass

struct__dglHeapNode.__slots__ = [
    'key',
    'value',
    'flags',
]
struct__dglHeapNode._fields_ = [
    ('key', c_long),
    ('value', dglHeapData_u),
    ('flags', c_ubyte),
]

dglHeapNode_s = struct__dglHeapNode # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/heap.h: 42

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/heap.h: 52
class struct__dglHeap(Structure):
    pass

struct__dglHeap.__slots__ = [
    'index',
    'count',
    'block',
    'pnode',
]
struct__dglHeap._fields_ = [
    ('index', c_long),
    ('count', c_long),
    ('block', c_long),
    ('pnode', POINTER(dglHeapNode_s)),
]

dglHeap_s = struct__dglHeap # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/heap.h: 52

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/tree.h: 165
class struct__dglTreeEdgePri32(Structure):
    pass

struct__dglTreeEdgePri32.__slots__ = [
    'nKey',
    'cnData',
    'pnData',
]
struct__dglTreeEdgePri32._fields_ = [
    ('nKey', dglInt32_t),
    ('cnData', dglInt32_t),
    ('pnData', POINTER(dglInt32_t)),
]

dglTreeEdgePri32_s = struct__dglTreeEdgePri32 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/tree.h: 165

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/graph.h: 135
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'pvAVL',
]
struct_anon_23._fields_ = [
    ('pvAVL', POINTER(None)),
]

dglNodePrioritizer_s = struct_anon_23 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/graph.h: 135

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/graph.h: 146
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'cEdge',
    'iEdge',
    'pEdgePri32Item',
    'pvAVL',
]
struct_anon_24._fields_ = [
    ('cEdge', c_int),
    ('iEdge', c_int),
    ('pEdgePri32Item', POINTER(dglTreeEdgePri32_s)),
    ('pvAVL', POINTER(None)),
]

dglEdgePrioritizer_s = struct_anon_24 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/graph.h: 146

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/graph.h: 193
class struct__dglGraph(Structure):
    pass

struct__dglGraph.__slots__ = [
    'iErrno',
    'Version',
    'Endian',
    'NodeAttrSize',
    'EdgeAttrSize',
    'aOpaqueSet',
    'cNode',
    'cHead',
    'cTail',
    'cAlone',
    'cEdge',
    'nnCost',
    'Flags',
    'nFamily',
    'nOptions',
    'pNodeTree',
    'pEdgeTree',
    'pNodeBuffer',
    'iNodeBuffer',
    'pEdgeBuffer',
    'iEdgeBuffer',
    'edgePrioritizer',
    'nodePrioritizer',
]
struct__dglGraph._fields_ = [
    ('iErrno', c_int),
    ('Version', dglByte_t),
    ('Endian', dglByte_t),
    ('NodeAttrSize', dglInt32_t),
    ('EdgeAttrSize', dglInt32_t),
    ('aOpaqueSet', dglInt32_t * 16),
    ('cNode', dglInt32_t),
    ('cHead', dglInt32_t),
    ('cTail', dglInt32_t),
    ('cAlone', dglInt32_t),
    ('cEdge', dglInt32_t),
    ('nnCost', dglInt64_t),
    ('Flags', dglInt32_t),
    ('nFamily', dglInt32_t),
    ('nOptions', dglInt32_t),
    ('pNodeTree', POINTER(None)),
    ('pEdgeTree', POINTER(None)),
    ('pNodeBuffer', POINTER(dglByte_t)),
    ('iNodeBuffer', dglInt32_t),
    ('pEdgeBuffer', POINTER(dglByte_t)),
    ('iEdgeBuffer', dglInt32_t),
    ('edgePrioritizer', dglEdgePrioritizer_s),
    ('nodePrioritizer', dglNodePrioritizer_s),
]

dglGraph_s = struct__dglGraph # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/graph.h: 193

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/graph.h: 243
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'nStartNode',
    'NodeHeap',
    'pvVisited',
    'pvPredist',
]
struct_anon_25._fields_ = [
    ('nStartNode', dglInt32_t),
    ('NodeHeap', dglHeap_s),
    ('pvVisited', POINTER(None)),
    ('pvPredist', POINTER(None)),
]

dglSPCache_s = struct_anon_25 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/dgl/graph.h: 243

RectReal = c_double # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 29

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 59
class struct_RTree_Rect(Structure):
    pass

struct_RTree_Rect.__slots__ = [
    'boundary',
]
struct_RTree_Rect._fields_ = [
    ('boundary', RectReal * (2 * 3)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 79
class struct_RTree_Node(Structure):
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 66
class union_RTree_Child(Union):
    pass

union_RTree_Child.__slots__ = [
    'id',
    'ptr',
    'pos',
]
union_RTree_Child._fields_ = [
    ('id', c_int),
    ('ptr', POINTER(struct_RTree_Node)),
    ('pos', off_t),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 73
class struct_RTree_Branch(Structure):
    pass

struct_RTree_Branch.__slots__ = [
    'rect',
    'child',
]
struct_RTree_Branch._fields_ = [
    ('rect', struct_RTree_Rect),
    ('child', union_RTree_Child),
]

struct_RTree_Node.__slots__ = [
    'count',
    'level',
    'branch',
]
struct_RTree_Node._fields_ = [
    ('count', c_int),
    ('level', c_int),
    ('branch', struct_RTree_Branch * 9),
]

SearchHitCallback = CFUNCTYPE(UNCHECKED(c_int), c_int, struct_RTree_Rect, POINTER(None)) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 93

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 103
class struct_RTree(Structure):
    pass

rt_search_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree), POINTER(struct_RTree_Rect), POINTER(SearchHitCallback), POINTER(None)) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 97

rt_insert_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree_Rect), union_RTree_Child, c_int, POINTER(struct_RTree)) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 99

rt_delete_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree_Rect), union_RTree_Child, POINTER(struct_RTree)) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 100

rt_valid_child_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(union_RTree_Child)) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 101

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 127
class struct__recycle(Structure):
    pass

struct__recycle.__slots__ = [
    'avail',
    'alloc',
    'pos',
]
struct__recycle._fields_ = [
    ('avail', c_int),
    ('alloc', c_int),
    ('pos', POINTER(off_t)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rtree/index.h: 135
class struct_NodeBuffer(Structure):
    pass

struct_NodeBuffer.__slots__ = [
    'n',
    'pos',
    'dirty',
]
struct_NodeBuffer._fields_ = [
    ('n', struct_RTree_Node),
    ('pos', off_t),
    ('dirty', c_char),
]

struct_RTree.__slots__ = [
    'fd',
    'ndims',
    'nsides',
    'nodesize',
    'branchsize',
    'rectsize',
    'n_nodes',
    'n_leafs',
    'rootlevel',
    'nodecard',
    'leafcard',
    'min_node_fill',
    'min_leaf_fill',
    'minfill_node_split',
    'minfill_leaf_split',
    'free_nodes',
    'nb',
    'used',
    'insert_rect',
    'delete_rect',
    'search_rect',
    'valid_child',
    'root',
    'rootpos',
]
struct_RTree._fields_ = [
    ('fd', c_int),
    ('ndims', c_ubyte),
    ('nsides', c_ubyte),
    ('nodesize', c_int),
    ('branchsize', c_int),
    ('rectsize', c_int),
    ('n_nodes', c_int),
    ('n_leafs', c_int),
    ('rootlevel', c_int),
    ('nodecard', c_int),
    ('leafcard', c_int),
    ('min_node_fill', c_int),
    ('min_leaf_fill', c_int),
    ('minfill_node_split', c_int),
    ('minfill_leaf_split', c_int),
    ('free_nodes', struct__recycle),
    ('nb', (struct_NodeBuffer * 3) * 20),
    ('used', (c_char * 3) * 20),
    ('insert_rect', POINTER(rt_insert_fn)),
    ('delete_rect', POINTER(rt_delete_fn)),
    ('search_rect', POINTER(rt_search_fn)),
    ('valid_child', POINTER(rt_valid_child_fn)),
    ('root', POINTER(struct_RTree_Node)),
    ('rootpos', off_t),
]

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

OGRFeatureH = POINTER(None) # /usr/local/include/ogr_api.h: 199

OGRLayerH = POINTER(None) # /usr/local/include/ogr_api.h: 302

OGRDataSourceH = POINTER(None) # /usr/local/include/ogr_api.h: 303

OGRSFDriverH = POINTER(None) # /usr/local/include/ogr_api.h: 304

plus_t = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 41

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 46
class struct_site_att(Structure):
    pass

struct_site_att.__slots__ = [
    'cat',
    'dbl',
    'str',
]
struct_site_att._fields_ = [
    ('cat', c_int),
    ('dbl', POINTER(c_double)),
    ('str', POINTER(POINTER(c_char))),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 65
class struct_bound_box(Structure):
    pass

struct_bound_box.__slots__ = [
    'N',
    'S',
    'E',
    'W',
    'T',
    'B',
]
struct_bound_box._fields_ = [
    ('N', c_double),
    ('S', c_double),
    ('E', c_double),
    ('W', c_double),
    ('T', c_double),
    ('B', c_double),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 96
class struct_gvfile(Structure):
    pass

struct_gvfile.__slots__ = [
    'file',
    'start',
    'current',
    'end',
    'size',
    'alloc',
    'loaded',
]
struct_gvfile._fields_ = [
    ('file', POINTER(FILE)),
    ('start', String),
    ('current', String),
    ('end', String),
    ('size', off_t),
    ('alloc', off_t),
    ('loaded', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 134
class struct_field_info(Structure):
    pass

struct_field_info.__slots__ = [
    'number',
    'name',
    'driver',
    'database',
    'table',
    'key',
]
struct_field_info._fields_ = [
    ('number', c_int),
    ('name', String),
    ('driver', String),
    ('database', String),
    ('table', String),
    ('key', String),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 165
class struct_dblinks(Structure):
    pass

struct_dblinks.__slots__ = [
    'field',
    'alloc_fields',
    'n_fields',
]
struct_dblinks._fields_ = [
    ('field', POINTER(struct_field_info)),
    ('alloc_fields', c_int),
    ('n_fields', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 186
class struct_Port_info(Structure):
    pass

struct_Port_info.__slots__ = [
    'byte_order',
    'off_t_size',
    'dbl_cnvrt',
    'flt_cnvrt',
    'lng_cnvrt',
    'int_cnvrt',
    'shrt_cnvrt',
    'off_t_cnvrt',
    'dbl_quick',
    'flt_quick',
    'lng_quick',
    'int_quick',
    'shrt_quick',
    'off_t_quick',
]
struct_Port_info._fields_ = [
    ('byte_order', c_int),
    ('off_t_size', c_int),
    ('dbl_cnvrt', c_ubyte * 8),
    ('flt_cnvrt', c_ubyte * 4),
    ('lng_cnvrt', c_ubyte * 4),
    ('int_cnvrt', c_ubyte * 4),
    ('shrt_cnvrt', c_ubyte * 2),
    ('off_t_cnvrt', c_ubyte * 8),
    ('dbl_quick', c_int),
    ('flt_quick', c_int),
    ('lng_quick', c_int),
    ('int_quick', c_int),
    ('shrt_quick', c_int),
    ('off_t_quick', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 272
class struct_recycle(Structure):
    pass

struct_recycle.__slots__ = [
    'dummy',
]
struct_recycle._fields_ = [
    ('dummy', c_char),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 282
class struct_dig_head(Structure):
    pass

struct_dig_head.__slots__ = [
    'organization',
    'date',
    'user_name',
    'map_name',
    'source_date',
    'orig_scale',
    'comment',
    'proj',
    'plani_zone',
    'digit_thresh',
    'Version_Major',
    'Version_Minor',
    'Back_Major',
    'Back_Minor',
    'with_z',
    'size',
    'head_size',
    'port',
    'last_offset',
    'recycle',
]
struct_dig_head._fields_ = [
    ('organization', String),
    ('date', String),
    ('user_name', String),
    ('map_name', String),
    ('source_date', String),
    ('orig_scale', c_long),
    ('comment', String),
    ('proj', c_int),
    ('plani_zone', c_int),
    ('digit_thresh', c_double),
    ('Version_Major', c_int),
    ('Version_Minor', c_int),
    ('Back_Major', c_int),
    ('Back_Minor', c_int),
    ('with_z', c_int),
    ('size', off_t),
    ('head_size', c_long),
    ('port', struct_Port_info),
    ('last_offset', off_t),
    ('recycle', POINTER(struct_recycle)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1469
class struct_line_pnts(Structure):
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 399
class struct_Format_info_ogr(Structure):
    pass

struct_Format_info_ogr.__slots__ = [
    'driver_name',
    'dsn',
    'layer_name',
    'driver',
    'ds',
    'layer',
    'dbdriver',
    'dsn_options',
    'layer_options',
    'lines',
    'lines_types',
    'lines_alloc',
    'lines_num',
    'lines_next',
    'feature_cache',
    'feature_cache_id',
    'offset',
    'offset_num',
    'offset_alloc',
    'next_line',
]
struct_Format_info_ogr._fields_ = [
    ('driver_name', String),
    ('dsn', String),
    ('layer_name', String),
    ('driver', OGRSFDriverH),
    ('ds', OGRDataSourceH),
    ('layer', OGRLayerH),
    ('dbdriver', POINTER(dbDriver)),
    ('dsn_options', POINTER(POINTER(c_char))),
    ('layer_options', POINTER(POINTER(c_char))),
    ('lines', POINTER(POINTER(struct_line_pnts))),
    ('lines_types', POINTER(c_int)),
    ('lines_alloc', c_int),
    ('lines_num', c_int),
    ('lines_next', c_int),
    ('feature_cache', OGRFeatureH),
    ('feature_cache_id', c_int),
    ('offset', POINTER(c_int)),
    ('offset_num', c_int),
    ('offset_alloc', c_int),
    ('next_line', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 522
class struct_Format_info(Structure):
    pass

struct_Format_info.__slots__ = [
    'i',
    'ogr',
]
struct_Format_info._fields_ = [
    ('i', c_int),
    ('ogr', struct_Format_info_ogr),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 537
class struct_Cat_index(Structure):
    pass

struct_Cat_index.__slots__ = [
    'field',
    'n_cats',
    'a_cats',
    'cat',
    'n_ucats',
    'n_types',
    'type',
    'offset',
]
struct_Cat_index._fields_ = [
    ('field', c_int),
    ('n_cats', c_int),
    ('a_cats', c_int),
    ('cat', POINTER(c_int * 3)),
    ('n_ucats', c_int),
    ('n_types', c_int),
    ('type', (c_int * 2) * 7),
    ('offset', off_t),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1249
class struct_P_node(Structure):
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1371
class struct_P_line(Structure):
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1399
class struct_P_area(Structure):
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1440
class struct_P_isle(Structure):
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 586
class struct_Plus_head(Structure):
    pass

struct_Plus_head.__slots__ = [
    'Version_Major',
    'Version_Minor',
    'Back_Major',
    'Back_Minor',
    'spidx_Version_Major',
    'spidx_Version_Minor',
    'spidx_Back_Major',
    'spidx_Back_Minor',
    'cidx_Version_Major',
    'cidx_Version_Minor',
    'cidx_Back_Major',
    'cidx_Back_Minor',
    'with_z',
    'spidx_with_z',
    'off_t_size',
    'head_size',
    'spidx_head_size',
    'cidx_head_size',
    'release_support',
    'port',
    'spidx_port',
    'cidx_port',
    'mode',
    'built',
    'box',
    'Node',
    'Line',
    'Area',
    'Isle',
    'n_plines',
    'n_llines',
    'n_blines',
    'n_clines',
    'n_flines',
    'n_klines',
    'n_vfaces',
    'n_hfaces',
    'n_nodes',
    'n_edges',
    'n_lines',
    'n_areas',
    'n_isles',
    'n_faces',
    'n_volumes',
    'n_holes',
    'alloc_nodes',
    'alloc_edges',
    'alloc_lines',
    'alloc_areas',
    'alloc_isles',
    'alloc_faces',
    'alloc_volumes',
    'alloc_holes',
    'Node_offset',
    'Edge_offset',
    'Line_offset',
    'Area_offset',
    'Isle_offset',
    'Volume_offset',
    'Hole_offset',
    'Spidx_built',
    'Spidx_new',
    'Spidx_file',
    'spidx_fp',
    'Node_spidx_offset',
    'Line_spidx_offset',
    'Area_spidx_offset',
    'Isle_spidx_offset',
    'Face_spidx_offset',
    'Volume_spidx_offset',
    'Hole_spidx_offset',
    'Node_spidx',
    'Line_spidx',
    'Area_spidx',
    'Isle_spidx',
    'Face_spidx',
    'Volume_spidx',
    'Hole_spidx',
    'update_cidx',
    'n_cidx',
    'a_cidx',
    'cidx',
    'cidx_up_to_date',
    'coor_size',
    'coor_mtime',
    'do_uplist',
    'uplines',
    'alloc_uplines',
    'n_uplines',
    'upnodes',
    'alloc_upnodes',
    'n_upnodes',
]
struct_Plus_head._fields_ = [
    ('Version_Major', c_int),
    ('Version_Minor', c_int),
    ('Back_Major', c_int),
    ('Back_Minor', c_int),
    ('spidx_Version_Major', c_int),
    ('spidx_Version_Minor', c_int),
    ('spidx_Back_Major', c_int),
    ('spidx_Back_Minor', c_int),
    ('cidx_Version_Major', c_int),
    ('cidx_Version_Minor', c_int),
    ('cidx_Back_Major', c_int),
    ('cidx_Back_Minor', c_int),
    ('with_z', c_int),
    ('spidx_with_z', c_int),
    ('off_t_size', c_int),
    ('head_size', c_long),
    ('spidx_head_size', c_long),
    ('cidx_head_size', c_long),
    ('release_support', c_int),
    ('port', struct_Port_info),
    ('spidx_port', struct_Port_info),
    ('cidx_port', struct_Port_info),
    ('mode', c_int),
    ('built', c_int),
    ('box', struct_bound_box),
    ('Node', POINTER(POINTER(struct_P_node))),
    ('Line', POINTER(POINTER(struct_P_line))),
    ('Area', POINTER(POINTER(struct_P_area))),
    ('Isle', POINTER(POINTER(struct_P_isle))),
    ('n_plines', plus_t),
    ('n_llines', plus_t),
    ('n_blines', plus_t),
    ('n_clines', plus_t),
    ('n_flines', plus_t),
    ('n_klines', plus_t),
    ('n_vfaces', plus_t),
    ('n_hfaces', plus_t),
    ('n_nodes', plus_t),
    ('n_edges', plus_t),
    ('n_lines', plus_t),
    ('n_areas', plus_t),
    ('n_isles', plus_t),
    ('n_faces', plus_t),
    ('n_volumes', plus_t),
    ('n_holes', plus_t),
    ('alloc_nodes', plus_t),
    ('alloc_edges', plus_t),
    ('alloc_lines', plus_t),
    ('alloc_areas', plus_t),
    ('alloc_isles', plus_t),
    ('alloc_faces', plus_t),
    ('alloc_volumes', plus_t),
    ('alloc_holes', plus_t),
    ('Node_offset', off_t),
    ('Edge_offset', off_t),
    ('Line_offset', off_t),
    ('Area_offset', off_t),
    ('Isle_offset', off_t),
    ('Volume_offset', off_t),
    ('Hole_offset', off_t),
    ('Spidx_built', c_int),
    ('Spidx_new', c_int),
    ('Spidx_file', c_int),
    ('spidx_fp', struct_gvfile),
    ('Node_spidx_offset', off_t),
    ('Line_spidx_offset', off_t),
    ('Area_spidx_offset', off_t),
    ('Isle_spidx_offset', off_t),
    ('Face_spidx_offset', off_t),
    ('Volume_spidx_offset', off_t),
    ('Hole_spidx_offset', off_t),
    ('Node_spidx', POINTER(struct_RTree)),
    ('Line_spidx', POINTER(struct_RTree)),
    ('Area_spidx', POINTER(struct_RTree)),
    ('Isle_spidx', POINTER(struct_RTree)),
    ('Face_spidx', POINTER(struct_RTree)),
    ('Volume_spidx', POINTER(struct_RTree)),
    ('Hole_spidx', POINTER(struct_RTree)),
    ('update_cidx', c_int),
    ('n_cidx', c_int),
    ('a_cidx', c_int),
    ('cidx', POINTER(struct_Cat_index)),
    ('cidx_up_to_date', c_int),
    ('coor_size', off_t),
    ('coor_mtime', c_long),
    ('do_uplist', c_int),
    ('uplines', POINTER(c_int)),
    ('alloc_uplines', c_int),
    ('n_uplines', c_int),
    ('upnodes', POINTER(c_int)),
    ('alloc_upnodes', c_int),
    ('n_upnodes', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1052
class struct_Map_info(Structure):
    pass

struct_Map_info.__slots__ = [
    'format',
    'temporary',
    'dblnk',
    'plus',
    'graph_line_type',
    'graph',
    'spCache',
    'edge_fcosts',
    'edge_bcosts',
    'node_costs',
    'cost_multip',
    'open',
    'mode',
    'level',
    'head_only',
    'support_updated',
    'next_line',
    'name',
    'mapset',
    'location',
    'gisdbase',
    'Constraint_region_flag',
    'Constraint_type_flag',
    'Constraint_box',
    'Constraint_type',
    'proj',
    'dig_fp',
    'head',
    'fInfo',
    'hist_fp',
    'site_att',
    'n_site_att',
    'n_site_dbl',
    'n_site_str',
]
struct_Map_info._fields_ = [
    ('format', c_int),
    ('temporary', c_int),
    ('dblnk', POINTER(struct_dblinks)),
    ('plus', struct_Plus_head),
    ('graph_line_type', c_int),
    ('graph', dglGraph_s),
    ('spCache', dglSPCache_s),
    ('edge_fcosts', POINTER(c_double)),
    ('edge_bcosts', POINTER(c_double)),
    ('node_costs', POINTER(c_double)),
    ('cost_multip', c_int),
    ('open', c_int),
    ('mode', c_int),
    ('level', c_int),
    ('head_only', c_int),
    ('support_updated', c_int),
    ('next_line', plus_t),
    ('name', String),
    ('mapset', String),
    ('location', String),
    ('gisdbase', String),
    ('Constraint_region_flag', c_int),
    ('Constraint_type_flag', c_int),
    ('Constraint_box', struct_bound_box),
    ('Constraint_type', c_int),
    ('proj', c_int),
    ('dig_fp', struct_gvfile),
    ('head', struct_dig_head),
    ('fInfo', struct_Format_info),
    ('hist_fp', POINTER(FILE)),
    ('site_att', POINTER(struct_site_att)),
    ('n_site_att', c_int),
    ('n_site_dbl', c_int),
    ('n_site_str', c_int),
]

struct_P_node.__slots__ = [
    'x',
    'y',
    'z',
    'alloc_lines',
    'n_lines',
    'lines',
    'angles',
]
struct_P_node._fields_ = [
    ('x', c_double),
    ('y', c_double),
    ('z', c_double),
    ('alloc_lines', plus_t),
    ('n_lines', plus_t),
    ('lines', POINTER(plus_t)),
    ('angles', POINTER(c_float)),
]

struct_P_line.__slots__ = [
    'type',
    'offset',
    'topo',
]
struct_P_line._fields_ = [
    ('type', c_char),
    ('offset', off_t),
    ('topo', POINTER(None)),
]

struct_P_area.__slots__ = [
    'n_lines',
    'alloc_lines',
    'lines',
    'centroid',
    'n_isles',
    'alloc_isles',
    'isles',
]
struct_P_area._fields_ = [
    ('n_lines', plus_t),
    ('alloc_lines', plus_t),
    ('lines', POINTER(plus_t)),
    ('centroid', plus_t),
    ('n_isles', plus_t),
    ('alloc_isles', plus_t),
    ('isles', POINTER(plus_t)),
]

struct_P_isle.__slots__ = [
    'n_lines',
    'alloc_lines',
    'lines',
    'area',
]
struct_P_isle._fields_ = [
    ('n_lines', plus_t),
    ('alloc_lines', plus_t),
    ('lines', POINTER(plus_t)),
    ('area', plus_t),
]

struct_line_pnts.__slots__ = [
    'x',
    'y',
    'z',
    'n_points',
    'alloc_points',
]
struct_line_pnts._fields_ = [
    ('x', POINTER(c_double)),
    ('y', POINTER(c_double)),
    ('z', POINTER(c_double)),
    ('n_points', c_int),
    ('alloc_points', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1517
class struct_cat_list(Structure):
    pass

struct_cat_list.__slots__ = [
    'field',
    'min',
    'max',
    'n_ranges',
    'alloc_ranges',
]
struct_cat_list._fields_ = [
    ('field', c_int),
    ('min', POINTER(c_int)),
    ('max', POINTER(c_int)),
    ('n_ranges', c_int),
    ('alloc_ranges', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1546
class struct_ilist(Structure):
    pass

struct_ilist.__slots__ = [
    'value',
    'n_values',
    'alloc_values',
]
struct_ilist._fields_ = [
    ('value', POINTER(c_int)),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 45
class struct_rpoint(Structure):
    pass

struct_rpoint.__slots__ = [
    'x',
    'y',
]
struct_rpoint._fields_ = [
    ('x', c_int),
    ('y', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 50
class struct_robject(Structure):
    pass

struct_robject.__slots__ = [
    'fid',
    'type',
    'npoints',
    'point',
]
struct_robject._fields_ = [
    ('fid', c_int),
    ('type', c_int),
    ('npoints', c_int),
    ('point', POINTER(struct_rpoint)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 58
class struct_robject_list(Structure):
    pass

struct_robject_list.__slots__ = [
    'nitems',
    'item',
]
struct_robject_list._fields_ = [
    ('nitems', c_int),
    ('item', POINTER(POINTER(struct_robject))),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 65
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_split_lines'):
    Vedit_split_lines = _libs['grass_vedit.7.0.svn'].Vedit_split_lines
    Vedit_split_lines.restype = c_int
    Vedit_split_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), POINTER(struct_line_pnts), c_double, POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 67
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_connect_lines'):
    Vedit_connect_lines = _libs['grass_vedit.7.0.svn'].Vedit_connect_lines
    Vedit_connect_lines.restype = c_int
    Vedit_connect_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 70
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_modify_cats'):
    Vedit_modify_cats = _libs['grass_vedit.7.0.svn'].Vedit_modify_cats
    Vedit_modify_cats.restype = c_int
    Vedit_modify_cats.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), c_int, c_int, POINTER(struct_cat_list)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 74
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_copy_lines'):
    Vedit_copy_lines = _libs['grass_vedit.7.0.svn'].Vedit_copy_lines
    Vedit_copy_lines.restype = c_int
    Vedit_copy_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 77
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_chtype_lines'):
    Vedit_chtype_lines = _libs['grass_vedit.7.0.svn'].Vedit_chtype_lines
    Vedit_chtype_lines.restype = c_int
    Vedit_chtype_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 81
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_delete_lines'):
    Vedit_delete_lines = _libs['grass_vedit.7.0.svn'].Vedit_delete_lines
    Vedit_delete_lines.restype = c_int
    Vedit_delete_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 84
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_get_min_distance'):
    Vedit_get_min_distance = _libs['grass_vedit.7.0.svn'].Vedit_get_min_distance
    Vedit_get_min_distance.restype = c_double
    Vedit_get_min_distance.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int, POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 88
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_flip_lines'):
    Vedit_flip_lines = _libs['grass_vedit.7.0.svn'].Vedit_flip_lines
    Vedit_flip_lines.restype = c_int
    Vedit_flip_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 91
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_merge_lines'):
    Vedit_merge_lines = _libs['grass_vedit.7.0.svn'].Vedit_merge_lines
    Vedit_merge_lines.restype = c_int
    Vedit_merge_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 94
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_move_lines'):
    Vedit_move_lines = _libs['grass_vedit.7.0.svn'].Vedit_move_lines
    Vedit_move_lines.restype = c_int
    Vedit_move_lines.argtypes = [POINTER(struct_Map_info), POINTER(POINTER(struct_Map_info)), c_int, POINTER(struct_ilist), c_double, c_double, c_double, c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 98
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_render_map'):
    Vedit_render_map = _libs['grass_vedit.7.0.svn'].Vedit_render_map
    Vedit_render_map.restype = POINTER(struct_robject_list)
    Vedit_render_map.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box), c_int, c_double, c_double, c_int, c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 102
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_select_by_query'):
    Vedit_select_by_query = _libs['grass_vedit.7.0.svn'].Vedit_select_by_query
    Vedit_select_by_query.restype = c_int
    Vedit_select_by_query.argtypes = [POINTER(struct_Map_info), c_int, c_int, c_double, c_int, POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 106
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_snap_point'):
    Vedit_snap_point = _libs['grass_vedit.7.0.svn'].Vedit_snap_point
    Vedit_snap_point.restype = c_int
    Vedit_snap_point.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 108
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_snap_line'):
    Vedit_snap_line = _libs['grass_vedit.7.0.svn'].Vedit_snap_line
    Vedit_snap_line.restype = c_int
    Vedit_snap_line.argtypes = [POINTER(struct_Map_info), POINTER(POINTER(struct_Map_info)), c_int, c_int, POINTER(struct_line_pnts), c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 110
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_snap_lines'):
    Vedit_snap_lines = _libs['grass_vedit.7.0.svn'].Vedit_snap_lines
    Vedit_snap_lines.restype = c_int
    Vedit_snap_lines.argtypes = [POINTER(struct_Map_info), POINTER(POINTER(struct_Map_info)), c_int, POINTER(struct_ilist), c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 114
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_move_vertex'):
    Vedit_move_vertex = _libs['grass_vedit.7.0.svn'].Vedit_move_vertex
    Vedit_move_vertex.restype = c_int
    Vedit_move_vertex.argtypes = [POINTER(struct_Map_info), POINTER(POINTER(struct_Map_info)), c_int, POINTER(struct_ilist), POINTER(struct_line_pnts), c_double, c_double, c_double, c_double, c_double, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 118
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_add_vertex'):
    Vedit_add_vertex = _libs['grass_vedit.7.0.svn'].Vedit_add_vertex
    Vedit_add_vertex.restype = c_int
    Vedit_add_vertex.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), POINTER(struct_line_pnts), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 120
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_remove_vertex'):
    Vedit_remove_vertex = _libs['grass_vedit.7.0.svn'].Vedit_remove_vertex
    Vedit_remove_vertex.restype = c_int
    Vedit_remove_vertex.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), POINTER(struct_line_pnts), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 124
if hasattr(_libs['grass_vedit.7.0.svn'], 'Vedit_bulk_labeling'):
    Vedit_bulk_labeling = _libs['grass_vedit.7.0.svn'].Vedit_bulk_labeling
    Vedit_bulk_labeling.restype = c_int
    Vedit_bulk_labeling.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), c_double, c_double, c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 7
try:
    NO_SNAP = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 7
try:
    SNAP = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 7
try:
    SNAPVERTEX = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 8
try:
    QUERY_UNKNOWN = (-1)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 8
try:
    QUERY_LENGTH = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 8
try:
    QUERY_DANGLE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_POINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_LINE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_BOUNDARYNO = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_BOUNDARYTWO = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_BOUNDARYONE = 16
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_CENTROIDIN = 32
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_CENTROIDOUT = 64
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_CENTROIDDUP = 128
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_NODEONE = 256
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_NODETWO = 512
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_VERTEX = 1024
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_AREA = 2048
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_ISLE = 4096
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 10
try:
    TYPE_DIRECTION = 8192
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_POINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_LINE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_BOUNDARYNO = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_BOUNDARYTWO = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_BOUNDARYONE = 16
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_CENTROIDIN = 32
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_CENTROIDOUT = 64
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_CENTROIDDUP = 128
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_NODEONE = 256
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_NODETWO = 512
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_VERTEX = 1024
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_AREA = 2048
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 11
try:
    DRAW_DIRECTION = 4096
except:
    pass

rpoint = struct_rpoint # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 45

robject = struct_robject # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 50

robject_list = struct_robject_list # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vedit.h: 58

# No inserted files

