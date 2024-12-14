from flask import jsonify, request
from app.services.logging_service import LoggerService
from app.services.ApiService import ApiService
from app.middleware.token_verify import TokenService
from app.services.arsitektur_service import make_model
import pandas as pd
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, \
    Flatten, Dense, Activation, Dropout, LeakyReLU
from tensorflow.keras.utils import load_img, img_to_array
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as ts
import argparse
import io
import re
import cv2
from PIL import Image
import io


logger_service = LoggerService()
logger = logger_service.get_logger()
token_service = TokenService()

# Instantiate the service classes
api_service = ApiService()

class RouteLogic:
    def __init__(self):
        self.company_id = None
        self.model = make_model()
        base_path = os.path.join(os.getcwd(), "app", "logic")
        self.file_model = self.model.load_weights(os.path.join(base_path, "dog_and_cat_InceptionV3.h5"))
        self.model_nlp = TFBertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone', num_labels=3)
        self.model_nlp.load_weights(os.path.join(base_path, "bert-model-danielmrnthh-uncased.h5"))
        self.tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

    @token_service.token_required
    def PredGambar(self):
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']

        allowed_extensions = {'png', 'jpg', 'jpeg', 'bmp', 'tiff'}
        if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions):
            return jsonify({'error': 'File must be an image with one of the following extensions: png, jpg, jpeg, bmp, tiff'}), 400

        try:
            image = Image.open(io.BytesIO(file.read()))
            image = image.resize((224, 224))
            image_array = np.array(image) / 255.0

            if image_array.shape[-1] != 3:
                return jsonify({'error': 'Image must have 3 color channels (RGB)'}), 400

            image_input = tf.reshape(image_array, shape=[1, 224, 224, 3])

            predik_array = self.model.predict(image_input)[0]

            df = pd.DataFrame(predik_array, columns=['NilaiKemiripan'])
            Kualitas = ['cats', 'dogs']
            df['Kelas'] = Kualitas
            df = df[['Kelas', 'NilaiKemiripan']]

            predik_kelas = np.argmax(predik_array)
            predik_kualitas = Kualitas[predik_kelas]

            response = {
                'predicted_class': predik_kualitas,
                'details': df.to_dict(orient='records')
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({'error': f'Error processing image: {str(e)}'}), 500


    @token_service.token_required
    def sentimen_analisis(self):
        if 'text' not in request.json:
            return jsonify({'error': 'No text provided'}), 400

        input_text = request.json['text']

        if not input_text.strip():
            return jsonify({'error': 'Input text cannot be empty'}), 400

        try:
            input_text_tokenized = self.tokenizer.encode(
                input_text,
                truncation=True,
                padding='max_length',
                return_tensors='tf'
            )

            bert_predict = self.model_nlp(input_text_tokenized)
            bert_output = tf.nn.softmax(bert_predict[0], axis=-1)

            Sentimen = ['neutral', 'negative', 'positive']

            terdeteksi = tf.argmax(bert_output, axis=1).numpy()
            predicted_sentiment = Sentimen[terdeteksi[0]]

            response = {
                'input_text': input_text,
                'predicted_sentiment': predicted_sentiment,
                'probabilities': {
                    'neutral': float(bert_output[0][0]),
                    'negative': float(bert_output[0][1]),
                    'positive': float(bert_output[0][2])
                }
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({'error': f'Error processing sentiment analysis: {str(e)}'}), 500

