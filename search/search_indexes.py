from whoosh.fields import Schema, TEXT, ID, DATETIME
from whoosh.analysis import StemmingAnalyzer, RegexAnalyzer, KeywordAnalyzer
from jieba.analyse import ChineseAnalyzer
from whoosh import index
from django.conf import settings
import os

def create_schema():
    chinese_analyzer = ChineseAnalyzer()
    return Schema(
        id=ID(stored=True, unique=True),
        title=TEXT(stored=True, analyzer=chinese_analyzer),
        content=TEXT(stored=True, analyzer=chinese_analyzer),
        created_at=DATETIME(stored=True)
    )

def create_index():
    if not os.path.exists(settings.WHOOSH_INDEX):
        os.makedirs(settings.WHOOSH_INDEX)
    
    schema = create_schema()
    return index.create_in(settings.WHOOSH_INDEX, schema) 