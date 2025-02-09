#======================================================
# data_storage
#======================================================

def save_data(data, file_name='personel_data.txt'):
    with open(file_name, 'w') as file :
              for person in data:
                file.write (f"{person['name']})|{person['rank']}||{person['nrp']}|{person['position']}\n")

def load_data(file_name='personel_data.txt'):
     data=[]
     try:
          with open (file_name, 'r') as file: 
               for line  in file :
                    name, rank, nrp, position =line.strip().split('|')
                    data.append ({'name':name,'rank':rank,'nrp':nrp, 'position': position})
     except FileNotFoundError:
        pass
     return data