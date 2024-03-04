
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        dicti = count_letters(file_contents)
        converted_dict = convert_to_dict_list_and_sort(dicti)
        reportti = report(word_count, converted_dict)

def count_words(word):
    words = word.split()
    return len(word)

def count_letters(word):
    letters = {}
    word_to_lower = word.lower()
    for letter in word_to_lower:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
        
    return letters

def sort_on(dict):
    return dict["num"]
def convert_to_dict_list_and_sort(dict):
    letters = []
    for value in dict.keys():
        if value.isalpha():
            new_dict = {
                "name": value,
                "num": dict[value]
            }
            letters.append(new_dict)
    letters.sort(reverse=True, key=sort_on)
    return letters

def report(word_count, dicti):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for d in dicti:
        print(f"The '{d["name"]}' was found {d["num"]} times")
    print("--- End report ---")

    


main()