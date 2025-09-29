import sys, marshal, dis, importlib.util

fn = sys.argv[1]
with open(fn, "rb") as f:
    magic = f.read(4)
    if magic == importlib.util.MAGIC_NUMBER:
        f.read(12)
    else:
        f.read(8)
    code = marshal.load(f)
dis.dis(code)
