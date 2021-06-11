# Step 1: create account

You need an account to access this website
`http://tienganhk12.com/`

# Step 2: Edit constant_data.py

1.  Open file `constant_data.py`
2.  Replace your email and password
3.  Add list of test code this list

    This is your test you want to extract

    ![Screenshot](image/image1.png "example")

    Press button "Làm bài" and this link will like this

    `http://tienganhk12.com/ex/60/on-nen-tieng-anh-vao-lop-6/q/5154/de-minh-hoa-bai-thi-vao-lop-6-mon-tieng-anh-truong-thcs-cau-giay-so-9/atid/2732057`

    The last number on this link is test code = 2732057

    Add this code to this list. Add more code to get more result :))

        def list_of_test_code():
                return ["2531365", "2531453", "2531460"]

# Step 3: Run

## Option 1: using docker

    bash start.sh

## Option 2: not using docker

    python3 index.py

# Result

Your result will be here

    ./data/test{your_test_code}.txt

And it look like this

    ...
    ================
    Question: Choose the word that differs from the rest in the position of the main stress.

    Answer: alien
    Answer: expensive
    Answer: grocery
    Answer: generous
    ================
    Question: Choose the word that differs from the rest in the position of the main stress.

    Answer: inhale
    Answer: travel
    Answer: impress
    Answer: design
    ================
    ...

Done :)