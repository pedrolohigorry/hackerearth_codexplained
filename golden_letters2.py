def golden_char (key, string):

    dict_key = {}
    for letter in key:
        dict_key[letter] = dict_key.get(letter,0) + 1

    count = 0
    for letter in string:
        if letter in dict_key:
            count += 1
        else:
            continue

    return count

key = input()
string = input()

out_ = golden_char(key, string)
print (out_)
