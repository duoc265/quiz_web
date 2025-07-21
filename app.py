from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        df = pd.read_excel("questions_trac_nghiem.xlsx")
        first_question = df.iloc[0]["question"]
    except:
        first_question = "Không đọc được file câu hỏi."

    return render_template_string("<h1>Câu hỏi đầu tiên:</h1><p>{{q}}</p>", q=first_question)
