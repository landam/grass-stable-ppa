'''Wrapper for vector.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_vector.7.0.svn -lgrass_dig2.7.0.svn -lgrass_dgl.7.0.svn -lgrass_rtree.7.0.svn -lgrass_linkm.7.0.svn -lgrass_dbmiclient.7.0.svn -lgrass_dbmibase.7.0.svn -lgrass_btree2.7.0.svn -lgrass_gproj.7.0.svn -I/usr/local/include /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h -o vector.py

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

_libs["grass_vector.7.0.svn"] = load_library("grass_vector.7.0.svn")
_libs["grass_dig2.7.0.svn"] = load_library("grass_dig2.7.0.svn")
_libs["grass_dgl.7.0.svn"] = load_library("grass_dgl.7.0.svn")
_libs["grass_rtree.7.0.svn"] = load_library("grass_rtree.7.0.svn")
_libs["grass_linkm.7.0.svn"] = load_library("grass_linkm.7.0.svn")
_libs["grass_dbmiclient.7.0.svn"] = load_library("grass_dbmiclient.7.0.svn")
_libs["grass_dbmibase.7.0.svn"] = load_library("grass_dbmibase.7.0.svn")
_libs["grass_btree2.7.0.svn"] = load_library("grass_btree2.7.0.svn")
_libs["grass_gproj.7.0.svn"] = load_library("grass_gproj.7.0.svn")

# 9 libraries
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 335
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

DCELL = c_double # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 403

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

off_t = __off64_t # /usr/include/sys/types.h: 90

enum_overlay_operator = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 216

GV_O_AND = 0 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 216

GV_O_OVERLAP = (GV_O_AND + 1) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 216

OVERLAY_OPERATOR = enum_overlay_operator # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 222

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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 381
class struct_Coor_info(Structure):
    pass

struct_Coor_info.__slots__ = [
    'size',
    'mtime',
]
struct_Coor_info._fields_ = [
    ('size', off_t),
    ('mtime', c_long),
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1291
class struct_P_topo_l(Structure):
    pass

struct_P_topo_l.__slots__ = [
    'N1',
    'N2',
]
struct_P_topo_l._fields_ = [
    ('N1', plus_t),
    ('N2', plus_t),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1306
class struct_P_topo_b(Structure):
    pass

struct_P_topo_b.__slots__ = [
    'N1',
    'N2',
    'left',
    'right',
]
struct_P_topo_b._fields_ = [
    ('N1', plus_t),
    ('N2', plus_t),
    ('left', plus_t),
    ('right', plus_t),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1329
class struct_P_topo_c(Structure):
    pass

struct_P_topo_c.__slots__ = [
    'area',
]
struct_P_topo_c._fields_ = [
    ('area', plus_t),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1340
class struct_P_topo_f(Structure):
    pass

struct_P_topo_f.__slots__ = [
    'E',
    'left',
    'right',
]
struct_P_topo_f._fields_ = [
    ('E', plus_t * 3),
    ('left', plus_t),
    ('right', plus_t),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1360
class struct_P_topo_k(Structure):
    pass

struct_P_topo_k.__slots__ = [
    'volume',
]
struct_P_topo_k._fields_ = [
    ('volume', plus_t),
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1496
class struct_line_cats(Structure):
    pass

struct_line_cats.__slots__ = [
    'field',
    'cat',
    'n_cats',
    'alloc_cats',
]
struct_line_cats._fields_ = [
    ('field', POINTER(c_int)),
    ('cat', POINTER(c_int)),
    ('n_cats', c_int),
    ('alloc_cats', c_int),
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1565
class struct_boxlist(Structure):
    pass

struct_boxlist.__slots__ = [
    'id',
    'box',
    'have_boxes',
    'n_values',
    'alloc_values',
]
struct_boxlist._fields_ = [
    ('id', POINTER(c_int)),
    ('box', POINTER(struct_bound_box)),
    ('have_boxes', c_int),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1594
class struct_varray(Structure):
    pass

struct_varray.__slots__ = [
    'size',
    'c',
]
struct_varray._fields_ = [
    ('size', c_int),
    ('c', POINTER(c_int)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1614
class struct_spatial_index(Structure):
    pass

struct_spatial_index.__slots__ = [
    'si_tree',
    'name',
]
struct_spatial_index._fields_ = [
    ('si_tree', POINTER(struct_RTree)),
    ('name', String),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 20
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_new_line_struct'):
    Vect_new_line_struct = _libs['grass_vector.7.0.svn'].Vect_new_line_struct
    Vect_new_line_struct.restype = POINTER(struct_line_pnts)
    Vect_new_line_struct.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 21
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_append_point'):
    Vect_append_point = _libs['grass_vector.7.0.svn'].Vect_append_point
    Vect_append_point.restype = c_int
    Vect_append_point.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 22
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_append_points'):
    Vect_append_points = _libs['grass_vector.7.0.svn'].Vect_append_points
    Vect_append_points.restype = c_int
    Vect_append_points.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 23
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_insert_point'):
    Vect_line_insert_point = _libs['grass_vector.7.0.svn'].Vect_line_insert_point
    Vect_line_insert_point.restype = c_int
    Vect_line_insert_point.argtypes = [POINTER(struct_line_pnts), c_int, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 24
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_delete_point'):
    Vect_line_delete_point = _libs['grass_vector.7.0.svn'].Vect_line_delete_point
    Vect_line_delete_point.restype = c_int
    Vect_line_delete_point.argtypes = [POINTER(struct_line_pnts), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 25
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_get_point'):
    Vect_line_get_point = _libs['grass_vector.7.0.svn'].Vect_line_get_point
    Vect_line_get_point.restype = c_int
    Vect_line_get_point.argtypes = [POINTER(struct_line_pnts), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 27
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_line_points'):
    Vect_get_num_line_points = _libs['grass_vector.7.0.svn'].Vect_get_num_line_points
    Vect_get_num_line_points.restype = c_int
    Vect_get_num_line_points.argtypes = [POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 28
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_prune'):
    Vect_line_prune = _libs['grass_vector.7.0.svn'].Vect_line_prune
    Vect_line_prune.restype = c_int
    Vect_line_prune.argtypes = [POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 29
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_prune_thresh'):
    Vect_line_prune_thresh = _libs['grass_vector.7.0.svn'].Vect_line_prune_thresh
    Vect_line_prune_thresh.restype = c_int
    Vect_line_prune_thresh.argtypes = [POINTER(struct_line_pnts), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 30
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_reverse'):
    Vect_line_reverse = _libs['grass_vector.7.0.svn'].Vect_line_reverse
    Vect_line_reverse.restype = None
    Vect_line_reverse.argtypes = [POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 31
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_copy_xyz_to_pnts'):
    Vect_copy_xyz_to_pnts = _libs['grass_vector.7.0.svn'].Vect_copy_xyz_to_pnts
    Vect_copy_xyz_to_pnts.restype = c_int
    Vect_copy_xyz_to_pnts.argtypes = [POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 33
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_copy_pnts_to_xyz'):
    Vect_copy_pnts_to_xyz = _libs['grass_vector.7.0.svn'].Vect_copy_pnts_to_xyz
    Vect_copy_pnts_to_xyz.restype = c_int
    Vect_copy_pnts_to_xyz.argtypes = [POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 35
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_reset_line'):
    Vect_reset_line = _libs['grass_vector.7.0.svn'].Vect_reset_line
    Vect_reset_line.restype = None
    Vect_reset_line.argtypes = [POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 36
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_destroy_line_struct'):
    Vect_destroy_line_struct = _libs['grass_vector.7.0.svn'].Vect_destroy_line_struct
    Vect_destroy_line_struct.restype = None
    Vect_destroy_line_struct.argtypes = [POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 37
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_point_on_line'):
    Vect_point_on_line = _libs['grass_vector.7.0.svn'].Vect_point_on_line
    Vect_point_on_line.restype = c_int
    Vect_point_on_line.argtypes = [POINTER(struct_line_pnts), c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 39
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_segment'):
    Vect_line_segment = _libs['grass_vector.7.0.svn'].Vect_line_segment
    Vect_line_segment.restype = c_int
    Vect_line_segment.argtypes = [POINTER(struct_line_pnts), c_double, c_double, POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 40
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_length'):
    Vect_line_length = _libs['grass_vector.7.0.svn'].Vect_line_length
    Vect_line_length.restype = c_double
    Vect_line_length.argtypes = [POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 41
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_area_perimeter'):
    Vect_area_perimeter = _libs['grass_vector.7.0.svn'].Vect_area_perimeter
    Vect_area_perimeter.restype = c_double
    Vect_area_perimeter.argtypes = [POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 42
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_geodesic_length'):
    Vect_line_geodesic_length = _libs['grass_vector.7.0.svn'].Vect_line_geodesic_length
    Vect_line_geodesic_length.restype = c_double
    Vect_line_geodesic_length.argtypes = [POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 43
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_distance'):
    Vect_line_distance = _libs['grass_vector.7.0.svn'].Vect_line_distance
    Vect_line_distance.restype = c_int
    Vect_line_distance.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_double, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 46
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_box'):
    Vect_line_box = _libs['grass_vector.7.0.svn'].Vect_line_box
    Vect_line_box.restype = None
    Vect_line_box.argtypes = [POINTER(struct_line_pnts), POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 47
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_parallel'):
    Vect_line_parallel = _libs['grass_vector.7.0.svn'].Vect_line_parallel
    Vect_line_parallel.restype = None
    Vect_line_parallel.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_int, POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 49
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_parallel2'):
    Vect_line_parallel2 = _libs['grass_vector.7.0.svn'].Vect_line_parallel2
    Vect_line_parallel2.restype = None
    Vect_line_parallel2.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_double, c_int, c_int, c_double, POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 52
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_buffer'):
    Vect_line_buffer = _libs['grass_vector.7.0.svn'].Vect_line_buffer
    Vect_line_buffer.restype = None
    Vect_line_buffer.argtypes = [POINTER(struct_line_pnts), c_double, c_double, POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 53
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_buffer2'):
    Vect_line_buffer2 = _libs['grass_vector.7.0.svn'].Vect_line_buffer2
    Vect_line_buffer2.restype = None
    Vect_line_buffer2.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_double, c_int, c_int, c_double, POINTER(POINTER(struct_line_pnts)), POINTER(POINTER(POINTER(struct_line_pnts))), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 57
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_area_buffer2'):
    Vect_area_buffer2 = _libs['grass_vector.7.0.svn'].Vect_area_buffer2
    Vect_area_buffer2.restype = None
    Vect_area_buffer2.argtypes = [POINTER(struct_Map_info), c_int, c_double, c_double, c_double, c_int, c_int, c_double, POINTER(POINTER(struct_line_pnts)), POINTER(POINTER(POINTER(struct_line_pnts))), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 61
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_point_buffer2'):
    Vect_point_buffer2 = _libs['grass_vector.7.0.svn'].Vect_point_buffer2
    Vect_point_buffer2.restype = None
    Vect_point_buffer2.argtypes = [c_double, c_double, c_double, c_double, c_double, c_int, c_double, POINTER(POINTER(struct_line_pnts))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 67
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_new_cats_struct'):
    Vect_new_cats_struct = _libs['grass_vector.7.0.svn'].Vect_new_cats_struct
    Vect_new_cats_struct.restype = POINTER(struct_line_cats)
    Vect_new_cats_struct.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 68
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cat_set'):
    Vect_cat_set = _libs['grass_vector.7.0.svn'].Vect_cat_set
    Vect_cat_set.restype = c_int
    Vect_cat_set.argtypes = [POINTER(struct_line_cats), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 69
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cat_get'):
    Vect_cat_get = _libs['grass_vector.7.0.svn'].Vect_cat_get
    Vect_cat_get.restype = c_int
    Vect_cat_get.argtypes = [POINTER(struct_line_cats), c_int, POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 70
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cat_del'):
    Vect_cat_del = _libs['grass_vector.7.0.svn'].Vect_cat_del
    Vect_cat_del.restype = c_int
    Vect_cat_del.argtypes = [POINTER(struct_line_cats), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 71
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_field_cat_del'):
    Vect_field_cat_del = _libs['grass_vector.7.0.svn'].Vect_field_cat_del
    Vect_field_cat_del.restype = c_int
    Vect_field_cat_del.argtypes = [POINTER(struct_line_cats), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 72
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_field_cat_get'):
    Vect_field_cat_get = _libs['grass_vector.7.0.svn'].Vect_field_cat_get
    Vect_field_cat_get.restype = c_int
    Vect_field_cat_get.argtypes = [POINTER(struct_line_cats), c_int, POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 73
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cat_in_array'):
    Vect_cat_in_array = _libs['grass_vector.7.0.svn'].Vect_cat_in_array
    Vect_cat_in_array.restype = c_int
    Vect_cat_in_array.argtypes = [c_int, POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 74
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_reset_cats'):
    Vect_reset_cats = _libs['grass_vector.7.0.svn'].Vect_reset_cats
    Vect_reset_cats.restype = c_int
    Vect_reset_cats.argtypes = [POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 75
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_destroy_cats_struct'):
    Vect_destroy_cats_struct = _libs['grass_vector.7.0.svn'].Vect_destroy_cats_struct
    Vect_destroy_cats_struct.restype = None
    Vect_destroy_cats_struct.argtypes = [POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 76
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_area_cats'):
    Vect_get_area_cats = _libs['grass_vector.7.0.svn'].Vect_get_area_cats
    Vect_get_area_cats.restype = c_int
    Vect_get_area_cats.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 77
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_area_cat'):
    Vect_get_area_cat = _libs['grass_vector.7.0.svn'].Vect_get_area_cat
    Vect_get_area_cat.restype = c_int
    Vect_get_area_cat.argtypes = [POINTER(struct_Map_info), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 78
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_line_cat'):
    Vect_get_line_cat = _libs['grass_vector.7.0.svn'].Vect_get_line_cat
    Vect_get_line_cat.restype = c_int
    Vect_get_line_cat.argtypes = [POINTER(struct_Map_info), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 81
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_new_cat_list'):
    Vect_new_cat_list = _libs['grass_vector.7.0.svn'].Vect_new_cat_list
    Vect_new_cat_list.restype = POINTER(struct_cat_list)
    Vect_new_cat_list.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 82
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_str_to_cat_list'):
    Vect_str_to_cat_list = _libs['grass_vector.7.0.svn'].Vect_str_to_cat_list
    Vect_str_to_cat_list.restype = c_int
    Vect_str_to_cat_list.argtypes = [String, POINTER(struct_cat_list)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 83
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_array_to_cat_list'):
    Vect_array_to_cat_list = _libs['grass_vector.7.0.svn'].Vect_array_to_cat_list
    Vect_array_to_cat_list.restype = c_int
    Vect_array_to_cat_list.argtypes = [POINTER(c_int), c_int, POINTER(struct_cat_list)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 84
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cat_in_cat_list'):
    Vect_cat_in_cat_list = _libs['grass_vector.7.0.svn'].Vect_cat_in_cat_list
    Vect_cat_in_cat_list.restype = c_int
    Vect_cat_in_cat_list.argtypes = [c_int, POINTER(struct_cat_list)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 85
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_destroy_cat_list'):
    Vect_destroy_cat_list = _libs['grass_vector.7.0.svn'].Vect_destroy_cat_list
    Vect_destroy_cat_list.restype = None
    Vect_destroy_cat_list.argtypes = [POINTER(struct_cat_list)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 88
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_new_varray'):
    Vect_new_varray = _libs['grass_vector.7.0.svn'].Vect_new_varray
    Vect_new_varray.restype = POINTER(struct_varray)
    Vect_new_varray.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 89
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_varray_from_cat_string'):
    Vect_set_varray_from_cat_string = _libs['grass_vector.7.0.svn'].Vect_set_varray_from_cat_string
    Vect_set_varray_from_cat_string.restype = c_int
    Vect_set_varray_from_cat_string.argtypes = [POINTER(struct_Map_info), c_int, String, c_int, c_int, POINTER(struct_varray)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 91
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_varray_from_cat_list'):
    Vect_set_varray_from_cat_list = _libs['grass_vector.7.0.svn'].Vect_set_varray_from_cat_list
    Vect_set_varray_from_cat_list.restype = c_int
    Vect_set_varray_from_cat_list.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_cat_list), c_int, c_int, POINTER(struct_varray)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 93
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_varray_from_db'):
    Vect_set_varray_from_db = _libs['grass_vector.7.0.svn'].Vect_set_varray_from_db
    Vect_set_varray_from_db.restype = c_int
    Vect_set_varray_from_db.argtypes = [POINTER(struct_Map_info), c_int, String, c_int, c_int, POINTER(struct_varray)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 97
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_new_dblinks_struct'):
    Vect_new_dblinks_struct = _libs['grass_vector.7.0.svn'].Vect_new_dblinks_struct
    Vect_new_dblinks_struct.restype = POINTER(struct_dblinks)
    Vect_new_dblinks_struct.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 98
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_reset_dblinks'):
    Vect_reset_dblinks = _libs['grass_vector.7.0.svn'].Vect_reset_dblinks
    Vect_reset_dblinks.restype = None
    Vect_reset_dblinks.argtypes = [POINTER(struct_dblinks)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 99
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_add_dblink'):
    Vect_add_dblink = _libs['grass_vector.7.0.svn'].Vect_add_dblink
    Vect_add_dblink.restype = c_int
    Vect_add_dblink.argtypes = [POINTER(struct_dblinks), c_int, String, String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 101
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_check_dblink'):
    Vect_check_dblink = _libs['grass_vector.7.0.svn'].Vect_check_dblink
    Vect_check_dblink.restype = c_int
    Vect_check_dblink.argtypes = [POINTER(struct_dblinks), c_int, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 102
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_map_add_dblink'):
    Vect_map_add_dblink = _libs['grass_vector.7.0.svn'].Vect_map_add_dblink
    Vect_map_add_dblink.restype = c_int
    Vect_map_add_dblink.argtypes = [POINTER(struct_Map_info), c_int, String, String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 105
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_map_del_dblink'):
    Vect_map_del_dblink = _libs['grass_vector.7.0.svn'].Vect_map_del_dblink
    Vect_map_del_dblink.restype = c_int
    Vect_map_del_dblink.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 106
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_map_check_dblink'):
    Vect_map_check_dblink = _libs['grass_vector.7.0.svn'].Vect_map_check_dblink
    Vect_map_check_dblink.restype = c_int
    Vect_map_check_dblink.argtypes = [POINTER(struct_Map_info), c_int, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 107
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_read_dblinks'):
    Vect_read_dblinks = _libs['grass_vector.7.0.svn'].Vect_read_dblinks
    Vect_read_dblinks.restype = c_int
    Vect_read_dblinks.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 108
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_write_dblinks'):
    Vect_write_dblinks = _libs['grass_vector.7.0.svn'].Vect_write_dblinks
    Vect_write_dblinks.restype = c_int
    Vect_write_dblinks.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 109
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_default_field_info'):
    Vect_default_field_info = _libs['grass_vector.7.0.svn'].Vect_default_field_info
    Vect_default_field_info.restype = POINTER(struct_field_info)
    Vect_default_field_info.argtypes = [POINTER(struct_Map_info), c_int, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 111
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_dblink'):
    Vect_get_dblink = _libs['grass_vector.7.0.svn'].Vect_get_dblink
    Vect_get_dblink.restype = POINTER(struct_field_info)
    Vect_get_dblink.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 112
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_field'):
    Vect_get_field = _libs['grass_vector.7.0.svn'].Vect_get_field
    Vect_get_field.restype = POINTER(struct_field_info)
    Vect_get_field.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 113
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_field_by_name'):
    Vect_get_field_by_name = _libs['grass_vector.7.0.svn'].Vect_get_field_by_name
    Vect_get_field_by_name.restype = POINTER(struct_field_info)
    Vect_get_field_by_name.argtypes = [POINTER(struct_Map_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 114
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_field2'):
    Vect_get_field2 = _libs['grass_vector.7.0.svn'].Vect_get_field2
    Vect_get_field2.restype = POINTER(struct_field_info)
    Vect_get_field2.argtypes = [POINTER(struct_Map_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 115
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_field_number'):
    Vect_get_field_number = _libs['grass_vector.7.0.svn'].Vect_get_field_number
    Vect_get_field_number.restype = c_int
    Vect_get_field_number.argtypes = [POINTER(struct_Map_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 116
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_db_updated'):
    Vect_set_db_updated = _libs['grass_vector.7.0.svn'].Vect_set_db_updated
    Vect_set_db_updated.restype = None
    Vect_set_db_updated.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 117
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_column_names'):
    Vect_get_column_names = _libs['grass_vector.7.0.svn'].Vect_get_column_names
    Vect_get_column_names.restype = ReturnString
    Vect_get_column_names.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 118
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_column_types'):
    Vect_get_column_types = _libs['grass_vector.7.0.svn'].Vect_get_column_types
    Vect_get_column_types.restype = ReturnString
    Vect_get_column_types.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 119
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_column_names_types'):
    Vect_get_column_names_types = _libs['grass_vector.7.0.svn'].Vect_get_column_names_types
    Vect_get_column_names_types.restype = ReturnString
    Vect_get_column_names_types.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 122
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_new_list'):
    Vect_new_list = _libs['grass_vector.7.0.svn'].Vect_new_list
    Vect_new_list.restype = POINTER(struct_ilist)
    Vect_new_list.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 123
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_list_append'):
    Vect_list_append = _libs['grass_vector.7.0.svn'].Vect_list_append
    Vect_list_append.restype = c_int
    Vect_list_append.argtypes = [POINTER(struct_ilist), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 124
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_list_append_list'):
    Vect_list_append_list = _libs['grass_vector.7.0.svn'].Vect_list_append_list
    Vect_list_append_list.restype = c_int
    Vect_list_append_list.argtypes = [POINTER(struct_ilist), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 125
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_list_delete'):
    Vect_list_delete = _libs['grass_vector.7.0.svn'].Vect_list_delete
    Vect_list_delete.restype = c_int
    Vect_list_delete.argtypes = [POINTER(struct_ilist), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 126
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_list_delete_list'):
    Vect_list_delete_list = _libs['grass_vector.7.0.svn'].Vect_list_delete_list
    Vect_list_delete_list.restype = c_int
    Vect_list_delete_list.argtypes = [POINTER(struct_ilist), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 127
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_val_in_list'):
    Vect_val_in_list = _libs['grass_vector.7.0.svn'].Vect_val_in_list
    Vect_val_in_list.restype = c_int
    Vect_val_in_list.argtypes = [POINTER(struct_ilist), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 128
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_reset_list'):
    Vect_reset_list = _libs['grass_vector.7.0.svn'].Vect_reset_list
    Vect_reset_list.restype = c_int
    Vect_reset_list.argtypes = [POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 129
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_destroy_list'):
    Vect_destroy_list = _libs['grass_vector.7.0.svn'].Vect_destroy_list
    Vect_destroy_list.restype = None
    Vect_destroy_list.argtypes = [POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 132
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_new_boxlist'):
    Vect_new_boxlist = _libs['grass_vector.7.0.svn'].Vect_new_boxlist
    Vect_new_boxlist.restype = POINTER(struct_boxlist)
    Vect_new_boxlist.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 133
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_boxlist_append'):
    Vect_boxlist_append = _libs['grass_vector.7.0.svn'].Vect_boxlist_append
    Vect_boxlist_append.restype = c_int
    Vect_boxlist_append.argtypes = [POINTER(struct_boxlist), c_int, struct_bound_box]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 134
for _lib in _libs.values():
    if hasattr(_lib, 'Vect_boxlist_append_list'):
        Vect_boxlist_append_list = _lib.Vect_boxlist_append_list
        Vect_boxlist_append_list.restype = c_int
        Vect_boxlist_append_list.argtypes = [POINTER(struct_boxlist), POINTER(struct_boxlist)]
        break

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 135
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_boxlist_delete'):
    Vect_boxlist_delete = _libs['grass_vector.7.0.svn'].Vect_boxlist_delete
    Vect_boxlist_delete.restype = c_int
    Vect_boxlist_delete.argtypes = [POINTER(struct_boxlist), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 136
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_boxlist_delete_boxlist'):
    Vect_boxlist_delete_boxlist = _libs['grass_vector.7.0.svn'].Vect_boxlist_delete_boxlist
    Vect_boxlist_delete_boxlist.restype = c_int
    Vect_boxlist_delete_boxlist.argtypes = [POINTER(struct_boxlist), POINTER(struct_boxlist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 137
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_val_in_boxlist'):
    Vect_val_in_boxlist = _libs['grass_vector.7.0.svn'].Vect_val_in_boxlist
    Vect_val_in_boxlist.restype = c_int
    Vect_val_in_boxlist.argtypes = [POINTER(struct_boxlist), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 138
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_reset_boxlist'):
    Vect_reset_boxlist = _libs['grass_vector.7.0.svn'].Vect_reset_boxlist
    Vect_reset_boxlist.restype = c_int
    Vect_reset_boxlist.argtypes = [POINTER(struct_boxlist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 139
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_destroy_boxlist'):
    Vect_destroy_boxlist = _libs['grass_vector.7.0.svn'].Vect_destroy_boxlist
    Vect_destroy_boxlist.restype = None
    Vect_destroy_boxlist.argtypes = [POINTER(struct_boxlist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 142
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_point_in_box'):
    Vect_point_in_box = _libs['grass_vector.7.0.svn'].Vect_point_in_box
    Vect_point_in_box.restype = c_int
    Vect_point_in_box.argtypes = [c_double, c_double, c_double, POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 143
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_box_overlap'):
    Vect_box_overlap = _libs['grass_vector.7.0.svn'].Vect_box_overlap
    Vect_box_overlap.restype = c_int
    Vect_box_overlap.argtypes = [POINTER(struct_bound_box), POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 144
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_box_copy'):
    Vect_box_copy = _libs['grass_vector.7.0.svn'].Vect_box_copy
    Vect_box_copy.restype = c_int
    Vect_box_copy.argtypes = [POINTER(struct_bound_box), POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 145
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_box_extend'):
    Vect_box_extend = _libs['grass_vector.7.0.svn'].Vect_box_extend
    Vect_box_extend.restype = c_int
    Vect_box_extend.argtypes = [POINTER(struct_bound_box), POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 146
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_box_clip'):
    Vect_box_clip = _libs['grass_vector.7.0.svn'].Vect_box_clip
    Vect_box_clip.restype = c_int
    Vect_box_clip.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 147
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_region_box'):
    Vect_region_box = _libs['grass_vector.7.0.svn'].Vect_region_box
    Vect_region_box.restype = c_int
    Vect_region_box.argtypes = [POINTER(struct_Cell_head), POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 150
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_get_num_fields'):
    Vect_cidx_get_num_fields = _libs['grass_vector.7.0.svn'].Vect_cidx_get_num_fields
    Vect_cidx_get_num_fields.restype = c_int
    Vect_cidx_get_num_fields.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 151
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_get_field_number'):
    Vect_cidx_get_field_number = _libs['grass_vector.7.0.svn'].Vect_cidx_get_field_number
    Vect_cidx_get_field_number.restype = c_int
    Vect_cidx_get_field_number.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 152
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_get_field_index'):
    Vect_cidx_get_field_index = _libs['grass_vector.7.0.svn'].Vect_cidx_get_field_index
    Vect_cidx_get_field_index.restype = c_int
    Vect_cidx_get_field_index.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 153
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_get_num_unique_cats_by_index'):
    Vect_cidx_get_num_unique_cats_by_index = _libs['grass_vector.7.0.svn'].Vect_cidx_get_num_unique_cats_by_index
    Vect_cidx_get_num_unique_cats_by_index.restype = c_int
    Vect_cidx_get_num_unique_cats_by_index.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 154
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_get_num_cats_by_index'):
    Vect_cidx_get_num_cats_by_index = _libs['grass_vector.7.0.svn'].Vect_cidx_get_num_cats_by_index
    Vect_cidx_get_num_cats_by_index.restype = c_int
    Vect_cidx_get_num_cats_by_index.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 155
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_get_num_types_by_index'):
    Vect_cidx_get_num_types_by_index = _libs['grass_vector.7.0.svn'].Vect_cidx_get_num_types_by_index
    Vect_cidx_get_num_types_by_index.restype = c_int
    Vect_cidx_get_num_types_by_index.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 156
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_get_type_count_by_index'):
    Vect_cidx_get_type_count_by_index = _libs['grass_vector.7.0.svn'].Vect_cidx_get_type_count_by_index
    Vect_cidx_get_type_count_by_index.restype = c_int
    Vect_cidx_get_type_count_by_index.argtypes = [POINTER(struct_Map_info), c_int, c_int, POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 158
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_get_type_count'):
    Vect_cidx_get_type_count = _libs['grass_vector.7.0.svn'].Vect_cidx_get_type_count
    Vect_cidx_get_type_count.restype = c_int
    Vect_cidx_get_type_count.argtypes = [POINTER(struct_Map_info), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 159
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_get_cat_by_index'):
    Vect_cidx_get_cat_by_index = _libs['grass_vector.7.0.svn'].Vect_cidx_get_cat_by_index
    Vect_cidx_get_cat_by_index.restype = c_int
    Vect_cidx_get_cat_by_index.argtypes = [POINTER(struct_Map_info), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 161
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_find_next'):
    Vect_cidx_find_next = _libs['grass_vector.7.0.svn'].Vect_cidx_find_next
    Vect_cidx_find_next.restype = c_int
    Vect_cidx_find_next.argtypes = [POINTER(struct_Map_info), c_int, c_int, c_int, c_int, POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 162
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_find_all'):
    Vect_cidx_find_all = _libs['grass_vector.7.0.svn'].Vect_cidx_find_all
    Vect_cidx_find_all.restype = None
    Vect_cidx_find_all.argtypes = [POINTER(struct_Map_info), c_int, c_int, c_int, POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 163
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_dump'):
    Vect_cidx_dump = _libs['grass_vector.7.0.svn'].Vect_cidx_dump
    Vect_cidx_dump.restype = c_int
    Vect_cidx_dump.argtypes = [POINTER(struct_Map_info), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 164
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_save'):
    Vect_cidx_save = _libs['grass_vector.7.0.svn'].Vect_cidx_save
    Vect_cidx_save.restype = c_int
    Vect_cidx_save.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 165
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_cidx_open'):
    Vect_cidx_open = _libs['grass_vector.7.0.svn'].Vect_cidx_open
    Vect_cidx_open.restype = c_int
    Vect_cidx_open.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 169
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_read_header'):
    Vect_read_header = _libs['grass_vector.7.0.svn'].Vect_read_header
    Vect_read_header.restype = c_int
    Vect_read_header.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 170
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_write_header'):
    Vect_write_header = _libs['grass_vector.7.0.svn'].Vect_write_header
    Vect_write_header.restype = c_int
    Vect_write_header.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 171
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_name'):
    Vect_get_name = _libs['grass_vector.7.0.svn'].Vect_get_name
    Vect_get_name.restype = ReturnString
    Vect_get_name.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 172
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_mapset'):
    Vect_get_mapset = _libs['grass_vector.7.0.svn'].Vect_get_mapset
    Vect_get_mapset.restype = ReturnString
    Vect_get_mapset.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 173
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_full_name'):
    Vect_get_full_name = _libs['grass_vector.7.0.svn'].Vect_get_full_name
    Vect_get_full_name.restype = ReturnString
    Vect_get_full_name.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 174
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_ogr_dsn_name'):
    Vect_get_ogr_dsn_name = _libs['grass_vector.7.0.svn'].Vect_get_ogr_dsn_name
    Vect_get_ogr_dsn_name.restype = ReturnString
    Vect_get_ogr_dsn_name.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 175
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_ogr_layer_name'):
    Vect_get_ogr_layer_name = _libs['grass_vector.7.0.svn'].Vect_get_ogr_layer_name
    Vect_get_ogr_layer_name.restype = ReturnString
    Vect_get_ogr_layer_name.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 176
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_ogr_format_info'):
    Vect_get_ogr_format_info = _libs['grass_vector.7.0.svn'].Vect_get_ogr_format_info
    Vect_get_ogr_format_info.restype = ReturnString
    Vect_get_ogr_format_info.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 177
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_ogr_geometry_type'):
    Vect_get_ogr_geometry_type = _libs['grass_vector.7.0.svn'].Vect_get_ogr_geometry_type
    Vect_get_ogr_geometry_type.restype = ReturnString
    Vect_get_ogr_geometry_type.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 178
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_is_3d'):
    Vect_is_3d = _libs['grass_vector.7.0.svn'].Vect_is_3d
    Vect_is_3d.restype = c_int
    Vect_is_3d.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 179
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_organization'):
    Vect_set_organization = _libs['grass_vector.7.0.svn'].Vect_set_organization
    Vect_set_organization.restype = c_int
    Vect_set_organization.argtypes = [POINTER(struct_Map_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 180
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_organization'):
    Vect_get_organization = _libs['grass_vector.7.0.svn'].Vect_get_organization
    Vect_get_organization.restype = ReturnString
    Vect_get_organization.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 181
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_date'):
    Vect_set_date = _libs['grass_vector.7.0.svn'].Vect_set_date
    Vect_set_date.restype = c_int
    Vect_set_date.argtypes = [POINTER(struct_Map_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 182
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_date'):
    Vect_get_date = _libs['grass_vector.7.0.svn'].Vect_get_date
    Vect_get_date.restype = ReturnString
    Vect_get_date.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 183
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_person'):
    Vect_set_person = _libs['grass_vector.7.0.svn'].Vect_set_person
    Vect_set_person.restype = c_int
    Vect_set_person.argtypes = [POINTER(struct_Map_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 184
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_person'):
    Vect_get_person = _libs['grass_vector.7.0.svn'].Vect_get_person
    Vect_get_person.restype = ReturnString
    Vect_get_person.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 185
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_map_name'):
    Vect_set_map_name = _libs['grass_vector.7.0.svn'].Vect_set_map_name
    Vect_set_map_name.restype = c_int
    Vect_set_map_name.argtypes = [POINTER(struct_Map_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 186
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_map_name'):
    Vect_get_map_name = _libs['grass_vector.7.0.svn'].Vect_get_map_name
    Vect_get_map_name.restype = ReturnString
    Vect_get_map_name.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 187
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_map_date'):
    Vect_set_map_date = _libs['grass_vector.7.0.svn'].Vect_set_map_date
    Vect_set_map_date.restype = c_int
    Vect_set_map_date.argtypes = [POINTER(struct_Map_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 188
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_map_date'):
    Vect_get_map_date = _libs['grass_vector.7.0.svn'].Vect_get_map_date
    Vect_get_map_date.restype = ReturnString
    Vect_get_map_date.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 189
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_comment'):
    Vect_set_comment = _libs['grass_vector.7.0.svn'].Vect_set_comment
    Vect_set_comment.restype = c_int
    Vect_set_comment.argtypes = [POINTER(struct_Map_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 190
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_comment'):
    Vect_get_comment = _libs['grass_vector.7.0.svn'].Vect_get_comment
    Vect_get_comment.restype = ReturnString
    Vect_get_comment.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 191
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_scale'):
    Vect_set_scale = _libs['grass_vector.7.0.svn'].Vect_set_scale
    Vect_set_scale.restype = c_int
    Vect_set_scale.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 192
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_scale'):
    Vect_get_scale = _libs['grass_vector.7.0.svn'].Vect_get_scale
    Vect_get_scale.restype = c_int
    Vect_get_scale.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 193
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_zone'):
    Vect_set_zone = _libs['grass_vector.7.0.svn'].Vect_set_zone
    Vect_set_zone.restype = c_int
    Vect_set_zone.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 194
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_zone'):
    Vect_get_zone = _libs['grass_vector.7.0.svn'].Vect_get_zone
    Vect_get_zone.restype = c_int
    Vect_get_zone.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 195
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_proj'):
    Vect_get_proj = _libs['grass_vector.7.0.svn'].Vect_get_proj
    Vect_get_proj.restype = c_int
    Vect_get_proj.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 196
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_proj'):
    Vect_set_proj = _libs['grass_vector.7.0.svn'].Vect_set_proj
    Vect_set_proj.restype = c_int
    Vect_set_proj.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 197
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_proj_name'):
    Vect_get_proj_name = _libs['grass_vector.7.0.svn'].Vect_get_proj_name
    Vect_get_proj_name.restype = ReturnString
    Vect_get_proj_name.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 198
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_thresh'):
    Vect_set_thresh = _libs['grass_vector.7.0.svn'].Vect_set_thresh
    Vect_set_thresh.restype = c_int
    Vect_set_thresh.argtypes = [POINTER(struct_Map_info), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 199
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_thresh'):
    Vect_get_thresh = _libs['grass_vector.7.0.svn'].Vect_get_thresh
    Vect_get_thresh.restype = c_double
    Vect_get_thresh.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 200
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_constraint_box'):
    Vect_get_constraint_box = _libs['grass_vector.7.0.svn'].Vect_get_constraint_box
    Vect_get_constraint_box.restype = c_int
    Vect_get_constraint_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 204
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_level'):
    Vect_level = _libs['grass_vector.7.0.svn'].Vect_level
    Vect_level.restype = c_int
    Vect_level.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 205
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_line_type'):
    Vect_get_line_type = _libs['grass_vector.7.0.svn'].Vect_get_line_type
    Vect_get_line_type.restype = c_int
    Vect_get_line_type.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 206
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_nodes'):
    Vect_get_num_nodes = _libs['grass_vector.7.0.svn'].Vect_get_num_nodes
    Vect_get_num_nodes.restype = plus_t
    Vect_get_num_nodes.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 207
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_primitives'):
    Vect_get_num_primitives = _libs['grass_vector.7.0.svn'].Vect_get_num_primitives
    Vect_get_num_primitives.restype = plus_t
    Vect_get_num_primitives.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 208
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_lines'):
    Vect_get_num_lines = _libs['grass_vector.7.0.svn'].Vect_get_num_lines
    Vect_get_num_lines.restype = plus_t
    Vect_get_num_lines.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 209
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_areas'):
    Vect_get_num_areas = _libs['grass_vector.7.0.svn'].Vect_get_num_areas
    Vect_get_num_areas.restype = plus_t
    Vect_get_num_areas.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 210
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_faces'):
    Vect_get_num_faces = _libs['grass_vector.7.0.svn'].Vect_get_num_faces
    Vect_get_num_faces.restype = plus_t
    Vect_get_num_faces.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 211
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_kernels'):
    Vect_get_num_kernels = _libs['grass_vector.7.0.svn'].Vect_get_num_kernels
    Vect_get_num_kernels.restype = plus_t
    Vect_get_num_kernels.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 212
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_volumes'):
    Vect_get_num_volumes = _libs['grass_vector.7.0.svn'].Vect_get_num_volumes
    Vect_get_num_volumes.restype = plus_t
    Vect_get_num_volumes.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 213
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_islands'):
    Vect_get_num_islands = _libs['grass_vector.7.0.svn'].Vect_get_num_islands
    Vect_get_num_islands.restype = plus_t
    Vect_get_num_islands.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 214
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_holes'):
    Vect_get_num_holes = _libs['grass_vector.7.0.svn'].Vect_get_num_holes
    Vect_get_num_holes.restype = plus_t
    Vect_get_num_holes.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 215
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_line_box'):
    Vect_get_line_box = _libs['grass_vector.7.0.svn'].Vect_get_line_box
    Vect_get_line_box.restype = c_int
    Vect_get_line_box.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 216
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_area_box'):
    Vect_get_area_box = _libs['grass_vector.7.0.svn'].Vect_get_area_box
    Vect_get_area_box.restype = c_int
    Vect_get_area_box.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 217
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_isle_box'):
    Vect_get_isle_box = _libs['grass_vector.7.0.svn'].Vect_get_isle_box
    Vect_get_isle_box.restype = c_int
    Vect_get_isle_box.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 218
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_map_box'):
    Vect_get_map_box = _libs['grass_vector.7.0.svn'].Vect_get_map_box
    Vect_get_map_box.restype = c_int
    Vect_get_map_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 219
if hasattr(_libs['grass_vector.7.0.svn'], 'V__map_overlap'):
    V__map_overlap = _libs['grass_vector.7.0.svn'].V__map_overlap
    V__map_overlap.restype = c_int
    V__map_overlap.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 220
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_release_support'):
    Vect_set_release_support = _libs['grass_vector.7.0.svn'].Vect_set_release_support
    Vect_set_release_support.restype = None
    Vect_set_release_support.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 221
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_category_index_update'):
    Vect_set_category_index_update = _libs['grass_vector.7.0.svn'].Vect_set_category_index_update
    Vect_set_category_index_update.restype = None
    Vect_set_category_index_update.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 224
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_fatal_error'):
    Vect_set_fatal_error = _libs['grass_vector.7.0.svn'].Vect_set_fatal_error
    Vect_set_fatal_error.restype = c_int
    Vect_set_fatal_error.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 225
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_fatal_error'):
    Vect_get_fatal_error = _libs['grass_vector.7.0.svn'].Vect_get_fatal_error
    Vect_get_fatal_error.restype = c_int
    Vect_get_fatal_error.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 228
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_check_input_output_name'):
    Vect_check_input_output_name = _libs['grass_vector.7.0.svn'].Vect_check_input_output_name
    Vect_check_input_output_name.restype = c_int
    Vect_check_input_output_name.argtypes = [String, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 229
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_legal_filename'):
    Vect_legal_filename = _libs['grass_vector.7.0.svn'].Vect_legal_filename
    Vect_legal_filename.restype = c_int
    Vect_legal_filename.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 230
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_open_level'):
    Vect_set_open_level = _libs['grass_vector.7.0.svn'].Vect_set_open_level
    Vect_set_open_level.restype = c_int
    Vect_set_open_level.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 231
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_open_old'):
    Vect_open_old = _libs['grass_vector.7.0.svn'].Vect_open_old
    Vect_open_old.restype = c_int
    Vect_open_old.argtypes = [POINTER(struct_Map_info), String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 232
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_open_old2'):
    Vect_open_old2 = _libs['grass_vector.7.0.svn'].Vect_open_old2
    Vect_open_old2.restype = c_int
    Vect_open_old2.argtypes = [POINTER(struct_Map_info), String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 233
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_open_old_head'):
    Vect_open_old_head = _libs['grass_vector.7.0.svn'].Vect_open_old_head
    Vect_open_old_head.restype = c_int
    Vect_open_old_head.argtypes = [POINTER(struct_Map_info), String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 234
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_open_old_head2'):
    Vect_open_old_head2 = _libs['grass_vector.7.0.svn'].Vect_open_old_head2
    Vect_open_old_head2.restype = c_int
    Vect_open_old_head2.argtypes = [POINTER(struct_Map_info), String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 235
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_open_new'):
    Vect_open_new = _libs['grass_vector.7.0.svn'].Vect_open_new
    Vect_open_new.restype = c_int
    Vect_open_new.argtypes = [POINTER(struct_Map_info), String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 236
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_open_update'):
    Vect_open_update = _libs['grass_vector.7.0.svn'].Vect_open_update
    Vect_open_update.restype = c_int
    Vect_open_update.argtypes = [POINTER(struct_Map_info), String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 237
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_open_update2'):
    Vect_open_update2 = _libs['grass_vector.7.0.svn'].Vect_open_update2
    Vect_open_update2.restype = c_int
    Vect_open_update2.argtypes = [POINTER(struct_Map_info), String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 238
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_open_update_head'):
    Vect_open_update_head = _libs['grass_vector.7.0.svn'].Vect_open_update_head
    Vect_open_update_head.restype = c_int
    Vect_open_update_head.argtypes = [POINTER(struct_Map_info), String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 239
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_copy_head_data'):
    Vect_copy_head_data = _libs['grass_vector.7.0.svn'].Vect_copy_head_data
    Vect_copy_head_data.restype = c_int
    Vect_copy_head_data.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 240
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_build'):
    Vect_build = _libs['grass_vector.7.0.svn'].Vect_build
    Vect_build.restype = c_int
    Vect_build.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 241
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_built'):
    Vect_get_built = _libs['grass_vector.7.0.svn'].Vect_get_built
    Vect_get_built.restype = c_int
    Vect_get_built.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 242
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_build_partial'):
    Vect_build_partial = _libs['grass_vector.7.0.svn'].Vect_build_partial
    Vect_build_partial.restype = c_int
    Vect_build_partial.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 243
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_constraint_region'):
    Vect_set_constraint_region = _libs['grass_vector.7.0.svn'].Vect_set_constraint_region
    Vect_set_constraint_region.restype = c_int
    Vect_set_constraint_region.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 245
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_set_constraint_type'):
    Vect_set_constraint_type = _libs['grass_vector.7.0.svn'].Vect_set_constraint_type
    Vect_set_constraint_type.restype = c_int
    Vect_set_constraint_type.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 246
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_remove_constraints'):
    Vect_remove_constraints = _libs['grass_vector.7.0.svn'].Vect_remove_constraints
    Vect_remove_constraints.restype = c_int
    Vect_remove_constraints.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 247
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_rewind'):
    Vect_rewind = _libs['grass_vector.7.0.svn'].Vect_rewind
    Vect_rewind.restype = c_int
    Vect_rewind.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 248
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_close'):
    Vect_close = _libs['grass_vector.7.0.svn'].Vect_close
    Vect_close.restype = c_int
    Vect_close.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 252
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_read_next_line'):
    Vect_read_next_line = _libs['grass_vector.7.0.svn'].Vect_read_next_line
    Vect_read_next_line.restype = c_int
    Vect_read_next_line.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 254
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_write_line'):
    Vect_write_line = _libs['grass_vector.7.0.svn'].Vect_write_line
    Vect_write_line.restype = off_t
    Vect_write_line.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 257
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_dblinks'):
    Vect_get_num_dblinks = _libs['grass_vector.7.0.svn'].Vect_get_num_dblinks
    Vect_get_num_dblinks.restype = c_int
    Vect_get_num_dblinks.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 260
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_read_line'):
    Vect_read_line = _libs['grass_vector.7.0.svn'].Vect_read_line
    Vect_read_line.restype = c_int
    Vect_read_line.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 262
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_rewrite_line'):
    Vect_rewrite_line = _libs['grass_vector.7.0.svn'].Vect_rewrite_line
    Vect_rewrite_line.restype = off_t
    Vect_rewrite_line.argtypes = [POINTER(struct_Map_info), c_int, c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 264
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_delete_line'):
    Vect_delete_line = _libs['grass_vector.7.0.svn'].Vect_delete_line
    Vect_delete_line.restype = c_int
    Vect_delete_line.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 265
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_restore_line'):
    Vect_restore_line = _libs['grass_vector.7.0.svn'].Vect_restore_line
    Vect_restore_line.restype = c_int
    Vect_restore_line.argtypes = [POINTER(struct_Map_info), c_int, off_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 267
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_alive'):
    Vect_line_alive = _libs['grass_vector.7.0.svn'].Vect_line_alive
    Vect_line_alive.restype = c_int
    Vect_line_alive.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 268
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_node_alive'):
    Vect_node_alive = _libs['grass_vector.7.0.svn'].Vect_node_alive
    Vect_node_alive.restype = c_int
    Vect_node_alive.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 269
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_area_alive'):
    Vect_area_alive = _libs['grass_vector.7.0.svn'].Vect_area_alive
    Vect_area_alive.restype = c_int
    Vect_area_alive.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 270
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_isle_alive'):
    Vect_isle_alive = _libs['grass_vector.7.0.svn'].Vect_isle_alive
    Vect_isle_alive.restype = c_int
    Vect_isle_alive.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 271
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_line_nodes'):
    Vect_get_line_nodes = _libs['grass_vector.7.0.svn'].Vect_get_line_nodes
    Vect_get_line_nodes.restype = c_int
    Vect_get_line_nodes.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 272
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_line_areas'):
    Vect_get_line_areas = _libs['grass_vector.7.0.svn'].Vect_get_line_areas
    Vect_get_line_areas.restype = c_int
    Vect_get_line_areas.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 273
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_line_offset'):
    Vect_get_line_offset = _libs['grass_vector.7.0.svn'].Vect_get_line_offset
    Vect_get_line_offset.restype = off_t
    Vect_get_line_offset.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 275
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_node_coor'):
    Vect_get_node_coor = _libs['grass_vector.7.0.svn'].Vect_get_node_coor
    Vect_get_node_coor.restype = c_int
    Vect_get_node_coor.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 276
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_node_n_lines'):
    Vect_get_node_n_lines = _libs['grass_vector.7.0.svn'].Vect_get_node_n_lines
    Vect_get_node_n_lines.restype = c_int
    Vect_get_node_n_lines.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 277
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_node_line'):
    Vect_get_node_line = _libs['grass_vector.7.0.svn'].Vect_get_node_line
    Vect_get_node_line.restype = c_int
    Vect_get_node_line.argtypes = [POINTER(struct_Map_info), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 278
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_node_line_angle'):
    Vect_get_node_line_angle = _libs['grass_vector.7.0.svn'].Vect_get_node_line_angle
    Vect_get_node_line_angle.restype = c_float
    Vect_get_node_line_angle.argtypes = [POINTER(struct_Map_info), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 280
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_area_points'):
    Vect_get_area_points = _libs['grass_vector.7.0.svn'].Vect_get_area_points
    Vect_get_area_points.restype = c_int
    Vect_get_area_points.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 281
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_area_centroid'):
    Vect_get_area_centroid = _libs['grass_vector.7.0.svn'].Vect_get_area_centroid
    Vect_get_area_centroid.restype = c_int
    Vect_get_area_centroid.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 282
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_area_num_isles'):
    Vect_get_area_num_isles = _libs['grass_vector.7.0.svn'].Vect_get_area_num_isles
    Vect_get_area_num_isles.restype = c_int
    Vect_get_area_num_isles.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 283
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_area_isle'):
    Vect_get_area_isle = _libs['grass_vector.7.0.svn'].Vect_get_area_isle
    Vect_get_area_isle.restype = c_int
    Vect_get_area_isle.argtypes = [POINTER(struct_Map_info), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 284
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_area_area'):
    Vect_get_area_area = _libs['grass_vector.7.0.svn'].Vect_get_area_area
    Vect_get_area_area.restype = c_double
    Vect_get_area_area.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 285
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_area_boundaries'):
    Vect_get_area_boundaries = _libs['grass_vector.7.0.svn'].Vect_get_area_boundaries
    Vect_get_area_boundaries.restype = c_int
    Vect_get_area_boundaries.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 287
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_isle_points'):
    Vect_get_isle_points = _libs['grass_vector.7.0.svn'].Vect_get_isle_points
    Vect_get_isle_points.restype = c_int
    Vect_get_isle_points.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 288
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_isle_area'):
    Vect_get_isle_area = _libs['grass_vector.7.0.svn'].Vect_get_isle_area
    Vect_get_isle_area.restype = c_int
    Vect_get_isle_area.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 289
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_isle_boundaries'):
    Vect_get_isle_boundaries = _libs['grass_vector.7.0.svn'].Vect_get_isle_boundaries
    Vect_get_isle_boundaries.restype = c_int
    Vect_get_isle_boundaries.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 291
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_centroid_area'):
    Vect_get_centroid_area = _libs['grass_vector.7.0.svn'].Vect_get_centroid_area
    Vect_get_centroid_area.restype = c_int
    Vect_get_centroid_area.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 294
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_updated_lines'):
    Vect_get_num_updated_lines = _libs['grass_vector.7.0.svn'].Vect_get_num_updated_lines
    Vect_get_num_updated_lines.restype = c_int
    Vect_get_num_updated_lines.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 295
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_updated_line'):
    Vect_get_updated_line = _libs['grass_vector.7.0.svn'].Vect_get_updated_line
    Vect_get_updated_line.restype = c_int
    Vect_get_updated_line.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 296
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_num_updated_nodes'):
    Vect_get_num_updated_nodes = _libs['grass_vector.7.0.svn'].Vect_get_num_updated_nodes
    Vect_get_num_updated_nodes.restype = c_int
    Vect_get_num_updated_nodes.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 297
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_updated_node'):
    Vect_get_updated_node = _libs['grass_vector.7.0.svn'].Vect_get_updated_node
    Vect_get_updated_node.restype = c_int
    Vect_get_updated_node.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 300
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_hist_command'):
    Vect_hist_command = _libs['grass_vector.7.0.svn'].Vect_hist_command
    Vect_hist_command.restype = c_int
    Vect_hist_command.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 301
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_hist_write'):
    Vect_hist_write = _libs['grass_vector.7.0.svn'].Vect_hist_write
    Vect_hist_write.restype = c_int
    Vect_hist_write.argtypes = [POINTER(struct_Map_info), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 302
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_hist_copy'):
    Vect_hist_copy = _libs['grass_vector.7.0.svn'].Vect_hist_copy
    Vect_hist_copy.restype = c_int
    Vect_hist_copy.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 303
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_hist_rewind'):
    Vect_hist_rewind = _libs['grass_vector.7.0.svn'].Vect_hist_rewind
    Vect_hist_rewind.restype = None
    Vect_hist_rewind.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 304
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_hist_read'):
    Vect_hist_read = _libs['grass_vector.7.0.svn'].Vect_hist_read
    Vect_hist_read.restype = ReturnString
    Vect_hist_read.argtypes = [String, c_int, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 307
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_select_lines_by_box'):
    Vect_select_lines_by_box = _libs['grass_vector.7.0.svn'].Vect_select_lines_by_box
    Vect_select_lines_by_box.restype = c_int
    Vect_select_lines_by_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box), c_int, POINTER(struct_boxlist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 309
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_select_areas_by_box'):
    Vect_select_areas_by_box = _libs['grass_vector.7.0.svn'].Vect_select_areas_by_box
    Vect_select_areas_by_box.restype = c_int
    Vect_select_areas_by_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box), POINTER(struct_boxlist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 310
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_select_isles_by_box'):
    Vect_select_isles_by_box = _libs['grass_vector.7.0.svn'].Vect_select_isles_by_box
    Vect_select_isles_by_box.restype = c_int
    Vect_select_isles_by_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box), POINTER(struct_boxlist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 311
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_select_nodes_by_box'):
    Vect_select_nodes_by_box = _libs['grass_vector.7.0.svn'].Vect_select_nodes_by_box
    Vect_select_nodes_by_box.restype = c_int
    Vect_select_nodes_by_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 312
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_find_node'):
    Vect_find_node = _libs['grass_vector.7.0.svn'].Vect_find_node
    Vect_find_node.restype = c_int
    Vect_find_node.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 313
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_find_line'):
    Vect_find_line = _libs['grass_vector.7.0.svn'].Vect_find_line
    Vect_find_line.restype = c_int
    Vect_find_line.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_int, c_double, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 315
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_find_line_list'):
    Vect_find_line_list = _libs['grass_vector.7.0.svn'].Vect_find_line_list
    Vect_find_line_list.restype = c_int
    Vect_find_line_list.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_int, c_double, c_int, POINTER(struct_ilist), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 317
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_find_area'):
    Vect_find_area = _libs['grass_vector.7.0.svn'].Vect_find_area
    Vect_find_area.restype = c_int
    Vect_find_area.argtypes = [POINTER(struct_Map_info), c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 318
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_find_island'):
    Vect_find_island = _libs['grass_vector.7.0.svn'].Vect_find_island
    Vect_find_island.restype = c_int
    Vect_find_island.argtypes = [POINTER(struct_Map_info), c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 319
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_select_lines_by_polygon'):
    Vect_select_lines_by_polygon = _libs['grass_vector.7.0.svn'].Vect_select_lines_by_polygon
    Vect_select_lines_by_polygon.restype = c_int
    Vect_select_lines_by_polygon.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), c_int, POINTER(POINTER(struct_line_pnts)), c_int, POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 321
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_select_areas_by_polygon'):
    Vect_select_areas_by_polygon = _libs['grass_vector.7.0.svn'].Vect_select_areas_by_polygon
    Vect_select_areas_by_polygon.restype = c_int
    Vect_select_areas_by_polygon.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), c_int, POINTER(POINTER(struct_line_pnts)), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 325
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_tin_get_z'):
    Vect_tin_get_z = _libs['grass_vector.7.0.svn'].Vect_tin_get_z
    Vect_tin_get_z.restype = c_int
    Vect_tin_get_z.argtypes = [POINTER(struct_Map_info), c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 329
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_find_poly_centroid'):
    Vect_find_poly_centroid = _libs['grass_vector.7.0.svn'].Vect_find_poly_centroid
    Vect_find_poly_centroid.restype = c_int
    Vect_find_poly_centroid.argtypes = [POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 330
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect__intersect_line_with_poly'):
    Vect__intersect_line_with_poly = _libs['grass_vector.7.0.svn'].Vect__intersect_line_with_poly
    Vect__intersect_line_with_poly.restype = c_int
    Vect__intersect_line_with_poly.argtypes = [POINTER(struct_line_pnts), c_double, POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 332
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_point_in_area'):
    Vect_get_point_in_area = _libs['grass_vector.7.0.svn'].Vect_get_point_in_area
    Vect_get_point_in_area.restype = c_int
    Vect_get_point_in_area.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 333
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_point_in_poly'):
    Vect_get_point_in_poly = _libs['grass_vector.7.0.svn'].Vect_get_point_in_poly
    Vect_get_point_in_poly.restype = c_int
    Vect_get_point_in_poly.argtypes = [POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 334
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_get_point_in_poly_isl'):
    Vect_get_point_in_poly_isl = _libs['grass_vector.7.0.svn'].Vect_get_point_in_poly_isl
    Vect_get_point_in_poly_isl.restype = c_int
    Vect_get_point_in_poly_isl.argtypes = [POINTER(struct_line_pnts), POINTER(POINTER(struct_line_pnts)), c_int, POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 336
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_point_in_area'):
    Vect_point_in_area = _libs['grass_vector.7.0.svn'].Vect_point_in_area
    Vect_point_in_area.restype = c_int
    Vect_point_in_area.argtypes = [c_double, c_double, POINTER(struct_Map_info), c_int, struct_bound_box]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 337
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_point_in_area_outer_ring'):
    Vect_point_in_area_outer_ring = _libs['grass_vector.7.0.svn'].Vect_point_in_area_outer_ring
    Vect_point_in_area_outer_ring.restype = c_int
    Vect_point_in_area_outer_ring.argtypes = [c_double, c_double, POINTER(struct_Map_info), c_int, struct_bound_box]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 338
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_point_in_island'):
    Vect_point_in_island = _libs['grass_vector.7.0.svn'].Vect_point_in_island
    Vect_point_in_island.restype = c_int
    Vect_point_in_island.argtypes = [c_double, c_double, POINTER(struct_Map_info), c_int, struct_bound_box]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 339
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_point_in_poly'):
    Vect_point_in_poly = _libs['grass_vector.7.0.svn'].Vect_point_in_poly
    Vect_point_in_poly.restype = c_int
    Vect_point_in_poly.argtypes = [c_double, c_double, POINTER(struct_line_pnts)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 342
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_break_lines'):
    Vect_break_lines = _libs['grass_vector.7.0.svn'].Vect_break_lines
    Vect_break_lines.restype = None
    Vect_break_lines.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 343
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_break_lines_list'):
    Vect_break_lines_list = _libs['grass_vector.7.0.svn'].Vect_break_lines_list
    Vect_break_lines_list.restype = c_int
    Vect_break_lines_list.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), POINTER(struct_ilist), c_int, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 345
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_merge_lines'):
    Vect_merge_lines = _libs['grass_vector.7.0.svn'].Vect_merge_lines
    Vect_merge_lines.restype = c_int
    Vect_merge_lines.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_int), POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 346
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_break_polygons'):
    Vect_break_polygons = _libs['grass_vector.7.0.svn'].Vect_break_polygons
    Vect_break_polygons.restype = None
    Vect_break_polygons.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 347
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_remove_duplicates'):
    Vect_remove_duplicates = _libs['grass_vector.7.0.svn'].Vect_remove_duplicates
    Vect_remove_duplicates.restype = None
    Vect_remove_duplicates.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 348
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_check_duplicate'):
    Vect_line_check_duplicate = _libs['grass_vector.7.0.svn'].Vect_line_check_duplicate
    Vect_line_check_duplicate.restype = c_int
    Vect_line_check_duplicate.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 350
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_snap_lines'):
    Vect_snap_lines = _libs['grass_vector.7.0.svn'].Vect_snap_lines
    Vect_snap_lines.restype = None
    Vect_snap_lines.argtypes = [POINTER(struct_Map_info), c_int, c_double, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 351
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_snap_lines_list'):
    Vect_snap_lines_list = _libs['grass_vector.7.0.svn'].Vect_snap_lines_list
    Vect_snap_lines_list.restype = None
    Vect_snap_lines_list.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), c_double, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 353
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_remove_dangles'):
    Vect_remove_dangles = _libs['grass_vector.7.0.svn'].Vect_remove_dangles
    Vect_remove_dangles.restype = None
    Vect_remove_dangles.argtypes = [POINTER(struct_Map_info), c_int, c_double, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 354
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_chtype_dangles'):
    Vect_chtype_dangles = _libs['grass_vector.7.0.svn'].Vect_chtype_dangles
    Vect_chtype_dangles.restype = None
    Vect_chtype_dangles.argtypes = [POINTER(struct_Map_info), c_double, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 355
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_select_dangles'):
    Vect_select_dangles = _libs['grass_vector.7.0.svn'].Vect_select_dangles
    Vect_select_dangles.restype = None
    Vect_select_dangles.argtypes = [POINTER(struct_Map_info), c_int, c_double, POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 356
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_remove_bridges'):
    Vect_remove_bridges = _libs['grass_vector.7.0.svn'].Vect_remove_bridges
    Vect_remove_bridges.restype = None
    Vect_remove_bridges.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 357
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_chtype_bridges'):
    Vect_chtype_bridges = _libs['grass_vector.7.0.svn'].Vect_chtype_bridges
    Vect_chtype_bridges.restype = None
    Vect_chtype_bridges.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 358
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_remove_small_areas'):
    Vect_remove_small_areas = _libs['grass_vector.7.0.svn'].Vect_remove_small_areas
    Vect_remove_small_areas.restype = c_int
    Vect_remove_small_areas.argtypes = [POINTER(struct_Map_info), c_double, POINTER(struct_Map_info), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 360
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_clean_small_angles_at_nodes'):
    Vect_clean_small_angles_at_nodes = _libs['grass_vector.7.0.svn'].Vect_clean_small_angles_at_nodes
    Vect_clean_small_angles_at_nodes.restype = c_int
    Vect_clean_small_angles_at_nodes.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 364
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_overlay_str_to_operator'):
    Vect_overlay_str_to_operator = _libs['grass_vector.7.0.svn'].Vect_overlay_str_to_operator
    Vect_overlay_str_to_operator.restype = c_int
    Vect_overlay_str_to_operator.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 365
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_overlay'):
    Vect_overlay = _libs['grass_vector.7.0.svn'].Vect_overlay
    Vect_overlay.restype = c_int
    Vect_overlay.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_ilist), POINTER(struct_ilist), POINTER(struct_Map_info), c_int, POINTER(struct_ilist), POINTER(struct_ilist), c_int, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 368
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_overlay_and'):
    Vect_overlay_and = _libs['grass_vector.7.0.svn'].Vect_overlay_and
    Vect_overlay_and.restype = c_int
    Vect_overlay_and.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_ilist), POINTER(struct_ilist), POINTER(struct_Map_info), c_int, POINTER(struct_ilist), POINTER(struct_ilist), POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 373
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_graph_init'):
    Vect_graph_init = _libs['grass_vector.7.0.svn'].Vect_graph_init
    Vect_graph_init.restype = None
    Vect_graph_init.argtypes = [POINTER(dglGraph_s), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 374
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_graph_build'):
    Vect_graph_build = _libs['grass_vector.7.0.svn'].Vect_graph_build
    Vect_graph_build.restype = None
    Vect_graph_build.argtypes = [POINTER(dglGraph_s)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 375
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_graph_add_edge'):
    Vect_graph_add_edge = _libs['grass_vector.7.0.svn'].Vect_graph_add_edge
    Vect_graph_add_edge.restype = None
    Vect_graph_add_edge.argtypes = [POINTER(dglGraph_s), c_int, c_int, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 376
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_graph_set_node_costs'):
    Vect_graph_set_node_costs = _libs['grass_vector.7.0.svn'].Vect_graph_set_node_costs
    Vect_graph_set_node_costs.restype = None
    Vect_graph_set_node_costs.argtypes = [POINTER(dglGraph_s), c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 377
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_graph_shortest_path'):
    Vect_graph_shortest_path = _libs['grass_vector.7.0.svn'].Vect_graph_shortest_path
    Vect_graph_shortest_path.restype = c_int
    Vect_graph_shortest_path.argtypes = [POINTER(dglGraph_s), c_int, c_int, POINTER(struct_ilist), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 380
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_net_build_graph'):
    Vect_net_build_graph = _libs['grass_vector.7.0.svn'].Vect_net_build_graph
    Vect_net_build_graph.restype = c_int
    Vect_net_build_graph.argtypes = [POINTER(struct_Map_info), c_int, c_int, c_int, String, String, String, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 382
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_net_shortest_path'):
    Vect_net_shortest_path = _libs['grass_vector.7.0.svn'].Vect_net_shortest_path
    Vect_net_shortest_path.restype = c_int
    Vect_net_shortest_path.argtypes = [POINTER(struct_Map_info), c_int, c_int, POINTER(struct_ilist), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 384
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_net_get_line_cost'):
    Vect_net_get_line_cost = _libs['grass_vector.7.0.svn'].Vect_net_get_line_cost
    Vect_net_get_line_cost.restype = c_int
    Vect_net_get_line_cost.argtypes = [POINTER(struct_Map_info), c_int, c_int, POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 385
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_net_get_node_cost'):
    Vect_net_get_node_cost = _libs['grass_vector.7.0.svn'].Vect_net_get_node_cost
    Vect_net_get_node_cost.restype = c_int
    Vect_net_get_node_cost.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 386
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_net_nearest_nodes'):
    Vect_net_nearest_nodes = _libs['grass_vector.7.0.svn'].Vect_net_nearest_nodes
    Vect_net_nearest_nodes.restype = c_int
    Vect_net_nearest_nodes.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_int, c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 389
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_net_shortest_path_coor'):
    Vect_net_shortest_path_coor = _libs['grass_vector.7.0.svn'].Vect_net_shortest_path_coor
    Vect_net_shortest_path_coor.restype = c_int
    Vect_net_shortest_path_coor.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(struct_line_pnts), POINTER(struct_ilist), POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 394
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_net_shortest_path_coor2'):
    Vect_net_shortest_path_coor2 = _libs['grass_vector.7.0.svn'].Vect_net_shortest_path_coor2
    Vect_net_shortest_path_coor2.restype = c_int
    Vect_net_shortest_path_coor2.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(struct_line_pnts), POINTER(struct_ilist), POINTER(struct_ilist), POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 401
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_topo_dump'):
    Vect_topo_dump = _libs['grass_vector.7.0.svn'].Vect_topo_dump
    Vect_topo_dump.restype = c_int
    Vect_topo_dump.argtypes = [POINTER(struct_Map_info), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 402
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_points_distance'):
    Vect_points_distance = _libs['grass_vector.7.0.svn'].Vect_points_distance
    Vect_points_distance.restype = c_double
    Vect_points_distance.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 404
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_option_to_types'):
    Vect_option_to_types = _libs['grass_vector.7.0.svn'].Vect_option_to_types
    Vect_option_to_types.restype = c_int
    Vect_option_to_types.argtypes = [POINTER(struct_Option)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 405
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_copy_map_lines'):
    Vect_copy_map_lines = _libs['grass_vector.7.0.svn'].Vect_copy_map_lines
    Vect_copy_map_lines.restype = c_int
    Vect_copy_map_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 406
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_copy_map_lines_field'):
    Vect_copy_map_lines_field = _libs['grass_vector.7.0.svn'].Vect_copy_map_lines_field
    Vect_copy_map_lines_field.restype = c_int
    Vect_copy_map_lines_field.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 407
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_copy'):
    Vect_copy = _libs['grass_vector.7.0.svn'].Vect_copy
    Vect_copy.restype = c_int
    Vect_copy.argtypes = [String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 408
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_rename'):
    Vect_rename = _libs['grass_vector.7.0.svn'].Vect_rename
    Vect_rename.restype = c_int
    Vect_rename.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 409
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_copy_table'):
    Vect_copy_table = _libs['grass_vector.7.0.svn'].Vect_copy_table
    Vect_copy_table.restype = c_int
    Vect_copy_table.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), c_int, c_int, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 411
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_copy_table_by_cats'):
    Vect_copy_table_by_cats = _libs['grass_vector.7.0.svn'].Vect_copy_table_by_cats
    Vect_copy_table_by_cats.restype = c_int
    Vect_copy_table_by_cats.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), c_int, c_int, String, c_int, POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 413
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_copy_tables'):
    Vect_copy_tables = _libs['grass_vector.7.0.svn'].Vect_copy_tables
    Vect_copy_tables.restype = c_int
    Vect_copy_tables.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 414
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_delete'):
    Vect_delete = _libs['grass_vector.7.0.svn'].Vect_delete
    Vect_delete.restype = c_int
    Vect_delete.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 415
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_segment_intersection'):
    Vect_segment_intersection = _libs['grass_vector.7.0.svn'].Vect_segment_intersection
    Vect_segment_intersection.restype = c_int
    Vect_segment_intersection.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 419
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_intersection'):
    Vect_line_intersection = _libs['grass_vector.7.0.svn'].Vect_line_intersection
    Vect_line_intersection.restype = c_int
    Vect_line_intersection.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(POINTER(POINTER(struct_line_pnts))), POINTER(POINTER(POINTER(struct_line_pnts))), POINTER(c_int), POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 422
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_check_intersection'):
    Vect_line_check_intersection = _libs['grass_vector.7.0.svn'].Vect_line_check_intersection
    Vect_line_check_intersection.restype = c_int
    Vect_line_check_intersection.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 423
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_line_get_intersections'):
    Vect_line_get_intersections = _libs['grass_vector.7.0.svn'].Vect_line_get_intersections
    Vect_line_get_intersections.restype = c_int
    Vect_line_get_intersections.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 425
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_subst_var'):
    Vect_subst_var = _libs['grass_vector.7.0.svn'].Vect_subst_var
    Vect_subst_var.restype = ReturnString
    Vect_subst_var.argtypes = [String, POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 428
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_spatial_index_init'):
    Vect_spatial_index_init = _libs['grass_vector.7.0.svn'].Vect_spatial_index_init
    Vect_spatial_index_init.restype = None
    Vect_spatial_index_init.argtypes = [POINTER(struct_spatial_index), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 429
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_spatial_index_destroy'):
    Vect_spatial_index_destroy = _libs['grass_vector.7.0.svn'].Vect_spatial_index_destroy
    Vect_spatial_index_destroy.restype = None
    Vect_spatial_index_destroy.argtypes = [POINTER(struct_spatial_index)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 430
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_spatial_index_add_item'):
    Vect_spatial_index_add_item = _libs['grass_vector.7.0.svn'].Vect_spatial_index_add_item
    Vect_spatial_index_add_item.restype = None
    Vect_spatial_index_add_item.argtypes = [POINTER(struct_spatial_index), c_int, POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 431
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_spatial_index_del_item'):
    Vect_spatial_index_del_item = _libs['grass_vector.7.0.svn'].Vect_spatial_index_del_item
    Vect_spatial_index_del_item.restype = None
    Vect_spatial_index_del_item.argtypes = [POINTER(struct_spatial_index), c_int, POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 432
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_spatial_index_select'):
    Vect_spatial_index_select = _libs['grass_vector.7.0.svn'].Vect_spatial_index_select
    Vect_spatial_index_select.restype = c_int
    Vect_spatial_index_select.argtypes = [POINTER(struct_spatial_index), POINTER(struct_bound_box), POINTER(struct_ilist)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 435
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_read_ascii'):
    Vect_read_ascii = _libs['grass_vector.7.0.svn'].Vect_read_ascii
    Vect_read_ascii.restype = c_int
    Vect_read_ascii.argtypes = [POINTER(FILE), POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 436
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_read_ascii_head'):
    Vect_read_ascii_head = _libs['grass_vector.7.0.svn'].Vect_read_ascii_head
    Vect_read_ascii_head.restype = c_int
    Vect_read_ascii_head.argtypes = [POINTER(FILE), POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 437
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_write_ascii'):
    Vect_write_ascii = _libs['grass_vector.7.0.svn'].Vect_write_ascii
    Vect_write_ascii.restype = c_int
    Vect_write_ascii.argtypes = [POINTER(FILE), POINTER(FILE), POINTER(struct_Map_info), c_int, c_int, c_int, String, c_int, c_int, POINTER(struct_cat_list), String, POINTER(POINTER(c_char)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 441
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_write_ascii_head'):
    Vect_write_ascii_head = _libs['grass_vector.7.0.svn'].Vect_write_ascii_head
    Vect_write_ascii_head.restype = None
    Vect_write_ascii_head.argtypes = [POINTER(FILE), POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 444
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_sfa_get_line_type'):
    Vect_sfa_get_line_type = _libs['grass_vector.7.0.svn'].Vect_sfa_get_line_type
    Vect_sfa_get_line_type.restype = c_int
    Vect_sfa_get_line_type.argtypes = [POINTER(struct_line_pnts), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 445
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_sfa_check_line_type'):
    Vect_sfa_check_line_type = _libs['grass_vector.7.0.svn'].Vect_sfa_check_line_type
    Vect_sfa_check_line_type.restype = c_int
    Vect_sfa_check_line_type.argtypes = [POINTER(struct_line_pnts), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 446
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_sfa_line_dimension'):
    Vect_sfa_line_dimension = _libs['grass_vector.7.0.svn'].Vect_sfa_line_dimension
    Vect_sfa_line_dimension.restype = c_int
    Vect_sfa_line_dimension.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 447
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_sfa_line_geometry_type'):
    Vect_sfa_line_geometry_type = _libs['grass_vector.7.0.svn'].Vect_sfa_line_geometry_type
    Vect_sfa_line_geometry_type.restype = ReturnString
    Vect_sfa_line_geometry_type.argtypes = [POINTER(struct_line_pnts), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 448
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_sfa_line_astext'):
    Vect_sfa_line_astext = _libs['grass_vector.7.0.svn'].Vect_sfa_line_astext
    Vect_sfa_line_astext.restype = c_int
    Vect_sfa_line_astext.argtypes = [POINTER(struct_line_pnts), c_int, c_int, c_int, POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 449
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_sfa_is_line_simple'):
    Vect_sfa_is_line_simple = _libs['grass_vector.7.0.svn'].Vect_sfa_is_line_simple
    Vect_sfa_is_line_simple.restype = c_int
    Vect_sfa_is_line_simple.argtypes = [POINTER(struct_line_pnts), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 450
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_sfa_is_line_closed'):
    Vect_sfa_is_line_closed = _libs['grass_vector.7.0.svn'].Vect_sfa_is_line_closed
    Vect_sfa_is_line_closed.restype = c_int
    Vect_sfa_is_line_closed.argtypes = [POINTER(struct_line_pnts), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 455
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_print_header'):
    Vect_print_header = _libs['grass_vector.7.0.svn'].Vect_print_header
    Vect_print_header.restype = c_int
    Vect_print_header.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 456
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect__init_head'):
    Vect__init_head = _libs['grass_vector.7.0.svn'].Vect__init_head
    Vect__init_head.restype = None
    Vect__init_head.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 459
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_coor_info'):
    Vect_coor_info = _libs['grass_vector.7.0.svn'].Vect_coor_info
    Vect_coor_info.restype = c_int
    Vect_coor_info.argtypes = [POINTER(struct_Map_info), POINTER(struct_Coor_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 460
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_maptype_info'):
    Vect_maptype_info = _libs['grass_vector.7.0.svn'].Vect_maptype_info
    Vect_maptype_info.restype = ReturnString
    Vect_maptype_info.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 461
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_maptype'):
    Vect_maptype = _libs['grass_vector.7.0.svn'].Vect_maptype
    Vect_maptype.restype = c_int
    Vect_maptype.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 462
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_open_topo'):
    Vect_open_topo = _libs['grass_vector.7.0.svn'].Vect_open_topo
    Vect_open_topo.restype = c_int
    Vect_open_topo.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 463
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_save_topo'):
    Vect_save_topo = _libs['grass_vector.7.0.svn'].Vect_save_topo
    Vect_save_topo.restype = c_int
    Vect_save_topo.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 464
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_open_sidx'):
    Vect_open_sidx = _libs['grass_vector.7.0.svn'].Vect_open_sidx
    Vect_open_sidx.restype = c_int
    Vect_open_sidx.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 465
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_save_sidx'):
    Vect_save_sidx = _libs['grass_vector.7.0.svn'].Vect_save_sidx
    Vect_save_sidx.restype = c_int
    Vect_save_sidx.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 466
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_sidx_dump'):
    Vect_sidx_dump = _libs['grass_vector.7.0.svn'].Vect_sidx_dump
    Vect_sidx_dump.restype = c_int
    Vect_sidx_dump.argtypes = [POINTER(struct_Map_info), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 467
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_build_sidx_from_topo'):
    Vect_build_sidx_from_topo = _libs['grass_vector.7.0.svn'].Vect_build_sidx_from_topo
    Vect_build_sidx_from_topo.restype = c_int
    Vect_build_sidx_from_topo.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 468
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_build_sidx'):
    Vect_build_sidx = _libs['grass_vector.7.0.svn'].Vect_build_sidx
    Vect_build_sidx.restype = c_int
    Vect_build_sidx.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 470
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect__write_head'):
    Vect__write_head = _libs['grass_vector.7.0.svn'].Vect__write_head
    Vect__write_head.restype = c_int
    Vect__write_head.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 471
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect__read_head'):
    Vect__read_head = _libs['grass_vector.7.0.svn'].Vect__read_head
    Vect__read_head.restype = c_int
    Vect__read_head.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 472
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_open_old_nat'):
    V1_open_old_nat = _libs['grass_vector.7.0.svn'].V1_open_old_nat
    V1_open_old_nat.restype = c_int
    V1_open_old_nat.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 473
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_open_old_ogr'):
    V1_open_old_ogr = _libs['grass_vector.7.0.svn'].V1_open_old_ogr
    V1_open_old_ogr.restype = c_int
    V1_open_old_ogr.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 474
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_open_old_ogr'):
    V2_open_old_ogr = _libs['grass_vector.7.0.svn'].V2_open_old_ogr
    V2_open_old_ogr.restype = c_int
    V2_open_old_ogr.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 475
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_open_new_nat'):
    V1_open_new_nat = _libs['grass_vector.7.0.svn'].V1_open_new_nat
    V1_open_new_nat.restype = c_int
    V1_open_new_nat.argtypes = [POINTER(struct_Map_info), String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 476
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_open_new_ogr'):
    V1_open_new_ogr = _libs['grass_vector.7.0.svn'].V1_open_new_ogr
    V1_open_new_ogr.restype = c_int
    V1_open_new_ogr.argtypes = [POINTER(struct_Map_info), String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 477
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_open_new_ogr'):
    V2_open_new_ogr = _libs['grass_vector.7.0.svn'].V2_open_new_ogr
    V2_open_new_ogr.restype = c_int
    V2_open_new_ogr.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 478
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_rewind_nat'):
    V1_rewind_nat = _libs['grass_vector.7.0.svn'].V1_rewind_nat
    V1_rewind_nat.restype = c_int
    V1_rewind_nat.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 479
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_rewind_ogr'):
    V1_rewind_ogr = _libs['grass_vector.7.0.svn'].V1_rewind_ogr
    V1_rewind_ogr.restype = c_int
    V1_rewind_ogr.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 480
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_rewind_nat'):
    V2_rewind_nat = _libs['grass_vector.7.0.svn'].V2_rewind_nat
    V2_rewind_nat.restype = c_int
    V2_rewind_nat.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 481
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_rewind_ogr'):
    V2_rewind_ogr = _libs['grass_vector.7.0.svn'].V2_rewind_ogr
    V2_rewind_ogr.restype = c_int
    V2_rewind_ogr.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 482
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_close_nat'):
    V1_close_nat = _libs['grass_vector.7.0.svn'].V1_close_nat
    V1_close_nat.restype = c_int
    V1_close_nat.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 483
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_close_ogr'):
    V1_close_ogr = _libs['grass_vector.7.0.svn'].V1_close_ogr
    V1_close_ogr.restype = c_int
    V1_close_ogr.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 484
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_close_ogr'):
    V2_close_ogr = _libs['grass_vector.7.0.svn'].V2_close_ogr
    V2_close_ogr.restype = c_int
    V2_close_ogr.argtypes = [POINTER(struct_Map_info)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 487
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_read_line_nat'):
    V1_read_line_nat = _libs['grass_vector.7.0.svn'].V1_read_line_nat
    V1_read_line_nat.restype = c_int
    V1_read_line_nat.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), off_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 489
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_read_line_ogr'):
    V1_read_line_ogr = _libs['grass_vector.7.0.svn'].V1_read_line_ogr
    V1_read_line_ogr.restype = c_int
    V1_read_line_ogr.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), off_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 491
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_read_next_line_nat'):
    V1_read_next_line_nat = _libs['grass_vector.7.0.svn'].V1_read_next_line_nat
    V1_read_next_line_nat.restype = c_int
    V1_read_next_line_nat.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 493
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_read_next_line_ogr'):
    V1_read_next_line_ogr = _libs['grass_vector.7.0.svn'].V1_read_next_line_ogr
    V1_read_next_line_ogr.restype = c_int
    V1_read_next_line_ogr.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 495
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_read_line_nat'):
    V2_read_line_nat = _libs['grass_vector.7.0.svn'].V2_read_line_nat
    V2_read_line_nat.restype = c_int
    V2_read_line_nat.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 497
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_read_line_ogr'):
    V2_read_line_ogr = _libs['grass_vector.7.0.svn'].V2_read_line_ogr
    V2_read_line_ogr.restype = c_int
    V2_read_line_ogr.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 499
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_read_next_line_nat'):
    V2_read_next_line_nat = _libs['grass_vector.7.0.svn'].V2_read_next_line_nat
    V2_read_next_line_nat.restype = c_int
    V2_read_next_line_nat.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 501
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_read_next_line_ogr'):
    V2_read_next_line_ogr = _libs['grass_vector.7.0.svn'].V2_read_next_line_ogr
    V2_read_next_line_ogr.restype = c_int
    V2_read_next_line_ogr.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 503
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_delete_line_nat'):
    V1_delete_line_nat = _libs['grass_vector.7.0.svn'].V1_delete_line_nat
    V1_delete_line_nat.restype = c_int
    V1_delete_line_nat.argtypes = [POINTER(struct_Map_info), off_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 504
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_delete_line_nat'):
    V2_delete_line_nat = _libs['grass_vector.7.0.svn'].V2_delete_line_nat
    V2_delete_line_nat.restype = c_int
    V2_delete_line_nat.argtypes = [POINTER(struct_Map_info), off_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 505
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_delete_line_ogr'):
    V1_delete_line_ogr = _libs['grass_vector.7.0.svn'].V1_delete_line_ogr
    V1_delete_line_ogr.restype = c_int
    V1_delete_line_ogr.argtypes = [POINTER(struct_Map_info), off_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 506
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_delete_line_ogr'):
    V2_delete_line_ogr = _libs['grass_vector.7.0.svn'].V2_delete_line_ogr
    V2_delete_line_ogr.restype = c_int
    V2_delete_line_ogr.argtypes = [POINTER(struct_Map_info), off_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 507
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_restore_line_nat'):
    V1_restore_line_nat = _libs['grass_vector.7.0.svn'].V1_restore_line_nat
    V1_restore_line_nat.restype = c_int
    V1_restore_line_nat.argtypes = [POINTER(struct_Map_info), off_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 508
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_restore_line_nat'):
    V2_restore_line_nat = _libs['grass_vector.7.0.svn'].V2_restore_line_nat
    V2_restore_line_nat.restype = c_int
    V2_restore_line_nat.argtypes = [POINTER(struct_Map_info), c_int, off_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 509
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_write_line_nat'):
    V1_write_line_nat = _libs['grass_vector.7.0.svn'].V1_write_line_nat
    V1_write_line_nat.restype = off_t
    V1_write_line_nat.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 511
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_write_line_nat'):
    V2_write_line_nat = _libs['grass_vector.7.0.svn'].V2_write_line_nat
    V2_write_line_nat.restype = off_t
    V2_write_line_nat.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 513
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_write_line_ogr'):
    V1_write_line_ogr = _libs['grass_vector.7.0.svn'].V1_write_line_ogr
    V1_write_line_ogr.restype = off_t
    V1_write_line_ogr.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 515
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_write_line_ogr'):
    V2_write_line_ogr = _libs['grass_vector.7.0.svn'].V2_write_line_ogr
    V2_write_line_ogr.restype = off_t
    V2_write_line_ogr.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 517
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_rewrite_line_nat'):
    V1_rewrite_line_nat = _libs['grass_vector.7.0.svn'].V1_rewrite_line_nat
    V1_rewrite_line_nat.restype = off_t
    V1_rewrite_line_nat.argtypes = [POINTER(struct_Map_info), c_int, c_int, off_t, POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 519
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_rewrite_line_nat'):
    V2_rewrite_line_nat = _libs['grass_vector.7.0.svn'].V2_rewrite_line_nat
    V2_rewrite_line_nat.restype = off_t
    V2_rewrite_line_nat.argtypes = [POINTER(struct_Map_info), c_int, c_int, off_t, POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 521
if hasattr(_libs['grass_vector.7.0.svn'], 'V1_rewrite_line_ogr'):
    V1_rewrite_line_ogr = _libs['grass_vector.7.0.svn'].V1_rewrite_line_ogr
    V1_rewrite_line_ogr.restype = off_t
    V1_rewrite_line_ogr.argtypes = [POINTER(struct_Map_info), c_int, c_int, off_t, POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 523
if hasattr(_libs['grass_vector.7.0.svn'], 'V2_rewrite_line_ogr'):
    V2_rewrite_line_ogr = _libs['grass_vector.7.0.svn'].V2_rewrite_line_ogr
    V2_rewrite_line_ogr.restype = off_t
    V2_rewrite_line_ogr.argtypes = [POINTER(struct_Map_info), c_int, c_int, off_t, POINTER(struct_line_pnts), POINTER(struct_line_cats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 527
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_build_nat'):
    Vect_build_nat = _libs['grass_vector.7.0.svn'].Vect_build_nat
    Vect_build_nat.restype = c_int
    Vect_build_nat.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 528
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_build_ogr'):
    Vect_build_ogr = _libs['grass_vector.7.0.svn'].Vect_build_ogr
    Vect_build_ogr.restype = c_int
    Vect_build_ogr.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 529
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_build_line_area'):
    Vect_build_line_area = _libs['grass_vector.7.0.svn'].Vect_build_line_area
    Vect_build_line_area.restype = c_int
    Vect_build_line_area.argtypes = [POINTER(struct_Map_info), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 530
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_isle_find_area'):
    Vect_isle_find_area = _libs['grass_vector.7.0.svn'].Vect_isle_find_area
    Vect_isle_find_area.restype = c_int
    Vect_isle_find_area.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 531
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_attach_isle'):
    Vect_attach_isle = _libs['grass_vector.7.0.svn'].Vect_attach_isle
    Vect_attach_isle.restype = c_int
    Vect_attach_isle.argtypes = [POINTER(struct_Map_info), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 532
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_attach_isles'):
    Vect_attach_isles = _libs['grass_vector.7.0.svn'].Vect_attach_isles
    Vect_attach_isles.restype = c_int
    Vect_attach_isles.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 533
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_attach_centroids'):
    Vect_attach_centroids = _libs['grass_vector.7.0.svn'].Vect_attach_centroids
    Vect_attach_centroids.restype = c_int
    Vect_attach_centroids.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 545
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_read_colors'):
    Vect_read_colors = _libs['grass_vector.7.0.svn'].Vect_read_colors
    Vect_read_colors.restype = c_int
    Vect_read_colors.argtypes = [String, String, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 546
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_remove_colors'):
    Vect_remove_colors = _libs['grass_vector.7.0.svn'].Vect_remove_colors
    Vect_remove_colors.restype = c_int
    Vect_remove_colors.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vector.h: 547
if hasattr(_libs['grass_vector.7.0.svn'], 'Vect_write_colors'):
    Vect_write_colors = _libs['grass_vector.7.0.svn'].Vect_write_colors
    Vect_write_colors.restype = None
    Vect_write_colors.argtypes = [String, String, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 11
try:
    GV_FATAL_EXIT = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 11
try:
    GV_FATAL_PRINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 11
try:
    GV_FATAL_RETURN = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 13
try:
    GV_DIRECTORY = 'vector'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 14
try:
    GV_FRMT_ELEMENT = 'frmt'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 15
try:
    GV_COOR_ELEMENT = 'coor'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 16
try:
    GV_HEAD_ELEMENT = 'head'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 17
try:
    GV_DBLN_ELEMENT = 'dbln'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 18
try:
    GV_HIST_ELEMENT = 'hist'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 19
try:
    GV_TOPO_ELEMENT = 'topo'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 20
try:
    GV_SIDX_ELEMENT = 'sidx'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 21
try:
    GV_CIDX_ELEMENT = 'cidx'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 22
try:
    GV_FIDX_ELEMENT = 'fidx'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 23
try:
    GV_COLR_ELEMENT = 'colr'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 24
try:
    GV_COLR2_DIRECTORY = 'vcolr2'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 29
try:
    ENDIAN_LITTLE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 29
try:
    ENDIAN_BIG = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 29
try:
    ENDIAN_OTHER = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_DOUBLE = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_FLOAT = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_LONG = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_INT = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_SHORT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_CHAR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_OFF_T = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 64
try:
    DBL_SIZ = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 64
try:
    FLT_SIZ = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 64
try:
    LNG_SIZ = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 64
try:
    SHRT_SIZ = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_DOUBLE_MAX = 1.7976931348623157e+308
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_DOUBLE_MIN = 2.2250738585072014e-308
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_FLOAT_MAX = 3.4028234699999998e+38
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_FLOAT_MIN = 1.17549435e-38
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_LONG_MAX = 2147483647L
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_LONG_MIN = (-2147483647L)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_INT_MAX = 2147483647
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_INT_MIN = (-2147483647)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_SHORT_MAX = 32767
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_SHORT_MIN = (-32768)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_CHAR_MAX = 127
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_CHAR_MIN = (-128)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 74
try:
    GV_FORMAT_NATIVE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 75
try:
    GV_FORMAT_OGR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 76
try:
    GV_FORMAT_OGR_DIRECT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 78
try:
    GV_1TABLE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 79
try:
    GV_MTABLE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 81
try:
    GV_MODE_READ = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 82
try:
    GV_MODE_WRITE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 83
try:
    GV_MODE_RW = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 85
try:
    VECT_OPEN_CODE = 1428335138
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 86
try:
    VECT_CLOSED_CODE = 581575253
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 93
try:
    LEVEL_1 = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 93
try:
    LEVEL_2 = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 93
try:
    LEVEL_3 = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 96
try:
    GV_BUILD_NONE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 97
try:
    GV_BUILD_BASE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 98
try:
    GV_BUILD_AREAS = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 99
try:
    GV_BUILD_ATTACH_ISLES = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 100
try:
    GV_BUILD_CENTROIDS = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 100
try:
    GV_BUILD_ALL = GV_BUILD_CENTROIDS
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 102
def VECT_OPEN(Map):
    return (((Map.contents.open).value) == VECT_OPEN_CODE)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 104
try:
    GV_MEMORY_ALWAYS = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 104
try:
    GV_MEMORY_NEVER = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 104
try:
    GV_MEMORY_AUTO = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 106
try:
    GV_COOR_HEAD_SIZE = 14
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 107
try:
    GRASS_V_VERSION = '5.0'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_COOR_VER_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_COOR_VER_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_TOPO_VER_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_TOPO_VER_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_SIDX_VER_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_SIDX_VER_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_CIDX_VER_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_CIDX_VER_MINOR = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_COOR_EARLIEST_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_COOR_EARLIEST_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_TOPO_EARLIEST_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_TOPO_EARLIEST_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_SIDX_EARLIEST_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_SIDX_EARLIEST_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_CIDX_EARLIEST_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_CIDX_EARLIEST_MINOR = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 114
try:
    WITHOUT_Z = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 114
try:
    WITH_Z = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 116
try:
    GV_LEFT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 116
try:
    GV_RIGHT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 118
try:
    GV_FORWARD = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 118
try:
    GV_BACKWARD = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_POINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_LINE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_BOUNDARY = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_CENTROID = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_FACE = 16
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_KERNEL = 32
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_AREA = 64
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_VOLUME = 128
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 121
try:
    GV_POINTS = (GV_POINT | GV_CENTROID)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 121
try:
    GV_LINES = (GV_LINE | GV_BOUNDARY)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_POINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_LINE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_BOUNDARY = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_CENTROID = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_FACE = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_KERNEL = 6
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_AREA = 7
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_VOLUME = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 125
try:
    GV_ON_AND = 'AND'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 125
try:
    GV_ON_OVERLAP = 'OVERLAP'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 135
try:
    GV_NCATS_MAX = PORT_INT_MAX
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 136
try:
    GV_FIELD_MAX = PORT_INT_MAX
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 137
try:
    GV_CAT_MAX = PORT_INT_MAX
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 139
try:
    GV_ASCII_FORMAT_POINT = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 139
try:
    GV_ASCII_FORMAT_STD = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 139
try:
    GV_ASCII_FORMAT_WKT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 141
try:
    SF_POINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 141
try:
    SF_LINE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 141
try:
    SF_LINESTRING = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 141
try:
    SF_LINEARRING = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 141
try:
    SF_POLYGON = 16
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 142
try:
    HEADSTR = 50
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 11
try:
    GV_FATAL_EXIT = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 11
try:
    GV_FATAL_PRINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 11
try:
    GV_FATAL_RETURN = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 13
try:
    GV_DIRECTORY = 'vector'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 14
try:
    GV_FRMT_ELEMENT = 'frmt'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 15
try:
    GV_COOR_ELEMENT = 'coor'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 16
try:
    GV_HEAD_ELEMENT = 'head'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 17
try:
    GV_DBLN_ELEMENT = 'dbln'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 18
try:
    GV_HIST_ELEMENT = 'hist'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 19
try:
    GV_TOPO_ELEMENT = 'topo'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 20
try:
    GV_SIDX_ELEMENT = 'sidx'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 21
try:
    GV_CIDX_ELEMENT = 'cidx'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 22
try:
    GV_FIDX_ELEMENT = 'fidx'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 23
try:
    GV_COLR_ELEMENT = 'colr'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 24
try:
    GV_COLR2_DIRECTORY = 'vcolr2'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 29
try:
    ENDIAN_LITTLE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 29
try:
    ENDIAN_BIG = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 29
try:
    ENDIAN_OTHER = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_DOUBLE = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_FLOAT = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_LONG = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_INT = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_SHORT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_CHAR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 59
try:
    PORT_OFF_T = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 64
try:
    DBL_SIZ = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 64
try:
    FLT_SIZ = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 64
try:
    LNG_SIZ = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 64
try:
    SHRT_SIZ = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_DOUBLE_MAX = 1.7976931348623157e+308
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_DOUBLE_MIN = 2.2250738585072014e-308
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_FLOAT_MAX = 3.4028234699999998e+38
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_FLOAT_MIN = 1.17549435e-38
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_LONG_MAX = 2147483647L
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_LONG_MIN = (-2147483647L)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_INT_MAX = 2147483647
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_INT_MIN = (-2147483647)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_SHORT_MAX = 32767
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_SHORT_MIN = (-32768)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_CHAR_MAX = 127
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 69
try:
    PORT_CHAR_MIN = (-128)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 74
try:
    GV_FORMAT_NATIVE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 75
try:
    GV_FORMAT_OGR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 76
try:
    GV_FORMAT_OGR_DIRECT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 78
try:
    GV_1TABLE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 79
try:
    GV_MTABLE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 81
try:
    GV_MODE_READ = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 82
try:
    GV_MODE_WRITE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 83
try:
    GV_MODE_RW = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 85
try:
    VECT_OPEN_CODE = 1428335138
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 86
try:
    VECT_CLOSED_CODE = 581575253
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 93
try:
    LEVEL_1 = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 93
try:
    LEVEL_2 = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 93
try:
    LEVEL_3 = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 96
try:
    GV_BUILD_NONE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 97
try:
    GV_BUILD_BASE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 98
try:
    GV_BUILD_AREAS = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 99
try:
    GV_BUILD_ATTACH_ISLES = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 100
try:
    GV_BUILD_CENTROIDS = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 100
try:
    GV_BUILD_ALL = GV_BUILD_CENTROIDS
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 102
def VECT_OPEN(Map):
    return (((Map.contents.open).value) == VECT_OPEN_CODE)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 104
try:
    GV_MEMORY_ALWAYS = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 104
try:
    GV_MEMORY_NEVER = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 104
try:
    GV_MEMORY_AUTO = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 106
try:
    GV_COOR_HEAD_SIZE = 14
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 107
try:
    GRASS_V_VERSION = '5.0'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_COOR_VER_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_COOR_VER_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_TOPO_VER_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_TOPO_VER_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_SIDX_VER_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_SIDX_VER_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_CIDX_VER_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 109
try:
    GV_CIDX_VER_MINOR = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_COOR_EARLIEST_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_COOR_EARLIEST_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_TOPO_EARLIEST_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_TOPO_EARLIEST_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_SIDX_EARLIEST_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_SIDX_EARLIEST_MINOR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_CIDX_EARLIEST_MAJOR = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 112
try:
    GV_CIDX_EARLIEST_MINOR = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 114
try:
    WITHOUT_Z = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 114
try:
    WITH_Z = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 116
try:
    GV_LEFT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 116
try:
    GV_RIGHT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 118
try:
    GV_FORWARD = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 118
try:
    GV_BACKWARD = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_POINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_LINE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_BOUNDARY = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_CENTROID = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_FACE = 16
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_KERNEL = 32
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_AREA = 64
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 120
try:
    GV_VOLUME = 128
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 121
try:
    GV_POINTS = (GV_POINT | GV_CENTROID)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 121
try:
    GV_LINES = (GV_LINE | GV_BOUNDARY)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_POINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_LINE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_BOUNDARY = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_CENTROID = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_FACE = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_KERNEL = 6
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_AREA = 7
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 123
try:
    GV_STORE_VOLUME = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 125
try:
    GV_ON_AND = 'AND'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 125
try:
    GV_ON_OVERLAP = 'OVERLAP'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 135
try:
    GV_NCATS_MAX = PORT_INT_MAX
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 136
try:
    GV_FIELD_MAX = PORT_INT_MAX
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 137
try:
    GV_CAT_MAX = PORT_INT_MAX
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 139
try:
    GV_ASCII_FORMAT_POINT = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 139
try:
    GV_ASCII_FORMAT_STD = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 139
try:
    GV_ASCII_FORMAT_WKT = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 141
try:
    SF_POINT = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 141
try:
    SF_LINE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 141
try:
    SF_LINESTRING = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 141
try:
    SF_LINEARRING = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 141
try:
    SF_POLYGON = 16
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_defines.h: 142
try:
    HEADSTR = 50
except:
    pass

site_att = struct_site_att # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 46

bound_box = struct_bound_box # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 65

gvfile = struct_gvfile # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 96

field_info = struct_field_info # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 134

dblinks = struct_dblinks # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 165

Port_info = struct_Port_info # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 186

recycle = struct_recycle # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 272

dig_head = struct_dig_head # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 282

Coor_info = struct_Coor_info # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 381

line_pnts = struct_line_pnts # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1469

Format_info_ogr = struct_Format_info_ogr # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 399

Format_info = struct_Format_info # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 522

Cat_index = struct_Cat_index # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 537

P_node = struct_P_node # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1249

P_line = struct_P_line # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1371

P_area = struct_P_area # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1399

P_isle = struct_P_isle # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1440

Plus_head = struct_Plus_head # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 586

Map_info = struct_Map_info # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1052

P_topo_l = struct_P_topo_l # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1291

P_topo_b = struct_P_topo_b # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1306

P_topo_c = struct_P_topo_c # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1329

P_topo_f = struct_P_topo_f # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1340

P_topo_k = struct_P_topo_k # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1360

line_cats = struct_line_cats # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1496

cat_list = struct_cat_list # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1517

ilist = struct_ilist # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1546

boxlist = struct_boxlist # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1565

varray = struct_varray # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1594

spatial_index = struct_spatial_index # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/vect/dig_structs.h: 1614

# No inserted files

