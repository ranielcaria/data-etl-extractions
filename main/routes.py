import os
from flask import request, redirect, flash

# Define where files go based on your tree
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'api', 'input')

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        flash("File uploaded successfully to api/input!")
        return redirect('/')