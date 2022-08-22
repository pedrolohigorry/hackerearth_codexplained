def golden_char (key, string):
    count = 0

    for letter in string:
        if letter in key:
            count += 1
        else:
            continue

    return count

key = input()
string = input()

out_ = golden_char(key, string)
print (out_)
