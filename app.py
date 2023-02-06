from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from app_service import AppService
import json

app = Flask(__name__)
appService = AppService();

files= []

@app.route('/')
def home():
    return "App Works V2!!!"


@app.route('/api/tasks')
def tasks():
    return appService.get_tasks()

@app.route('/api/task', methods=['POST'])
def create_task():
    request_data = request.get_json()
    task = request_data['task']
    return appService.create_task(task)


@app.route('/api/task', methods=['PUT'])
def update_task():
    request_data = request.get_json()
    return appService.update_task(request_data['task'])


@app.route('/api/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    return appService.delete_task(id)

@app.route('/upload')
def upload_file_p():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      open_file = open(f.filename, "r", encoding="utf8", errors='ignore')
      files.append(open_file.read())
      return 'file uploaded successfully'
