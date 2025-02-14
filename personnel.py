# personnel.py

from data_storage import save_data, load_data

def add_person(data):
    name = input('Enter Name: ')
    nrp = input('Enter NRP: ')
    position = input('Enter Position: ')
    rank = input('Enter Rank: ')
    new_person = {'name': name, 'nrp': nrp, 'position': position, 'rank': rank}
    data.append(new_person)
    save_data(data)
    print('Personnel data successfully added.\n')

def display_personnel(data):
    if not data:
        print('No personnel data available.\n')
        return
    for idx, person in enumerate(data):
        print(f"{idx + 1}. NRP: {person['nrp']}, Name: {person['name']}, Position: {person['position']}, Rank: {person['rank']}")
    print()

def update_person(data):
    display_personnel(data)
    idx = int(input('Choose the number of the personnel to update: ')) - 1
    if 0 <= idx < len(data):
        name = input('Enter new Name: ')
        nrp = input('Enter new NRP: ')
        position = input('Enter new Position: ')
        rank = input('Enter new Rank: ')
        data[idx]['name'] = name
        data[idx]['nrp'] = nrp
        data[idx]['position'] = position
        data[idx]['rank'] = rank
        save_data(data)
        print('Personnel data successfully updated.\n')
    else:
        print('Personnel not found.\n')

def delete_person(data):
    display_personnel(data)
    idx = int(input('Choose the number of the personnel to delete: ')) - 1
    if 0 <= idx < len(data):
        del data[idx]
        save_data(data)
        print('Personnel data successfully deleted.\n')
    else:
        print('Personnel not found.\n')
