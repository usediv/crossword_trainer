from bs4 import BeautifulSoup
import requests


r = requests.get('https://www.xwordinfo.com/Crossword?date=6/15/2019')

day = 'Saturday'

soup = BeautifulSoup(r.text, 'lxml')

for numClues in soup.find_all('div', class_='numclue'):
    clues = numClues.findChildren('div' , recursive=False)
    for clue in clues[1::2]:
        answer = []
        clue = clue.text.split(': ')
        answer.append(day)
        answer.append(clue[0])
        answer.append(clue[1])
        answer.append(len(clue[1]))
        print(answer)
