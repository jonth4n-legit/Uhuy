# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'pyi_rth_multiprocessing.py'
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

def _pyi_rthook():
    import sys
    import multiprocessing
    import multiprocessing.spawn
    from subprocess import _args_from_interpreter_flags
    multiprocessing.process.ORIGINAL_DIR = None
    def _freeze_support():
        if len(sys.argv) >= 2 and sys.argv[(-2)] == '-c' and sys.argv[(-1)].startswith(('from multiprocessing.resource_tracker import main', 'from multiprocessing.forkserver import main')) and (set(sys.argv[1:(-2)]) == set(_args_from_interpreter_flags())):
                        exec(sys.argv[(-1)])
                        sys.exit()
        if multiprocessing.spawn.is_forking(sys.argv):
            kwds = {}
            for arg in sys.argv[2:]:
                name, value = arg.split('=')
                if value == 'None':
                    kwds[name] = None
                else:
                    kwds[name] = int(value)
            multiprocessing.spawn.spawn_main(**kwds)
            sys.exit()
    multiprocessing.freeze_support = multiprocessing.spawn.freeze_support = _freeze_support
_pyi_rthook()
del _pyi_rthook