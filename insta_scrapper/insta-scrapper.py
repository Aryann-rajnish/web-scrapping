import py_instagram_dl as pyigdl
import sys

try:
    pyigdl.download(sys.argv[1], wait_between_requests=1)
except Exception as e:
    print(e)
