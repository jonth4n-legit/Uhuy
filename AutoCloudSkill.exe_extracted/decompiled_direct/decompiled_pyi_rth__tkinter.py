# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'pyi_rth__tkinter.py'
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

def _pyi_rthook():
    import os
    import sys
    tcldir = os.path.join(sys._MEIPASS, '_tcl_data')
    tkdir = os.path.join(sys._MEIPASS, '_tk_data')
    is_darwin = sys.platform == 'darwin'
    if os.path.isdir(tcldir):
        os.environ['TCL_LIBRARY'] = tcldir
    else:
        if not is_darwin:
            raise FileNotFoundError('Tcl data directory \"%s\" not found.' % tcldir)
    if os.path.isdir(tkdir):
        os.environ['TK_LIBRARY'] = tkdir
    else:
        if not is_darwin:
            raise FileNotFoundError('Tk data directory \"%s\" not found.' % tkdir)
_pyi_rthook()
del _pyi_rthook