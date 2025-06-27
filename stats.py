
def word_count(text):
    file_list = text.split()
    return len(file_list)

def check_freq(x):
    low_x = x.lower()
    freq = {}
    for c in set(low_x):
       freq[c] = low_x.count(c)
    return freq

def sort_on(item):
    return item[1]