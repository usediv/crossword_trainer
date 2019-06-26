import csv
# from flask import Flask


fieldnames = ['year','weekday','clue','word','total','explanation']

# read data with DictReader
with open('NYT Crossword_2009_2016.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file,fieldnames=fieldnames)
    for item in csv_reader:
        clue = item['clue']
        word = item['word']
        wordlen = len(word)
        for letter in word:
            print('[]')
        # print(clue)
        # print(f'This is your {word} and this is how long it is {wordlen}')
        # print(wordlen)


# app = Flask(__name__)
# @app.route("/")
# def hello():
#     return test