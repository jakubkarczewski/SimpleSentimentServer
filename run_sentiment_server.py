from keras.models import load_model
from keras.datasets import imdb
from keras.preprocessing import sequence
import numpy as np
import flask
import tensorflow as tf


# initialize our Flask application and Keras model
app = flask.Flask(__name__)

# todo: initialize global variables for graph and model


def prepare_model():
    """Loads model for sentiment analysis and it's graph."""
    # todo: load model
    # todo: load graph
    raise NotImplementedError


def get_imdb_vocab():
    """Returns a dict with mappings: word -> int used in Keras IMDB dataset."""
    word_index = imdb.get_word_index()
    word_index = {k: (v + 3) for k, v in word_index.items()}
    word_index["<PAD>"] = 0
    word_index["<START>"] = 1
    word_index["<UNK>"] = 2
    word_index["<UNUSED>"] = 3
    return word_index


def preprocess(text, maxlen=80):
    """Performs necessary preprocessing on text used for inference."""
    # todo: get dictionary
    # todo: split text into words
    # todo: convert words into imdb ints
    # todo: cast to array and perform padding
    raise NotImplementedError


@app.route("/predict", methods=["POST"])
def predict():
    """Returns result of inference using data from incoming POST request."""
    # initialize the data dict that will be returned
    data = {"success": False}

    # ensure we received valid text
    if flask.request.method == "POST":
        if 'text' in flask.request.get_json():
            assert len(flask.request.get_json()['text']) > 0

            # todo: extract text from query
            # todo: preprocess text
            # todo: perform inference (hint: need context manager)
            # todo: convert prediction into some sensible message i.e. it was pos/neg

            data['predictions'] = None  # todo: assign return message
            data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)


if __name__ == "__main__":
    print("* Loading Keras model and Flask starting server... \n  Please wait until server has fully started")
    # todo: prepare model for inference
    app.run()
