from bs4 import BeautifulSoup
import requests, datetime, csv, os

with open('crossword_training_data.csv', 'w') as csv_file:
    fieldnames = ['day','clue','answer','length','date']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

print('Initialising dates...')

startDate = datetime.date(2019,6,1)
today = datetime.date.today()

date = startDate

while date <= today:
    day = date.weekday()
    splitDate = str(date).split('-')
    formattedDate = str(int(splitDate[1])) + '/' + splitDate[2] + '/' + splitDate[0]

    url = f'https://www.xwordinfo.com/Crossword?date={formattedDate}'
    r = requests.get(url)

    # soupify webpage data
    soup = BeautifulSoup(r.text, 'lxml')

    print('Getting clues and answers for ' + str(date))

    clueCount = 0

    # iterate through both blocks of clues and answers (across and down)
    for numClues in soup.find_all('div', class_='numclue'):
        # break out individual divs from blocks
        clues = numClues.findChildren('div', recursive=False)
        # grab just the clues and answers, ditch the numbers and format
        for clue in clues[1::2]:
            clueCount += 1
            clue = clue.text.split(' : ')
            # create/set dictionary values
            info = {}
            info.update({'day': day, 'clue': clue[0], 'answer': clue[1], 'length': len(clue[1]), 'date': date})
            # open csv and append dictionary as row
            with open('crossword_training_data.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
                csv_writer.writerow(info)

    print(str(clueCount) + ' clues and answers found')
    date += datetime.timedelta(days=1)

# reading data with DictReader
# with open('crossword_training_data.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file,fieldnames=fieldnames)
#     for item in csv_reader:
#         print(item['answer'])
