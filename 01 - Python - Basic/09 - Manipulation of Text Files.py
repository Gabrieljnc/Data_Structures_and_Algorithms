
students = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

####################################################
# list_1 = []

# for name,score in students.items():
#    list_1.append(str(name))
#    list_1.append(str(score))

# text = ','.join(list_1)
# text_final = text[0:9] + "\n" + text[10:20] + "\n" + text[21:]

# with open("Name_Score.txt", "w") as Name_Score:
#     text = Name_Score.write(text_final)

# with open("Name_Score.txt") as Name_Score:
#     for line in Name_Score:
#         print(line)

####################################################

with open("Name_Score.txt", "w") as Name_Score:
    for student,score in students.items():
        Name_Score.write(f"{student},{score}\n")

with open("Name_Score.txt") as Name_Score:
    for line in Name_Score:
        print(line)