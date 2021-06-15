from ipywidgets import widgets
from IPython.display import display, clear_output
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from rkcrawler import rknews_crwaler
from cleaning import get_cleaning_lst
from result import show_result
from models import identify_tokenizer, create_NB_model, create_tuner_model

def widget():
    # widgets buttons
    models = ('Naive-Bayes', 'BiLSTM')
    summarizers = ('Abstractive', 'Extractive')

    newsnum = widgets.BoundedIntText(value=5, min=1, max=10, step=1, description='Article cnt', disabled=False, layout=widgets.Layout(width='25%', height='40px'))                         
    model_select = widgets.Dropdown(options=models, description='Classifier', layout=widgets.Layout(width='25%', height='40px'))
    summarizer_select = widgets.Dropdown(options=summarizers, description='Summarizer', layout=widgets.Layout(width='25%', height='40px'))
    getnews = widgets.Button(description='Check Ranking News', layout=widgets.Layout(width='25%', height='80px'))
    output = widgets.Output()
    clear = widgets.Button(description='Clear all', layout=widgets.Layout(width='25%', height='40px'))
        
    def getnews_click(b, identify_tokenizer=identify_tokenizer):

        texts = rknews_crwaler(newsnum.value)
        tokens_lst, clean_text_lst, abs_summary_lst, ext_summary_lst = get_cleaning_lst(texts)
        
        print('기사를 요약중입니다. 잠시만 기다려주세요!')
        
        vectorizer = pickle.load(open('tfidf.pickle', 'rb'))
        X = vectorizer.transform(tokens_lst)
        NB_clf = create_NB_model()
        
        tokenizer = pickle.load(open('tokenizer.pickle', 'rb'))
        X_encoded = tokenizer.texts_to_sequences(clean_text_lst)
        X_padding = pad_sequences(X_encoded, maxlen=1917)
        BiLSTM_clf = create_tuner_model()
        BiLSTM_clf.load_weights('BiLSTM-weights-best-usingAugumentation-kerastuner.hdf5')

        pred_class_lst_nb = NB_clf.predict(X)
        pred_proba_lst_nb = [max(x) for x in NB_clf.predict_proba(X)]
        pred_bi = BiLSTM_clf.predict(X_padding)
        pred_proba_lst_bi = [max(x) for x in pred_bi]
        pred_class_lst_bi = np.argmax(pred_bi, axis=1)
    
        model = model_select.value
        summarizer = summarizer_select.value

        with output:
            clear_output()
            show_result(model, summarizer, texts,
                        pred_class_lst_nb, pred_proba_lst_nb,
                        pred_class_lst_bi, pred_proba_lst_bi,
                        abs_summary_lst, ext_summary_lst)

    def clear_all(b):
        with output:
            clear_output()
            print('='*150)
            
    display(newsnum, model_select, summarizer_select, getnews, clear, output)
    getnews.on_click(getnews_click)
    clear.on_click(clear_all)