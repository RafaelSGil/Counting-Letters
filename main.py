import string

from exact_counter import *
from file_processing import *
from lossy_counting import *


datastream = format_text(read_file("The Norwegian Fairy Book.txt", 258, 7848), string.ascii_letters).upper()
print("Exact counter: ", exact_count(datastream, 10))


lc = LossyCount(0.02, 0.002)
lc.processDatastream(datastream)
print("Lossy counter: ", lc.getResults(10))