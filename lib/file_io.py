
def write_file(file_name, file_content):
   with open(str(file_name) + '.txt', 'w') as file_name:
       file_name.write(file_content)
   
   
   pass



def append_file(file_name, file_content):
    with open(str(file_name) + '.txt', 'a') as file_name:
        file_name.write(file_content)


    pass

def read_file(file_name):
    with open(str(file_name) + '.txt', 'r') as file:
        return file.read()
    pass









