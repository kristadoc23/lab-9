#Emily Nixon and Saeran Bong and Krista Dockery
def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index<len(string):
        if string[index:index+len(substring)] == substring:
            index += len(substring)
            output.append(replacement)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

replace_substring("I love dogs.", "dogs","cats")
