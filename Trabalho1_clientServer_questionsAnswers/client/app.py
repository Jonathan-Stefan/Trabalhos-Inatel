import flask
from flask import render_template, request
import mysql.connector

app = flask.Flask(__name__)

# Conectar ao banco de dados MySQL
db_connection = mysql.connector.connect(
   host="mysql-container", # tem que ser o mesmo nome do container
   user="root",
   password="",
   database="trabalho1clienteservidor"
)

@app.route('/')
def index():
   cursor = db_connection.cursor() # abrindo a conexão dentro da função
   # Preparar e executar consulta SQL para obter questões do banco de dados
   cursor.execute("SELECT question, option1, option2, option3, option4 FROM questions")
   questions = cursor.fetchall()
   cursor.close() # fechando a conexão
   return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    # Processar respostas submetidas pelo formulário
    cursor = db_connection.cursor() # abrindo a conexão dentro da função
    score = 0
    for question, user_answer in request.form.items():
        cursor.execute("SELECT correct_answer FROM questions WHERE question = %s", (question,))
        correct_answer_db = cursor.fetchone()
        if correct_answer_db and user_answer == str(correct_answer_db[0]):
            score += 1
    return f'Respostas corretas: {score}'


if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port="5000")