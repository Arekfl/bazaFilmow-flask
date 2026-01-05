from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home_page():
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()
    return render_template('Index.html', movies=movies)

@app.route("/addMovie", methods=['GET'])
def addMovie():
    return render_template('add.html')

@app.route("/addMovie", methods=['POST'])
def addMovie_post():
    title = request.form['title']
    year = request.form['year']
    actors = request.form['actors']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO movies (title, year, actors) VALUES (?, ?, ?)',
                 (title, year, actors))
    conn.commit()
    conn.close()
    
    return redirect(url_for('home_page'))

@app.route("/deleteMovie/<int:movie_id>", methods=['POST'])
def deleteMovie(movie_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM movies WHERE ID = ?', (movie_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)