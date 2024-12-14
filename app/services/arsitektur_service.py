import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, Dropout, LeakyReLU
from tensorflow.keras.layers import Input, Dense, Flatten, GlobalAveragePooling2D, MaxPooling2D
from tensorflow.keras.applications import InceptionV3
# from keras.applications.resnet import ResNet50


def make_model():
    ModelDenseNet201 = tf.keras.models.Sequential([
        tf.keras.applications.InceptionV3(input_shape=(224, 224, 3),
                                          include_top=False,
                                          pooling='max',
                                          weights='imagenet'),
        # tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        # 512 neuron hidden layer
        tf.keras.layers.Dense(2, activation='softmax')
    ])
    return ModelDenseNet201
