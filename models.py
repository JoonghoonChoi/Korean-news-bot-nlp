import joblib
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Bidirectional, Dropout, SpatialDropout1D, Dense
from tensorflow.keras import regularizers


### NB model create
def identify_tokenizer(text):
    return text

def create_NB_model():
    model = joblib.load('nb_clf_model.pkl')
    return model


## BiLSTM model create
# 튜닝모델의 학습 가중치를 불러와서 모델 정의할 때 사용할 수 있는 모델 생성 함수
def create_tuner_model():
    max_features = 512818
    embedding_dim = 128
    maxlen = 1917

    model = Sequential()
    
    model.add(Embedding(max_features, embedding_dim, input_length=maxlen))
    model.add(SpatialDropout1D(0.3))

    model.add(Bidirectional(LSTM(160, return_sequences=True, kernel_regularizer=regularizers.l2(1e-06))))
    model.add(Bidirectional(LSTM(160)))

    model.add(Dropout(0.4))
    model.add(Dense(448, activation='tanh', kernel_regularizer=regularizers.l2(1e-06)))

    model.add(Dropout(0.4))
    model.add(Dense(4, activation='softmax'))

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    return model