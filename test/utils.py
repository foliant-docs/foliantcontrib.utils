import os
from contextlib import contextmanager


@contextmanager
def chcwd(newcwd, *args, **kwargs):
    '''
    Temporary change working directory to `newcwd` (should be rel path)
    '''

    init_cwd = os.getcwd()
    try:
        os.chdir(os.path.join(init_cwd, newcwd))
        yield
    finally:
        os.chdir(init_cwd)
