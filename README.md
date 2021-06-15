# Korean-newsbot-nlp

## on Google-Colab-Notebook
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
