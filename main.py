book_path = 'books/frankenstein.txt'

def get_book_text(path):
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_charars_dict(text):
    my_dict = {}
    for character in text:
        lower_case = character.lower()
        if lower_case in my_dict:
            my_dict[lower_case] += 1
        else:
            my_dict[lower_case] = 1
    return my_dict

def sort_on_key(z):
    return z['num']

def character_dict_to_sorted_dict(num_characters_dict):
    sorted_list = []

    for ch in num_characters_dict:
        sorted_list.append({'char': ch, 'num': num_characters_dict[ch]})
    
    sorted_list.sort(reverse=True, key=sort_on_key)
    return sorted_list






def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = get_charars_dict(text)
    character_sorted_list = character_dict_to_sorted_dict(character_dict)


    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} found in the document')
    print()
    print()

    for item in character_sorted_list:
        if item['char'].isalpha() != True:
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")


    print('--- End report ---')

main()