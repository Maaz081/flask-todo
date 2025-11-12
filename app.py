from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list (reset when the server restarts)
tasks = []

@app.route('/')
def index():
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task', '').strip()
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
