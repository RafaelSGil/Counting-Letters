import string
import time
from exact_counter import *
from file_processing import *
from lossy_counting import *
from aprox_counter import *

def process(language, filename, top):
    book_text = format_text(read_file(filename, 76, 5291), string.ascii_letters).upper()
    
    exact_start_time = time.perf_counter()
    exact_result = exact_count(book_text, top)
    exact_end_time = time.perf_counter()
    
    lc = LossyCount(0.02, 0.002)
    lossy_start_time = time.perf_counter()
    lc.processDatastream(book_text)
    lossy_result = lc.getResults(top)
    lossy_end_time = time.perf_counter()
    
    approx_start_time = time.perf_counter()
    approx_result = aprox_counter(book_text, top=top)
    approx_end_time = time.perf_counter()

    print(f"Book: Romeo & Juliet --> {language} version\n")
    
    print("Exact counter: ", exact_result)
    print("Lossy counter: ", lossy_result)
    print("Approximate counter: ", approx_result)
    
    print("\nExact counter took ", exact_end_time - exact_start_time, " seconds")
    print("Lossy counter took ", lossy_end_time - lossy_start_time, " seconds")
    print("Approximate counter took ", approx_end_time - approx_start_time, " seconds")
    
    print("\n==================================================================================\n")

    with open("results.txt", 'a') as file:
        file.write(f"Book: Romeo & Juliet --> {language} version\n\n")
        file.write(f"Exact counter: {exact_result}\n")
        file.write(f"Lossy counter: {lossy_result}\n")
        file.write(f"Approximate counter: {approx_result}\n")
        file.write(f"\nExact counter took {exact_end_time - exact_start_time} seconds\n")
        file.write(f"Lossy counter took {lossy_end_time - lossy_start_time} seconds\n")
        file.write(f"Approximate counter took {approx_end_time - approx_start_time} seconds\n")
        file.write("\n==================================================================================\n\n")

process("English", "RomeoJuliet_eng.txt", 10)
process("German", "RomeoJuliet_de.txt", 10)
process("French", "RomeoJuliet_fr.txt", 10)
