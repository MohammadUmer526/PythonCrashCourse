file_path = 'C:\\Users\\Muhammad Umer\\Desktop\\10.10.txt'

try:
    with open(file_path) as f_obj:
        content = f_obj.read()
        print(content)

except:
    message = "The file, " + file_path + " does not exist."


else:
    line = content
    line.count('the')
