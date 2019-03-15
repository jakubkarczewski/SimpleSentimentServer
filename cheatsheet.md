# Cheat Sheet

Load model in Keras:
```keras.models.load_model(path)```

Get global, default TF graph:
```tensorflow.get_default_graph()```

Pad sequences to the same length
````keras.preprocessing.sequence.pad_sequences(array, maxlen=maxlen)````

Get json body of request:
```flask.request.get_json()```

Perform inference in Keras (need to have ```model``` first)
```model.predict(data)```