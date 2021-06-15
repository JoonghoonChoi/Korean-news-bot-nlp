from konlpy.tag import Mecab
import re
import pandas as pd
from pororo import Pororo

get_summary_abs = Pororo(task='summary', lang='kr', model='abstractive')
get_summary_ext = Pororo(task='summary', lang='kr', model='extractive')

def get_cleaning_lst(texts):
    
    print('텍스트를 정제중입니다...')
    def text_cleaning_get_tokens(text):

        mecab = Mecab()

        def text_preprocessing(txt):
            find_email = '[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]+[a-zA-Z0-9]'
            get_email = re.search(find_email, txt)
            if get_email:
                txt = txt[:get_email.start()] + txt[get_email.end():]
            txt = re.sub('[^가-힣a-zA-Z ]', '', txt)
            txt = re.sub('[ ]+', ' ', txt)
            remove_msg = re.search('flash 오류를 우회하기 위한 함수 추가 function flashremoveCallback', txt)
            if remove_msg != None:
                txt = txt[:remove_msg.start()] + txt[remove_msg.end():]
            remove_msg = re.search('코로나 현황 속보 가장 확실한 SBS 제보 클릭 제보하기', txt)
            if remove_msg != None:
                txt = txt[:remove_msg.start()] + txt[remove_msg.end():]
            txt = txt.replace('앵커', '')

            txt = txt.strip()
            return txt

        def text_to_morphs(txt, tokenizer=mecab):
            stop_words = pd.read_csv('한국어불용어100.txt', sep='\t', header=None)
            stop_words = stop_words[0].tolist()
            add_stop_words = ['에서', '의', '을', '를', '이', '가', '는', '은', 'search', '에', '앵커', '기자']
            for word in add_stop_words:
                stop_words.append(word)
            stop_words = list(set(stop_words))

            morphs = tokenizer.morphs(txt)
            tokens = [m for m in morphs if m not in stop_words]
            return tokens

        text = text_preprocessing(text)
        tokens = text_to_morphs(text)

        return text, tokens


    tokens_lst = []
    clean_text_lst = []
    abs_summary_lst = []
    ext_summary_lst = []
    
    for text in texts:
        clean_text, tokens = text_cleaning_get_tokens(text)
        tokens_lst.append(tokens)
        clean_text_lst.append(clean_text)
        abs_summary_lst.append(get_summary_abs(clean_text))
        ext_summary_lst.append(get_summary_ext(clean_text))
    
    return tokens_lst, clean_text_lst, abs_summary_lst, ext_summary_lst