#Emily Nixon and Saeran Bong and Krista Dockery
def remove_substring(string, substring):
    output = []
    index = 0
    while index<len(string):
        if string[index:index+len(substring)] == substring:
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

remove_substring("Th.is ma.kes no. sens.e",".")
