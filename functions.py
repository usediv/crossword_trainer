bigList = ['clue1', 'clue2', 'clue3']

listIndex = 0
counter = 0

while True:
    print(bigList[listIndex])
    listIndex+=1
    counter+=1
    if listIndex > len(bigList)-1:
        listIndex=0
    if counter > 20:
        break

# if counter < 400:
  #clue = clue
# if counter > 400:
  # check wrong table
  # if wrong table is empty
    #end
  # if wrong table isn't empty
    # clue = wrongclue
