import sys
import marshal
import dis as _std_dis
import importlib.util


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python dis.py <pyc_file>")
        return 2
    fn = sys.argv[1]
    with open(fn, "rb") as f:
        magic = f.read(4)
        # Skip header according to magic
        if magic == importlib.util.MAGIC_NUMBER:
            f.read(12)
        else:
            f.read(8)
        code = marshal.load(f)
    _std_dis.dis(code)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
