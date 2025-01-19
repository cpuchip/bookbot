def word_count(book):
    count = book.split()
    return len(count)

def sort_on(dict):
    return dict["count"]

def letter_count(book):
    # convert to lower case
    chars = {}
    book_lower = book.lower()
    for char in book_lower:
        if char.isalpha():
            chars[char] = chars.get(char, 0) + 1

    # convert to list of dictionaries
    result = []
    for char in chars.keys():
        result.append({"letter": char, "count": chars[char]})
    result.sort(reverse=True, key=sort_on)
    return result


def main(filename):
    with open(filename, "r") as f:
        file_contents = f.read()
    # print(file_contents)
    count = word_count(file_contents)
    ltr_count = letter_count(file_contents)

    print(f"--- Begin report of {filename} ---")
    print(f"{count} words found in the document")
    print()
    for letter in ltr_count:
        print(f"The '{letter['letter']}' was found {letter['count']} times")
    print(f"--- End report ---")

if __name__ == "__main__":
    main("./books/frankenstein.txt")