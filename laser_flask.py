"""Flask server to host UI"""

import json

from flask_cors import CORS

from flask import Flask, request, redirect, jsonify, url_for

from laser_assistant import (svg_to_model,
                             get_original_model, process_web_outputsvg, LaserParameters)
from laser_svg_parser import model_to_svg_file

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

import csv
import sys

UPLOAD_FOLDER = './upload_csv'

# tell flask to host the front end
VUE_STATIC = "./laser_frontend/dist/"

# it's common practice to use lowercase app, so we'll ignore pep8 just this once
app = Flask(__name__, static_folder=VUE_STATIC)  # pylint: disable=invalid-name

# Allow VUE client to make requests to this API server
VUE_CLIENT = {"origins": "*"}
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"*": VUE_CLIENT})  # pylint: disable=invalid-name


def get_svg_response(filename):
    """returns a response with svg file"""
    svgfile = open(filename, "r")
    svgdata = svgfile.read()
    svgfile.close()
    response = app.response_class(
        response=svgdata,
        status=200,
        mimetype='image/svg+xml'
    )
    return response


@app.route('/')
def main_interface():
    """This is the root of the html interface"""
    return redirect('http://localhost:8080') # for development
    # return redirect('index.html')

@app.route('/presets', methods=['POST'])
def save_presets():
    """saves presets csv"""
    print("NOTE: preset saving not implemented yet!")
    #TODO: actually parse the preset CSV to make sure it has all the needed parameters
    #file = request.form['file']
    #print(file)
    #with open('presets.csv', 'w') as f:
    #    f.write(file)
    return ""

@app.route('/presets', methods=['GET'])
def load_presets():
    """loads presets csv"""
    presets = []
    #based on: https://docs.python.org/2/library/csv.html
    with open('presets.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                LaserParameters(row) #see if row can be parsed into LaserParameters
                presets.append(row)
            except:
                print("Skipping row because it failed to parse:", row)
    return json.dumps(presets)


@app.route('/get_design', methods=['GET', 'POST'])
def get_design():
    """returns design.svg"""
    if request.method == 'POST':
        model = json.loads(request.form['inputModel'])
        # params = json.loads(request.form['laserParams'])
        new_model = get_original_model(model)
        model_to_svg_file(new_model, design=model, filename="design.svg")
    return get_svg_response('design.svg')


@app.route('/get_output', methods=['GET', 'POST'])
def get_output():
    """returns output.svg"""
    if request.method == 'POST':
        model = json.loads(request.form['inputModel'])
        params = json.loads(request.form['laserParams'])
        print("Got parameters: ", params) #DEBUG
        params = LaserParameters(params)
        new_model = process_web_outputsvg(model, params)
        model_to_svg_file(new_model, design=model)
    return get_svg_response('output.svg')


@app.route('/get_model', methods=['POST'])
def get_model():
    """returns json model of svg posted"""
    svg_input = request.form['svgInput']
    svg_file = open("input.svg", "w")
    svg_file.write(svg_input)
    svg_file.close()
    model = svg_to_model('input.svg')
    return jsonify(model)


if __name__ == '__main__':
    app.run()
