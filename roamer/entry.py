"""
argh
"""

import os
import hashlib

class Entry(object):
    """
    argh
    """
    def __init__(self, name, directory, digest=None):
        self.directory = directory
        self.name = name
        self.set_path()
        if os.path.isdir(self.path) and name[-1] != '/':
            self.name = name + '/'
        if digest:
            self.digest = digest
        else:
            self.full_digest = hashlib.sha224(self.path).hexdigest()
            self.digest = self.full_digest[0:7]

    def __str__(self):
        return "%s | %s" % (self.name, self.digest)

    def set_path(self):
        self.path = os.path.join(str(self.directory), self.name)

    def append_to_name(self, text):
        self.name = self.base_name() + text + self.extension()
        self.set_path()

    def is_dir(self):
        return self.name[-1] == '/'

    def persisted(self):
        return os.path.exists(self.path)

    def base_name(self):
        extension_length = len(self.extension())
        return self.name[:-extension_length]

    def extension(self):
        if self.is_dir():
            return '/'
        else:
            return os.path.splitext(self.name)[1]
