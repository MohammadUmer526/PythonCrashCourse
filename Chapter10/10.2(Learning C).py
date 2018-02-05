file_path = 'C:\\Users\Muhammad Umer\\Desktop\\python.txt' # give a path of your file name

with open(file_path) as file:
    content = file.read()
    print(content.replace('Python', 'C'))  # use 'replace' method in which we passes two parameters 'Python' i.e
    # going to change 'C' in value