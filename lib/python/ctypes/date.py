'''Wrapper for datetime.h

Generated with:
./ctypesgen.py --cpp gcc -E  -D_FILE_OFFSET_BITS=64     -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -I/home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_datetime.7.0.svn /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h -o date.py

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

_libs["grass_datetime.7.0.svn"] = load_library("grass_datetime.7.0.svn")

# 1 libraries
# End libraries

# No modules

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

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 6
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_is_between'):
    datetime_is_between = _libs['grass_datetime.7.0.svn'].datetime_is_between
    datetime_is_between.restype = c_int
    datetime_is_between.argtypes = [c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 9
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_change_from_to'):
    datetime_change_from_to = _libs['grass_datetime.7.0.svn'].datetime_change_from_to
    datetime_change_from_to.restype = c_int
    datetime_change_from_to.argtypes = [POINTER(DateTime), c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 12
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_copy'):
    datetime_copy = _libs['grass_datetime.7.0.svn'].datetime_copy
    datetime_copy.restype = None
    datetime_copy.argtypes = [POINTER(DateTime), POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 15
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_difference'):
    datetime_difference = _libs['grass_datetime.7.0.svn'].datetime_difference
    datetime_difference.restype = c_int
    datetime_difference.argtypes = [POINTER(DateTime), POINTER(DateTime), POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 19
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_error'):
    datetime_error = _libs['grass_datetime.7.0.svn'].datetime_error
    datetime_error.restype = c_int
    datetime_error.argtypes = [c_int, String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 20
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_error_code'):
    datetime_error_code = _libs['grass_datetime.7.0.svn'].datetime_error_code
    datetime_error_code.restype = c_int
    datetime_error_code.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 21
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_error_msg'):
    datetime_error_msg = _libs['grass_datetime.7.0.svn'].datetime_error_msg
    datetime_error_msg.restype = ReturnString
    datetime_error_msg.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 22
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_clear_error'):
    datetime_clear_error = _libs['grass_datetime.7.0.svn'].datetime_clear_error
    datetime_clear_error.restype = None
    datetime_clear_error.argtypes = []

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 25
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_format'):
    datetime_format = _libs['grass_datetime.7.0.svn'].datetime_format
    datetime_format.restype = c_int
    datetime_format.argtypes = [POINTER(DateTime), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 28
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_increment'):
    datetime_increment = _libs['grass_datetime.7.0.svn'].datetime_increment
    datetime_increment.restype = c_int
    datetime_increment.argtypes = [POINTER(DateTime), POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 31
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_is_valid_increment'):
    datetime_is_valid_increment = _libs['grass_datetime.7.0.svn'].datetime_is_valid_increment
    datetime_is_valid_increment.restype = c_int
    datetime_is_valid_increment.argtypes = [POINTER(DateTime), POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 32
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_check_increment'):
    datetime_check_increment = _libs['grass_datetime.7.0.svn'].datetime_check_increment
    datetime_check_increment.restype = c_int
    datetime_check_increment.argtypes = [POINTER(DateTime), POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 35
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_increment_type'):
    datetime_get_increment_type = _libs['grass_datetime.7.0.svn'].datetime_get_increment_type
    datetime_get_increment_type.restype = c_int
    datetime_get_increment_type.argtypes = [POINTER(DateTime), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 37
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_increment_type'):
    datetime_set_increment_type = _libs['grass_datetime.7.0.svn'].datetime_set_increment_type
    datetime_set_increment_type.restype = c_int
    datetime_set_increment_type.argtypes = [POINTER(DateTime), POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 40
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_local_timezone'):
    datetime_get_local_timezone = _libs['grass_datetime.7.0.svn'].datetime_get_local_timezone
    datetime_get_local_timezone.restype = c_int
    datetime_get_local_timezone.argtypes = [POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 41
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_local_time'):
    datetime_get_local_time = _libs['grass_datetime.7.0.svn'].datetime_get_local_time
    datetime_get_local_time.restype = None
    datetime_get_local_time.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 44
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_days_in_month'):
    datetime_days_in_month = _libs['grass_datetime.7.0.svn'].datetime_days_in_month
    datetime_days_in_month.restype = c_int
    datetime_days_in_month.argtypes = [c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 45
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_is_leap_year'):
    datetime_is_leap_year = _libs['grass_datetime.7.0.svn'].datetime_is_leap_year
    datetime_is_leap_year.restype = c_int
    datetime_is_leap_year.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 46
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_days_in_year'):
    datetime_days_in_year = _libs['grass_datetime.7.0.svn'].datetime_days_in_year
    datetime_days_in_year.restype = c_int
    datetime_days_in_year.argtypes = [c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 49
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_is_same'):
    datetime_is_same = _libs['grass_datetime.7.0.svn'].datetime_is_same
    datetime_is_same.restype = c_int
    datetime_is_same.argtypes = [POINTER(DateTime), POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 52
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_scan'):
    datetime_scan = _libs['grass_datetime.7.0.svn'].datetime_scan
    datetime_scan.restype = c_int
    datetime_scan.argtypes = [POINTER(DateTime), String]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 55
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_is_positive'):
    datetime_is_positive = _libs['grass_datetime.7.0.svn'].datetime_is_positive
    datetime_is_positive.restype = c_int
    datetime_is_positive.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 56
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_is_negative'):
    datetime_is_negative = _libs['grass_datetime.7.0.svn'].datetime_is_negative
    datetime_is_negative.restype = c_int
    datetime_is_negative.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 57
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_positive'):
    datetime_set_positive = _libs['grass_datetime.7.0.svn'].datetime_set_positive
    datetime_set_positive.restype = None
    datetime_set_positive.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 58
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_negative'):
    datetime_set_negative = _libs['grass_datetime.7.0.svn'].datetime_set_negative
    datetime_set_negative.restype = None
    datetime_set_negative.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 59
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_invert_sign'):
    datetime_invert_sign = _libs['grass_datetime.7.0.svn'].datetime_invert_sign
    datetime_invert_sign.restype = None
    datetime_invert_sign.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 62
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_type'):
    datetime_set_type = _libs['grass_datetime.7.0.svn'].datetime_set_type
    datetime_set_type.restype = c_int
    datetime_set_type.argtypes = [POINTER(DateTime), c_int, c_int, c_int, c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 63
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_type'):
    datetime_get_type = _libs['grass_datetime.7.0.svn'].datetime_get_type
    datetime_get_type.restype = c_int
    datetime_get_type.argtypes = [POINTER(DateTime), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 65
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_is_valid_type'):
    datetime_is_valid_type = _libs['grass_datetime.7.0.svn'].datetime_is_valid_type
    datetime_is_valid_type.restype = c_int
    datetime_is_valid_type.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 66
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_check_type'):
    datetime_check_type = _libs['grass_datetime.7.0.svn'].datetime_check_type
    datetime_check_type.restype = c_int
    datetime_check_type.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 67
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_in_interval_year_month'):
    datetime_in_interval_year_month = _libs['grass_datetime.7.0.svn'].datetime_in_interval_year_month
    datetime_in_interval_year_month.restype = c_int
    datetime_in_interval_year_month.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 68
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_in_interval_day_second'):
    datetime_in_interval_day_second = _libs['grass_datetime.7.0.svn'].datetime_in_interval_day_second
    datetime_in_interval_day_second.restype = c_int
    datetime_in_interval_day_second.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 69
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_is_absolute'):
    datetime_is_absolute = _libs['grass_datetime.7.0.svn'].datetime_is_absolute
    datetime_is_absolute.restype = c_int
    datetime_is_absolute.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 70
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_is_relative'):
    datetime_is_relative = _libs['grass_datetime.7.0.svn'].datetime_is_relative
    datetime_is_relative.restype = c_int
    datetime_is_relative.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 73
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_check_timezone'):
    datetime_check_timezone = _libs['grass_datetime.7.0.svn'].datetime_check_timezone
    datetime_check_timezone.restype = c_int
    datetime_check_timezone.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 74
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_timezone'):
    datetime_get_timezone = _libs['grass_datetime.7.0.svn'].datetime_get_timezone
    datetime_get_timezone.restype = c_int
    datetime_get_timezone.argtypes = [POINTER(DateTime), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 75
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_timezone'):
    datetime_set_timezone = _libs['grass_datetime.7.0.svn'].datetime_set_timezone
    datetime_set_timezone.restype = c_int
    datetime_set_timezone.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 76
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_unset_timezone'):
    datetime_unset_timezone = _libs['grass_datetime.7.0.svn'].datetime_unset_timezone
    datetime_unset_timezone.restype = c_int
    datetime_unset_timezone.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 77
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_is_valid_timezone'):
    datetime_is_valid_timezone = _libs['grass_datetime.7.0.svn'].datetime_is_valid_timezone
    datetime_is_valid_timezone.restype = c_int
    datetime_is_valid_timezone.argtypes = [c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 80
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_change_timezone'):
    datetime_change_timezone = _libs['grass_datetime.7.0.svn'].datetime_change_timezone
    datetime_change_timezone.restype = c_int
    datetime_change_timezone.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 81
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_change_to_utc'):
    datetime_change_to_utc = _libs['grass_datetime.7.0.svn'].datetime_change_to_utc
    datetime_change_to_utc.restype = c_int
    datetime_change_to_utc.argtypes = [POINTER(DateTime)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 82
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_decompose_timezone'):
    datetime_decompose_timezone = _libs['grass_datetime.7.0.svn'].datetime_decompose_timezone
    datetime_decompose_timezone.restype = None
    datetime_decompose_timezone.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 85
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_check_year'):
    datetime_check_year = _libs['grass_datetime.7.0.svn'].datetime_check_year
    datetime_check_year.restype = c_int
    datetime_check_year.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 86
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_check_month'):
    datetime_check_month = _libs['grass_datetime.7.0.svn'].datetime_check_month
    datetime_check_month.restype = c_int
    datetime_check_month.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 87
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_check_day'):
    datetime_check_day = _libs['grass_datetime.7.0.svn'].datetime_check_day
    datetime_check_day.restype = c_int
    datetime_check_day.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 88
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_check_hour'):
    datetime_check_hour = _libs['grass_datetime.7.0.svn'].datetime_check_hour
    datetime_check_hour.restype = c_int
    datetime_check_hour.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 89
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_check_minute'):
    datetime_check_minute = _libs['grass_datetime.7.0.svn'].datetime_check_minute
    datetime_check_minute.restype = c_int
    datetime_check_minute.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 90
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_check_second'):
    datetime_check_second = _libs['grass_datetime.7.0.svn'].datetime_check_second
    datetime_check_second.restype = c_int
    datetime_check_second.argtypes = [POINTER(DateTime), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 91
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_check_fracsec'):
    datetime_check_fracsec = _libs['grass_datetime.7.0.svn'].datetime_check_fracsec
    datetime_check_fracsec.restype = c_int
    datetime_check_fracsec.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 92
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_year'):
    datetime_get_year = _libs['grass_datetime.7.0.svn'].datetime_get_year
    datetime_get_year.restype = c_int
    datetime_get_year.argtypes = [POINTER(DateTime), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 93
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_year'):
    datetime_set_year = _libs['grass_datetime.7.0.svn'].datetime_set_year
    datetime_set_year.restype = c_int
    datetime_set_year.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 94
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_month'):
    datetime_get_month = _libs['grass_datetime.7.0.svn'].datetime_get_month
    datetime_get_month.restype = c_int
    datetime_get_month.argtypes = [POINTER(DateTime), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 95
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_month'):
    datetime_set_month = _libs['grass_datetime.7.0.svn'].datetime_set_month
    datetime_set_month.restype = c_int
    datetime_set_month.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 96
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_day'):
    datetime_get_day = _libs['grass_datetime.7.0.svn'].datetime_get_day
    datetime_get_day.restype = c_int
    datetime_get_day.argtypes = [POINTER(DateTime), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 97
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_day'):
    datetime_set_day = _libs['grass_datetime.7.0.svn'].datetime_set_day
    datetime_set_day.restype = c_int
    datetime_set_day.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 98
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_hour'):
    datetime_get_hour = _libs['grass_datetime.7.0.svn'].datetime_get_hour
    datetime_get_hour.restype = c_int
    datetime_get_hour.argtypes = [POINTER(DateTime), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 99
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_hour'):
    datetime_set_hour = _libs['grass_datetime.7.0.svn'].datetime_set_hour
    datetime_set_hour.restype = c_int
    datetime_set_hour.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 100
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_minute'):
    datetime_get_minute = _libs['grass_datetime.7.0.svn'].datetime_get_minute
    datetime_get_minute.restype = c_int
    datetime_get_minute.argtypes = [POINTER(DateTime), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 101
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_minute'):
    datetime_set_minute = _libs['grass_datetime.7.0.svn'].datetime_set_minute
    datetime_set_minute.restype = c_int
    datetime_set_minute.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 102
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_second'):
    datetime_get_second = _libs['grass_datetime.7.0.svn'].datetime_get_second
    datetime_get_second.restype = c_int
    datetime_get_second.argtypes = [POINTER(DateTime), POINTER(c_double)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 103
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_second'):
    datetime_set_second = _libs['grass_datetime.7.0.svn'].datetime_set_second
    datetime_set_second.restype = c_int
    datetime_set_second.argtypes = [POINTER(DateTime), c_double]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 104
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_get_fracsec'):
    datetime_get_fracsec = _libs['grass_datetime.7.0.svn'].datetime_get_fracsec
    datetime_get_fracsec.restype = c_int
    datetime_get_fracsec.argtypes = [POINTER(DateTime), POINTER(c_int)]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/P_datetime.h: 105
if hasattr(_libs['grass_datetime.7.0.svn'], 'datetime_set_fracsec'):
    datetime_set_fracsec = _libs['grass_datetime.7.0.svn'].datetime_set_fracsec
    datetime_set_fracsec.restype = c_int
    datetime_set_fracsec.argtypes = [POINTER(DateTime), c_int]

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 3
try:
    DATETIME_ABSOLUTE = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 3
try:
    DATETIME_RELATIVE = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 5
try:
    DATETIME_YEAR = 1
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 5
try:
    DATETIME_MONTH = 2
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 5
try:
    DATETIME_DAY = 3
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 5
try:
    DATETIME_HOUR = 4
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 5
try:
    DATETIME_MINUTE = 5
except:
    pass

# /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 5
try:
    DATETIME_SECOND = 6
except:
    pass

DateTime = struct_DateTime # /home/neteler/grass70/dist.x86_64-unknown-linux-gnu/include/grass/datetime.h: 25

# No inserted files

