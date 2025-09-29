# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'pyi_rth_pkgres.py'
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

def _pyi_rthook():
    import os
    import pathlib
    import sys
    import warnings
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=UserWarning, message='pkg_resources is deprecated')
        import pkg_resources
    import pyimod02_importers
    SYS_PREFIX = pathlib.PurePath(sys._MEIPASS)
    class _TocFilesystem:
        """\n        A prefix tree implementation for embedded filesystem reconstruction.\n\n        NOTE: as of PyInstaller 6.0, the embedded PYZ archive cannot contain data files anymore. Instead, it contains\n        only .pyc modules - which are by design not returned by `PyiFrozenProvider`. So this implementation has been\n        reduced to supporting only directories implied by collected packages.\n        """
        def __init__(self, tree_node):
            self._tree = tree_node
        def _get_tree_node(self, path):
            path = pathlib.PurePath(path)
            current = self._tree
            for component in path.parts:
                if component not in current:
                    return
                else:
                    current = current[component]
            return current
        def path_exists(self, path):
            node = self._get_tree_node(path)
            return isinstance(node, dict)
        def path_isdir(self, path):
            node = self._get_tree_node(path)
            return isinstance(node, dict)
        def path_listdir(self, path):
            node = self._get_tree_node(path)
            if not isinstance(node, dict):
                return []
            else:
                return [entry_name for entry_name, entry_data in node.items() if isinstance(entry_data, dict)]
    class PyiFrozenProvider(pkg_resources.NullProvider):
        """\n        Custom pkg_resources provider for PyiFrozenLoader.\n        """
        def __init__(self, module):
            super().__init__(module)
            self._pkg_path = pathlib.PurePath(module.__file__).parent
            self.embedded_tree = _TocFilesystem(pyimod02_importers.get_pyz_toc_tree())
        def _normalize_path(self, path):
            return pathlib.Path(os.path.normpath(path))
        def _is_relative_to_package(self, path):
            return path == self._pkg_path or self._pkg_path in path.parents
        def _has(self, path):
            path = self._normalize_path(path)
            if not self._is_relative_to_package(path):
                return False
            else:
                if path.exists():
                    return True
                else:
                    rel_path = path.relative_to(SYS_PREFIX)
                    return self.embedded_tree.path_exists(rel_path)
        def _isdir(self, path):
            path = self._normalize_path(path)
            if not self._is_relative_to_package(path):
                return False
            else:
                rel_path = path.relative_to(SYS_PREFIX)
                node = self.embedded_tree._get_tree_node(rel_path)
                if node is None:
                    return path.is_dir()
                else:
                    return not isinstance(node, str)
        def _listdir(self, path):
            path = self._normalize_path(path)
            if not self._is_relative_to_package(path):
                return []
            else:
                rel_path = path.relative_to(SYS_PREFIX)
                content = self.embedded_tree.path_listdir(rel_path)
                if path.is_dir():
                    path = str(path)
                    content = list(set(content + os.listdir(path)))
                return content
    pkg_resources.register_loader_type(pyimod02_importers.PyiFrozenLoader, PyiFrozenProvider)
    pkg_resources.register_finder(pyimod02_importers.PyiFrozenFinder, pkg_resources.find_on_path)
    if hasattr(pkg_resources, '_initialize_master_working_set'):
        pkg_resources._initialize_master_working_set()
_pyi_rthook()
del _pyi_rthook