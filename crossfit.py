import csv
from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS

app = FlaskAPI(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})



# # read data from CSV and populate in bigList
# bigList = []
#
# with open('NYT Crossword_2009_2016.csv', 'r') as csv_file:
#     fieldnames = ['Year','Weekday','Clue','Word','Total','Explanation']
#     csv_reader = csv.DictReader(csv_file,fieldnames=fieldnames)
#     limit = 1
#     for item in csv_reader:
#         if item['Weekday'] == 'Wed' and limit < 20:
#             bigList.append(item)
#             limit+=1
#
#
# wrongList = []
# listIndex = 0
# counter = 0
#
# # infinite loop
# while True:
#     # check counter to see if fifth clue
#     if counter%5 == 0:
#         # check wrongList
#         if len(wrongList) != 0:
#             clue = wrongList.pop(0)
#             counter+=1
#         else:
#             # otherwise, iterate through list
#             clue = bigList[listIndex]
#             listIndex+=1
#             counter+=1
#     else:
#         clue = bigList[listIndex]
#         listIndex+=1
#         counter+=1
#     print(clue['Clue'])
#     # reset index at end of list to keep looping
#     if listIndex > len(bigList)-1:
#         listIndex=0
#     # check if we've been round once already and if wrongList is empty
#     if counter > len(bigList)-1 and len(wrongList) == 0:
#         break
#
#     answer = input()
#     if answer == "0":
#         wrongList.append(clue)


notes = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}

def note_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': notes[key]
    }


@app.route("/", methods=['GET', 'POST'])
def notes_list():
    """
    List or create notes.
    """
    if request.method == 'POST':
        note = str(request.data.get('text', ''))
        idx = max(notes.keys()) + 1
        notes[idx] = note
        return note_repr(idx), status.HTTP_201_CREATED

    # request.method == 'GET'
    return jsonify([note_repr(idx) for idx in sorted(notes.keys())])


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        notes[key] = note
        return note_repr(key)

    elif request.method == 'DELETE':
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in notes:
        raise exceptions.NotFound()
    return note_repr(key)


if __name__ == "__main__":
    app.run(debug=True)
