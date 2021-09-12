要安裝scrapy先確認以下安裝

easy_install -U pip
pip3 install cryptography
pip3 install scrapy

創建項目
scrapy startproject 項目名稱
ex : scrapy startproject anime

系統會創建
scrapy.cfg: 项目的配置文件
tutorial/: 该项目的python模块。之后您将在此加入代码。
tutorial/items.py: 项目中的item文件.
tutorial/pipelines.py: 项目中的pipelines文件.
tutorial/settings.py: 项目的设置文件.
tutorial/spiders/: 放置spider代码的目录.

第一步定義items