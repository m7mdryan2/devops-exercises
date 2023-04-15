from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['todolist']
collection = db['tasks']

class Task:
    def __init__(self, content, date_created):
        self.content = content
        self.date_created = date_created

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Task(content=task_content, date_created=datetime.utcnow())

        try:
            collection.insert_one(new_task.__dict__)
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = [Task(**task) for task in collection.find().sort('date_created')]
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<id>')
def delete(id):
    try:
        collection.delete_one({'_id': ObjectId(id)})
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    task = Task(**collection.find_one({'_id': ObjectId(id)}))

    if request.method == 'POST':
        task.content = request.form['content']
        task.date_created = datetime.utcnow()

        try:
            collection.update_one({'_id': ObjectId(id)}, {'$set': task.__dict__})
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
