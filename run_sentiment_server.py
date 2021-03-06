from keras.models import load_model
from keras.datasets import imdb
from keras.preprocessing import sequence
import numpy as np
import flask
from flask import request
import tensorflow as tf


# initialize our Flask application and Keras model
app = flask.Flask(__name__)

# todo: initialize global variables for graph and model
model = None
graph = None


def prepare_model():
    """Loads model for sentiment analysis and it's graph."""
    global model, graph
    # todo: load model
    model = load_model('./model.h5')
    # todo: load graph
    graph = tf.get_default_graph()


def get_imdb_vocab():
    """Returns a dict with mappings: word -> int used in Keras IMDB dataset."""
    word_index = imdb.get_word_index()
    word_index = {k: (v + 3) for k, v in word_index.items()}
    word_index['<PAD>'] = 0
    word_index['<START>'] = 1
    word_index['<UNK>'] = 2
    word_index['<UNUSED>'] = 3
    return word_index


def preprocess(text, maxlen=80):
    """Performs necessary preprocessing on text used for inference."""
    # todo: get dictionary
    vocab = get_imdb_vocab()
    # todo: split text into words
    words = text.lower().replace('!', '').replace('?', '').replace('.', '').split()
    # todo: convert words into imdb ints
    unknown = vocab['<UNK>']
    ints = [vocab.get(word, unknown) for word in words]
    # todo: cast to array and perform padding
    arr = [np.array(ints)]
    padded = sequence.pad_sequences(arr, maxlen=maxlen)
    return padded


@app.route("/predict", methods=["POST"])
def predict():
    """Returns result of inference using data from incoming POST request."""
    # initialize the data dict that will be returned
    data = {"success": False}

    # ensure we received valid text
    if 'text' in request.get_json():
        assert len(request.get_json()['text']) > 0

        # todo: extract text from query
        text = request.get_json()['text']
        # todo: preprocess text
        preprocessed = preprocess(text)
        # todo: perform inference (hint: need context manager)
        with graph.as_default():
            preds = model.predict(preprocessed)[0][0]

        data['predictions'] = float(preds)  # todo: assign return message
        data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)


if __name__ == "__main__":
    print("* Loading Keras model and Flask starting server... \n  Please wait until server has fully started")
    # todo: prepare model for inference
    prepare_model()
    app.run()
