# Team Awesome -- William Yin, Liam Kronman, Jason Chan
# SoftDev
# K13 -- Template for Success
# 2020-10-18


from flask import Flask, render_template
from random import random
app = Flask(__name__)


def build_dict(file_name):
    """
    Takes a str parameter representing name of the csv file to be opened, and
    creates a dictionary where for each pair, the key is the occupation name in
    the first column, and the value is the percentage in the second column.
    """
    file = open(file_name, 'r')
    headers = file.readline().split(',')
    occupation_dict = {}
    for line in file:
        values = line.split(',')
        occupation_name = ','.join(values[:-2])
        occupation_link = values[-2]
        occupation_percentage = float(values[-1])
        occupation_dict[occupation_name] = {'percentage': occupation_percentage, 'link': occupation_link}
    file.close()
    return {'dict': occupation_dict, 'headers': headers}


def select_occupation(occupation_dict):
    """
    Takes a parameter of type dict and selects a random occupation weighted by
    the percentage given.
    """
    num = random() * occupation_dict['Total']['percentage']
    counter = 0
    for name, data in occupation_dict.items():
        counter += data['percentage']
        if counter >= num:
            return name


dict = build_dict('data/occupations.csv')
occupation_dict = dict['dict']
headers = dict['headers']


@app.route("/")
def root():
    return "No hablo queso!"

@app.route("/occupyflaskst")
def display_occupations():
    return render_template('occupations.html', occupation=select_occupation(occupation_dict).replace('"', ''), occupations=occupation_dict, headers=headers)

if __name__ == "__main__":
    app.debug = True
    app.run()
