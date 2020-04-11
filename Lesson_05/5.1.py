line_list = []
while True:
    line = input("пишите или не пишите!(1): ")
    if line == '':
        break
    line_list.append(line + '\n')

my_file1 = open("my_file1.txt", 'w')
my_file1.writelines(line_list)
my_file1.close()

'''*****************************************************************************************************'''

with open("my_file2.txt", 'w') as my_file2:

    while True:
        line = input("пишите или не пишите!(2): ")
        if not line:
            break
        my_file2.write(f"{line}\n")

'''*****************************************************************************************************'''

my_file3 = open("my_file3.txt", 'w')

line = None
while line != '':
    line = input("пишите или не пишите!(3): ")
    my_file3.write(f"{line}\n") if line != '' else my_file3.close()    # баловство



