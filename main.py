import string

from exact_counter import *
from file_processing import *


datastream = format_text(read_file("The Norwegian Fairy Book.txt", 258, 7848), string.ascii_letters).upper()

print(exact_count(datastream))