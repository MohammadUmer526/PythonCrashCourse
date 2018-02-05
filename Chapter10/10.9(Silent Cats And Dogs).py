filenames = ['C:\\Users\\Muhammad Umer\\Desktop\\dogs.txt' , 'C:\\Users\\Muhammad Umer\\Desktop\\cats.txt' ]

for filename in filenames:

    print("Reading file: " + filename )

    try:
        with open(filename) as file_object:
            content = file_object.read()
            print(content)

    except FileNotFoundError:
        pass # just define a func 'pass' if file does not exist
