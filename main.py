def sort_on(dict):
    return dict["char"]


def main():
    chars = {}
    chars_list = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        for char in file_contents.lower():
            if chars.get(char) != None:
                chars[char] += 1
            else:
                chars[char] = 1

        for key in chars:
            if key.isalpha():
                chars_list.append({"char": key, "count": chars[key]})
    chars_list.sort(reverse=True, key=sort_on)
    # print(f"chars: {chars}\n words {len(words)}\n char_list {chars_list}")
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document\n")
    for ch in chars_list:
        print(f"The '{ch["char"]}' character was found {ch["count"]} times")


main()
