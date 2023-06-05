from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)


# [{'class': 'ViratKholi', 
#   'class_probability': [11.66, 0.25, 80.55, 4.65, 2.89], 
#   'class_dictionary': {'Ronaldo': 0, 'pv_sindhu': 1, 'ViratKholi': 2, 'MSD': 3, 'serena_williams': 4}}]