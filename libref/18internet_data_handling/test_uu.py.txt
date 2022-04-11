
# uu - encode and decode uuencode files
import uu
from uu import *

# encode(in_file, out_file[, name[, mode]])
encode("test_uu.py", "test_uu.txt")


#decode(in_file[, out_file[, mode[, quiet]]])
decode("test_uu.txt", "test_uu.py.txt")


 