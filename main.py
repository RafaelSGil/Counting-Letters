import string

from exact_counter import *
from file_processing import *
from lossy_counting import *
from aprox_counter import *

rj_english = format_text(read_file("RomeoJuliet_eng.txt", 76, 5291), string.ascii_letters).upper()

print("Book: Romeo & Juliet --> English version")
print("Exact counter: ", exact_count(rj_english, 10))

lc1 = LossyCount(0.02, 0.002)
lc1.processDatastream(rj_english)
print("Lossy counter: ", lc1.getResults(10))
print("Approximate counter: ", aprox_counter(rj_english, top=10))
print("\n")

""" rj_german = format_text(read_file("RomeoJuliet_de.txt", 76, 5291), string.ascii_letters).upper()

print("Book: Romeo & Juliet --> German version")
print("Exact counter: ", exact_count(rj_german, 10))

lc2 = LossyCount(0.02, 0.002)
lc2.processDatastream(rj_german)
print("Lossy counter: ", lc2.getResults(10))
print("\n")

rj_french = format_text(read_file("RomeoJuliet_fr.txt", 76, 5291), string.ascii_letters).upper()

print("Book: Romeo & Juliet --> French version")
print("Exact counter: ", exact_count(rj_french, 10))

lc3 = LossyCount(0.02, 0.002)
lc3.processDatastream(rj_french)
print("Lossy counter: ", lc3.getResults(10))
print("\n") """