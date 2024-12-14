from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)
DATABASE = 'blog.db'

# Database initialization
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Insert new post into database
        title = request.form['title']
        content = request.form['content']
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
            conn.commit()
        return redirect('/')

    # Fetch all posts from the database
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, created_at FROM posts ORDER BY created_at DESC")
        posts = cursor.fetchall()

    # Simple HTML layout
    return f"""
    <html>
        <head><title>Simple Blog</title></head>
        <body>
            <h1>Simple Blog</h1>

            <h2>Create a New Post</h2>
            <form method="POST">
                <label>Title:</label><br>
                <input type="text" name="title" required><br><br>
                <label>Content:</label><br>
                <textarea name="content" required></textarea><br><br>
                <button type="submit">Submit</button>
            </form>

            <h2>All Posts</h2>
            <ul>
                {''.join([f'<li><strong>{post[1]}</strong><br>{post[2]}</li>' for post in posts])}
            </ul>
        </body>
    </html>
    """

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
