'''Wrapper for gmath.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_gmath.7.0.svn /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h -o gmath.py

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

_libs["grass_gmath.7.0.svn"] = load_library("grass_gmath.7.0.svn")

# 1 libraries
# End libraries

# No modules

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 50
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_alloc_vector'):
    G_alloc_vector = _libs['grass_gmath.7.0.svn'].G_alloc_vector
    G_alloc_vector.restype = POINTER(c_double)
    G_alloc_vector.argtypes = [c_size_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 51
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_alloc_matrix'):
    G_alloc_matrix = _libs['grass_gmath.7.0.svn'].G_alloc_matrix
    G_alloc_matrix.restype = POINTER(POINTER(c_double))
    G_alloc_matrix.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 52
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_alloc_fvector'):
    G_alloc_fvector = _libs['grass_gmath.7.0.svn'].G_alloc_fvector
    G_alloc_fvector.restype = POINTER(c_float)
    G_alloc_fvector.argtypes = [c_size_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 53
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_alloc_fmatrix'):
    G_alloc_fmatrix = _libs['grass_gmath.7.0.svn'].G_alloc_fmatrix
    G_alloc_fmatrix.restype = POINTER(POINTER(c_float))
    G_alloc_fmatrix.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 54
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_free_vector'):
    G_free_vector = _libs['grass_gmath.7.0.svn'].G_free_vector
    G_free_vector.restype = None
    G_free_vector.argtypes = [POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 55
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_free_matrix'):
    G_free_matrix = _libs['grass_gmath.7.0.svn'].G_free_matrix
    G_free_matrix.restype = None
    G_free_matrix.argtypes = [POINTER(POINTER(c_double))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 56
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_free_fvector'):
    G_free_fvector = _libs['grass_gmath.7.0.svn'].G_free_fvector
    G_free_fvector.restype = None
    G_free_fvector.argtypes = [POINTER(c_float)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 57
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_free_fmatrix'):
    G_free_fmatrix = _libs['grass_gmath.7.0.svn'].G_free_fmatrix
    G_free_fmatrix.restype = None
    G_free_fmatrix.argtypes = [POINTER(POINTER(c_float))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 60
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_alloc_ivector'):
    G_alloc_ivector = _libs['grass_gmath.7.0.svn'].G_alloc_ivector
    G_alloc_ivector.restype = POINTER(c_int)
    G_alloc_ivector.argtypes = [c_size_t]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 61
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_alloc_imatrix'):
    G_alloc_imatrix = _libs['grass_gmath.7.0.svn'].G_alloc_imatrix
    G_alloc_imatrix.restype = POINTER(POINTER(c_int))
    G_alloc_imatrix.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 62
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_free_ivector'):
    G_free_ivector = _libs['grass_gmath.7.0.svn'].G_free_ivector
    G_free_ivector.restype = None
    G_free_ivector.argtypes = [POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 63
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_free_imatrix'):
    G_free_imatrix = _libs['grass_gmath.7.0.svn'].G_free_imatrix
    G_free_imatrix.restype = None
    G_free_imatrix.argtypes = [POINTER(POINTER(c_int))]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 66
if hasattr(_libs['grass_gmath.7.0.svn'], 'fft'):
    fft = _libs['grass_gmath.7.0.svn'].fft
    fft.restype = c_int
    fft.argtypes = [c_int, POINTER(c_double) * 2, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 67
if hasattr(_libs['grass_gmath.7.0.svn'], 'fft2'):
    fft2 = _libs['grass_gmath.7.0.svn'].fft2
    fft2.restype = c_int
    fft2.argtypes = [c_int, POINTER(c_double * 2), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 70
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_rand_gauss'):
    G_math_rand_gauss = _libs['grass_gmath.7.0.svn'].G_math_rand_gauss
    G_math_rand_gauss.restype = c_double
    G_math_rand_gauss.argtypes = [c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 73
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_max_pow2'):
    G_math_max_pow2 = _libs['grass_gmath.7.0.svn'].G_math_max_pow2
    G_math_max_pow2.restype = c_long
    G_math_max_pow2.argtypes = [c_long]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 74
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_min_pow2'):
    G_math_min_pow2 = _libs['grass_gmath.7.0.svn'].G_math_min_pow2
    G_math_min_pow2.restype = c_long
    G_math_min_pow2.argtypes = [c_long]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 77
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_rand'):
    G_math_rand = _libs['grass_gmath.7.0.svn'].G_math_rand
    G_math_rand.restype = c_float
    G_math_rand.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 80
if hasattr(_libs['grass_gmath.7.0.svn'], 'del2g'):
    del2g = _libs['grass_gmath.7.0.svn'].del2g
    del2g.restype = c_int
    del2g.argtypes = [POINTER(c_double) * 2, c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 83
if hasattr(_libs['grass_gmath.7.0.svn'], 'getg'):
    getg = _libs['grass_gmath.7.0.svn'].getg
    getg.restype = c_int
    getg.argtypes = [c_double, POINTER(c_double) * 2, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 86
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_egvorder'):
    G_math_egvorder = _libs['grass_gmath.7.0.svn'].G_math_egvorder
    G_math_egvorder.restype = c_int
    G_math_egvorder.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_long]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 89
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_complex_mult'):
    G_math_complex_mult = _libs['grass_gmath.7.0.svn'].G_math_complex_mult
    G_math_complex_mult.restype = c_int
    G_math_complex_mult.argtypes = [POINTER(c_double) * 2, c_int, POINTER(c_double) * 2, c_int, POINTER(c_double) * 2, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 92
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_ludcmp'):
    G_ludcmp = _libs['grass_gmath.7.0.svn'].G_ludcmp
    G_ludcmp.restype = c_int
    G_ludcmp.argtypes = [POINTER(POINTER(c_double)), c_int, POINTER(c_int), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 93
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_lubksb'):
    G_lubksb = _libs['grass_gmath.7.0.svn'].G_lubksb
    G_lubksb.restype = None
    G_lubksb.argtypes = [POINTER(POINTER(c_double)), c_int, POINTER(c_int), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 96
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_findzc'):
    G_math_findzc = _libs['grass_gmath.7.0.svn'].G_math_findzc
    G_math_findzc.restype = c_int
    G_math_findzc.argtypes = [POINTER(c_double), c_int, POINTER(c_double), c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 102
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solv'):
    G_math_solv = _libs['grass_gmath.7.0.svn'].G_math_solv
    G_math_solv.restype = c_int
    G_math_solv.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 103
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solvps'):
    G_math_solvps = _libs['grass_gmath.7.0.svn'].G_math_solvps
    G_math_solvps.restype = c_int
    G_math_solvps.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 104
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solvtd'):
    G_math_solvtd = _libs['grass_gmath.7.0.svn'].G_math_solvtd
    G_math_solvtd.restype = None
    G_math_solvtd.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 105
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solvru'):
    G_math_solvru = _libs['grass_gmath.7.0.svn'].G_math_solvru
    G_math_solvru.restype = c_int
    G_math_solvru.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 106
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_minv'):
    G_math_minv = _libs['grass_gmath.7.0.svn'].G_math_minv
    G_math_minv.restype = c_int
    G_math_minv.argtypes = [POINTER(POINTER(c_double)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 107
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_psinv'):
    G_math_psinv = _libs['grass_gmath.7.0.svn'].G_math_psinv
    G_math_psinv.restype = c_int
    G_math_psinv.argtypes = [POINTER(POINTER(c_double)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 108
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_ruinv'):
    G_math_ruinv = _libs['grass_gmath.7.0.svn'].G_math_ruinv
    G_math_ruinv.restype = c_int
    G_math_ruinv.argtypes = [POINTER(POINTER(c_double)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 109
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_eigval'):
    G_math_eigval = _libs['grass_gmath.7.0.svn'].G_math_eigval
    G_math_eigval.restype = None
    G_math_eigval.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 110
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_eigen'):
    G_math_eigen = _libs['grass_gmath.7.0.svn'].G_math_eigen
    G_math_eigen.restype = None
    G_math_eigen.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 111
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_evmax'):
    G_math_evmax = _libs['grass_gmath.7.0.svn'].G_math_evmax
    G_math_evmax.restype = c_double
    G_math_evmax.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 112
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_svdval'):
    G_math_svdval = _libs['grass_gmath.7.0.svn'].G_math_svdval
    G_math_svdval.restype = c_int
    G_math_svdval.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 113
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_sv2val'):
    G_math_sv2val = _libs['grass_gmath.7.0.svn'].G_math_sv2val
    G_math_sv2val.restype = c_int
    G_math_sv2val.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 114
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_svduv'):
    G_math_svduv = _libs['grass_gmath.7.0.svn'].G_math_svduv
    G_math_svduv.restype = c_int
    G_math_svduv.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, POINTER(POINTER(c_double)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 115
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_sv2uv'):
    G_math_sv2uv = _libs['grass_gmath.7.0.svn'].G_math_sv2uv
    G_math_sv2uv.restype = c_int
    G_math_sv2uv.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, POINTER(POINTER(c_double)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 116
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_svdu1v'):
    G_math_svdu1v = _libs['grass_gmath.7.0.svn'].G_math_svdu1v
    G_math_svdu1v.restype = c_int
    G_math_svdu1v.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_int, POINTER(POINTER(c_double)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 131
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    'values',
    'cols',
    'index',
]
struct_anon_1._fields_ = [
    ('values', POINTER(c_double)),
    ('cols', c_uint),
    ('index', POINTER(c_uint)),
]

G_math_spvector = struct_anon_1 # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 131

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 135
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_alloc_spvector'):
    G_math_alloc_spvector = _libs['grass_gmath.7.0.svn'].G_math_alloc_spvector
    G_math_alloc_spvector.restype = POINTER(G_math_spvector)
    G_math_alloc_spvector.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 136
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_alloc_spmatrix'):
    G_math_alloc_spmatrix = _libs['grass_gmath.7.0.svn'].G_math_alloc_spmatrix
    G_math_alloc_spmatrix.restype = POINTER(POINTER(G_math_spvector))
    G_math_alloc_spmatrix.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 137
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_free_spmatrix'):
    G_math_free_spmatrix = _libs['grass_gmath.7.0.svn'].G_math_free_spmatrix
    G_math_free_spmatrix.restype = None
    G_math_free_spmatrix.argtypes = [POINTER(POINTER(G_math_spvector)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 138
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_free_spvector'):
    G_math_free_spvector = _libs['grass_gmath.7.0.svn'].G_math_free_spvector
    G_math_free_spvector.restype = None
    G_math_free_spvector.argtypes = [POINTER(G_math_spvector)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 139
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_add_spvector'):
    G_math_add_spvector = _libs['grass_gmath.7.0.svn'].G_math_add_spvector
    G_math_add_spvector.restype = c_int
    G_math_add_spvector.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(G_math_spvector), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 140
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_A_to_Asp'):
    G_math_A_to_Asp = _libs['grass_gmath.7.0.svn'].G_math_A_to_Asp
    G_math_A_to_Asp.restype = POINTER(POINTER(G_math_spvector))
    G_math_A_to_Asp.argtypes = [POINTER(POINTER(c_double)), c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 141
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_Asp_to_A'):
    G_math_Asp_to_A = _libs['grass_gmath.7.0.svn'].G_math_Asp_to_A
    G_math_Asp_to_A.restype = POINTER(POINTER(c_double))
    G_math_Asp_to_A.argtypes = [POINTER(POINTER(G_math_spvector)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 142
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_Asp_to_sband_matrix'):
    G_math_Asp_to_sband_matrix = _libs['grass_gmath.7.0.svn'].G_math_Asp_to_sband_matrix
    G_math_Asp_to_sband_matrix.restype = POINTER(POINTER(c_double))
    G_math_Asp_to_sband_matrix.argtypes = [POINTER(POINTER(G_math_spvector)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 143
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_sband_matrix_to_Asp'):
    G_math_sband_matrix_to_Asp = _libs['grass_gmath.7.0.svn'].G_math_sband_matrix_to_Asp
    G_math_sband_matrix_to_Asp.restype = POINTER(POINTER(G_math_spvector))
    G_math_sband_matrix_to_Asp.argtypes = [POINTER(POINTER(c_double)), c_int, c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 144
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_print_spmatrix'):
    G_math_print_spmatrix = _libs['grass_gmath.7.0.svn'].G_math_print_spmatrix
    G_math_print_spmatrix.restype = None
    G_math_print_spmatrix.argtypes = [POINTER(POINTER(G_math_spvector)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 145
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_Ax_sparse'):
    G_math_Ax_sparse = _libs['grass_gmath.7.0.svn'].G_math_Ax_sparse
    G_math_Ax_sparse.restype = None
    G_math_Ax_sparse.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 148
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_matrix_to_sband_matrix'):
    G_math_matrix_to_sband_matrix = _libs['grass_gmath.7.0.svn'].G_math_matrix_to_sband_matrix
    G_math_matrix_to_sband_matrix.restype = POINTER(POINTER(c_double))
    G_math_matrix_to_sband_matrix.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 149
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_sband_matrix_to_matrix'):
    G_math_sband_matrix_to_matrix = _libs['grass_gmath.7.0.svn'].G_math_sband_matrix_to_matrix
    G_math_sband_matrix_to_matrix.restype = POINTER(POINTER(c_double))
    G_math_sband_matrix_to_matrix.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 150
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_Ax_sband'):
    G_math_Ax_sband = _libs['grass_gmath.7.0.svn'].G_math_Ax_sband
    G_math_Ax_sband.restype = None
    G_math_Ax_sband.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 153
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_gauss'):
    G_math_solver_gauss = _libs['grass_gmath.7.0.svn'].G_math_solver_gauss
    G_math_solver_gauss.restype = c_int
    G_math_solver_gauss.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 154
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_lu'):
    G_math_solver_lu = _libs['grass_gmath.7.0.svn'].G_math_solver_lu
    G_math_solver_lu.restype = c_int
    G_math_solver_lu.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 155
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_cholesky'):
    G_math_solver_cholesky = _libs['grass_gmath.7.0.svn'].G_math_solver_cholesky
    G_math_solver_cholesky.restype = c_int
    G_math_solver_cholesky.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 156
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_cholesky_sband'):
    G_math_solver_cholesky_sband = _libs['grass_gmath.7.0.svn'].G_math_solver_cholesky_sband
    G_math_solver_cholesky_sband.restype = None
    G_math_solver_cholesky_sband.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 157
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_jacobi'):
    G_math_solver_jacobi = _libs['grass_gmath.7.0.svn'].G_math_solver_jacobi
    G_math_solver_jacobi.restype = c_int
    G_math_solver_jacobi.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 158
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_gs'):
    G_math_solver_gs = _libs['grass_gmath.7.0.svn'].G_math_solver_gs
    G_math_solver_gs.restype = c_int
    G_math_solver_gs.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 160
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_pcg'):
    G_math_solver_pcg = _libs['grass_gmath.7.0.svn'].G_math_solver_pcg
    G_math_solver_pcg.restype = c_int
    G_math_solver_pcg.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 161
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_cg'):
    G_math_solver_cg = _libs['grass_gmath.7.0.svn'].G_math_solver_cg
    G_math_solver_cg.restype = c_int
    G_math_solver_cg.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 162
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_cg_sband'):
    G_math_solver_cg_sband = _libs['grass_gmath.7.0.svn'].G_math_solver_cg_sband
    G_math_solver_cg_sband.restype = c_int
    G_math_solver_cg_sband.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 163
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_bicgstab'):
    G_math_solver_bicgstab = _libs['grass_gmath.7.0.svn'].G_math_solver_bicgstab
    G_math_solver_bicgstab.restype = c_int
    G_math_solver_bicgstab.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 164
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_sparse_jacobi'):
    G_math_solver_sparse_jacobi = _libs['grass_gmath.7.0.svn'].G_math_solver_sparse_jacobi
    G_math_solver_sparse_jacobi.restype = c_int
    G_math_solver_sparse_jacobi.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 165
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_sparse_gs'):
    G_math_solver_sparse_gs = _libs['grass_gmath.7.0.svn'].G_math_solver_sparse_gs
    G_math_solver_sparse_gs.restype = c_int
    G_math_solver_sparse_gs.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 166
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_sparse_pcg'):
    G_math_solver_sparse_pcg = _libs['grass_gmath.7.0.svn'].G_math_solver_sparse_pcg
    G_math_solver_sparse_pcg.restype = c_int
    G_math_solver_sparse_pcg.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 167
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_sparse_cg'):
    G_math_solver_sparse_cg = _libs['grass_gmath.7.0.svn'].G_math_solver_sparse_cg
    G_math_solver_sparse_cg.restype = c_int
    G_math_solver_sparse_cg.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 168
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_solver_sparse_bicgstab'):
    G_math_solver_sparse_bicgstab = _libs['grass_gmath.7.0.svn'].G_math_solver_sparse_bicgstab
    G_math_solver_sparse_bicgstab.restype = c_int
    G_math_solver_sparse_bicgstab.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 171
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_gauss_elimination'):
    G_math_gauss_elimination = _libs['grass_gmath.7.0.svn'].G_math_gauss_elimination
    G_math_gauss_elimination.restype = None
    G_math_gauss_elimination.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 172
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_lu_decomposition'):
    G_math_lu_decomposition = _libs['grass_gmath.7.0.svn'].G_math_lu_decomposition
    G_math_lu_decomposition.restype = None
    G_math_lu_decomposition.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 173
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_cholesky_decomposition'):
    G_math_cholesky_decomposition = _libs['grass_gmath.7.0.svn'].G_math_cholesky_decomposition
    G_math_cholesky_decomposition.restype = c_int
    G_math_cholesky_decomposition.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 174
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_cholesky_sband_decomposition'):
    G_math_cholesky_sband_decomposition = _libs['grass_gmath.7.0.svn'].G_math_cholesky_sband_decomposition
    G_math_cholesky_sband_decomposition.restype = None
    G_math_cholesky_sband_decomposition.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 175
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_backward_substitution'):
    G_math_backward_substitution = _libs['grass_gmath.7.0.svn'].G_math_backward_substitution
    G_math_backward_substitution.restype = None
    G_math_backward_substitution.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 176
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_forward_substitution'):
    G_math_forward_substitution = _libs['grass_gmath.7.0.svn'].G_math_forward_substitution
    G_math_forward_substitution.restype = None
    G_math_forward_substitution.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 177
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_cholesky_sband_substitution'):
    G_math_cholesky_sband_substitution = _libs['grass_gmath.7.0.svn'].G_math_cholesky_sband_substitution
    G_math_cholesky_sband_substitution.restype = None
    G_math_cholesky_sband_substitution.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 182
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_x_dot_y'):
    G_math_d_x_dot_y = _libs['grass_gmath.7.0.svn'].G_math_d_x_dot_y
    G_math_d_x_dot_y.restype = None
    G_math_d_x_dot_y.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 183
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_asum_norm'):
    G_math_d_asum_norm = _libs['grass_gmath.7.0.svn'].G_math_d_asum_norm
    G_math_d_asum_norm.restype = None
    G_math_d_asum_norm.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 184
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_euclid_norm'):
    G_math_d_euclid_norm = _libs['grass_gmath.7.0.svn'].G_math_d_euclid_norm
    G_math_d_euclid_norm.restype = None
    G_math_d_euclid_norm.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 185
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_max_norm'):
    G_math_d_max_norm = _libs['grass_gmath.7.0.svn'].G_math_d_max_norm
    G_math_d_max_norm.restype = None
    G_math_d_max_norm.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 186
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_ax_by'):
    G_math_d_ax_by = _libs['grass_gmath.7.0.svn'].G_math_d_ax_by
    G_math_d_ax_by.restype = None
    G_math_d_ax_by.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_double, c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 187
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_copy'):
    G_math_d_copy = _libs['grass_gmath.7.0.svn'].G_math_d_copy
    G_math_d_copy.restype = None
    G_math_d_copy.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 189
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_x_dot_y'):
    G_math_f_x_dot_y = _libs['grass_gmath.7.0.svn'].G_math_f_x_dot_y
    G_math_f_x_dot_y.restype = None
    G_math_f_x_dot_y.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 190
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_asum_norm'):
    G_math_f_asum_norm = _libs['grass_gmath.7.0.svn'].G_math_f_asum_norm
    G_math_f_asum_norm.restype = None
    G_math_f_asum_norm.argtypes = [POINTER(c_float), POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 191
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_euclid_norm'):
    G_math_f_euclid_norm = _libs['grass_gmath.7.0.svn'].G_math_f_euclid_norm
    G_math_f_euclid_norm.restype = None
    G_math_f_euclid_norm.argtypes = [POINTER(c_float), POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 192
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_max_norm'):
    G_math_f_max_norm = _libs['grass_gmath.7.0.svn'].G_math_f_max_norm
    G_math_f_max_norm.restype = None
    G_math_f_max_norm.argtypes = [POINTER(c_float), POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 193
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_ax_by'):
    G_math_f_ax_by = _libs['grass_gmath.7.0.svn'].G_math_f_ax_by
    G_math_f_ax_by.restype = None
    G_math_f_ax_by.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), c_float, c_float, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 194
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_copy'):
    G_math_f_copy = _libs['grass_gmath.7.0.svn'].G_math_f_copy
    G_math_f_copy.restype = None
    G_math_f_copy.argtypes = [POINTER(c_float), POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 196
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_i_x_dot_y'):
    G_math_i_x_dot_y = _libs['grass_gmath.7.0.svn'].G_math_i_x_dot_y
    G_math_i_x_dot_y.restype = None
    G_math_i_x_dot_y.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 197
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_i_asum_norm'):
    G_math_i_asum_norm = _libs['grass_gmath.7.0.svn'].G_math_i_asum_norm
    G_math_i_asum_norm.restype = None
    G_math_i_asum_norm.argtypes = [POINTER(c_int), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 198
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_i_euclid_norm'):
    G_math_i_euclid_norm = _libs['grass_gmath.7.0.svn'].G_math_i_euclid_norm
    G_math_i_euclid_norm.restype = None
    G_math_i_euclid_norm.argtypes = [POINTER(c_int), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 199
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_i_max_norm'):
    G_math_i_max_norm = _libs['grass_gmath.7.0.svn'].G_math_i_max_norm
    G_math_i_max_norm.restype = None
    G_math_i_max_norm.argtypes = [POINTER(c_int), POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 200
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_i_ax_by'):
    G_math_i_ax_by = _libs['grass_gmath.7.0.svn'].G_math_i_ax_by
    G_math_i_ax_by.restype = None
    G_math_i_ax_by.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 201
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_i_copy'):
    G_math_i_copy = _libs['grass_gmath.7.0.svn'].G_math_i_copy
    G_math_i_copy.restype = None
    G_math_i_copy.argtypes = [POINTER(c_int), POINTER(c_int), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 204
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_ddot'):
    G_math_ddot = _libs['grass_gmath.7.0.svn'].G_math_ddot
    G_math_ddot.restype = c_double
    G_math_ddot.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 205
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_sdot'):
    G_math_sdot = _libs['grass_gmath.7.0.svn'].G_math_sdot
    G_math_sdot.restype = c_float
    G_math_sdot.argtypes = [POINTER(c_float), POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 206
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_sdsdot'):
    G_math_sdsdot = _libs['grass_gmath.7.0.svn'].G_math_sdsdot
    G_math_sdsdot.restype = c_float
    G_math_sdsdot.argtypes = [POINTER(c_float), POINTER(c_float), c_float, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 207
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_dnrm2'):
    G_math_dnrm2 = _libs['grass_gmath.7.0.svn'].G_math_dnrm2
    G_math_dnrm2.restype = c_double
    G_math_dnrm2.argtypes = [POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 208
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_dasum'):
    G_math_dasum = _libs['grass_gmath.7.0.svn'].G_math_dasum
    G_math_dasum.restype = c_double
    G_math_dasum.argtypes = [POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 209
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_idamax'):
    G_math_idamax = _libs['grass_gmath.7.0.svn'].G_math_idamax
    G_math_idamax.restype = c_double
    G_math_idamax.argtypes = [POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 210
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_snrm2'):
    G_math_snrm2 = _libs['grass_gmath.7.0.svn'].G_math_snrm2
    G_math_snrm2.restype = c_float
    G_math_snrm2.argtypes = [POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 211
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_sasum'):
    G_math_sasum = _libs['grass_gmath.7.0.svn'].G_math_sasum
    G_math_sasum.restype = c_float
    G_math_sasum.argtypes = [POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 212
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_isamax'):
    G_math_isamax = _libs['grass_gmath.7.0.svn'].G_math_isamax
    G_math_isamax.restype = c_float
    G_math_isamax.argtypes = [POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 213
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_dscal'):
    G_math_dscal = _libs['grass_gmath.7.0.svn'].G_math_dscal
    G_math_dscal.restype = None
    G_math_dscal.argtypes = [POINTER(c_double), c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 214
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_sscal'):
    G_math_sscal = _libs['grass_gmath.7.0.svn'].G_math_sscal
    G_math_sscal.restype = None
    G_math_sscal.argtypes = [POINTER(c_float), c_float, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 215
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_dcopy'):
    G_math_dcopy = _libs['grass_gmath.7.0.svn'].G_math_dcopy
    G_math_dcopy.restype = None
    G_math_dcopy.argtypes = [POINTER(c_double), POINTER(c_double), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 216
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_scopy'):
    G_math_scopy = _libs['grass_gmath.7.0.svn'].G_math_scopy
    G_math_scopy.restype = None
    G_math_scopy.argtypes = [POINTER(c_float), POINTER(c_float), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 217
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_daxpy'):
    G_math_daxpy = _libs['grass_gmath.7.0.svn'].G_math_daxpy
    G_math_daxpy.restype = None
    G_math_daxpy.argtypes = [POINTER(c_double), POINTER(c_double), c_double, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 218
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_saxpy'):
    G_math_saxpy = _libs['grass_gmath.7.0.svn'].G_math_saxpy
    G_math_saxpy.restype = None
    G_math_saxpy.argtypes = [POINTER(c_float), POINTER(c_float), c_float, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 221
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_Ax'):
    G_math_d_Ax = _libs['grass_gmath.7.0.svn'].G_math_d_Ax
    G_math_d_Ax.restype = None
    G_math_d_Ax.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 222
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_Ax'):
    G_math_f_Ax = _libs['grass_gmath.7.0.svn'].G_math_f_Ax
    G_math_f_Ax.restype = None
    G_math_f_Ax.argtypes = [POINTER(POINTER(c_float)), POINTER(c_float), POINTER(c_float), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 223
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_x_dyad_y'):
    G_math_d_x_dyad_y = _libs['grass_gmath.7.0.svn'].G_math_d_x_dyad_y
    G_math_d_x_dyad_y.restype = None
    G_math_d_x_dyad_y.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(POINTER(c_double)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 224
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_x_dyad_y'):
    G_math_f_x_dyad_y = _libs['grass_gmath.7.0.svn'].G_math_f_x_dyad_y
    G_math_f_x_dyad_y.restype = None
    G_math_f_x_dyad_y.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(POINTER(c_float)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 225
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_aAx_by'):
    G_math_d_aAx_by = _libs['grass_gmath.7.0.svn'].G_math_d_aAx_by
    G_math_d_aAx_by.restype = None
    G_math_d_aAx_by.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_double, c_double, POINTER(c_double), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 226
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_aAx_by'):
    G_math_f_aAx_by = _libs['grass_gmath.7.0.svn'].G_math_f_aAx_by
    G_math_f_aAx_by.restype = None
    G_math_f_aAx_by.argtypes = [POINTER(POINTER(c_float)), POINTER(c_float), POINTER(c_float), c_float, c_float, POINTER(c_float), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 227
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_A_T'):
    G_math_d_A_T = _libs['grass_gmath.7.0.svn'].G_math_d_A_T
    G_math_d_A_T.restype = c_int
    G_math_d_A_T.argtypes = [POINTER(POINTER(c_double)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 228
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_A_T'):
    G_math_f_A_T = _libs['grass_gmath.7.0.svn'].G_math_f_A_T
    G_math_f_A_T.restype = c_int
    G_math_f_A_T.argtypes = [POINTER(POINTER(c_float)), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 231
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_aA_B'):
    G_math_d_aA_B = _libs['grass_gmath.7.0.svn'].G_math_d_aA_B
    G_math_d_aA_B.restype = None
    G_math_d_aA_B.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_double, POINTER(POINTER(c_double)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 232
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_aA_B'):
    G_math_f_aA_B = _libs['grass_gmath.7.0.svn'].G_math_f_aA_B
    G_math_f_aA_B.restype = None
    G_math_f_aA_B.argtypes = [POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), c_float, POINTER(POINTER(c_float)), c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 233
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_d_AB'):
    G_math_d_AB = _libs['grass_gmath.7.0.svn'].G_math_d_AB
    G_math_d_AB.restype = None
    G_math_d_AB.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 234
if hasattr(_libs['grass_gmath.7.0.svn'], 'G_math_f_AB'):
    G_math_f_AB = _libs['grass_gmath.7.0.svn'].G_math_f_AB
    G_math_f_AB.restype = None
    G_math_f_AB.argtypes = [POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 34
try:
    G_MATH_SOLVER_DIRECT_GAUSS = 'gauss'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 34
try:
    G_MATH_SOLVER_DIRECT_LU = 'lu'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 34
try:
    G_MATH_SOLVER_DIRECT_CHOLESKY = 'cholesky'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 34
try:
    G_MATH_SOLVER_ITERATIVE_JACOBI = 'jacobi'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 34
try:
    G_MATH_SOLVER_ITERATIVE_SOR = 'sor'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 34
try:
    G_MATH_SOLVER_ITERATIVE_CG = 'cg'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 34
try:
    G_MATH_SOLVER_ITERATIVE_PCG = 'pcg'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 34
try:
    G_MATH_SOLVER_ITERATIVE_BICGSTAB = 'bicgstab'
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 36
try:
    G_MATH_DIAGONAL_PRECONDITION = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 36
try:
    G_MATH_ROWSCALE_ABSSUMNORM_PRECONDITION = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 36
try:
    G_MATH_ROWSCALE_EUKLIDNORM_PRECONDITION = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/gmath.h: 36
try:
    G_MATH_ROWSCALE_MAXNORM_PRECONDITION = 4
except:
    pass

# No inserted files

