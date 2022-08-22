### Problem taken from HackerEarth, CodeExplained Practice Portal
### Problem name: Destroy Those Pairs!

def remove_pair(string):
    if len(string) == 1 or len(string) == 0:
        return string
    res = ""
    for letter in string:
        if res == "":
            res += letter
        elif letter == res[-1]:
            res = res[:-1]
        else:
            res += letter
    return res

string = input()

out_ = remove_pair(string)
print (out_)
