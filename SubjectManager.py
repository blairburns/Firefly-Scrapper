import JsonFetcher as jf
import json


JSON = jf.fetchJSON()

currentLesson = 0
subjects = []

with open('Subjects.json') as s:
    SubjectJSON = json.load(s)

lessons = JSON['events']
for x in lessons:
    currentClass = lessons[currentLesson]
    try:
        currentSubject = currentClass['subject']
        if currentSubject in SubjectJSON:
            currentJSON = SubjectJSON[currentSubject]
            currentSubject = currentJSON['Lesson_Name']
        subjects.append(currentSubject)
        currentLesson += 1
    except:
        currentLesson += 1


print(subjects)
