'''Wrapper for raster.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_raster.7.0.svn /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h -o raster.py

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

_libs["grass_raster.7.0.svn"] = load_library("grass_raster.7.0.svn")

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

INTERP_TYPE = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 25

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 28
class struct_Reclass(Structure):
    pass

struct_Reclass.__slots__ = [
    'name',
    'mapset',
    'type',
    'num',
    'min',
    'max',
    'table',
]
struct_Reclass._fields_ = [
    ('name', String),
    ('mapset', String),
    ('type', c_int),
    ('num', c_int),
    ('min', CELL),
    ('max', CELL),
    ('table', POINTER(CELL)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 39
class struct_FPReclass_table(Structure):
    pass

struct_FPReclass_table.__slots__ = [
    'dLow',
    'dHigh',
    'rLow',
    'rHigh',
]
struct_FPReclass_table._fields_ = [
    ('dLow', DCELL),
    ('dHigh', DCELL),
    ('rLow', DCELL),
    ('rHigh', DCELL),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 49
class struct_FPReclass(Structure):
    pass

struct_FPReclass.__slots__ = [
    'defaultDRuleSet',
    'defaultRRuleSet',
    'infiniteLeftSet',
    'infiniteRightSet',
    'rRangeSet',
    'maxNofRules',
    'nofRules',
    'defaultDMin',
    'defaultDMax',
    'defaultRMin',
    'defaultRMax',
    'infiniteDLeft',
    'infiniteDRight',
    'infiniteRLeft',
    'infiniteRRight',
    'dMin',
    'dMax',
    'rMin',
    'rMax',
    'table',
]
struct_FPReclass._fields_ = [
    ('defaultDRuleSet', c_int),
    ('defaultRRuleSet', c_int),
    ('infiniteLeftSet', c_int),
    ('infiniteRightSet', c_int),
    ('rRangeSet', c_int),
    ('maxNofRules', c_int),
    ('nofRules', c_int),
    ('defaultDMin', DCELL),
    ('defaultDMax', DCELL),
    ('defaultRMin', DCELL),
    ('defaultRMax', DCELL),
    ('infiniteDLeft', DCELL),
    ('infiniteDRight', DCELL),
    ('infiniteRLeft', DCELL),
    ('infiniteRRight', DCELL),
    ('dMin', DCELL),
    ('dMax', DCELL),
    ('rMin', DCELL),
    ('rMax', DCELL),
    ('table', POINTER(struct_FPReclass_table)),
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

enum_History_field = c_int # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 150

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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 173
class struct_Cell_stats_node(Structure):
    pass

struct_Cell_stats_node.__slots__ = [
    'idx',
    'count',
    'left',
    'right',
]
struct_Cell_stats_node._fields_ = [
    ('idx', c_int),
    ('count', POINTER(c_long)),
    ('left', c_int),
    ('right', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 171
class struct_Cell_stats(Structure):
    pass

struct_Cell_stats.__slots__ = [
    'node',
    'tlen',
    'N',
    'curp',
    'null_data_count',
    'curoffset',
]
struct_Cell_stats._fields_ = [
    ('node', POINTER(struct_Cell_stats_node)),
    ('tlen', c_int),
    ('N', c_int),
    ('curp', c_int),
    ('null_data_count', c_long),
    ('curoffset', c_int),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 192
class struct_Histogram_list(Structure):
    pass

struct_Histogram_list.__slots__ = [
    'cat',
    'count',
]
struct_Histogram_list._fields_ = [
    ('cat', CELL),
    ('count', c_long),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 188
class struct_Histogram(Structure):
    pass

struct_Histogram.__slots__ = [
    'num',
    'list',
]
struct_Histogram._fields_ = [
    ('num', c_int),
    ('list', POINTER(struct_Histogram_list)),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 199
class struct_Range(Structure):
    pass

struct_Range.__slots__ = [
    'min',
    'max',
    'first_time',
]
struct_Range._fields_ = [
    ('min', CELL),
    ('max', CELL),
    ('first_time', c_int),
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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 213
class struct_FP_stats(Structure):
    pass

struct_FP_stats.__slots__ = [
    'geometric',
    'geom_abs',
    'flip',
    'count',
    'min',
    'max',
    'stats',
    'total',
]
struct_FP_stats._fields_ = [
    ('geometric', c_int),
    ('geom_abs', c_int),
    ('flip', c_int),
    ('count', c_int),
    ('min', DCELL),
    ('max', DCELL),
    ('stats', POINTER(c_ulong)),
    ('total', c_ulong),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 223
class struct_GDAL_link(Structure):
    pass

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

RGB_Color = RGBA_Color # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 230

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 9
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_align_window'):
    Rast_align_window = _libs['grass_raster.7.0.svn'].Rast_align_window
    Rast_align_window.restype = None
    Rast_align_window.argtypes = [POINTER(struct_Cell_head), POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 12
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_cell_size'):
    Rast_cell_size = _libs['grass_raster.7.0.svn'].Rast_cell_size
    Rast_cell_size.restype = c_size_t
    Rast_cell_size.argtypes = [RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 13
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_buf'):
    Rast_allocate_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_buf
    Rast_allocate_buf.restype = POINTER(None)
    Rast_allocate_buf.argtypes = [RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 14
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_c_buf'):
    Rast_allocate_c_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_c_buf
    Rast_allocate_c_buf.restype = POINTER(CELL)
    Rast_allocate_c_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 15
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_f_buf'):
    Rast_allocate_f_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_f_buf
    Rast_allocate_f_buf.restype = POINTER(FCELL)
    Rast_allocate_f_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 16
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_d_buf'):
    Rast_allocate_d_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_d_buf
    Rast_allocate_d_buf.restype = POINTER(DCELL)
    Rast_allocate_d_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 17
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_null_buf'):
    Rast_allocate_null_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_null_buf
    Rast_allocate_null_buf.restype = ReturnString
    Rast_allocate_null_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 18
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__allocate_null_bits'):
    Rast__allocate_null_bits = _libs['grass_raster.7.0.svn'].Rast__allocate_null_bits
    Rast__allocate_null_bits.restype = POINTER(c_ubyte)
    Rast__allocate_null_bits.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 19
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__null_bitstream_size'):
    Rast__null_bitstream_size = _libs['grass_raster.7.0.svn'].Rast__null_bitstream_size
    Rast__null_bitstream_size.restype = c_int
    Rast__null_bitstream_size.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 21
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_input_buf'):
    Rast_allocate_input_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_input_buf
    Rast_allocate_input_buf.restype = POINTER(None)
    Rast_allocate_input_buf.argtypes = [RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 22
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_c_input_buf'):
    Rast_allocate_c_input_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_c_input_buf
    Rast_allocate_c_input_buf.restype = POINTER(CELL)
    Rast_allocate_c_input_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 23
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_f_input_buf'):
    Rast_allocate_f_input_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_f_input_buf
    Rast_allocate_f_input_buf.restype = POINTER(FCELL)
    Rast_allocate_f_input_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 24
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_d_input_buf'):
    Rast_allocate_d_input_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_d_input_buf
    Rast_allocate_d_input_buf.restype = POINTER(DCELL)
    Rast_allocate_d_input_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 25
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_null_input_buf'):
    Rast_allocate_null_input_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_null_input_buf
    Rast_allocate_null_input_buf.restype = ReturnString
    Rast_allocate_null_input_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 27
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_output_buf'):
    Rast_allocate_output_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_output_buf
    Rast_allocate_output_buf.restype = POINTER(None)
    Rast_allocate_output_buf.argtypes = [RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 28
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_c_output_buf'):
    Rast_allocate_c_output_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_c_output_buf
    Rast_allocate_c_output_buf.restype = POINTER(CELL)
    Rast_allocate_c_output_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 29
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_f_output_buf'):
    Rast_allocate_f_output_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_f_output_buf
    Rast_allocate_f_output_buf.restype = POINTER(FCELL)
    Rast_allocate_f_output_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 30
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_d_output_buf'):
    Rast_allocate_d_output_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_d_output_buf
    Rast_allocate_d_output_buf.restype = POINTER(DCELL)
    Rast_allocate_d_output_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 31
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_allocate_null_output_buf'):
    Rast_allocate_null_output_buf = _libs['grass_raster.7.0.svn'].Rast_allocate_null_output_buf
    Rast_allocate_null_output_buf.restype = ReturnString
    Rast_allocate_null_output_buf.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 34
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__check_for_auto_masking'):
    Rast__check_for_auto_masking = _libs['grass_raster.7.0.svn'].Rast__check_for_auto_masking
    Rast__check_for_auto_masking.restype = c_int
    Rast__check_for_auto_masking.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 35
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_suppress_masking'):
    Rast_suppress_masking = _libs['grass_raster.7.0.svn'].Rast_suppress_masking
    Rast_suppress_masking.restype = None
    Rast_suppress_masking.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 36
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_unsuppress_masking'):
    Rast_unsuppress_masking = _libs['grass_raster.7.0.svn'].Rast_unsuppress_masking
    Rast_unsuppress_masking.restype = None
    Rast_unsuppress_masking.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 39
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_cats'):
    Rast_read_cats = _libs['grass_raster.7.0.svn'].Rast_read_cats
    Rast_read_cats.restype = c_int
    Rast_read_cats.argtypes = [String, String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 40
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_vector_cats'):
    Rast_read_vector_cats = _libs['grass_raster.7.0.svn'].Rast_read_vector_cats
    Rast_read_vector_cats.restype = c_int
    Rast_read_vector_cats.argtypes = [String, String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 41
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_max_c_cat'):
    Rast_get_max_c_cat = _libs['grass_raster.7.0.svn'].Rast_get_max_c_cat
    Rast_get_max_c_cat.restype = CELL
    Rast_get_max_c_cat.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 42
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_cats_title'):
    Rast_get_cats_title = _libs['grass_raster.7.0.svn'].Rast_get_cats_title
    Rast_get_cats_title.restype = ReturnString
    Rast_get_cats_title.argtypes = [POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 43
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_c_cat'):
    Rast_get_c_cat = _libs['grass_raster.7.0.svn'].Rast_get_c_cat
    Rast_get_c_cat.restype = ReturnString
    Rast_get_c_cat.argtypes = [POINTER(CELL), POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 44
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_f_cat'):
    Rast_get_f_cat = _libs['grass_raster.7.0.svn'].Rast_get_f_cat
    Rast_get_f_cat.restype = ReturnString
    Rast_get_f_cat.argtypes = [POINTER(FCELL), POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 45
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_d_cat'):
    Rast_get_d_cat = _libs['grass_raster.7.0.svn'].Rast_get_d_cat
    Rast_get_d_cat.restype = ReturnString
    Rast_get_d_cat.argtypes = [POINTER(DCELL), POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 46
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_cat'):
    Rast_get_cat = _libs['grass_raster.7.0.svn'].Rast_get_cat
    Rast_get_cat.restype = ReturnString
    Rast_get_cat.argtypes = [POINTER(None), POINTER(struct_Categories), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 47
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_unmark_cats'):
    Rast_unmark_cats = _libs['grass_raster.7.0.svn'].Rast_unmark_cats
    Rast_unmark_cats.restype = None
    Rast_unmark_cats.argtypes = [POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 48
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_mark_c_cats'):
    Rast_mark_c_cats = _libs['grass_raster.7.0.svn'].Rast_mark_c_cats
    Rast_mark_c_cats.restype = None
    Rast_mark_c_cats.argtypes = [POINTER(CELL), c_int, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 49
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_mark_f_cats'):
    Rast_mark_f_cats = _libs['grass_raster.7.0.svn'].Rast_mark_f_cats
    Rast_mark_f_cats.restype = None
    Rast_mark_f_cats.argtypes = [POINTER(FCELL), c_int, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 50
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_mark_d_cats'):
    Rast_mark_d_cats = _libs['grass_raster.7.0.svn'].Rast_mark_d_cats
    Rast_mark_d_cats.restype = None
    Rast_mark_d_cats.argtypes = [POINTER(DCELL), c_int, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 51
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_mark_cats'):
    Rast_mark_cats = _libs['grass_raster.7.0.svn'].Rast_mark_cats
    Rast_mark_cats.restype = c_int
    Rast_mark_cats.argtypes = [POINTER(None), c_int, POINTER(struct_Categories), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 52
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_rewind_cats'):
    Rast_rewind_cats = _libs['grass_raster.7.0.svn'].Rast_rewind_cats
    Rast_rewind_cats.restype = None
    Rast_rewind_cats.argtypes = [POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 53
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_next_marked_d_cat'):
    Rast_get_next_marked_d_cat = _libs['grass_raster.7.0.svn'].Rast_get_next_marked_d_cat
    Rast_get_next_marked_d_cat.restype = ReturnString
    Rast_get_next_marked_d_cat.argtypes = [POINTER(struct_Categories), POINTER(DCELL), POINTER(DCELL), POINTER(c_long)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 55
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_next_marked_c_cat'):
    Rast_get_next_marked_c_cat = _libs['grass_raster.7.0.svn'].Rast_get_next_marked_c_cat
    Rast_get_next_marked_c_cat.restype = ReturnString
    Rast_get_next_marked_c_cat.argtypes = [POINTER(struct_Categories), POINTER(CELL), POINTER(CELL), POINTER(c_long)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 57
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_next_marked_f_cat'):
    Rast_get_next_marked_f_cat = _libs['grass_raster.7.0.svn'].Rast_get_next_marked_f_cat
    Rast_get_next_marked_f_cat.restype = ReturnString
    Rast_get_next_marked_f_cat.argtypes = [POINTER(struct_Categories), POINTER(FCELL), POINTER(FCELL), POINTER(c_long)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 59
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_next_marked_cat'):
    Rast_get_next_marked_cat = _libs['grass_raster.7.0.svn'].Rast_get_next_marked_cat
    Rast_get_next_marked_cat.restype = ReturnString
    Rast_get_next_marked_cat.argtypes = [POINTER(struct_Categories), POINTER(None), POINTER(None), POINTER(c_long), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 61
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_c_cat'):
    Rast_set_c_cat = _libs['grass_raster.7.0.svn'].Rast_set_c_cat
    Rast_set_c_cat.restype = c_int
    Rast_set_c_cat.argtypes = [POINTER(CELL), POINTER(CELL), String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 62
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_f_cat'):
    Rast_set_f_cat = _libs['grass_raster.7.0.svn'].Rast_set_f_cat
    Rast_set_f_cat.restype = c_int
    Rast_set_f_cat.argtypes = [POINTER(FCELL), POINTER(FCELL), String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 63
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_d_cat'):
    Rast_set_d_cat = _libs['grass_raster.7.0.svn'].Rast_set_d_cat
    Rast_set_d_cat.restype = c_int
    Rast_set_d_cat.argtypes = [POINTER(DCELL), POINTER(DCELL), String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 64
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_cat'):
    Rast_set_cat = _libs['grass_raster.7.0.svn'].Rast_set_cat
    Rast_set_cat.restype = c_int
    Rast_set_cat.argtypes = [POINTER(None), POINTER(None), String, POINTER(struct_Categories), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 66
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_cats'):
    Rast_write_cats = _libs['grass_raster.7.0.svn'].Rast_write_cats
    Rast_write_cats.restype = None
    Rast_write_cats.argtypes = [String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 67
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_vector_cats'):
    Rast_write_vector_cats = _libs['grass_raster.7.0.svn'].Rast_write_vector_cats
    Rast_write_vector_cats.restype = None
    Rast_write_vector_cats.argtypes = [String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 68
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_ith_d_cat'):
    Rast_get_ith_d_cat = _libs['grass_raster.7.0.svn'].Rast_get_ith_d_cat
    Rast_get_ith_d_cat.restype = ReturnString
    Rast_get_ith_d_cat.argtypes = [POINTER(struct_Categories), c_int, POINTER(DCELL), POINTER(DCELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 70
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_ith_f_cat'):
    Rast_get_ith_f_cat = _libs['grass_raster.7.0.svn'].Rast_get_ith_f_cat
    Rast_get_ith_f_cat.restype = ReturnString
    Rast_get_ith_f_cat.argtypes = [POINTER(struct_Categories), c_int, POINTER(None), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 71
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_ith_c_cat'):
    Rast_get_ith_c_cat = _libs['grass_raster.7.0.svn'].Rast_get_ith_c_cat
    Rast_get_ith_c_cat.restype = ReturnString
    Rast_get_ith_c_cat.argtypes = [POINTER(struct_Categories), c_int, POINTER(None), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 72
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_ith_cat'):
    Rast_get_ith_cat = _libs['grass_raster.7.0.svn'].Rast_get_ith_cat
    Rast_get_ith_cat.restype = ReturnString
    Rast_get_ith_cat.argtypes = [POINTER(struct_Categories), c_int, POINTER(None), POINTER(None), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 74
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_init_cats'):
    Rast_init_cats = _libs['grass_raster.7.0.svn'].Rast_init_cats
    Rast_init_cats.restype = None
    Rast_init_cats.argtypes = [String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 75
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_cats_title'):
    Rast_set_cats_title = _libs['grass_raster.7.0.svn'].Rast_set_cats_title
    Rast_set_cats_title.restype = None
    Rast_set_cats_title.argtypes = [String, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 76
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_cats_fmt'):
    Rast_set_cats_fmt = _libs['grass_raster.7.0.svn'].Rast_set_cats_fmt
    Rast_set_cats_fmt.restype = None
    Rast_set_cats_fmt.argtypes = [String, c_double, c_double, c_double, c_double, POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 78
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_free_cats'):
    Rast_free_cats = _libs['grass_raster.7.0.svn'].Rast_free_cats
    Rast_free_cats.restype = None
    Rast_free_cats.argtypes = [POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 79
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_copy_cats'):
    Rast_copy_cats = _libs['grass_raster.7.0.svn'].Rast_copy_cats
    Rast_copy_cats.restype = None
    Rast_copy_cats.argtypes = [POINTER(struct_Categories), POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 80
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_number_of_cats'):
    Rast_number_of_cats = _libs['grass_raster.7.0.svn'].Rast_number_of_cats
    Rast_number_of_cats.restype = c_int
    Rast_number_of_cats.argtypes = [POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 81
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_sort_cats'):
    Rast_sort_cats = _libs['grass_raster.7.0.svn'].Rast_sort_cats
    Rast_sort_cats.restype = c_int
    Rast_sort_cats.argtypes = [POINTER(struct_Categories)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 84
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_init_cell_stats'):
    Rast_init_cell_stats = _libs['grass_raster.7.0.svn'].Rast_init_cell_stats
    Rast_init_cell_stats.restype = None
    Rast_init_cell_stats.argtypes = [POINTER(struct_Cell_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 85
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_update_cell_stats'):
    Rast_update_cell_stats = _libs['grass_raster.7.0.svn'].Rast_update_cell_stats
    Rast_update_cell_stats.restype = c_int
    Rast_update_cell_stats.argtypes = [POINTER(CELL), c_int, POINTER(struct_Cell_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 86
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_find_cell_stat'):
    Rast_find_cell_stat = _libs['grass_raster.7.0.svn'].Rast_find_cell_stat
    Rast_find_cell_stat.restype = c_int
    Rast_find_cell_stat.argtypes = [CELL, POINTER(c_long), POINTER(struct_Cell_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 87
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_rewind_cell_stats'):
    Rast_rewind_cell_stats = _libs['grass_raster.7.0.svn'].Rast_rewind_cell_stats
    Rast_rewind_cell_stats.restype = c_int
    Rast_rewind_cell_stats.argtypes = [POINTER(struct_Cell_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 88
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_next_cell_stat'):
    Rast_next_cell_stat = _libs['grass_raster.7.0.svn'].Rast_next_cell_stat
    Rast_next_cell_stat.restype = c_int
    Rast_next_cell_stat.argtypes = [POINTER(CELL), POINTER(c_long), POINTER(struct_Cell_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 89
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_stats_for_null_value'):
    Rast_get_stats_for_null_value = _libs['grass_raster.7.0.svn'].Rast_get_stats_for_null_value
    Rast_get_stats_for_null_value.restype = None
    Rast_get_stats_for_null_value.argtypes = [POINTER(c_long), POINTER(struct_Cell_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 90
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_free_cell_stats'):
    Rast_free_cell_stats = _libs['grass_raster.7.0.svn'].Rast_free_cell_stats
    Rast_free_cell_stats.restype = None
    Rast_free_cell_stats.argtypes = [POINTER(struct_Cell_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 93
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_cell_title'):
    Rast_get_cell_title = _libs['grass_raster.7.0.svn'].Rast_get_cell_title
    Rast_get_cell_title.restype = ReturnString
    Rast_get_cell_title.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 96
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_cell_stats_histo_eq'):
    Rast_cell_stats_histo_eq = _libs['grass_raster.7.0.svn'].Rast_cell_stats_histo_eq
    Rast_cell_stats_histo_eq.restype = c_int
    Rast_cell_stats_histo_eq.argtypes = [POINTER(struct_Cell_stats), CELL, CELL, CELL, CELL, c_int, CFUNCTYPE(UNCHECKED(None), CELL, CELL, CELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 100
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_close'):
    Rast_close = _libs['grass_raster.7.0.svn'].Rast_close
    Rast_close.restype = None
    Rast_close.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 101
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_unopen'):
    Rast_unopen = _libs['grass_raster.7.0.svn'].Rast_unopen
    Rast_unopen.restype = None
    Rast_unopen.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 102
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__unopen_all'):
    Rast__unopen_all = _libs['grass_raster.7.0.svn'].Rast__unopen_all
    Rast__unopen_all.restype = None
    Rast__unopen_all.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 105
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_ryg_colors'):
    Rast_make_ryg_colors = _libs['grass_raster.7.0.svn'].Rast_make_ryg_colors
    Rast_make_ryg_colors.restype = None
    Rast_make_ryg_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 106
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_ryg_fp_colors'):
    Rast_make_ryg_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_ryg_fp_colors
    Rast_make_ryg_fp_colors.restype = None
    Rast_make_ryg_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 107
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_aspect_colors'):
    Rast_make_aspect_colors = _libs['grass_raster.7.0.svn'].Rast_make_aspect_colors
    Rast_make_aspect_colors.restype = None
    Rast_make_aspect_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 108
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_aspect_fp_colors'):
    Rast_make_aspect_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_aspect_fp_colors
    Rast_make_aspect_fp_colors.restype = None
    Rast_make_aspect_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 109
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_byr_colors'):
    Rast_make_byr_colors = _libs['grass_raster.7.0.svn'].Rast_make_byr_colors
    Rast_make_byr_colors.restype = None
    Rast_make_byr_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 110
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_byr_fp_colors'):
    Rast_make_byr_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_byr_fp_colors
    Rast_make_byr_fp_colors.restype = None
    Rast_make_byr_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 111
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_bgyr_colors'):
    Rast_make_bgyr_colors = _libs['grass_raster.7.0.svn'].Rast_make_bgyr_colors
    Rast_make_bgyr_colors.restype = None
    Rast_make_bgyr_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 112
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_bgyr_fp_colors'):
    Rast_make_bgyr_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_bgyr_fp_colors
    Rast_make_bgyr_fp_colors.restype = None
    Rast_make_bgyr_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 113
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_byg_colors'):
    Rast_make_byg_colors = _libs['grass_raster.7.0.svn'].Rast_make_byg_colors
    Rast_make_byg_colors.restype = None
    Rast_make_byg_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 114
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_byg_fp_colors'):
    Rast_make_byg_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_byg_fp_colors
    Rast_make_byg_fp_colors.restype = None
    Rast_make_byg_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 115
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_grey_scale_colors'):
    Rast_make_grey_scale_colors = _libs['grass_raster.7.0.svn'].Rast_make_grey_scale_colors
    Rast_make_grey_scale_colors.restype = None
    Rast_make_grey_scale_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 116
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_grey_scale_fp_colors'):
    Rast_make_grey_scale_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_grey_scale_fp_colors
    Rast_make_grey_scale_fp_colors.restype = None
    Rast_make_grey_scale_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 117
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_gyr_colors'):
    Rast_make_gyr_colors = _libs['grass_raster.7.0.svn'].Rast_make_gyr_colors
    Rast_make_gyr_colors.restype = None
    Rast_make_gyr_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 118
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_gyr_fp_colors'):
    Rast_make_gyr_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_gyr_fp_colors
    Rast_make_gyr_fp_colors.restype = None
    Rast_make_gyr_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 119
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_rainbow_colors'):
    Rast_make_rainbow_colors = _libs['grass_raster.7.0.svn'].Rast_make_rainbow_colors
    Rast_make_rainbow_colors.restype = None
    Rast_make_rainbow_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 120
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_rainbow_fp_colors'):
    Rast_make_rainbow_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_rainbow_fp_colors
    Rast_make_rainbow_fp_colors.restype = None
    Rast_make_rainbow_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 121
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_ramp_colors'):
    Rast_make_ramp_colors = _libs['grass_raster.7.0.svn'].Rast_make_ramp_colors
    Rast_make_ramp_colors.restype = None
    Rast_make_ramp_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 122
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_ramp_fp_colors'):
    Rast_make_ramp_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_ramp_fp_colors
    Rast_make_ramp_fp_colors.restype = None
    Rast_make_ramp_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 123
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_wave_colors'):
    Rast_make_wave_colors = _libs['grass_raster.7.0.svn'].Rast_make_wave_colors
    Rast_make_wave_colors.restype = None
    Rast_make_wave_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 124
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_wave_fp_colors'):
    Rast_make_wave_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_wave_fp_colors
    Rast_make_wave_fp_colors.restype = None
    Rast_make_wave_fp_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 127
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_free_colors'):
    Rast_free_colors = _libs['grass_raster.7.0.svn'].Rast_free_colors
    Rast_free_colors.restype = None
    Rast_free_colors.argtypes = [POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 128
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__color_free_rules'):
    Rast__color_free_rules = _libs['grass_raster.7.0.svn'].Rast__color_free_rules
    Rast__color_free_rules.restype = None
    Rast__color_free_rules.argtypes = [POINTER(struct__Color_Info_)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 129
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__color_free_lookup'):
    Rast__color_free_lookup = _libs['grass_raster.7.0.svn'].Rast__color_free_lookup
    Rast__color_free_lookup.restype = None
    Rast__color_free_lookup.argtypes = [POINTER(struct__Color_Info_)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 130
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__color_free_fp_lookup'):
    Rast__color_free_fp_lookup = _libs['grass_raster.7.0.svn'].Rast__color_free_fp_lookup
    Rast__color_free_fp_lookup.restype = None
    Rast__color_free_fp_lookup.argtypes = [POINTER(struct__Color_Info_)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 131
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__color_reset'):
    Rast__color_reset = _libs['grass_raster.7.0.svn'].Rast__color_reset
    Rast__color_reset.restype = None
    Rast__color_reset.argtypes = [POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 134
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_color'):
    Rast_get_color = _libs['grass_raster.7.0.svn'].Rast_get_color
    Rast_get_color.restype = c_int
    Rast_get_color.argtypes = [POINTER(None), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 136
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_c_color'):
    Rast_get_c_color = _libs['grass_raster.7.0.svn'].Rast_get_c_color
    Rast_get_c_color.restype = c_int
    Rast_get_c_color.argtypes = [POINTER(CELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 137
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_f_color'):
    Rast_get_f_color = _libs['grass_raster.7.0.svn'].Rast_get_f_color
    Rast_get_f_color.restype = c_int
    Rast_get_f_color.argtypes = [POINTER(FCELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 138
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_d_color'):
    Rast_get_d_color = _libs['grass_raster.7.0.svn'].Rast_get_d_color
    Rast_get_d_color.restype = c_int
    Rast_get_d_color.argtypes = [POINTER(DCELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 139
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_null_value_color'):
    Rast_get_null_value_color = _libs['grass_raster.7.0.svn'].Rast_get_null_value_color
    Rast_get_null_value_color.restype = None
    Rast_get_null_value_color.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 140
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_default_color'):
    Rast_get_default_color = _libs['grass_raster.7.0.svn'].Rast_get_default_color
    Rast_get_default_color.restype = None
    Rast_get_default_color.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 143
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_histogram_eq_colors'):
    Rast_make_histogram_eq_colors = _libs['grass_raster.7.0.svn'].Rast_make_histogram_eq_colors
    Rast_make_histogram_eq_colors.restype = None
    Rast_make_histogram_eq_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Cell_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 144
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_histogram_log_colors'):
    Rast_make_histogram_log_colors = _libs['grass_raster.7.0.svn'].Rast_make_histogram_log_colors
    Rast_make_histogram_log_colors.restype = None
    Rast_make_histogram_log_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Cell_stats), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 147
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_init_colors'):
    Rast_init_colors = _libs['grass_raster.7.0.svn'].Rast_init_colors
    Rast_init_colors.restype = None
    Rast_init_colors.argtypes = [POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 150
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__insert_color_into_lookup'):
    Rast__insert_color_into_lookup = _libs['grass_raster.7.0.svn'].Rast__insert_color_into_lookup
    Rast__insert_color_into_lookup.restype = c_int
    Rast__insert_color_into_lookup.argtypes = [CELL, c_int, c_int, c_int, POINTER(struct__Color_Info_)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 153
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_invert_colors'):
    Rast_invert_colors = _libs['grass_raster.7.0.svn'].Rast_invert_colors
    Rast_invert_colors.restype = None
    Rast_invert_colors.argtypes = [POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 156
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_lookup_c_colors'):
    Rast_lookup_c_colors = _libs['grass_raster.7.0.svn'].Rast_lookup_c_colors
    Rast_lookup_c_colors.restype = None
    Rast_lookup_c_colors.argtypes = [POINTER(CELL), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 159
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_lookup_colors'):
    Rast_lookup_colors = _libs['grass_raster.7.0.svn'].Rast_lookup_colors
    Rast_lookup_colors.restype = None
    Rast_lookup_colors.argtypes = [POINTER(None), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(struct_Colors), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 162
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_lookup_f_colors'):
    Rast_lookup_f_colors = _libs['grass_raster.7.0.svn'].Rast_lookup_f_colors
    Rast_lookup_f_colors.restype = None
    Rast_lookup_f_colors.argtypes = [POINTER(FCELL), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 165
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_lookup_d_colors'):
    Rast_lookup_d_colors = _libs['grass_raster.7.0.svn'].Rast_lookup_d_colors
    Rast_lookup_d_colors.restype = None
    Rast_lookup_d_colors.argtypes = [POINTER(DCELL), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 168
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__lookup_colors'):
    Rast__lookup_colors = _libs['grass_raster.7.0.svn'].Rast__lookup_colors
    Rast__lookup_colors.restype = None
    Rast__lookup_colors.argtypes = [POINTER(None), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), c_int, POINTER(struct_Colors), c_int, c_int, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 171
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__interpolate_color_rule'):
    Rast__interpolate_color_rule = _libs['grass_raster.7.0.svn'].Rast__interpolate_color_rule
    Rast__interpolate_color_rule.restype = None
    Rast__interpolate_color_rule.argtypes = [DCELL, POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(struct__Color_Rule_)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 175
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__organize_colors'):
    Rast__organize_colors = _libs['grass_raster.7.0.svn'].Rast__organize_colors
    Rast__organize_colors.restype = None
    Rast__organize_colors.argtypes = [POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 178
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_print_colors'):
    Rast_print_colors = _libs['grass_raster.7.0.svn'].Rast_print_colors
    Rast_print_colors.restype = None
    Rast_print_colors.argtypes = [POINTER(struct_Colors), DCELL, DCELL, POINTER(FILE), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 181
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_random_colors'):
    Rast_make_random_colors = _libs['grass_raster.7.0.svn'].Rast_make_random_colors
    Rast_make_random_colors.restype = None
    Rast_make_random_colors.argtypes = [POINTER(struct_Colors), CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 184
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_c_color_range'):
    Rast_set_c_color_range = _libs['grass_raster.7.0.svn'].Rast_set_c_color_range
    Rast_set_c_color_range.restype = None
    Rast_set_c_color_range.argtypes = [CELL, CELL, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 185
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_d_color_range'):
    Rast_set_d_color_range = _libs['grass_raster.7.0.svn'].Rast_set_d_color_range
    Rast_set_d_color_range.restype = None
    Rast_set_d_color_range.argtypes = [DCELL, DCELL, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 186
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_c_color_range'):
    Rast_get_c_color_range = _libs['grass_raster.7.0.svn'].Rast_get_c_color_range
    Rast_get_c_color_range.restype = None
    Rast_get_c_color_range.argtypes = [POINTER(CELL), POINTER(CELL), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 187
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_d_color_range'):
    Rast_get_d_color_range = _libs['grass_raster.7.0.svn'].Rast_get_d_color_range
    Rast_get_d_color_range.restype = None
    Rast_get_d_color_range.argtypes = [POINTER(DCELL), POINTER(DCELL), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 190
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_colors'):
    Rast_read_colors = _libs['grass_raster.7.0.svn'].Rast_read_colors
    Rast_read_colors.restype = c_int
    Rast_read_colors.argtypes = [String, String, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 191
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__read_colors'):
    Rast__read_colors = _libs['grass_raster.7.0.svn'].Rast__read_colors
    Rast__read_colors.restype = c_int
    Rast__read_colors.argtypes = [String, String, String, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 192
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_mark_colors_as_fp'):
    Rast_mark_colors_as_fp = _libs['grass_raster.7.0.svn'].Rast_mark_colors_as_fp
    Rast_mark_colors_as_fp.restype = None
    Rast_mark_colors_as_fp.argtypes = [POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 195
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_remove_colors'):
    Rast_remove_colors = _libs['grass_raster.7.0.svn'].Rast_remove_colors
    Rast_remove_colors.restype = c_int
    Rast_remove_colors.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 198
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_add_d_color_rule'):
    Rast_add_d_color_rule = _libs['grass_raster.7.0.svn'].Rast_add_d_color_rule
    Rast_add_d_color_rule.restype = None
    Rast_add_d_color_rule.argtypes = [POINTER(DCELL), c_int, c_int, c_int, POINTER(DCELL), c_int, c_int, c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 201
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_add_f_color_rule'):
    Rast_add_f_color_rule = _libs['grass_raster.7.0.svn'].Rast_add_f_color_rule
    Rast_add_f_color_rule.restype = None
    Rast_add_f_color_rule.argtypes = [POINTER(FCELL), c_int, c_int, c_int, POINTER(FCELL), c_int, c_int, c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 204
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_add_c_color_rule'):
    Rast_add_c_color_rule = _libs['grass_raster.7.0.svn'].Rast_add_c_color_rule
    Rast_add_c_color_rule.restype = None
    Rast_add_c_color_rule.argtypes = [POINTER(CELL), c_int, c_int, c_int, POINTER(CELL), c_int, c_int, c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 207
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_add_color_rule'):
    Rast_add_color_rule = _libs['grass_raster.7.0.svn'].Rast_add_color_rule
    Rast_add_color_rule.restype = None
    Rast_add_color_rule.argtypes = [POINTER(None), c_int, c_int, c_int, POINTER(None), c_int, c_int, c_int, POINTER(struct_Colors), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 210
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_add_modular_d_color_rule'):
    Rast_add_modular_d_color_rule = _libs['grass_raster.7.0.svn'].Rast_add_modular_d_color_rule
    Rast_add_modular_d_color_rule.restype = c_int
    Rast_add_modular_d_color_rule.argtypes = [POINTER(DCELL), c_int, c_int, c_int, POINTER(DCELL), c_int, c_int, c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 213
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_add_modular_f_color_rule'):
    Rast_add_modular_f_color_rule = _libs['grass_raster.7.0.svn'].Rast_add_modular_f_color_rule
    Rast_add_modular_f_color_rule.restype = c_int
    Rast_add_modular_f_color_rule.argtypes = [POINTER(FCELL), c_int, c_int, c_int, POINTER(FCELL), c_int, c_int, c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 216
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_add_modular_c_color_rule'):
    Rast_add_modular_c_color_rule = _libs['grass_raster.7.0.svn'].Rast_add_modular_c_color_rule
    Rast_add_modular_c_color_rule.restype = c_int
    Rast_add_modular_c_color_rule.argtypes = [POINTER(CELL), c_int, c_int, c_int, POINTER(CELL), c_int, c_int, c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 219
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_add_modular_color_rule'):
    Rast_add_modular_color_rule = _libs['grass_raster.7.0.svn'].Rast_add_modular_color_rule
    Rast_add_modular_color_rule.restype = c_int
    Rast_add_modular_color_rule.argtypes = [POINTER(None), c_int, c_int, c_int, POINTER(None), c_int, c_int, c_int, POINTER(struct_Colors), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 224
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_colors_count'):
    Rast_colors_count = _libs['grass_raster.7.0.svn'].Rast_colors_count
    Rast_colors_count.restype = c_int
    Rast_colors_count.argtypes = [POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 225
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_fp_color_rule'):
    Rast_get_fp_color_rule = _libs['grass_raster.7.0.svn'].Rast_get_fp_color_rule
    Rast_get_fp_color_rule.restype = c_int
    Rast_get_fp_color_rule.argtypes = [POINTER(DCELL), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(DCELL), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(struct_Colors), c_int]

read_rule_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), DCELL, DCELL, POINTER(DCELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)) # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 231

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 233
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_parse_color_rule'):
    Rast_parse_color_rule = _libs['grass_raster.7.0.svn'].Rast_parse_color_rule
    Rast_parse_color_rule.restype = c_int
    Rast_parse_color_rule.argtypes = [DCELL, DCELL, String, POINTER(DCELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 235
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_parse_color_rule_error'):
    Rast_parse_color_rule_error = _libs['grass_raster.7.0.svn'].Rast_parse_color_rule_error
    Rast_parse_color_rule_error.restype = ReturnString
    Rast_parse_color_rule_error.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 236
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_color_rule'):
    Rast_read_color_rule = _libs['grass_raster.7.0.svn'].Rast_read_color_rule
    Rast_read_color_rule.restype = c_int
    Rast_read_color_rule.argtypes = [POINTER(None), DCELL, DCELL, POINTER(DCELL), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 238
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_color_rules'):
    Rast_read_color_rules = _libs['grass_raster.7.0.svn'].Rast_read_color_rules
    Rast_read_color_rules.restype = c_int
    Rast_read_color_rules.argtypes = [POINTER(struct_Colors), DCELL, DCELL, POINTER(read_rule_fn), POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 239
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_load_colors'):
    Rast_load_colors = _libs['grass_raster.7.0.svn'].Rast_load_colors
    Rast_load_colors.restype = c_int
    Rast_load_colors.argtypes = [POINTER(struct_Colors), String, CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 240
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_load_fp_colors'):
    Rast_load_fp_colors = _libs['grass_raster.7.0.svn'].Rast_load_fp_colors
    Rast_load_fp_colors.restype = c_int
    Rast_load_fp_colors.argtypes = [POINTER(struct_Colors), String, DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 241
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_colors'):
    Rast_make_colors = _libs['grass_raster.7.0.svn'].Rast_make_colors
    Rast_make_colors.restype = None
    Rast_make_colors.argtypes = [POINTER(struct_Colors), String, CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 242
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_fp_colors'):
    Rast_make_fp_colors = _libs['grass_raster.7.0.svn'].Rast_make_fp_colors
    Rast_make_fp_colors.restype = None
    Rast_make_fp_colors.argtypes = [POINTER(struct_Colors), String, DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 245
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_c_color'):
    Rast_set_c_color = _libs['grass_raster.7.0.svn'].Rast_set_c_color
    Rast_set_c_color.restype = None
    Rast_set_c_color.argtypes = [CELL, c_int, c_int, c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 246
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_d_color'):
    Rast_set_d_color = _libs['grass_raster.7.0.svn'].Rast_set_d_color
    Rast_set_d_color.restype = None
    Rast_set_d_color.argtypes = [DCELL, c_int, c_int, c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 247
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_null_value_color'):
    Rast_set_null_value_color = _libs['grass_raster.7.0.svn'].Rast_set_null_value_color
    Rast_set_null_value_color.restype = None
    Rast_set_null_value_color.argtypes = [c_int, c_int, c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 248
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_default_color'):
    Rast_set_default_color = _libs['grass_raster.7.0.svn'].Rast_set_default_color
    Rast_set_default_color.restype = None
    Rast_set_default_color.argtypes = [c_int, c_int, c_int, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 251
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_shift_c_colors'):
    Rast_shift_c_colors = _libs['grass_raster.7.0.svn'].Rast_shift_c_colors
    Rast_shift_c_colors.restype = None
    Rast_shift_c_colors.argtypes = [CELL, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 252
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_shift_d_colors'):
    Rast_shift_d_colors = _libs['grass_raster.7.0.svn'].Rast_shift_d_colors
    Rast_shift_d_colors.restype = None
    Rast_shift_d_colors.argtypes = [DCELL, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 255
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_colors'):
    Rast_write_colors = _libs['grass_raster.7.0.svn'].Rast_write_colors
    Rast_write_colors.restype = None
    Rast_write_colors.argtypes = [String, String, POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 256
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__write_colors'):
    Rast__write_colors = _libs['grass_raster.7.0.svn'].Rast__write_colors
    Rast__write_colors.restype = None
    Rast__write_colors.argtypes = [POINTER(FILE), POINTER(struct_Colors)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 259
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_histogram_eq_colors'):
    Rast_histogram_eq_colors = _libs['grass_raster.7.0.svn'].Rast_histogram_eq_colors
    Rast_histogram_eq_colors.restype = None
    Rast_histogram_eq_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Colors), POINTER(struct_Cell_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 261
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_histogram_eq_fp_colors'):
    Rast_histogram_eq_fp_colors = _libs['grass_raster.7.0.svn'].Rast_histogram_eq_fp_colors
    Rast_histogram_eq_fp_colors.restype = None
    Rast_histogram_eq_fp_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Colors), POINTER(struct_FP_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 263
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_log_colors'):
    Rast_log_colors = _libs['grass_raster.7.0.svn'].Rast_log_colors
    Rast_log_colors.restype = None
    Rast_log_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Colors), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 264
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_abs_log_colors'):
    Rast_abs_log_colors = _libs['grass_raster.7.0.svn'].Rast_abs_log_colors
    Rast_abs_log_colors.restype = None
    Rast_abs_log_colors.argtypes = [POINTER(struct_Colors), POINTER(struct_Colors), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 267
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__check_format'):
    Rast__check_format = _libs['grass_raster.7.0.svn'].Rast__check_format
    Rast__check_format.restype = c_int
    Rast__check_format.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 268
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__read_row_ptrs'):
    Rast__read_row_ptrs = _libs['grass_raster.7.0.svn'].Rast__read_row_ptrs
    Rast__read_row_ptrs.restype = c_int
    Rast__read_row_ptrs.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 269
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__write_row_ptrs'):
    Rast__write_row_ptrs = _libs['grass_raster.7.0.svn'].Rast__write_row_ptrs
    Rast__write_row_ptrs.restype = c_int
    Rast__write_row_ptrs.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 272
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_clear'):
    Rast_fpreclass_clear = _libs['grass_raster.7.0.svn'].Rast_fpreclass_clear
    Rast_fpreclass_clear.restype = None
    Rast_fpreclass_clear.argtypes = [POINTER(struct_FPReclass)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 273
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_reset'):
    Rast_fpreclass_reset = _libs['grass_raster.7.0.svn'].Rast_fpreclass_reset
    Rast_fpreclass_reset.restype = None
    Rast_fpreclass_reset.argtypes = [POINTER(struct_FPReclass)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 274
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_init'):
    Rast_fpreclass_init = _libs['grass_raster.7.0.svn'].Rast_fpreclass_init
    Rast_fpreclass_init.restype = None
    Rast_fpreclass_init.argtypes = [POINTER(struct_FPReclass)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 275
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_set_domain'):
    Rast_fpreclass_set_domain = _libs['grass_raster.7.0.svn'].Rast_fpreclass_set_domain
    Rast_fpreclass_set_domain.restype = None
    Rast_fpreclass_set_domain.argtypes = [POINTER(struct_FPReclass), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 276
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_set_range'):
    Rast_fpreclass_set_range = _libs['grass_raster.7.0.svn'].Rast_fpreclass_set_range
    Rast_fpreclass_set_range.restype = None
    Rast_fpreclass_set_range.argtypes = [POINTER(struct_FPReclass), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 277
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_get_limits'):
    Rast_fpreclass_get_limits = _libs['grass_raster.7.0.svn'].Rast_fpreclass_get_limits
    Rast_fpreclass_get_limits.restype = c_int
    Rast_fpreclass_get_limits.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(DCELL), POINTER(DCELL), POINTER(DCELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 279
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_nof_rules'):
    Rast_fpreclass_nof_rules = _libs['grass_raster.7.0.svn'].Rast_fpreclass_nof_rules
    Rast_fpreclass_nof_rules.restype = c_int
    Rast_fpreclass_nof_rules.argtypes = [POINTER(struct_FPReclass)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 280
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_get_ith_rule'):
    Rast_fpreclass_get_ith_rule = _libs['grass_raster.7.0.svn'].Rast_fpreclass_get_ith_rule
    Rast_fpreclass_get_ith_rule.restype = None
    Rast_fpreclass_get_ith_rule.argtypes = [POINTER(struct_FPReclass), c_int, POINTER(DCELL), POINTER(DCELL), POINTER(DCELL), POINTER(DCELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 282
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_set_neg_infinite_rule'):
    Rast_fpreclass_set_neg_infinite_rule = _libs['grass_raster.7.0.svn'].Rast_fpreclass_set_neg_infinite_rule
    Rast_fpreclass_set_neg_infinite_rule.restype = None
    Rast_fpreclass_set_neg_infinite_rule.argtypes = [POINTER(struct_FPReclass), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 283
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_get_neg_infinite_rule'):
    Rast_fpreclass_get_neg_infinite_rule = _libs['grass_raster.7.0.svn'].Rast_fpreclass_get_neg_infinite_rule
    Rast_fpreclass_get_neg_infinite_rule.restype = c_int
    Rast_fpreclass_get_neg_infinite_rule.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(DCELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 285
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_set_pos_infinite_rule'):
    Rast_fpreclass_set_pos_infinite_rule = _libs['grass_raster.7.0.svn'].Rast_fpreclass_set_pos_infinite_rule
    Rast_fpreclass_set_pos_infinite_rule.restype = None
    Rast_fpreclass_set_pos_infinite_rule.argtypes = [POINTER(struct_FPReclass), DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 286
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_get_pos_infinite_rule'):
    Rast_fpreclass_get_pos_infinite_rule = _libs['grass_raster.7.0.svn'].Rast_fpreclass_get_pos_infinite_rule
    Rast_fpreclass_get_pos_infinite_rule.restype = c_int
    Rast_fpreclass_get_pos_infinite_rule.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(DCELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 288
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_add_rule'):
    Rast_fpreclass_add_rule = _libs['grass_raster.7.0.svn'].Rast_fpreclass_add_rule
    Rast_fpreclass_add_rule.restype = None
    Rast_fpreclass_add_rule.argtypes = [POINTER(struct_FPReclass), DCELL, DCELL, DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 289
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_reverse_rule_order'):
    Rast_fpreclass_reverse_rule_order = _libs['grass_raster.7.0.svn'].Rast_fpreclass_reverse_rule_order
    Rast_fpreclass_reverse_rule_order.restype = None
    Rast_fpreclass_reverse_rule_order.argtypes = [POINTER(struct_FPReclass)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 290
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_get_cell_value'):
    Rast_fpreclass_get_cell_value = _libs['grass_raster.7.0.svn'].Rast_fpreclass_get_cell_value
    Rast_fpreclass_get_cell_value.restype = DCELL
    Rast_fpreclass_get_cell_value.argtypes = [POINTER(struct_FPReclass), DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 291
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_perform_di'):
    Rast_fpreclass_perform_di = _libs['grass_raster.7.0.svn'].Rast_fpreclass_perform_di
    Rast_fpreclass_perform_di.restype = None
    Rast_fpreclass_perform_di.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(CELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 293
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_perform_df'):
    Rast_fpreclass_perform_df = _libs['grass_raster.7.0.svn'].Rast_fpreclass_perform_df
    Rast_fpreclass_perform_df.restype = None
    Rast_fpreclass_perform_df.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(FCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 295
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_perform_dd'):
    Rast_fpreclass_perform_dd = _libs['grass_raster.7.0.svn'].Rast_fpreclass_perform_dd
    Rast_fpreclass_perform_dd.restype = None
    Rast_fpreclass_perform_dd.argtypes = [POINTER(struct_FPReclass), POINTER(DCELL), POINTER(DCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 297
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_perform_fi'):
    Rast_fpreclass_perform_fi = _libs['grass_raster.7.0.svn'].Rast_fpreclass_perform_fi
    Rast_fpreclass_perform_fi.restype = None
    Rast_fpreclass_perform_fi.argtypes = [POINTER(struct_FPReclass), POINTER(FCELL), POINTER(CELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 299
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_perform_ff'):
    Rast_fpreclass_perform_ff = _libs['grass_raster.7.0.svn'].Rast_fpreclass_perform_ff
    Rast_fpreclass_perform_ff.restype = None
    Rast_fpreclass_perform_ff.argtypes = [POINTER(struct_FPReclass), POINTER(FCELL), POINTER(FCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 301
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_perform_fd'):
    Rast_fpreclass_perform_fd = _libs['grass_raster.7.0.svn'].Rast_fpreclass_perform_fd
    Rast_fpreclass_perform_fd.restype = None
    Rast_fpreclass_perform_fd.argtypes = [POINTER(struct_FPReclass), POINTER(FCELL), POINTER(DCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 303
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_perform_ii'):
    Rast_fpreclass_perform_ii = _libs['grass_raster.7.0.svn'].Rast_fpreclass_perform_ii
    Rast_fpreclass_perform_ii.restype = None
    Rast_fpreclass_perform_ii.argtypes = [POINTER(struct_FPReclass), POINTER(CELL), POINTER(CELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 305
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_perform_if'):
    Rast_fpreclass_perform_if = _libs['grass_raster.7.0.svn'].Rast_fpreclass_perform_if
    Rast_fpreclass_perform_if.restype = None
    Rast_fpreclass_perform_if.argtypes = [POINTER(struct_FPReclass), POINTER(CELL), POINTER(FCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 307
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_fpreclass_perform_id'):
    Rast_fpreclass_perform_id = _libs['grass_raster.7.0.svn'].Rast_fpreclass_perform_id
    Rast_fpreclass_perform_id.restype = None
    Rast_fpreclass_perform_id.argtypes = [POINTER(struct_FPReclass), POINTER(CELL), POINTER(DCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 310
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_init_gdal'):
    Rast_init_gdal = _libs['grass_raster.7.0.svn'].Rast_init_gdal
    Rast_init_gdal.restype = None
    Rast_init_gdal.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 311
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_gdal_link'):
    Rast_get_gdal_link = _libs['grass_raster.7.0.svn'].Rast_get_gdal_link
    Rast_get_gdal_link.restype = POINTER(struct_GDAL_link)
    Rast_get_gdal_link.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 312
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_create_gdal_link'):
    Rast_create_gdal_link = _libs['grass_raster.7.0.svn'].Rast_create_gdal_link
    Rast_create_gdal_link.restype = POINTER(struct_GDAL_link)
    Rast_create_gdal_link.argtypes = [String, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 313
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_close_gdal_link'):
    Rast_close_gdal_link = _libs['grass_raster.7.0.svn'].Rast_close_gdal_link
    Rast_close_gdal_link.restype = None
    Rast_close_gdal_link.argtypes = [POINTER(struct_GDAL_link)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 314
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_close_gdal_write_link'):
    Rast_close_gdal_write_link = _libs['grass_raster.7.0.svn'].Rast_close_gdal_write_link
    Rast_close_gdal_write_link.restype = c_int
    Rast_close_gdal_write_link.argtypes = [POINTER(struct_GDAL_link)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 317
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_cellhd'):
    Rast_get_cellhd = _libs['grass_raster.7.0.svn'].Rast_get_cellhd
    Rast_get_cellhd.restype = None
    Rast_get_cellhd.argtypes = [String, String, POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 320
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_row_nomask'):
    Rast_get_row_nomask = _libs['grass_raster.7.0.svn'].Rast_get_row_nomask
    Rast_get_row_nomask.restype = None
    Rast_get_row_nomask.argtypes = [c_int, POINTER(None), c_int, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 321
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_c_row_nomask'):
    Rast_get_c_row_nomask = _libs['grass_raster.7.0.svn'].Rast_get_c_row_nomask
    Rast_get_c_row_nomask.restype = None
    Rast_get_c_row_nomask.argtypes = [c_int, POINTER(CELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 322
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_f_row_nomask'):
    Rast_get_f_row_nomask = _libs['grass_raster.7.0.svn'].Rast_get_f_row_nomask
    Rast_get_f_row_nomask.restype = None
    Rast_get_f_row_nomask.argtypes = [c_int, POINTER(FCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 323
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_d_row_nomask'):
    Rast_get_d_row_nomask = _libs['grass_raster.7.0.svn'].Rast_get_d_row_nomask
    Rast_get_d_row_nomask.restype = None
    Rast_get_d_row_nomask.argtypes = [c_int, POINTER(DCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 324
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_row'):
    Rast_get_row = _libs['grass_raster.7.0.svn'].Rast_get_row
    Rast_get_row.restype = None
    Rast_get_row.argtypes = [c_int, POINTER(None), c_int, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 325
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_c_row'):
    Rast_get_c_row = _libs['grass_raster.7.0.svn'].Rast_get_c_row
    Rast_get_c_row.restype = None
    Rast_get_c_row.argtypes = [c_int, POINTER(CELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 326
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_f_row'):
    Rast_get_f_row = _libs['grass_raster.7.0.svn'].Rast_get_f_row
    Rast_get_f_row.restype = None
    Rast_get_f_row.argtypes = [c_int, POINTER(FCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 327
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_d_row'):
    Rast_get_d_row = _libs['grass_raster.7.0.svn'].Rast_get_d_row
    Rast_get_d_row.restype = None
    Rast_get_d_row.argtypes = [c_int, POINTER(DCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 328
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_null_value_row'):
    Rast_get_null_value_row = _libs['grass_raster.7.0.svn'].Rast_get_null_value_row
    Rast_get_null_value_row.restype = None
    Rast_get_null_value_row.argtypes = [c_int, String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 331
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_row_colors'):
    Rast_get_row_colors = _libs['grass_raster.7.0.svn'].Rast_get_row_colors
    Rast_get_row_colors.restype = None
    Rast_get_row_colors.argtypes = [c_int, c_int, POINTER(struct_Colors), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 335
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_histogram_eq'):
    Rast_histogram_eq = _libs['grass_raster.7.0.svn'].Rast_histogram_eq
    Rast_histogram_eq.restype = None
    Rast_histogram_eq.argtypes = [POINTER(struct_Histogram), POINTER(POINTER(c_ubyte)), POINTER(CELL), POINTER(CELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 339
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_init_histogram'):
    Rast_init_histogram = _libs['grass_raster.7.0.svn'].Rast_init_histogram
    Rast_init_histogram.restype = None
    Rast_init_histogram.argtypes = [POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 340
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_histogram'):
    Rast_read_histogram = _libs['grass_raster.7.0.svn'].Rast_read_histogram
    Rast_read_histogram.restype = c_int
    Rast_read_histogram.argtypes = [String, String, POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 341
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_histogram'):
    Rast_write_histogram = _libs['grass_raster.7.0.svn'].Rast_write_histogram
    Rast_write_histogram.restype = None
    Rast_write_histogram.argtypes = [String, POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 342
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_histogram_cs'):
    Rast_write_histogram_cs = _libs['grass_raster.7.0.svn'].Rast_write_histogram_cs
    Rast_write_histogram_cs.restype = None
    Rast_write_histogram_cs.argtypes = [String, POINTER(struct_Cell_stats)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 343
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_make_histogram_cs'):
    Rast_make_histogram_cs = _libs['grass_raster.7.0.svn'].Rast_make_histogram_cs
    Rast_make_histogram_cs.restype = None
    Rast_make_histogram_cs.argtypes = [POINTER(struct_Cell_stats), POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 344
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_histogram_num'):
    Rast_get_histogram_num = _libs['grass_raster.7.0.svn'].Rast_get_histogram_num
    Rast_get_histogram_num.restype = c_int
    Rast_get_histogram_num.argtypes = [POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 345
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_histogram_cat'):
    Rast_get_histogram_cat = _libs['grass_raster.7.0.svn'].Rast_get_histogram_cat
    Rast_get_histogram_cat.restype = CELL
    Rast_get_histogram_cat.argtypes = [c_int, POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 346
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_histogram_count'):
    Rast_get_histogram_count = _libs['grass_raster.7.0.svn'].Rast_get_histogram_count
    Rast_get_histogram_count.restype = c_long
    Rast_get_histogram_count.argtypes = [c_int, POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 347
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_free_histogram'):
    Rast_free_histogram = _libs['grass_raster.7.0.svn'].Rast_free_histogram
    Rast_free_histogram.restype = None
    Rast_free_histogram.argtypes = [POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 348
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_sort_histogram'):
    Rast_sort_histogram = _libs['grass_raster.7.0.svn'].Rast_sort_histogram
    Rast_sort_histogram.restype = c_int
    Rast_sort_histogram.argtypes = [POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 349
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_sort_histogram_by_count'):
    Rast_sort_histogram_by_count = _libs['grass_raster.7.0.svn'].Rast_sort_histogram_by_count
    Rast_sort_histogram_by_count.restype = c_int
    Rast_sort_histogram_by_count.argtypes = [POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 350
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_remove_histogram'):
    Rast_remove_histogram = _libs['grass_raster.7.0.svn'].Rast_remove_histogram
    Rast_remove_histogram.restype = None
    Rast_remove_histogram.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 351
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_add_histogram'):
    Rast_add_histogram = _libs['grass_raster.7.0.svn'].Rast_add_histogram
    Rast_add_histogram.restype = c_int
    Rast_add_histogram.argtypes = [CELL, c_long, POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 352
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_histogram'):
    Rast_set_histogram = _libs['grass_raster.7.0.svn'].Rast_set_histogram
    Rast_set_histogram.restype = c_int
    Rast_set_histogram.argtypes = [CELL, c_long, POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 353
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_extend_histogram'):
    Rast_extend_histogram = _libs['grass_raster.7.0.svn'].Rast_extend_histogram
    Rast_extend_histogram.restype = None
    Rast_extend_histogram.argtypes = [CELL, c_long, POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 354
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_zero_histogram'):
    Rast_zero_histogram = _libs['grass_raster.7.0.svn'].Rast_zero_histogram
    Rast_zero_histogram.restype = None
    Rast_zero_histogram.argtypes = [POINTER(struct_Histogram)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 357
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__read_history'):
    Rast__read_history = _libs['grass_raster.7.0.svn'].Rast__read_history
    Rast__read_history.restype = c_int
    Rast__read_history.argtypes = [POINTER(struct_History), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 358
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_history'):
    Rast_read_history = _libs['grass_raster.7.0.svn'].Rast_read_history
    Rast_read_history.restype = c_int
    Rast_read_history.argtypes = [String, String, POINTER(struct_History)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 359
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__write_history'):
    Rast__write_history = _libs['grass_raster.7.0.svn'].Rast__write_history
    Rast__write_history.restype = None
    Rast__write_history.argtypes = [POINTER(struct_History), POINTER(FILE)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 360
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_history'):
    Rast_write_history = _libs['grass_raster.7.0.svn'].Rast_write_history
    Rast_write_history.restype = None
    Rast_write_history.argtypes = [String, POINTER(struct_History)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 361
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_short_history'):
    Rast_short_history = _libs['grass_raster.7.0.svn'].Rast_short_history
    Rast_short_history.restype = None
    Rast_short_history.argtypes = [String, String, POINTER(struct_History)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 362
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_command_history'):
    Rast_command_history = _libs['grass_raster.7.0.svn'].Rast_command_history
    Rast_command_history.restype = c_int
    Rast_command_history.argtypes = [POINTER(struct_History)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 363
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_append_history'):
    Rast_append_history = _libs['grass_raster.7.0.svn'].Rast_append_history
    Rast_append_history.restype = None
    Rast_append_history.argtypes = [POINTER(struct_History), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 364
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_append_format_history'):
    _func = _libs['grass_raster.7.0.svn'].Rast_append_format_history
    _restype = None
    _argtypes = [POINTER(struct_History), String]
    Rast_append_format_history = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 366
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_history'):
    Rast_get_history = _libs['grass_raster.7.0.svn'].Rast_get_history
    Rast_get_history.restype = ReturnString
    Rast_get_history.argtypes = [POINTER(struct_History), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 367
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_history'):
    Rast_set_history = _libs['grass_raster.7.0.svn'].Rast_set_history
    Rast_set_history.restype = None
    Rast_set_history.argtypes = [POINTER(struct_History), c_int, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 368
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_format_history'):
    _func = _libs['grass_raster.7.0.svn'].Rast_format_history
    _restype = None
    _argtypes = [POINTER(struct_History), c_int, String]
    Rast_format_history = _variadic_function(_func,_restype,_argtypes)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 370
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_clear_history'):
    Rast_clear_history = _libs['grass_raster.7.0.svn'].Rast_clear_history
    Rast_clear_history.restype = None
    Rast_clear_history.argtypes = [POINTER(struct_History)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 371
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_free_history'):
    Rast_free_history = _libs['grass_raster.7.0.svn'].Rast_free_history
    Rast_free_history.restype = None
    Rast_free_history.argtypes = [POINTER(struct_History)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 372
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_history_length'):
    Rast_history_length = _libs['grass_raster.7.0.svn'].Rast_history_length
    Rast_history_length.restype = c_int
    Rast_history_length.argtypes = [POINTER(struct_History)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 373
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_history_line'):
    Rast_history_line = _libs['grass_raster.7.0.svn'].Rast_history_line
    Rast_history_line.restype = ReturnString
    Rast_history_line.argtypes = [POINTER(struct_History), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 376
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_init'):
    Rast_init = _libs['grass_raster.7.0.svn'].Rast_init
    Rast_init.restype = None
    Rast_init.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 377
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__check_init'):
    Rast__check_init = _libs['grass_raster.7.0.svn'].Rast__check_init
    Rast__check_init.restype = None
    Rast__check_init.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 378
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_init_all'):
    Rast_init_all = _libs['grass_raster.7.0.svn'].Rast_init_all
    Rast_init_all.restype = None
    Rast_init_all.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 379
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__init'):
    Rast__init = _libs['grass_raster.7.0.svn'].Rast__init
    Rast__init.restype = None
    Rast__init.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 380
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__error_handler'):
    Rast__error_handler = _libs['grass_raster.7.0.svn'].Rast__error_handler
    Rast__error_handler.restype = None
    Rast__error_handler.argtypes = [POINTER(None)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 383
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_interp_linear'):
    Rast_interp_linear = _libs['grass_raster.7.0.svn'].Rast_interp_linear
    Rast_interp_linear.restype = DCELL
    Rast_interp_linear.argtypes = [c_double, DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 384
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_interp_bilinear'):
    Rast_interp_bilinear = _libs['grass_raster.7.0.svn'].Rast_interp_bilinear
    Rast_interp_bilinear.restype = DCELL
    Rast_interp_bilinear.argtypes = [c_double, c_double, DCELL, DCELL, DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 385
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_interp_cubic'):
    Rast_interp_cubic = _libs['grass_raster.7.0.svn'].Rast_interp_cubic
    Rast_interp_cubic.restype = DCELL
    Rast_interp_cubic.argtypes = [c_double, DCELL, DCELL, DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 386
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_interp_bicubic'):
    Rast_interp_bicubic = _libs['grass_raster.7.0.svn'].Rast_interp_bicubic
    Rast_interp_bicubic.restype = DCELL
    Rast_interp_bicubic.argtypes = [c_double, c_double, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 390
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_interp_lanczos'):
    Rast_interp_lanczos = _libs['grass_raster.7.0.svn'].Rast_interp_lanczos
    Rast_interp_lanczos.restype = DCELL
    Rast_interp_lanczos.argtypes = [c_double, c_double, POINTER(DCELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 391
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_interp_cubic_bspline'):
    Rast_interp_cubic_bspline = _libs['grass_raster.7.0.svn'].Rast_interp_cubic_bspline
    Rast_interp_cubic_bspline.restype = DCELL
    Rast_interp_cubic_bspline.argtypes = [c_double, DCELL, DCELL, DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 392
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_interp_bicubic_bspline'):
    Rast_interp_bicubic_bspline = _libs['grass_raster.7.0.svn'].Rast_interp_bicubic_bspline
    Rast_interp_bicubic_bspline.restype = DCELL
    Rast_interp_bicubic_bspline.argtypes = [c_double, c_double, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL, DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 398
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_mask_info'):
    Rast_mask_info = _libs['grass_raster.7.0.svn'].Rast_mask_info
    Rast_mask_info.restype = ReturnString
    Rast_mask_info.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 399
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__mask_info'):
    Rast__mask_info = _libs['grass_raster.7.0.svn'].Rast__mask_info
    Rast__mask_info.restype = c_int
    Rast__mask_info.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 402
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_maskfd'):
    Rast_maskfd = _libs['grass_raster.7.0.svn'].Rast_maskfd
    Rast_maskfd.restype = c_int
    Rast_maskfd.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 412
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__set_null_value'):
    Rast__set_null_value = _libs['grass_raster.7.0.svn'].Rast__set_null_value
    Rast__set_null_value.restype = None
    Rast__set_null_value.argtypes = [POINTER(None), c_int, c_int, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 413
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_null_value'):
    Rast_set_null_value = _libs['grass_raster.7.0.svn'].Rast_set_null_value
    Rast_set_null_value.restype = None
    Rast_set_null_value.argtypes = [POINTER(None), c_int, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 414
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_c_null_value'):
    Rast_set_c_null_value = _libs['grass_raster.7.0.svn'].Rast_set_c_null_value
    Rast_set_c_null_value.restype = None
    Rast_set_c_null_value.argtypes = [POINTER(CELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 415
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_f_null_value'):
    Rast_set_f_null_value = _libs['grass_raster.7.0.svn'].Rast_set_f_null_value
    Rast_set_f_null_value.restype = None
    Rast_set_f_null_value.argtypes = [POINTER(FCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 416
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_d_null_value'):
    Rast_set_d_null_value = _libs['grass_raster.7.0.svn'].Rast_set_d_null_value
    Rast_set_d_null_value.restype = None
    Rast_set_d_null_value.argtypes = [POINTER(DCELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 417
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_is_null_value'):
    Rast_is_null_value = _libs['grass_raster.7.0.svn'].Rast_is_null_value
    Rast_is_null_value.restype = c_int
    Rast_is_null_value.argtypes = [POINTER(None), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 427
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_insert_null_values'):
    Rast_insert_null_values = _libs['grass_raster.7.0.svn'].Rast_insert_null_values
    Rast_insert_null_values.restype = None
    Rast_insert_null_values.argtypes = [POINTER(None), String, c_int, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 428
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_insert_c_null_values'):
    Rast_insert_c_null_values = _libs['grass_raster.7.0.svn'].Rast_insert_c_null_values
    Rast_insert_c_null_values.restype = None
    Rast_insert_c_null_values.argtypes = [POINTER(CELL), String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 429
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_insert_f_null_values'):
    Rast_insert_f_null_values = _libs['grass_raster.7.0.svn'].Rast_insert_f_null_values
    Rast_insert_f_null_values.restype = None
    Rast_insert_f_null_values.argtypes = [POINTER(FCELL), String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 430
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_insert_d_null_values'):
    Rast_insert_d_null_values = _libs['grass_raster.7.0.svn'].Rast_insert_d_null_values
    Rast_insert_d_null_values.restype = None
    Rast_insert_d_null_values.argtypes = [POINTER(DCELL), String, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 431
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__check_null_bit'):
    Rast__check_null_bit = _libs['grass_raster.7.0.svn'].Rast__check_null_bit
    Rast__check_null_bit.restype = c_int
    Rast__check_null_bit.argtypes = [POINTER(c_ubyte), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 432
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__convert_01_flags'):
    Rast__convert_01_flags = _libs['grass_raster.7.0.svn'].Rast__convert_01_flags
    Rast__convert_01_flags.restype = None
    Rast__convert_01_flags.argtypes = [String, POINTER(c_ubyte), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 433
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__convert_flags_01'):
    Rast__convert_flags_01 = _libs['grass_raster.7.0.svn'].Rast__convert_flags_01
    Rast__convert_flags_01.restype = None
    Rast__convert_flags_01.argtypes = [String, POINTER(c_ubyte), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 434
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__init_null_bits'):
    Rast__init_null_bits = _libs['grass_raster.7.0.svn'].Rast__init_null_bits
    Rast__init_null_bits.restype = None
    Rast__init_null_bits.argtypes = [POINTER(c_ubyte), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 437
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_open_old'):
    Rast_open_old = _libs['grass_raster.7.0.svn'].Rast_open_old
    Rast_open_old.restype = c_int
    Rast_open_old.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 438
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__open_old'):
    Rast__open_old = _libs['grass_raster.7.0.svn'].Rast__open_old
    Rast__open_old.restype = c_int
    Rast__open_old.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 439
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_open_c_new'):
    Rast_open_c_new = _libs['grass_raster.7.0.svn'].Rast_open_c_new
    Rast_open_c_new.restype = c_int
    Rast_open_c_new.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 440
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_open_c_new_uncompressed'):
    Rast_open_c_new_uncompressed = _libs['grass_raster.7.0.svn'].Rast_open_c_new_uncompressed
    Rast_open_c_new_uncompressed.restype = c_int
    Rast_open_c_new_uncompressed.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 441
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_want_histogram'):
    Rast_want_histogram = _libs['grass_raster.7.0.svn'].Rast_want_histogram
    Rast_want_histogram.restype = None
    Rast_want_histogram.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 442
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_cell_format'):
    Rast_set_cell_format = _libs['grass_raster.7.0.svn'].Rast_set_cell_format
    Rast_set_cell_format.restype = None
    Rast_set_cell_format.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 443
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_cell_format'):
    Rast_get_cell_format = _libs['grass_raster.7.0.svn'].Rast_get_cell_format
    Rast_get_cell_format.restype = c_int
    Rast_get_cell_format.argtypes = [CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 444
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_open_fp_new'):
    Rast_open_fp_new = _libs['grass_raster.7.0.svn'].Rast_open_fp_new
    Rast_open_fp_new.restype = c_int
    Rast_open_fp_new.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 445
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_open_fp_new_uncompressed'):
    Rast_open_fp_new_uncompressed = _libs['grass_raster.7.0.svn'].Rast_open_fp_new_uncompressed
    Rast_open_fp_new_uncompressed.restype = c_int
    Rast_open_fp_new_uncompressed.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 446
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_fp_type'):
    Rast_set_fp_type = _libs['grass_raster.7.0.svn'].Rast_set_fp_type
    Rast_set_fp_type.restype = None
    Rast_set_fp_type.argtypes = [RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 447
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_map_is_fp'):
    Rast_map_is_fp = _libs['grass_raster.7.0.svn'].Rast_map_is_fp
    Rast_map_is_fp.restype = c_int
    Rast_map_is_fp.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 448
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_map_type'):
    Rast_map_type = _libs['grass_raster.7.0.svn'].Rast_map_type
    Rast_map_type.restype = RASTER_MAP_TYPE
    Rast_map_type.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 449
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__check_fp_type'):
    Rast__check_fp_type = _libs['grass_raster.7.0.svn'].Rast__check_fp_type
    Rast__check_fp_type.restype = RASTER_MAP_TYPE
    Rast__check_fp_type.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 450
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_map_type'):
    Rast_get_map_type = _libs['grass_raster.7.0.svn'].Rast_get_map_type
    Rast_get_map_type.restype = RASTER_MAP_TYPE
    Rast_get_map_type.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 451
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_open_new'):
    Rast_open_new = _libs['grass_raster.7.0.svn'].Rast_open_new
    Rast_open_new.restype = c_int
    Rast_open_new.argtypes = [String, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 452
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_open_new_uncompressed'):
    Rast_open_new_uncompressed = _libs['grass_raster.7.0.svn'].Rast_open_new_uncompressed
    Rast_open_new_uncompressed.restype = c_int
    Rast_open_new_uncompressed.argtypes = [String, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 453
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_quant_rules'):
    Rast_set_quant_rules = _libs['grass_raster.7.0.svn'].Rast_set_quant_rules
    Rast_set_quant_rules.restype = None
    Rast_set_quant_rules.argtypes = [c_int, POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 456
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_put_cellhd'):
    Rast_put_cellhd = _libs['grass_raster.7.0.svn'].Rast_put_cellhd
    Rast_put_cellhd.restype = None
    Rast_put_cellhd.argtypes = [String, POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 459
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_put_row'):
    Rast_put_row = _libs['grass_raster.7.0.svn'].Rast_put_row
    Rast_put_row.restype = None
    Rast_put_row.argtypes = [c_int, POINTER(None), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 460
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_put_c_row'):
    Rast_put_c_row = _libs['grass_raster.7.0.svn'].Rast_put_c_row
    Rast_put_c_row.restype = None
    Rast_put_c_row.argtypes = [c_int, POINTER(CELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 461
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_put_f_row'):
    Rast_put_f_row = _libs['grass_raster.7.0.svn'].Rast_put_f_row
    Rast_put_f_row.restype = None
    Rast_put_f_row.argtypes = [c_int, POINTER(FCELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 462
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_put_d_row'):
    Rast_put_d_row = _libs['grass_raster.7.0.svn'].Rast_put_d_row
    Rast_put_d_row.restype = None
    Rast_put_d_row.argtypes = [c_int, POINTER(DCELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 463
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__open_null_write'):
    Rast__open_null_write = _libs['grass_raster.7.0.svn'].Rast__open_null_write
    Rast__open_null_write.restype = c_int
    Rast__open_null_write.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 464
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__write_null_bits'):
    Rast__write_null_bits = _libs['grass_raster.7.0.svn'].Rast__write_null_bits
    Rast__write_null_bits.restype = None
    Rast__write_null_bits.argtypes = [c_int, POINTER(c_ubyte), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 467
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_put_cell_title'):
    Rast_put_cell_title = _libs['grass_raster.7.0.svn'].Rast_put_cell_title
    Rast_put_cell_title.restype = c_int
    Rast_put_cell_title.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 470
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_clear'):
    Rast_quant_clear = _libs['grass_raster.7.0.svn'].Rast_quant_clear
    Rast_quant_clear.restype = None
    Rast_quant_clear.argtypes = [POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 471
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_free'):
    Rast_quant_free = _libs['grass_raster.7.0.svn'].Rast_quant_free
    Rast_quant_free.restype = None
    Rast_quant_free.argtypes = [POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 472
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__quant_organize_fp_lookup'):
    Rast__quant_organize_fp_lookup = _libs['grass_raster.7.0.svn'].Rast__quant_organize_fp_lookup
    Rast__quant_organize_fp_lookup.restype = c_int
    Rast__quant_organize_fp_lookup.argtypes = [POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 473
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_init'):
    Rast_quant_init = _libs['grass_raster.7.0.svn'].Rast_quant_init
    Rast_quant_init.restype = None
    Rast_quant_init.argtypes = [POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 474
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_is_truncate'):
    Rast_quant_is_truncate = _libs['grass_raster.7.0.svn'].Rast_quant_is_truncate
    Rast_quant_is_truncate.restype = c_int
    Rast_quant_is_truncate.argtypes = [POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 475
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_is_round'):
    Rast_quant_is_round = _libs['grass_raster.7.0.svn'].Rast_quant_is_round
    Rast_quant_is_round.restype = c_int
    Rast_quant_is_round.argtypes = [POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 476
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_truncate'):
    Rast_quant_truncate = _libs['grass_raster.7.0.svn'].Rast_quant_truncate
    Rast_quant_truncate.restype = None
    Rast_quant_truncate.argtypes = [POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 477
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_round'):
    Rast_quant_round = _libs['grass_raster.7.0.svn'].Rast_quant_round
    Rast_quant_round.restype = None
    Rast_quant_round.argtypes = [POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 478
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_get_limits'):
    Rast_quant_get_limits = _libs['grass_raster.7.0.svn'].Rast_quant_get_limits
    Rast_quant_get_limits.restype = c_int
    Rast_quant_get_limits.argtypes = [POINTER(struct_Quant), POINTER(DCELL), POINTER(DCELL), POINTER(CELL), POINTER(CELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 480
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_nof_rules'):
    Rast_quant_nof_rules = _libs['grass_raster.7.0.svn'].Rast_quant_nof_rules
    Rast_quant_nof_rules.restype = c_int
    Rast_quant_nof_rules.argtypes = [POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 481
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_get_ith_rule'):
    Rast_quant_get_ith_rule = _libs['grass_raster.7.0.svn'].Rast_quant_get_ith_rule
    Rast_quant_get_ith_rule.restype = None
    Rast_quant_get_ith_rule.argtypes = [POINTER(struct_Quant), c_int, POINTER(DCELL), POINTER(DCELL), POINTER(CELL), POINTER(CELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 483
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_set_neg_infinite_rule'):
    Rast_quant_set_neg_infinite_rule = _libs['grass_raster.7.0.svn'].Rast_quant_set_neg_infinite_rule
    Rast_quant_set_neg_infinite_rule.restype = None
    Rast_quant_set_neg_infinite_rule.argtypes = [POINTER(struct_Quant), DCELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 484
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_get_neg_infinite_rule'):
    Rast_quant_get_neg_infinite_rule = _libs['grass_raster.7.0.svn'].Rast_quant_get_neg_infinite_rule
    Rast_quant_get_neg_infinite_rule.restype = c_int
    Rast_quant_get_neg_infinite_rule.argtypes = [POINTER(struct_Quant), POINTER(DCELL), POINTER(CELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 485
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_set_pos_infinite_rule'):
    Rast_quant_set_pos_infinite_rule = _libs['grass_raster.7.0.svn'].Rast_quant_set_pos_infinite_rule
    Rast_quant_set_pos_infinite_rule.restype = None
    Rast_quant_set_pos_infinite_rule.argtypes = [POINTER(struct_Quant), DCELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 486
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_get_pos_infinite_rule'):
    Rast_quant_get_pos_infinite_rule = _libs['grass_raster.7.0.svn'].Rast_quant_get_pos_infinite_rule
    Rast_quant_get_pos_infinite_rule.restype = c_int
    Rast_quant_get_pos_infinite_rule.argtypes = [POINTER(struct_Quant), POINTER(DCELL), POINTER(CELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 487
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_add_rule'):
    Rast_quant_add_rule = _libs['grass_raster.7.0.svn'].Rast_quant_add_rule
    Rast_quant_add_rule.restype = None
    Rast_quant_add_rule.argtypes = [POINTER(struct_Quant), DCELL, DCELL, CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 488
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_reverse_rule_order'):
    Rast_quant_reverse_rule_order = _libs['grass_raster.7.0.svn'].Rast_quant_reverse_rule_order
    Rast_quant_reverse_rule_order.restype = None
    Rast_quant_reverse_rule_order.argtypes = [POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 489
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_get_cell_value'):
    Rast_quant_get_cell_value = _libs['grass_raster.7.0.svn'].Rast_quant_get_cell_value
    Rast_quant_get_cell_value.restype = CELL
    Rast_quant_get_cell_value.argtypes = [POINTER(struct_Quant), DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 490
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_perform_d'):
    Rast_quant_perform_d = _libs['grass_raster.7.0.svn'].Rast_quant_perform_d
    Rast_quant_perform_d.restype = None
    Rast_quant_perform_d.argtypes = [POINTER(struct_Quant), POINTER(DCELL), POINTER(CELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 491
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quant_perform_f'):
    Rast_quant_perform_f = _libs['grass_raster.7.0.svn'].Rast_quant_perform_f
    Rast_quant_perform_f.restype = None
    Rast_quant_perform_f.argtypes = [POINTER(struct_Quant), POINTER(FCELL), POINTER(CELL), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 492
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__quant_get_rule_for_d_raster_val'):
    Rast__quant_get_rule_for_d_raster_val = _libs['grass_raster.7.0.svn'].Rast__quant_get_rule_for_d_raster_val
    Rast__quant_get_rule_for_d_raster_val.restype = POINTER(struct_Quant_table)
    Rast__quant_get_rule_for_d_raster_val.argtypes = [POINTER(struct_Quant), DCELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 496
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__quant_import'):
    Rast__quant_import = _libs['grass_raster.7.0.svn'].Rast__quant_import
    Rast__quant_import.restype = c_int
    Rast__quant_import.argtypes = [String, String, POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 497
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__quant_export'):
    Rast__quant_export = _libs['grass_raster.7.0.svn'].Rast__quant_export
    Rast__quant_export.restype = c_int
    Rast__quant_export.argtypes = [String, String, POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 500
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_truncate_fp_map'):
    Rast_truncate_fp_map = _libs['grass_raster.7.0.svn'].Rast_truncate_fp_map
    Rast_truncate_fp_map.restype = None
    Rast_truncate_fp_map.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 501
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_round_fp_map'):
    Rast_round_fp_map = _libs['grass_raster.7.0.svn'].Rast_round_fp_map
    Rast_round_fp_map.restype = None
    Rast_round_fp_map.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 502
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quantize_fp_map'):
    Rast_quantize_fp_map = _libs['grass_raster.7.0.svn'].Rast_quantize_fp_map
    Rast_quantize_fp_map.restype = None
    Rast_quantize_fp_map.argtypes = [String, String, CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 503
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_quantize_fp_map_range'):
    Rast_quantize_fp_map_range = _libs['grass_raster.7.0.svn'].Rast_quantize_fp_map_range
    Rast_quantize_fp_map_range.restype = None
    Rast_quantize_fp_map_range.argtypes = [String, String, DCELL, DCELL, CELL, CELL]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 505
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_quant'):
    Rast_write_quant = _libs['grass_raster.7.0.svn'].Rast_write_quant
    Rast_write_quant.restype = None
    Rast_write_quant.argtypes = [String, String, POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 506
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_quant'):
    Rast_read_quant = _libs['grass_raster.7.0.svn'].Rast_read_quant
    Rast_read_quant.restype = c_int
    Rast_read_quant.argtypes = [String, String, POINTER(struct_Quant)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 509
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__remove_fp_range'):
    Rast__remove_fp_range = _libs['grass_raster.7.0.svn'].Rast__remove_fp_range
    Rast__remove_fp_range.restype = None
    Rast__remove_fp_range.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 510
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_construct_default_range'):
    Rast_construct_default_range = _libs['grass_raster.7.0.svn'].Rast_construct_default_range
    Rast_construct_default_range.restype = None
    Rast_construct_default_range.argtypes = [POINTER(struct_Range)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 511
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_fp_range'):
    Rast_read_fp_range = _libs['grass_raster.7.0.svn'].Rast_read_fp_range
    Rast_read_fp_range.restype = c_int
    Rast_read_fp_range.argtypes = [String, String, POINTER(struct_FPRange)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 512
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_range'):
    Rast_read_range = _libs['grass_raster.7.0.svn'].Rast_read_range
    Rast_read_range.restype = c_int
    Rast_read_range.argtypes = [String, String, POINTER(struct_Range)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 513
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_range'):
    Rast_write_range = _libs['grass_raster.7.0.svn'].Rast_write_range
    Rast_write_range.restype = None
    Rast_write_range.argtypes = [String, POINTER(struct_Range)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 514
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_fp_range'):
    Rast_write_fp_range = _libs['grass_raster.7.0.svn'].Rast_write_fp_range
    Rast_write_fp_range.restype = None
    Rast_write_fp_range.argtypes = [String, POINTER(struct_FPRange)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 515
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_update_range'):
    Rast_update_range = _libs['grass_raster.7.0.svn'].Rast_update_range
    Rast_update_range.restype = None
    Rast_update_range.argtypes = [CELL, POINTER(struct_Range)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 516
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_update_fp_range'):
    Rast_update_fp_range = _libs['grass_raster.7.0.svn'].Rast_update_fp_range
    Rast_update_fp_range.restype = None
    Rast_update_fp_range.argtypes = [DCELL, POINTER(struct_FPRange)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 517
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_row_update_range'):
    Rast_row_update_range = _libs['grass_raster.7.0.svn'].Rast_row_update_range
    Rast_row_update_range.restype = None
    Rast_row_update_range.argtypes = [POINTER(CELL), c_int, POINTER(struct_Range)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 518
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__row_update_range'):
    Rast__row_update_range = _libs['grass_raster.7.0.svn'].Rast__row_update_range
    Rast__row_update_range.restype = None
    Rast__row_update_range.argtypes = [POINTER(CELL), c_int, POINTER(struct_Range), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 519
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_row_update_fp_range'):
    Rast_row_update_fp_range = _libs['grass_raster.7.0.svn'].Rast_row_update_fp_range
    Rast_row_update_fp_range.restype = None
    Rast_row_update_fp_range.argtypes = [POINTER(None), c_int, POINTER(struct_FPRange), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 521
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_init_range'):
    Rast_init_range = _libs['grass_raster.7.0.svn'].Rast_init_range
    Rast_init_range.restype = None
    Rast_init_range.argtypes = [POINTER(struct_Range)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 522
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_range_min_max'):
    Rast_get_range_min_max = _libs['grass_raster.7.0.svn'].Rast_get_range_min_max
    Rast_get_range_min_max.restype = None
    Rast_get_range_min_max.argtypes = [POINTER(struct_Range), POINTER(CELL), POINTER(CELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 523
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_init_fp_range'):
    Rast_init_fp_range = _libs['grass_raster.7.0.svn'].Rast_init_fp_range
    Rast_init_fp_range.restype = None
    Rast_init_fp_range.argtypes = [POINTER(struct_FPRange)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 524
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_fp_range_min_max'):
    Rast_get_fp_range_min_max = _libs['grass_raster.7.0.svn'].Rast_get_fp_range_min_max
    Rast_get_fp_range_min_max.restype = None
    Rast_get_fp_range_min_max.argtypes = [POINTER(struct_FPRange), POINTER(DCELL), POINTER(DCELL)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 527
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_raster_cmp'):
    Rast_raster_cmp = _libs['grass_raster.7.0.svn'].Rast_raster_cmp
    Rast_raster_cmp.restype = c_int
    Rast_raster_cmp.argtypes = [POINTER(None), POINTER(None), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 528
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_raster_cpy'):
    Rast_raster_cpy = _libs['grass_raster.7.0.svn'].Rast_raster_cpy
    Rast_raster_cpy.restype = None
    Rast_raster_cpy.argtypes = [POINTER(None), POINTER(None), c_int, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 529
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_c_value'):
    Rast_set_c_value = _libs['grass_raster.7.0.svn'].Rast_set_c_value
    Rast_set_c_value.restype = None
    Rast_set_c_value.argtypes = [POINTER(None), CELL, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 530
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_f_value'):
    Rast_set_f_value = _libs['grass_raster.7.0.svn'].Rast_set_f_value
    Rast_set_f_value.restype = None
    Rast_set_f_value.argtypes = [POINTER(None), FCELL, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 531
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_d_value'):
    Rast_set_d_value = _libs['grass_raster.7.0.svn'].Rast_set_d_value
    Rast_set_d_value.restype = None
    Rast_set_d_value.argtypes = [POINTER(None), DCELL, RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 532
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_c_value'):
    Rast_get_c_value = _libs['grass_raster.7.0.svn'].Rast_get_c_value
    Rast_get_c_value.restype = CELL
    Rast_get_c_value.argtypes = [POINTER(None), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 533
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_f_value'):
    Rast_get_f_value = _libs['grass_raster.7.0.svn'].Rast_get_f_value
    Rast_get_f_value.restype = FCELL
    Rast_get_f_value.argtypes = [POINTER(None), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 534
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_d_value'):
    Rast_get_d_value = _libs['grass_raster.7.0.svn'].Rast_get_d_value
    Rast_get_d_value.restype = DCELL
    Rast_get_d_value.argtypes = [POINTER(None), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 537
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_units'):
    Rast_read_units = _libs['grass_raster.7.0.svn'].Rast_read_units
    Rast_read_units.restype = ReturnString
    Rast_read_units.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 538
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_read_vdatum'):
    Rast_read_vdatum = _libs['grass_raster.7.0.svn'].Rast_read_vdatum
    Rast_read_vdatum.restype = ReturnString
    Rast_read_vdatum.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 539
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_units'):
    Rast_write_units = _libs['grass_raster.7.0.svn'].Rast_write_units
    Rast_write_units.restype = None
    Rast_write_units.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 540
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_write_vdatum'):
    Rast_write_vdatum = _libs['grass_raster.7.0.svn'].Rast_write_vdatum
    Rast_write_vdatum.restype = None
    Rast_write_vdatum.argtypes = [String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 543
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_is_reclass'):
    Rast_is_reclass = _libs['grass_raster.7.0.svn'].Rast_is_reclass
    Rast_is_reclass.restype = c_int
    Rast_is_reclass.argtypes = [String, String, String, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 544
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_is_reclassed_to'):
    Rast_is_reclassed_to = _libs['grass_raster.7.0.svn'].Rast_is_reclassed_to
    Rast_is_reclassed_to.restype = c_int
    Rast_is_reclassed_to.argtypes = [String, String, POINTER(c_int), POINTER(POINTER(POINTER(c_char)))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 545
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_reclass'):
    Rast_get_reclass = _libs['grass_raster.7.0.svn'].Rast_get_reclass
    Rast_get_reclass.restype = c_int
    Rast_get_reclass.argtypes = [String, String, POINTER(struct_Reclass)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 546
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_free_reclass'):
    Rast_free_reclass = _libs['grass_raster.7.0.svn'].Rast_free_reclass
    Rast_free_reclass.restype = None
    Rast_free_reclass.argtypes = [POINTER(struct_Reclass)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 547
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_put_reclass'):
    Rast_put_reclass = _libs['grass_raster.7.0.svn'].Rast_put_reclass
    Rast_put_reclass.restype = c_int
    Rast_put_reclass.argtypes = [String, POINTER(struct_Reclass)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 550
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_sample_nearest'):
    Rast_get_sample_nearest = _libs['grass_raster.7.0.svn'].Rast_get_sample_nearest
    Rast_get_sample_nearest.restype = DCELL
    Rast_get_sample_nearest.argtypes = [c_int, POINTER(struct_Cell_head), POINTER(struct_Categories), c_double, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 551
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_sample_bilinear'):
    Rast_get_sample_bilinear = _libs['grass_raster.7.0.svn'].Rast_get_sample_bilinear
    Rast_get_sample_bilinear.restype = DCELL
    Rast_get_sample_bilinear.argtypes = [c_int, POINTER(struct_Cell_head), POINTER(struct_Categories), c_double, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 552
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_sample_cubic'):
    Rast_get_sample_cubic = _libs['grass_raster.7.0.svn'].Rast_get_sample_cubic
    Rast_get_sample_cubic.restype = DCELL
    Rast_get_sample_cubic.argtypes = [c_int, POINTER(struct_Cell_head), POINTER(struct_Categories), c_double, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 553
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_sample'):
    Rast_get_sample = _libs['grass_raster.7.0.svn'].Rast_get_sample
    Rast_get_sample.restype = DCELL
    Rast_get_sample.argtypes = [c_int, POINTER(struct_Cell_head), POINTER(struct_Categories), c_double, c_double, c_int, INTERP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 556
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__init_window'):
    Rast__init_window = _libs['grass_raster.7.0.svn'].Rast__init_window
    Rast__init_window.restype = None
    Rast__init_window.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 557
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_window'):
    Rast_set_window = _libs['grass_raster.7.0.svn'].Rast_set_window
    Rast_set_window.restype = None
    Rast_set_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 558
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_unset_window'):
    Rast_unset_window = _libs['grass_raster.7.0.svn'].Rast_unset_window
    Rast_unset_window.restype = None
    Rast_unset_window.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 559
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_output_window'):
    Rast_set_output_window = _libs['grass_raster.7.0.svn'].Rast_set_output_window
    Rast_set_output_window.restype = None
    Rast_set_output_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 560
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_set_input_window'):
    Rast_set_input_window = _libs['grass_raster.7.0.svn'].Rast_set_input_window
    Rast_set_input_window.restype = None
    Rast_set_input_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 563
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_window'):
    Rast_get_window = _libs['grass_raster.7.0.svn'].Rast_get_window
    Rast_get_window.restype = None
    Rast_get_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 564
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_input_window'):
    Rast_get_input_window = _libs['grass_raster.7.0.svn'].Rast_get_input_window
    Rast_get_input_window.restype = None
    Rast_get_input_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 565
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_get_output_window'):
    Rast_get_output_window = _libs['grass_raster.7.0.svn'].Rast_get_output_window
    Rast_get_output_window.restype = None
    Rast_get_output_window.argtypes = [POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 566
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_window_rows'):
    Rast_window_rows = _libs['grass_raster.7.0.svn'].Rast_window_rows
    Rast_window_rows.restype = c_int
    Rast_window_rows.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 567
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_window_cols'):
    Rast_window_cols = _libs['grass_raster.7.0.svn'].Rast_window_cols
    Rast_window_cols.restype = c_int
    Rast_window_cols.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 568
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_input_window_rows'):
    Rast_input_window_rows = _libs['grass_raster.7.0.svn'].Rast_input_window_rows
    Rast_input_window_rows.restype = c_int
    Rast_input_window_rows.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 569
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_input_window_cols'):
    Rast_input_window_cols = _libs['grass_raster.7.0.svn'].Rast_input_window_cols
    Rast_input_window_cols.restype = c_int
    Rast_input_window_cols.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 570
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_output_window_rows'):
    Rast_output_window_rows = _libs['grass_raster.7.0.svn'].Rast_output_window_rows
    Rast_output_window_rows.restype = c_int
    Rast_output_window_rows.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 571
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_output_window_cols'):
    Rast_output_window_cols = _libs['grass_raster.7.0.svn'].Rast_output_window_cols
    Rast_output_window_cols.restype = c_int
    Rast_output_window_cols.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 572
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_northing_to_row'):
    Rast_northing_to_row = _libs['grass_raster.7.0.svn'].Rast_northing_to_row
    Rast_northing_to_row.restype = c_double
    Rast_northing_to_row.argtypes = [c_double, POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 573
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_easting_to_col'):
    Rast_easting_to_col = _libs['grass_raster.7.0.svn'].Rast_easting_to_col
    Rast_easting_to_col.restype = c_double
    Rast_easting_to_col.argtypes = [c_double, POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 574
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_row_to_northing'):
    Rast_row_to_northing = _libs['grass_raster.7.0.svn'].Rast_row_to_northing
    Rast_row_to_northing.restype = c_double
    Rast_row_to_northing.argtypes = [c_double, POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 575
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_col_to_easting'):
    Rast_col_to_easting = _libs['grass_raster.7.0.svn'].Rast_col_to_easting
    Rast_col_to_easting.restype = c_double
    Rast_col_to_easting.argtypes = [c_double, POINTER(struct_Cell_head)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 578
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast__create_window_mapping'):
    Rast__create_window_mapping = _libs['grass_raster.7.0.svn'].Rast__create_window_mapping
    Rast__create_window_mapping.restype = None
    Rast__create_window_mapping.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 579
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_row_repeat_nomask'):
    Rast_row_repeat_nomask = _libs['grass_raster.7.0.svn'].Rast_row_repeat_nomask
    Rast_row_repeat_nomask.restype = c_int
    Rast_row_repeat_nomask.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 582
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_zero_buf'):
    Rast_zero_buf = _libs['grass_raster.7.0.svn'].Rast_zero_buf
    Rast_zero_buf.restype = None
    Rast_zero_buf.argtypes = [POINTER(None), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 583
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_zero_input_buf'):
    Rast_zero_input_buf = _libs['grass_raster.7.0.svn'].Rast_zero_input_buf
    Rast_zero_input_buf.restype = None
    Rast_zero_input_buf.argtypes = [POINTER(None), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 584
if hasattr(_libs['grass_raster.7.0.svn'], 'Rast_zero_output_buf'):
    Rast_zero_output_buf = _libs['grass_raster.7.0.svn'].Rast_zero_output_buf
    Rast_zero_output_buf.restype = None
    Rast_zero_output_buf.argtypes = [POINTER(None), RASTER_MAP_TYPE]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 7
try:
    RECLASS_TABLE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 7
try:
    RECLASS_RULES = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 7
try:
    RECLASS_SCALE = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 8
try:
    CELL_TYPE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 8
try:
    FCELL_TYPE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 8
try:
    DCELL_TYPE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 10
try:
    UNKNOWN = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 10
try:
    NEAREST = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 10
try:
    BILINEAR = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 10
try:
    CUBIC = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 223
try:
    RGBA_COLOR_OPAQUE = 255
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 223
try:
    RGBA_COLOR_TRANSPARENT = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 223
try:
    RGBA_COLOR_NONE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 404
def Rast_is_c_null_value(cellVal):
    return ((cellVal[0]) == 2147483648)

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 405
def Rast_is_f_null_value(fcellVal):
    return ((fcellVal[0]) != (fcellVal[0]))

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/rasterdefs.h: 406
def Rast_is_d_null_value(dcellVal):
    return ((dcellVal[0]) != (dcellVal[0]))

Reclass = struct_Reclass # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 28

FPReclass_table = struct_FPReclass_table # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 39

FPReclass = struct_FPReclass # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 49

Quant_table = struct_Quant_table # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 73

Quant = struct_Quant # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 81

Categories = struct_Categories # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 124

History = struct_History # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 164

Cell_stats_node = struct_Cell_stats_node # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 173

Cell_stats = struct_Cell_stats # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 171

Histogram_list = struct_Histogram_list # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 192

Histogram = struct_Histogram # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 188

Range = struct_Range # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 199

FPRange = struct_FPRange # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 206

FP_stats = struct_FP_stats # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 213

GDAL_link = struct_GDAL_link # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/raster.h: 223

# No inserted files

