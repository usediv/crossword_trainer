from bs4 import BeautifulSoup
import requests, datetime, csv, os


print('Initialising dates...')

# set up dates
today = datetime.date.today()
day = today.weekday()
splitDate = str(today).split('-')
date = str(int(splitDate[1])) + '/' + splitDate[2] + '/' + splitDate[0]

# set URL
url = f'https://www.xwordinfo.com/Crossword?date={date}'
r = requests.get(url)

# soupify webpage data
soup = BeautifulSoup(r.text, 'lxml')

# csv stuff
# os.chdir('/Users/chriswilson/Documents/GitHub/crossword_trainer')
csv_file = open('crossword_training_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['day','clue','answer','length'])

# check crossword clues and answers
print('Checking for clues...')

try:
    # iterate through both blocks of clues and answers (across and down)
    for numClues in soup.find_all('div', class_='numclue'):
        # break out individual divs from blocks
        clues = numClues.findChildren('div' , recursive=False)
        # grab just the clues and answers, ditch the numbers and format
        clueCount = 0
        for clue in clues[1::2]:
            clueCount += 1
            answer = []
            clue = clue.text.split(' : ')
            csv_writer.writerow([day,clue[0],clue[1],len(clue[1])])
    print(str(clueCount) + ' clues and answers found')

    csv_file.close()

except:
    print('Sorry, clues not found')
