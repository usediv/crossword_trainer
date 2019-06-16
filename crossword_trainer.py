from bs4 import BeautifulSoup
import requests
import datetime


today = datetime.date.today()
day = today.weekday()
splitDate = str(today).split('-')


url = 'https://www.xwordinfo.com/Crossword?date=' + str(int(splitDate[1])) + '/' + splitDate[2] + '/' + splitDate[0]

r = requests.get(url)

# soupify
soup = BeautifulSoup(r.text, 'lxml')

# iterate through both blocks of clues and answers (across and down)
for numClues in soup.find_all('div', class_='numclue'):
    # break out individual divs from blocks
    clues = numClues.findChildren('div' , recursive=False)
    # grab just the clues and answers, ditch the numbers and format
    for clue in clues[1::2]:
        answer = []
        clue = clue.text.split(' : ')
        answer.extend([day,clue[0],clue[1],len(clue[1])])
        print(answer)
