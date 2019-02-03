#https://stackoverflow.com/questions/35155382/copying-specific-files-to-a-new-folder-while-maintaining-the-original-subdirect

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Works in Python 2.7 & 3.x

import fnmatch
from os.path import isdir, join

def include_patterns(*patterns):
    """ Function that can be used as shutil.copytree() ignore parameter that
    determines which files *not* to ignore, the inverse of "normal" usage.

    This is a factory function that creates a function which can be used as a
    callable for copytree()'s ignore argument, *not* ignoring files that match
    any of the glob-style patterns provided.

    ‛patterns’ are a sequence of pattern strings used to identify the files to
    include when copying the directory tree.

    Example usage:

        copytree(src_directory, dst_directory,
                 ignore=include_patterns('*.sldasm', '*.sldprt'))
    """
    def _ignore_patterns(path, all_names):
        # Determine names which match one or more patterns (that shouldn't be
        # ignored).
        keep = (name for pattern in patterns
                        for name in fnmatch.filter(all_names, pattern))
        # Ignore file names which *didn't* match any of the patterns given that
        # aren't directory names.
        dir_names = (name for name in all_names if isdir(join(path, name)))
        return set(all_names) - set(keep) - set(dir_names)

    return _ignore_patterns


if __name__ == '__main__':

    from shutil import copytree, rmtree
    import os

    src = r'C:\vols\Files\PythonLib\Stack Overflow'
    dst = r'C:\vols\Temp\temp\test'

    # Make sure the destination folder does not exist.
    if os.path.exists(dst) and os.path.isdir(dst):
        print('removing existing directory "{}"'.format(dst))
        rmtree(dst, ignore_errors=False)

    copytree(src, dst, ignore=include_patterns('*.png', '*.gif'))

    print('done')
