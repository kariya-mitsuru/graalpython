# Copyright (c) 2018, 2021, Oracle and/or its affiliates. All rights reserved.
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# The Universal Permissive License (UPL), Version 1.0
#
# Subject to the condition set forth below, permission is hereby granted to any
# person obtaining a copy of this software, associated documentation and/or
# data (collectively the "Software"), free of charge and under any and all
# copyright rights in the Software, and any and all patent rights owned or
# freely licensable by each licensor hereunder covering either (i) the
# unmodified Software as contributed to or provided by such licensor, or (ii)
# the Larger Works (as defined below), to deal in both
#
# (a) the Software, and
#
# (b) any piece of software and/or hardware listed in the lrgrwrks.txt file if
# one is included with the Software each a "Larger Work" to which the Software
# is contributed by such licensors),
#
# without restriction, including without limitation the rights to copy, create
# derivative works of, display, perform, and distribute the Software and make,
# use, sell, offer for sale, import, export, have made, and have sold the
# Software and the Larger Work(s), and to sublicense the foregoing rights on
# either these or other terms.
#
# This license is subject to the following condition:
#
# The above copyright notice and either this complete permission notice or at a
# minimum a reference to the UPL must be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# TODO lstat exception for graal_python_executable
# @__graalpython__.builtin
# def lstat(filename):
#     if not __graalpython__.is_native:
#         from sys import executable as graal_python_executable
#         if filename == graal_python_executable:
#             return stat_result((0,0,0,0,0,0,0,0,0,0))
#     return legacy_stat_result(old_stat(filename, False))


@__graalpython__.builtin
def fspath(path):
    """Return the file system path representation of the object.

    If the object is str or bytes, then allow it to pass through as-is. If the
    object defines __fspath__(), then return the result of that method. All other
    types raise a TypeError."""
    if isinstance(path, str) or isinstance(path, bytes):
        return path
    __fspath__ = getattr(path, "__fspath__", None)
    if __fspath__:
        return __fspath__()
    else:
        raise TypeError("expected str, bytes or os.PathLike object, not %r" % type(path))


@__graalpython__.builtin
def WIFSIGNALED(status):
    return status > 128


@__graalpython__.builtin
def WIFEXITED(status):
    return not WIFSIGNALED(status)


@__graalpython__.builtin
def WTERMSIG(status):
    return status - 128


@__graalpython__.builtin
def WEXITSTATUS(status):
    return status & 127


@__graalpython__.builtin
def WIFSTOPPED(status):
    return False


@__graalpython__.builtin
def WSTOPSIG(status):
    return 0


error = OSError
