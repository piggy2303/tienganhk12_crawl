import html
from os import access
import re
import requests
import json

from constant_data import(setup_email,setup_password,list_of_test_code)

# step 1 = login
def step_login():
    url_login = "http://data.tienganhk12.com/api/TokenAuth/Authenticate"

    data = json.dumps({
        "password": setup_password(),
        "usernameOrEmailAddress": setup_email()
    })

    headers = {'Content-Type': 'application/json'}
    r = requests.post(url_login, data=data, headers=headers).json()
    access_token = r["result"]["accessToken"]
    print(access_token)
    return access_token


# step 2 = get data
headers = {'Authorization': 'Bearer '+step_login()}
url_get_data = "http://data.tienganhk12.com/api/services/app/QuizPublic/GetQuestionByQuizAttempt?quizAttemptId="

# LIST OF TEST CODE
url_code_arr = list_of_test_code()

folder_data = './data/'

for url_code in url_code_arr:
    a = requests.get(url_get_data+url_code, headers=headers)
    a = a.json()

    def cleanhtml(raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        cleantext = html.unescape(cleantext)
        return cleantext

    a_question = a["result"]["questions"]
    a_question

    f = open(folder_data+"test"+url_code+".txt", "w+")

    for count, i in enumerate(a_question):
        f.write("================\n")
        questionText = "Question: " + cleanhtml(i["questionText"])+"\n\n"
        print(questionText)
        f.write(questionText)

        if i["answerList"] is not None:
            answerList = i["answerList"]
            print(count, answerList)
            for j in answerList:
                print(cleanhtml(j["answerText"]))
                b = "Answer: "+cleanhtml(j["answerText"]) + "\n"
                f.write(b)
    f.close()
