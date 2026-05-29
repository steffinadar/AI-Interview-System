from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Home Login Page
@app.route('/')
def login():
    return render_template('login.html')

# Dashboard Page
@app.route('/index')
def index():
    return render_template('index.html')

# Upload Resume Page
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':

        filename = request.files['resume'].filename

        skills = [
            "Python",
            "Machine Learning",
            "Flask",
            "HTML",
            "CSS",
            "JavaScript"
        ]

        score = random.randint(70, 95)

        return render_template(
            'result.html',
            filename=filename,
            score=score,
            skills=skills
        )

    return render_template('upload.html')

# Interview Questions Page
@app.route('/interview')
def interview():

    questions = [
        "Tell me about yourself.",
        "What is Machine Learning?",
        "Explain OOP concepts.",
        "Difference between list and tuple?",
        "What is Flask?",
        "What are APIs?"
    ]

    return render_template(
        'interview.html',
        questions=questions
    )

if __name__ == '__main__':
    app.run(debug=True)
