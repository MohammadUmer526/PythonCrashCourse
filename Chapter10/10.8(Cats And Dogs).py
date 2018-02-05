
file_names = ['C:\\Users\\Muhammad Umer\\Desktop\\dogs.txt' , 'C:\\Users\\Muhammad Umer\\Desktop\\cats.txt' ] # path of a files in a list

for file_name in file_names: # loop for accessing two files

    print("Reading file: "+ file_name) # give the name of file individually, after first file name it goes down then comes for secound file name

    try:
        with open(file_name) as f_obj: # use func 'open'
            content = f_obj.read()
            print(content)

    except FileNotFoundError:
        msg = "The file, " + file_name + " does not exist." # 'except' for file does not exist
        print(msg)







