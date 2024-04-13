newfile = open('newfile.txt', 'w+')

with open('/PythonPractice/Wenzhounese.txt', 'r') as f:
    group = ""
    for line in f:
        if len(line) > 0:
            group += line + " "
        else:
            group = group + "\n"
            newfile.write(group)

newfile.close()
