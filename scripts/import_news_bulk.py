import os
import sys
import django
import json
import random
from faker import Faker
from tqdm import tqdm

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search_engine_Django.settings')
django.setup()

from search.models import Document

fake = Faker(['zh_CN'])

topics = [
    "科技", "教育", "经济", "文化", "体育", "娱乐", "医疗", 
    "环保", "政治", "军事", "社会", "历史", "艺术", "旅游"
]

def generate_article():
    """生成一篇假新闻文章"""
    topic = random.choice(topics)
    title = f"{topic}：{fake.sentence()}"
    
    # 生成3-5段落的内容
    paragraphs = [fake.paragraph() for _ in range(random.randint(3, 5))]
    content = "\n".join(paragraphs)
    
    return {
        'title': title,
        'content': content
    }

def import_bulk_news(num_articles=10000):
    """批量生成并导入新闻文章"""
    print(f"开始生成{num_articles}篇文章...")
    
    for i in tqdm(range(num_articles)):
        article = generate_article()
        Document.objects.create(
            title=article['title'],
            content=article['content']
        )
        
        if (i + 1) % 1000 == 0:
            print(f"\n已生成 {i + 1} 篇文章")

if __name__ == "__main__":
    try:
        print("开始生成新闻文章...")
        import_bulk_news(10000)  # 生成10000篇文章
        print("生成完成！")
    except Exception as e:
        print(f"发生错误: {str(e)}") 