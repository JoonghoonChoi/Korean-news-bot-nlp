def show_result(model, summarizer, texts,
                pred_class_lst_nb, pred_proba_lst_nb,
                pred_class_lst_bi, pred_proba_lst_bi,
                abs_summary_lst, ext_summary_lst):
    
    category_dict = {0:'생활/문화',
                    1:'정치/사회',
                    2:'경제/산업',
                    3:'과학/건강'}

    def print_by_length(text):
        '''
        코랩 노트북에서 print()하면 텍스트가 1열로 나와서 가독성이 안좋음
        텍스트 길이 80을 기준으로 잘라서 출력해주는 함수 구현
        '''
        if len(text) > 100:    
            start = 0
            end = 100
            for _ in range(1, int(len(text) / 80)+2):
                print(text[start:end])
                start = end
                end += 80
        else:
            print(text)
            
        '''쥬피터 노트북에서는 전체 출력하는게 가독성이 좋음'''
#         print(text)

    for i in range(len(texts)):
        print('[Original:]')
        print_by_length(texts[i])
        print('\n')

        print('[Category:]')
        if model == 'Naive-Bayes':
            # print('Naive-Bayse Classifier =>')
            print(f'{category_dict[pred_class_lst_nb[i]]} in {round(pred_proba_lst_nb[i]*100, 2)}%',)
        if model == 'BiLSTM':
            # print('BiLSTM Classifier => ')
            print(f'{category_dict[pred_class_lst_bi[i]]} in {round(pred_proba_lst_bi[i]*100, 2)}%')
        print('\n')

        print('[Summarization:]')
        if summarizer == 'Abstractive':
            # print('Abstraction =>')
            print_by_length(abs_summary_lst[i])
        if summarizer == 'Extractive':
            # print('Extraction =>')
            print_by_length(ext_summary_lst[i])
        print('\n')

        print('='*150, '\n')
