def build_dict(file_name):
    file = open(file_name, 'r')
    file.readline()
    occupation_dict = {}
    for line in file:
        values = line.split(',')
        occupation_name = ''.join(values[:-1])
        occupation_percentage = float(values[-1])
        occupation_dict[occupation_name] = occupation_percentage
    file.close()
    return occupation_dict


def select_occupation(occupation_dict):
    from random import random
    num = random() * occupation_dict['Total']
    counter = 0
    for name, percentage in occupation_dict.items():
        counter += percentage
        if counter >= num:
            return name


def main():
    file_name = 'occupations.csv'
    occupation_dict = build_dict(file_name)
    occupation = select_occupation(occupation_dict)
    print(occupation)

main()
