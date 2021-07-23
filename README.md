# Korean-newsbot-nlp ([Presentation slide file](https://drive.google.com/file/d/1G7kpK4jrQVj3mOMMveB9UQRRnJ_V6PP0/view?usp=sharing/))
[네이버 랭킹뉴스](https://news.naver.com/main/ranking/popularDay.nhn?mid=etc&sid1=111) 로부터 가져온 기사를  4개의 카테고리(생활/문화, 정치/사회, 경제/산업, 과학/건강)로 분류하고 [Pororo package](https://github.com/kakaobrain/pororo)를 사용해 기사를 요약해주는 모델입니다.

![ezgif com-gif-maker](https://user-images.githubusercontent.com/74339882/122059104-41ec8c80-ce27-11eb-96d6-61f4e1241294.gif)

## Background
- 국내 신문, 뉴스, 잡지 등 정기간행물 등록사는 23,000여 개 ([문화체육관광부 정기간행물 등록시스템](https://pds.mcst.go.kr/main/regstatus/selectRegStatusDetail.do) 기준)
- 각종 웹사이트 혹은 어플리케이션을 통해 어디서든 접할 수 있는 정보 매체
- 기사의 전반 내용을 가늠할 수 없는 자극적인 헤드라인

<img width="600" alt="Screen Shot 2021-06-15 at 23 00 47" src="https://user-images.githubusercontent.com/74339882/122066245-8e3acb00-ce2d-11eb-8d5d-0791fe8e4be9.png">


## Results(Classifier)
- ML model: Naive-Bayse
- DL model: Bidirectional LSTM<br>

✏ Naive-Bayse ML 모델과 튜닝 전 후 BiLSTM 세 개의 모델의 성능 비교<br>
✏ 불균형한 데이터를 고려하여 f1 macro average 를 중점으로 모델 성능 개선<br>
✏ 모든 성능 지표에서 기본 ML 모델이 더 뛰어난 성능을 보임

<img width="300" alt="Screen Shot 2021-06-15 at 22 22 36" src="https://user-images.githubusercontent.com/74339882/122060353-76ad1380-ce28-11eb-95c0-e6dd91609929.png"><img width="300" alt="Screen Shot 2021-06-15 at 22 22 44" src="https://user-images.githubusercontent.com/74339882/122060363-790f6d80-ce28-11eb-84ed-4ef122bd5906.png"><img width="300" alt="Screen Shot 2021-06-15 at 22 22 55" src="https://user-images.githubusercontent.com/74339882/122060366-7a409a80-ce28-11eb-85bb-89c24031651e.png">

## Using on Google-Colab-Notebook
~~~python
!git clone https://github.com/JoonghoonChoi/Korean-newsbot-nlp.git
~~~
~~~python
# Mecab-ko-for-GoogleColab
!git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git
%cd Mecab-ko-for-Google-Colab
!bash install_mecab-ko_on_colab190912.sh
~~~
~~~python
import os
os.chdir('/content/Korean-newsbot-nlp')
~~~
~~~python
# git lfs file(.hdf5) pull
!sudo apt-get install git-lfs
!git lfs pull
~~~
~~~python
# Some packages get problems when installing
# Because I made requirements.txt file on colab
# Notwithstanding these errors, Our newsbot.widget() will be workging well
!pip install -r requirements.txt --q
~~~
~~~python
from rkcrawler import rknews_crwaler
from cleaning import get_cleaning_lst
from result import show_result
from models import identify_tokenizer, create_NB_model, create_tuner_model
import newsbot

newsbot.widget()
~~~

## Issues
- 코랩 및 로컬 환경에서 git clone 후 모델 테스트 중 git lfs 용량 초과 이슈 발생
- git lfs 관련해서 현재 사용가능한 bandwidth를 모두 사용한 것으로 나타납니다. (그림참조)
<img width="600" alt="Screen Shot 2021-06-15 at 21 19 59" src="https://user-images.githubusercontent.com/74339882/122051775-ef5ba200-ce1f-11eb-86c4-45867fb45223.png">

- 링크를 통해 .hdf5 가중치 파일을 별도로 다운받을 수 있습니다. ([다운로드링크](https://drive.google.com/file/d/1952SfHCgEXpuDxapDb_xRQxEmQGt9ye8/view?usp=sharing))
- 이미 bandwidth 용량이 초과하였기 때문에 해당 레포를 clone 후 .hdf5 파일을 사용할 수 없습니다. <br>(레포를 포킹한 이후 git clone하면 포킹한 사용자의 bandwidth로 할당되므로 사용가능 한 듯?)
- [git lfs 관련 안내링크](https://docs.github.com/en/github/managing-large-files/versioning-large-files/about-storage-and-bandwidth-usage)
<img width="600" alt="Screen Shot 2021-06-15 at 21 42 23" src="https://user-images.githubusercontent.com/74339882/122054427-9f320f00-ce22-11eb-8768-b33f8fd65eef.png">

## Feedback
✏ 데이터 증강을 사용해서 데이터불균형 문제를 처리해 줄 수 있지 않을까?<br>
✏ 기사 카테고리를 나누는 분류 문제에서 딥러닝 모델은 비효율적인가?<br>
✏ 오픈소스 패키지가 아닌 전이학습을 사용해 직접 요약모델 구축해보기

## References
- 분류기 학습을 위한 19,000여 개의 인터넷 뉴스 데이터 사용: [한국과학기술정보연구원과 충남대학교가 공동 개발한 정보검색시스템 평가를 위한 한글 테스트 컬렉션](http://kristalinfo.dynu.net/TestCollections/)
- [Pororo pacakge by Kakaobrain](https://github.com/kakaobrain/pororo)
- [이중번역을 활용한 텍스트 데이터 증강](https://hong-yp-ml-records.tistory.com/102)
- [keras-tuner tuning](https://www.sicara.ai/blog/hyperparameter-tuning-keras-tuner)
