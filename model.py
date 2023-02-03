contacts = []
path = 'contacts.txt'

def get_contacts():
    global contacts
    return contacts

def open_file():
    global contacts
    global path
    with open (path, 'r', encoding= 'utf-8') as data:
        file = data.readlines()
    for s in file:
        contacts.append(s.strip().split(';'))

def add_contact(new_contact:list):
    global contacts
    global path   
    with open (path, 'a', encoding='utf-8') as data:
        data.write('\n')
        data.write('; '.join(new_contact))
    contacts.append(new_contact)
    return contacts


def search_contact(find: str):
    global path
    result = []
    with open(path, 'r', encoding='utf-8') as data:
        line = data.readlines()
    for contact in line:
        for elem in contact:
            if find in elem:
                result.append(contact)
                break
    return result


    
def del_contact(c_del:str):   
    global path
    with open(path, 'r',encoding='utf-8') as data:
        line = data.readlines()
    for elem in line:
        if c_del in elem:
            line.remove(elem) 
    with open (path, 'w', encoding='utf-8') as data:
        data.write(''.join(line)) 
    return line


    
    
    

            
    



