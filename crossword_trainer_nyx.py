from bs4 import BeautifulSoup
import requests, datetime, csv, os

with open('crossword_training_data.csv', 'w') as csv_file:
    fieldnames = ['day','clue','answer','length','date']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

print('Initialising dates...')

startDate = datetime.date(2019,6,25)
today = datetime.date.today()

date = startDate

while date <= today:
    day = date.weekday()
    formattedDate = date.strftime('%Y') + '/' + date.strftime('%m') + '/' + date.strftime('%d')

    url = f'https://nyxcrossword.com/{formattedDate}'
    print(url)
    r = requests.get(url)

    # soupify webpage data
    soup = BeautifulSoup(r.text, 'lxml')

    print('Getting clues and answers for ' + str(date))

    clueCount = 0

    # iterate through both blocks of clues and answers (across and down)
    for clueList in soup.find_all('div', id='clue_list'):
        # break out paragraphs for across and down
        clues = clueList.findChildren('p', recursive=False)
        # separate at br tags for individual clue and answer pairs
        acrossClues = str(clues[0]).strip('<p>').split('<br/>')
        downClues = str(clues[1]).strip('<p>').split('<br/>')
        # strip bs at start of clue
        for clue in acrossClues:
            space = clue.index(' ')
            clue = clue[space+1:]
            clue = clue.strip('</').split(' : ')
            # create/set dictionary values
            info = {}
            info.update({'day': day, 'clue': clue[0], 'answer': clue[1],
                        'length': len(clue[1]), 'date': date})
            # open csv and append dictionary as row
            with open('nyx_crossword_training_data.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
                csv_writer.writerow(info)
            clueCount += 1
        for clue in downClues:
            space = clue.index(' ')
            clue = clue[space+1:]
            clue = clue.strip('</').strip('\n').split(' : ')
            # create/set dictionary values
            info = {}
            info.update({'day': day, 'clue': clue[0], 'answer': clue[1],
                        'length': len(clue[1]), 'date': date})
            # open csv and append dictionary as row
            with open('nyx_crossword_training_data.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
                csv_writer.writerow(info)
            clueCount += 1

    print(str(clueCount) + ' clues and answers found')

    #iterate dates (set value to 7 to retrieve answers for the same day)
    date += datetime.timedelta(days=1)

# # read data with DictReader
# with open('crossword_training_data.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file,fieldnames=fieldnames)
#     for item in csv_reader:
#         print(item['answer'])
