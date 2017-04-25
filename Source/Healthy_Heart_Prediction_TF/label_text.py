import tensorflow as tf, sys
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import base64
import numpy as np
# webapp
app = Flask(__name__)
#image_path = sys.argv[1]


@app.route('/api/predict', methods=['POST'])
@cross_origin()
def predict():
    input1 = request.values['value1']
    input2 = request.values['value2']
    input3 = request.values['value3']
    input4 = request.values['value4']
    input5 = request.values['value5']
    input6 = request.values['value6']
    input7 = request.values['value7']
    input8 = request.values['value8']
    input9 = request.values['value9']
    input10 = request.values['value10']
    input11 = request.values['value11']
    input12 = request.values['value12']
    input13 = request.values['value13']

    IRIS_TRAINING = "H_train.csv"
    IRIS_TEST = "H_test.csv"
    training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename=IRIS_TRAINING,
        target_dtype=np.int,
        features_dtype=np.float32)
    test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename=IRIS_TEST,
        target_dtype=np.int,
        features_dtype=np.float32)

    # Specify that all features have real-value data
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=13)]

    # Build 3 layer DNN with 10, 20, 10 units respectively.
    classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                                hidden_units=[30, 45, 30],
                                                n_classes=2,
                                                model_dir="model/combined/17")

    # Define the training inputs
    def get_train_inputs():
        x = tf.constant(training_set.data)
        y = tf.constant(training_set.target)

        return x, y

    # Fit model.
    classifier.fit(input_fn=get_train_inputs, steps=10000)

    # Define the test inputs
    def get_test_inputs():
        x = tf.constant(test_set.data)
        y = tf.constant(test_set.target)

        return x, y

    # Evaluate accuracy.
    accuracy_score = classifier.evaluate(input_fn=get_test_inputs,
                                         steps=1)["accuracy"]

    print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

    # Classify two new flower samples.
    def new_samples():
        h = [[45.0,1.0,4.0,115.0,260.0,0.0,2.0,185.0,0.0,0.0,1.0,0.0,3.0]]
        h[0][0]=input1
        h[0][1] = input2
        h[0][2] = input3
        h[0][3] = input4
        h[0][4] = input5
        h[0][5] = input6
        h[0][6] = input7
        h[0][7] = input8
        h[0][8] = input9
        h[0][9] = input10
        h[0][10] = input11
        h[0][11] = input12
        h[0][12] = input13


        print(h)
        print(h[0])
        print(h[0][0])
        return np.array(h,dtype=np.float32)
        '''
        return np.array(
            [[45.0,1.0,4.0,115.0,260.0,0.0,2.0,185.0,0.0,0.0,1.0,0.0,3.0],  # 1 output
             [45.0,1.0,4.0,115.0,260.0,0.0,2.0,185.0,0.0,0.0,1.0,0.0,3.0]], dtype=np.float32)  # 1 output
        '''

    #testip = [45.0,1.0,4.0,115.0,260.0,0.0,2.0,185.0,0.0,0.0,1.0,0.0,3.0]
    #testip=np.asarray(testip)
    predictions = list(classifier.predict(input_fn=new_samples))
    c= []
    print(predictions)
    for k in predictions:
        if k == 1:
            c.append("Given values indicate Presence of heart disease")
        elif k == 2:
            c.append("Given values indicate presence of heart disease")
    print(c)
    return jsonify(results=[c])

@app.route('/')
def main():
    return render_template('index.html')