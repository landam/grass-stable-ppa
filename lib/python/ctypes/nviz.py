'''Wrapper for nviz.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_nviz.7.0.svn /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h -o nviz.py

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

_libs["grass_nviz.7.0.svn"] = load_library("grass_nviz.7.0.svn")

# 1 libraries
# End libraries

# No modules

XID = c_ulong # /usr/include/X11/X.h: 66

Pixmap = XID # /usr/include/X11/X.h: 102

# /usr/include/X11/Xlib.h: 263
class struct__XDisplay(Structure):
    pass

Display = struct__XDisplay # /usr/include/X11/Xlib.h: 495

GLubyte = c_ubyte # /usr/include/GL/gl.h: 162

# /usr/include/GL/glx.h: 178
class struct___GLXcontextRec(Structure):
    pass

GLXContext = POINTER(struct___GLXcontextRec) # /usr/include/GL/glx.h: 178

GLXPixmap = XID # /usr/include/GL/glx.h: 179

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 73
class struct_anon_132(Structure):
    pass

struct_anon_132.__slots__ = [
    'id',
    'brt',
    'r',
    'g',
    'b',
    'ar',
    'ag',
    'ab',
    'x',
    'y',
    'z',
    'w',
]
struct_anon_132._fields_ = [
    ('id', c_int),
    ('brt', c_float),
    ('r', c_float),
    ('g', c_float),
    ('b', c_float),
    ('ar', c_float),
    ('ag', c_float),
    ('ab', c_float),
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('w', c_float),
]

light_data = struct_anon_132 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 73

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 75
class struct_fringe_data(Structure):
    pass

struct_fringe_data.__slots__ = [
    'id',
    'color',
    'elev',
    'where',
]
struct_fringe_data._fields_ = [
    ('id', c_int),
    ('color', c_ulong),
    ('elev', c_float),
    ('where', c_int * 4),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 83
class struct_arrow_data(Structure):
    pass

struct_arrow_data.__slots__ = [
    'color',
    'size',
    'where',
]
struct_arrow_data._fields_ = [
    ('color', c_ulong),
    ('size', c_float),
    ('where', c_float * 3),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 90
class struct_scalebar_data(Structure):
    pass

struct_scalebar_data.__slots__ = [
    'id',
    'color',
    'size',
    'where',
]
struct_scalebar_data._fields_ = [
    ('id', c_int),
    ('color', c_ulong),
    ('size', c_float),
    ('where', c_float * 3),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 127
class struct_anon_133(Structure):
    pass

struct_anon_133.__slots__ = [
    'zrange',
    'xyrange',
    'num_cplanes',
    'cur_cplane',
    'cp_on',
    'cp_trans',
    'cp_rot',
    'light',
    'num_fringes',
    'fringe',
    'draw_arrow',
    'arrow',
    'num_scalebars',
    'scalebar',
    'bgcolor',
]
struct_anon_133._fields_ = [
    ('zrange', c_float),
    ('xyrange', c_float),
    ('num_cplanes', c_int),
    ('cur_cplane', c_int),
    ('cp_on', c_int * 6),
    ('cp_trans', (c_float * 3) * 6),
    ('cp_rot', (c_float * 3) * 6),
    ('light', light_data * 3),
    ('num_fringes', c_int),
    ('fringe', POINTER(POINTER(struct_fringe_data))),
    ('draw_arrow', c_int),
    ('arrow', POINTER(struct_arrow_data)),
    ('num_scalebars', c_int),
    ('scalebar', POINTER(POINTER(struct_scalebar_data))),
    ('bgcolor', c_int),
]

nv_data = struct_anon_133 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 127

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 129
class struct_render_window(Structure):
    pass

struct_render_window.__slots__ = [
    'displayId',
    'contextId',
    'windowId',
    'pixmap',
]
struct_render_window._fields_ = [
    ('displayId', POINTER(Display)),
    ('contextId', GLXContext),
    ('windowId', GLXPixmap),
    ('pixmap', Pixmap),
]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 148
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_resize_window'):
    Nviz_resize_window = _libs['grass_nviz.7.0.svn'].Nviz_resize_window
    Nviz_resize_window.restype = c_int
    Nviz_resize_window.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 149
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_update_ranges'):
    Nviz_update_ranges = _libs['grass_nviz.7.0.svn'].Nviz_update_ranges
    Nviz_update_ranges.restype = c_int
    Nviz_update_ranges.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 150
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_viewpoint_position'):
    Nviz_set_viewpoint_position = _libs['grass_nviz.7.0.svn'].Nviz_set_viewpoint_position
    Nviz_set_viewpoint_position.restype = c_int
    Nviz_set_viewpoint_position.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 151
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_viewpoint_height'):
    Nviz_set_viewpoint_height = _libs['grass_nviz.7.0.svn'].Nviz_set_viewpoint_height
    Nviz_set_viewpoint_height.restype = c_int
    Nviz_set_viewpoint_height.argtypes = [c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 152
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_viewpoint_persp'):
    Nviz_set_viewpoint_persp = _libs['grass_nviz.7.0.svn'].Nviz_set_viewpoint_persp
    Nviz_set_viewpoint_persp.restype = c_int
    Nviz_set_viewpoint_persp.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 153
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_viewpoint_twist'):
    Nviz_set_viewpoint_twist = _libs['grass_nviz.7.0.svn'].Nviz_set_viewpoint_twist
    Nviz_set_viewpoint_twist.restype = c_int
    Nviz_set_viewpoint_twist.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 154
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_change_exag'):
    Nviz_change_exag = _libs['grass_nviz.7.0.svn'].Nviz_change_exag
    Nviz_change_exag.restype = c_int
    Nviz_change_exag.argtypes = [POINTER(nv_data), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 155
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_look_here'):
    Nviz_look_here = _libs['grass_nviz.7.0.svn'].Nviz_look_here
    Nviz_look_here.restype = c_int
    Nviz_look_here.argtypes = [c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 156
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_modelview'):
    Nviz_get_modelview = _libs['grass_nviz.7.0.svn'].Nviz_get_modelview
    Nviz_get_modelview.restype = None
    Nviz_get_modelview.argtypes = [POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 157
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_rotation'):
    Nviz_set_rotation = _libs['grass_nviz.7.0.svn'].Nviz_set_rotation
    Nviz_set_rotation.restype = None
    Nviz_set_rotation.argtypes = [c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 158
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_unset_rotation'):
    Nviz_unset_rotation = _libs['grass_nviz.7.0.svn'].Nviz_unset_rotation
    Nviz_unset_rotation.restype = None
    Nviz_unset_rotation.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 159
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_init_rotation'):
    Nviz_init_rotation = _libs['grass_nviz.7.0.svn'].Nviz_init_rotation
    Nviz_init_rotation.restype = None
    Nviz_init_rotation.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 162
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_new_cplane'):
    Nviz_new_cplane = _libs['grass_nviz.7.0.svn'].Nviz_new_cplane
    Nviz_new_cplane.restype = c_int
    Nviz_new_cplane.argtypes = [POINTER(nv_data), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 163
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_on_cplane'):
    Nviz_on_cplane = _libs['grass_nviz.7.0.svn'].Nviz_on_cplane
    Nviz_on_cplane.restype = c_int
    Nviz_on_cplane.argtypes = [POINTER(nv_data), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 164
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_off_cplane'):
    Nviz_off_cplane = _libs['grass_nviz.7.0.svn'].Nviz_off_cplane
    Nviz_off_cplane.restype = c_int
    Nviz_off_cplane.argtypes = [POINTER(nv_data), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 165
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_cplane'):
    Nviz_draw_cplane = _libs['grass_nviz.7.0.svn'].Nviz_draw_cplane
    Nviz_draw_cplane.restype = c_int
    Nviz_draw_cplane.argtypes = [POINTER(nv_data), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 166
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_num_cplanes'):
    Nviz_num_cplanes = _libs['grass_nviz.7.0.svn'].Nviz_num_cplanes
    Nviz_num_cplanes.restype = c_int
    Nviz_num_cplanes.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 167
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_current_cplane'):
    Nviz_get_current_cplane = _libs['grass_nviz.7.0.svn'].Nviz_get_current_cplane
    Nviz_get_current_cplane.restype = c_int
    Nviz_get_current_cplane.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 168
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_cplane_rotation'):
    Nviz_set_cplane_rotation = _libs['grass_nviz.7.0.svn'].Nviz_set_cplane_rotation
    Nviz_set_cplane_rotation.restype = c_int
    Nviz_set_cplane_rotation.argtypes = [POINTER(nv_data), c_int, c_float, c_float, c_float]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 169
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_cplane_rotation'):
    Nviz_get_cplane_rotation = _libs['grass_nviz.7.0.svn'].Nviz_get_cplane_rotation
    Nviz_get_cplane_rotation.restype = c_int
    Nviz_get_cplane_rotation.argtypes = [POINTER(nv_data), c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 170
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_cplane_translation'):
    Nviz_set_cplane_translation = _libs['grass_nviz.7.0.svn'].Nviz_set_cplane_translation
    Nviz_set_cplane_translation.restype = c_int
    Nviz_set_cplane_translation.argtypes = [POINTER(nv_data), c_int, c_float, c_float, c_float]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 171
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_cplane_translation'):
    Nviz_get_cplane_translation = _libs['grass_nviz.7.0.svn'].Nviz_get_cplane_translation
    Nviz_get_cplane_translation.restype = c_int
    Nviz_get_cplane_translation.argtypes = [POINTER(nv_data), c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 172
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_fence_color'):
    Nviz_set_fence_color = _libs['grass_nviz.7.0.svn'].Nviz_set_fence_color
    Nviz_set_fence_color.restype = c_int
    Nviz_set_fence_color.argtypes = [POINTER(nv_data), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 173
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_cplane_here'):
    Nviz_set_cplane_here = _libs['grass_nviz.7.0.svn'].Nviz_set_cplane_here
    Nviz_set_cplane_here.restype = c_int
    Nviz_set_cplane_here.argtypes = [POINTER(nv_data), c_int, c_float, c_float]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 177
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_all_surf'):
    Nviz_draw_all_surf = _libs['grass_nviz.7.0.svn'].Nviz_draw_all_surf
    Nviz_draw_all_surf.restype = c_int
    Nviz_draw_all_surf.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 178
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_all_vect'):
    Nviz_draw_all_vect = _libs['grass_nviz.7.0.svn'].Nviz_draw_all_vect
    Nviz_draw_all_vect.restype = c_int
    Nviz_draw_all_vect.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 179
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_all_site'):
    Nviz_draw_all_site = _libs['grass_nviz.7.0.svn'].Nviz_draw_all_site
    Nviz_draw_all_site.restype = c_int
    Nviz_draw_all_site.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 180
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_all_vol'):
    Nviz_draw_all_vol = _libs['grass_nviz.7.0.svn'].Nviz_draw_all_vol
    Nviz_draw_all_vol.restype = c_int
    Nviz_draw_all_vol.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 181
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_all'):
    Nviz_draw_all = _libs['grass_nviz.7.0.svn'].Nviz_draw_all
    Nviz_draw_all.restype = c_int
    Nviz_draw_all.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 182
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_quick'):
    Nviz_draw_quick = _libs['grass_nviz.7.0.svn'].Nviz_draw_quick
    Nviz_draw_quick.restype = c_int
    Nviz_draw_quick.argtypes = [POINTER(nv_data), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 183
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_load_image'):
    Nviz_load_image = _libs['grass_nviz.7.0.svn'].Nviz_load_image
    Nviz_load_image.restype = c_int
    Nviz_load_image.argtypes = [POINTER(GLubyte), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 184
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_image'):
    Nviz_draw_image = _libs['grass_nviz.7.0.svn'].Nviz_draw_image
    Nviz_draw_image.restype = None
    Nviz_draw_image.argtypes = [c_int, c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 185
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_2D'):
    Nviz_set_2D = _libs['grass_nviz.7.0.svn'].Nviz_set_2D
    Nviz_set_2D.restype = None
    Nviz_set_2D.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 186
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_del_texture'):
    Nviz_del_texture = _libs['grass_nviz.7.0.svn'].Nviz_del_texture
    Nviz_del_texture.restype = None
    Nviz_del_texture.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 187
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_max_texture'):
    Nviz_get_max_texture = _libs['grass_nviz.7.0.svn'].Nviz_get_max_texture
    Nviz_get_max_texture.restype = None
    Nviz_get_max_texture.argtypes = [POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 190
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_exag_height'):
    Nviz_get_exag_height = _libs['grass_nviz.7.0.svn'].Nviz_get_exag_height
    Nviz_get_exag_height.restype = c_int
    Nviz_get_exag_height.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 191
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_exag'):
    Nviz_get_exag = _libs['grass_nviz.7.0.svn'].Nviz_get_exag
    Nviz_get_exag.restype = c_double
    Nviz_get_exag.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 194
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_light_position'):
    Nviz_set_light_position = _libs['grass_nviz.7.0.svn'].Nviz_set_light_position
    Nviz_set_light_position.restype = c_int
    Nviz_set_light_position.argtypes = [POINTER(nv_data), c_int, c_double, c_double, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 195
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_light_bright'):
    Nviz_set_light_bright = _libs['grass_nviz.7.0.svn'].Nviz_set_light_bright
    Nviz_set_light_bright.restype = c_int
    Nviz_set_light_bright.argtypes = [POINTER(nv_data), c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 196
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_light_color'):
    Nviz_set_light_color = _libs['grass_nviz.7.0.svn'].Nviz_set_light_color
    Nviz_set_light_color.restype = c_int
    Nviz_set_light_color.argtypes = [POINTER(nv_data), c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 197
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_light_ambient'):
    Nviz_set_light_ambient = _libs['grass_nviz.7.0.svn'].Nviz_set_light_ambient
    Nviz_set_light_ambient.restype = c_int
    Nviz_set_light_ambient.argtypes = [POINTER(nv_data), c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 198
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_init_light'):
    Nviz_init_light = _libs['grass_nviz.7.0.svn'].Nviz_init_light
    Nviz_init_light.restype = c_int
    Nviz_init_light.argtypes = [POINTER(nv_data), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 199
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_new_light'):
    Nviz_new_light = _libs['grass_nviz.7.0.svn'].Nviz_new_light
    Nviz_new_light.restype = c_int
    Nviz_new_light.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 200
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_model'):
    Nviz_draw_model = _libs['grass_nviz.7.0.svn'].Nviz_draw_model
    Nviz_draw_model.restype = None
    Nviz_draw_model.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 203
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_new_map_obj'):
    Nviz_new_map_obj = _libs['grass_nviz.7.0.svn'].Nviz_new_map_obj
    Nviz_new_map_obj.restype = c_int
    Nviz_new_map_obj.argtypes = [c_int, String, c_double, POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 204
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_attr'):
    Nviz_set_attr = _libs['grass_nviz.7.0.svn'].Nviz_set_attr
    Nviz_set_attr.restype = c_int
    Nviz_set_attr.argtypes = [c_int, c_int, c_int, c_int, String, c_double, POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 205
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_surface_attr_default'):
    Nviz_set_surface_attr_default = _libs['grass_nviz.7.0.svn'].Nviz_set_surface_attr_default
    Nviz_set_surface_attr_default.restype = None
    Nviz_set_surface_attr_default.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 206
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_vpoint_attr_default'):
    Nviz_set_vpoint_attr_default = _libs['grass_nviz.7.0.svn'].Nviz_set_vpoint_attr_default
    Nviz_set_vpoint_attr_default.restype = c_int
    Nviz_set_vpoint_attr_default.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 207
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_volume_attr_default'):
    Nviz_set_volume_attr_default = _libs['grass_nviz.7.0.svn'].Nviz_set_volume_attr_default
    Nviz_set_volume_attr_default.restype = c_int
    Nviz_set_volume_attr_default.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 208
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_unset_attr'):
    Nviz_unset_attr = _libs['grass_nviz.7.0.svn'].Nviz_unset_attr
    Nviz_unset_attr.restype = c_int
    Nviz_unset_attr.argtypes = [c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 211
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_init_data'):
    Nviz_init_data = _libs['grass_nviz.7.0.svn'].Nviz_init_data
    Nviz_init_data.restype = None
    Nviz_init_data.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 212
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_destroy_data'):
    Nviz_destroy_data = _libs['grass_nviz.7.0.svn'].Nviz_destroy_data
    Nviz_destroy_data.restype = None
    Nviz_destroy_data.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 213
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_bgcolor'):
    Nviz_set_bgcolor = _libs['grass_nviz.7.0.svn'].Nviz_set_bgcolor
    Nviz_set_bgcolor.restype = None
    Nviz_set_bgcolor.argtypes = [POINTER(nv_data), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 214
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_bgcolor'):
    Nviz_get_bgcolor = _libs['grass_nviz.7.0.svn'].Nviz_get_bgcolor
    Nviz_get_bgcolor.restype = c_int
    Nviz_get_bgcolor.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 215
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_color_from_str'):
    Nviz_color_from_str = _libs['grass_nviz.7.0.svn'].Nviz_color_from_str
    Nviz_color_from_str.restype = c_int
    Nviz_color_from_str.argtypes = [String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 216
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_new_fringe'):
    Nviz_new_fringe = _libs['grass_nviz.7.0.svn'].Nviz_new_fringe
    Nviz_new_fringe.restype = POINTER(struct_fringe_data)
    Nviz_new_fringe.argtypes = [POINTER(nv_data), c_int, c_ulong, c_double, c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 218
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_fringe'):
    Nviz_set_fringe = _libs['grass_nviz.7.0.svn'].Nviz_set_fringe
    Nviz_set_fringe.restype = POINTER(struct_fringe_data)
    Nviz_set_fringe.argtypes = [POINTER(nv_data), c_int, c_ulong, c_double, c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 220
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_fringe'):
    Nviz_draw_fringe = _libs['grass_nviz.7.0.svn'].Nviz_draw_fringe
    Nviz_draw_fringe.restype = None
    Nviz_draw_fringe.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 221
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_arrow'):
    Nviz_draw_arrow = _libs['grass_nviz.7.0.svn'].Nviz_draw_arrow
    Nviz_draw_arrow.restype = c_int
    Nviz_draw_arrow.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 222
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_arrow'):
    Nviz_set_arrow = _libs['grass_nviz.7.0.svn'].Nviz_set_arrow
    Nviz_set_arrow.restype = c_int
    Nviz_set_arrow.argtypes = [POINTER(nv_data), c_int, c_int, c_float, c_uint]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 223
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_delete_arrow'):
    Nviz_delete_arrow = _libs['grass_nviz.7.0.svn'].Nviz_delete_arrow
    Nviz_delete_arrow.restype = None
    Nviz_delete_arrow.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 224
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_new_scalebar'):
    Nviz_new_scalebar = _libs['grass_nviz.7.0.svn'].Nviz_new_scalebar
    Nviz_new_scalebar.restype = POINTER(struct_scalebar_data)
    Nviz_new_scalebar.argtypes = [POINTER(nv_data), c_int, POINTER(c_float), c_float, c_uint]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 225
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_scalebar'):
    Nviz_set_scalebar = _libs['grass_nviz.7.0.svn'].Nviz_set_scalebar
    Nviz_set_scalebar.restype = POINTER(struct_scalebar_data)
    Nviz_set_scalebar.argtypes = [POINTER(nv_data), c_int, c_int, c_int, c_float, c_uint]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 226
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_draw_scalebar'):
    Nviz_draw_scalebar = _libs['grass_nviz.7.0.svn'].Nviz_draw_scalebar
    Nviz_draw_scalebar.restype = None
    Nviz_draw_scalebar.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 227
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_delete_scalebar'):
    Nviz_delete_scalebar = _libs['grass_nviz.7.0.svn'].Nviz_delete_scalebar
    Nviz_delete_scalebar.restype = None
    Nviz_delete_scalebar.argtypes = [POINTER(nv_data), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 230
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_init_view'):
    Nviz_init_view = _libs['grass_nviz.7.0.svn'].Nviz_init_view
    Nviz_init_view.restype = None
    Nviz_init_view.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 231
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_focus_state'):
    Nviz_set_focus_state = _libs['grass_nviz.7.0.svn'].Nviz_set_focus_state
    Nviz_set_focus_state.restype = c_int
    Nviz_set_focus_state.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 232
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_focus_map'):
    Nviz_set_focus_map = _libs['grass_nviz.7.0.svn'].Nviz_set_focus_map
    Nviz_set_focus_map.restype = c_int
    Nviz_set_focus_map.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 233
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_has_focus'):
    Nviz_has_focus = _libs['grass_nviz.7.0.svn'].Nviz_has_focus
    Nviz_has_focus.restype = c_int
    Nviz_has_focus.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 234
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_set_focus'):
    Nviz_set_focus = _libs['grass_nviz.7.0.svn'].Nviz_set_focus
    Nviz_set_focus.restype = c_int
    Nviz_set_focus.argtypes = [POINTER(nv_data), c_float, c_float, c_float]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 235
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_focus'):
    Nviz_get_focus = _libs['grass_nviz.7.0.svn'].Nviz_get_focus
    Nviz_get_focus.restype = c_int
    Nviz_get_focus.argtypes = [POINTER(nv_data), POINTER(c_float), POINTER(c_float), POINTER(c_float)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 236
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_xyrange'):
    Nviz_get_xyrange = _libs['grass_nviz.7.0.svn'].Nviz_get_xyrange
    Nviz_get_xyrange.restype = c_float
    Nviz_get_xyrange.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 237
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_zrange'):
    Nviz_get_zrange = _libs['grass_nviz.7.0.svn'].Nviz_get_zrange
    Nviz_get_zrange.restype = c_int
    Nviz_get_zrange.argtypes = [POINTER(nv_data), POINTER(c_float), POINTER(c_float)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 238
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_get_longdim'):
    Nviz_get_longdim = _libs['grass_nviz.7.0.svn'].Nviz_get_longdim
    Nviz_get_longdim.restype = c_float
    Nviz_get_longdim.argtypes = [POINTER(nv_data)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 241
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_new_render_window'):
    Nviz_new_render_window = _libs['grass_nviz.7.0.svn'].Nviz_new_render_window
    Nviz_new_render_window.restype = POINTER(struct_render_window)
    Nviz_new_render_window.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 242
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_init_render_window'):
    Nviz_init_render_window = _libs['grass_nviz.7.0.svn'].Nviz_init_render_window
    Nviz_init_render_window.restype = None
    Nviz_init_render_window.argtypes = [POINTER(struct_render_window)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 243
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_destroy_render_window'):
    Nviz_destroy_render_window = _libs['grass_nviz.7.0.svn'].Nviz_destroy_render_window
    Nviz_destroy_render_window.restype = None
    Nviz_destroy_render_window.argtypes = [POINTER(struct_render_window)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 244
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_create_render_window'):
    Nviz_create_render_window = _libs['grass_nviz.7.0.svn'].Nviz_create_render_window
    Nviz_create_render_window.restype = c_int
    Nviz_create_render_window.argtypes = [POINTER(struct_render_window), POINTER(None), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 245
if hasattr(_libs['grass_nviz.7.0.svn'], 'Nviz_make_current_render_window'):
    Nviz_make_current_render_window = _libs['grass_nviz.7.0.svn'].Nviz_make_current_render_window
    Nviz_make_current_render_window.restype = c_int
    Nviz_make_current_render_window.argtypes = [POINTER(struct_render_window)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gsurf.h: 16
try:
    GS_UNIT_SIZE = 1000.0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 39
try:
    MAP_OBJ_UNDEFINED = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 39
try:
    MAP_OBJ_SURF = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 39
try:
    MAP_OBJ_VOL = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 39
try:
    MAP_OBJ_VECT = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 39
try:
    MAP_OBJ_SITE = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 40
try:
    DRAW_COARSE = 0
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 40
try:
    DRAW_FINE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 40
try:
    DRAW_BOTH = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 42
try:
    DRAW_QUICK_SURFACE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 42
try:
    DRAW_QUICK_VLINES = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 42
try:
    DRAW_QUICK_VPOINTS = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 42
try:
    DRAW_QUICK_VOLUME = 8
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 43
try:
    RANGE = (5 * GS_UNIT_SIZE)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 43
try:
    RANGE_OFFSET = (2 * GS_UNIT_SIZE)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 43
try:
    ZRANGE = (3 * GS_UNIT_SIZE)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 43
try:
    ZRANGE_OFFSET = (1 * GS_UNIT_SIZE)
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 44
try:
    DEFAULT_SURF_COLOR = 3390463
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 45
try:
    FORMAT_PPM = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 45
try:
    FORMAT_TIF = 2
except:
    pass

fringe_data = struct_fringe_data # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 75

arrow_data = struct_arrow_data # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 83

scalebar_data = struct_scalebar_data # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 90

render_window = struct_render_window # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/nviz.h: 129

# No inserted files

