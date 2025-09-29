# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'pyimod01_archive.py'
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import struct
import marshal
import zlib
import _frozen_importlib
PYTHON_MAGIC_NUMBER = _frozen_importlib._bootstrap_external.MAGIC_NUMBER
PYZ_ITEM_MODULE = 0
PYZ_ITEM_PKG = 1
PYZ_ITEM_DATA = 2
PYZ_ITEM_NSPKG = 3
class ArchiveReadError(RuntimeError):
    # return None
    pass
class ZlibArchiveReader:
    """\n    Reader for PyInstaller\'s PYZ (ZlibArchive) archive. The archive is used to store collected byte-compiled Python\n    modules, as individually-compressed entries.\n    """
    _PYZ_MAGIC_PATTERN = b'PYZ\x00'
    def __init__(self, filename, start_offset=None, check_pymagic=False):
        self._filename = filename
        self._start_offset = start_offset
        self.toc = {}
        if start_offset is None:
            self._filename, self._start_offset = self._parse_offset_from_filename(filename)
        with open(self._filename, 'rb') as fp:
            fp.seek(self._start_offset, os.SEEK_SET)
            magic = fp.read(len(self._PYZ_MAGIC_PATTERN))
            if magic!= self._PYZ_MAGIC_PATTERN:
                raise ArchiveReadError('PYZ magic pattern mismatch!')
            else:
                pymagic = fp.read(len(PYTHON_MAGIC_NUMBER))
                if check_pymagic and pymagic!= PYTHON_MAGIC_NUMBER:
                    raise ArchiveReadError('Python magic pattern mismatch!')
                else:
                    toc_offset, *_ = struct.unpack('!i', fp.read(4))
                    fp.seek(self._start_offset + toc_offset, os.SEEK_SET)
                    self.toc = dict(marshal.load(fp))
    @staticmethod
    def _parse_offset_from_filename(filename):
        """\n        Parse the numeric offset from filename, stored as: `/path/to/file?offset`.\n        """
        offset = 0
        idx = filename.rfind('?')
        if idx == (-1):
            return (filename, offset)
        else:
            try:
                offset = int(filename[idx + 1:])
                filename = filename[:idx]
            except ValueError:
                pass
            return (filename, offset)
    def extract(self, name, raw=False):
        """\n        Extract data from entry with the given name.\n\n        If the entry belongs to a module or a package, the data is loaded (unmarshaled) into code object. To retrieve\n        raw data, set `raw` flag to True.\n        """
        entry = self.toc.get(name)
        if entry is None:
            raise KeyError(f'No entry named {name!r} found in the archive!')
        else:
            typecode, entry_offset, entry_length = entry
            if typecode == PYZ_ITEM_NSPKG:
                return
            else:
                try:
                    with open(self._filename, 'rb') as fp:
                        fp.seek(self._start_offset + entry_offset)
                        obj = fp.read(entry_length)
                except FileNotFoundError:
                    raise SystemExit(f'ERROR: {self._filename} appears to have been moved or deleted since this application was launched. Continouation from this state is impossible. Exiting now.')
                try:
                    obj = zlib.decompress(obj)
                    if typecode in (PYZ_ITEM_MODULE, PYZ_ITEM_PKG) and (not raw):
                            obj = marshal.loads(obj)
                except EOFError as e:
                    raise ImportError(f'Failed to unmarshal PYZ entry {name!r}!') from e
                return obj