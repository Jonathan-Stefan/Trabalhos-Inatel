from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Conectar ao banco de dados MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="trabalho1clienteservidor"
)
cursor = db_connection.cursor()

@app.route('/')
def index():
    # Preparar e executar consulta SQL para obter questões do banco de dados
    cursor.execute("SELECT question, option1, option2, option3, option4 FROM questions")
    questions = cursor.fetchall()
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    # Processar respostas submetidas pelo formulário
    score = 0
    for question in request.form:
        correct_answer = request.form[question]
        cursor.execute("SELECT correct_answer FROM questions WHERE question = %s", (question,))
        correct_answer_db = cursor.fetchone()
        if correct_answer_db and correct_answer == correct_answer_db[0]:
            score += 1
    return f'Seu placar é: {score}'


if __name__ == '__main__':
    app.run(debug=True)
