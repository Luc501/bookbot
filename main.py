from stats import word_count, check_freq, sort_on
import pprint
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
         file_contents = f.read()
    return file_contents 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    txt_file_location = sys.argv[1]
    file_contents = get_book_text(txt_file_location)
    num_words = word_count(file_contents)
    freq_dict = check_freq(file_contents)  # Call the function to get the frequency list
    sorted_freq = sorted(freq_dict.items(), reverse=True, key=sort_on)  # Use sorted() to sort the list
    transformed_freq = []
    for key, value in sorted_freq:
        if key.isalpha():
            transformed_freq.append({"char": key, "number": value})
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {txt_file_location}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    for i in transformed_freq:
        print(f"{i['char']}: {i['number']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

