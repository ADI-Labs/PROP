from flask import Flask

@app.route("/", methods=['POST'])
def process_image():
    img = request.form['image']
    timestamp = request.form['timestamp']
