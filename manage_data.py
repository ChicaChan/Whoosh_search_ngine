import os
import django

# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search_engine_Django.settings')
django.setup()

from search.models import Document

# 三国演义片段
text1 = """
细作探知这个消息，飞报吴国。孙权听到此报，便与众谋士商议。
鲁肃说道："荆州是国家重地，不可轻易放弃。明公可以写信与刘备，
说我们愿将荆州借给他暂时使用。待他取得益州之后，便将荆州还给我们。"
"""

# 水浒传片段
text2 = """
话说当下李逵便去房里收拾包裹，只见房门口走过一个人来，
却不是别人，正是杨志。李逵见了，便叫道："青面兽，你在这里做什么？"
杨志道："我特来寻你。"
"""

# 红楼梦片段
text3 = """
贾母因说："你们去罢，别处玩去。"王夫人等方退出，
让凤姐儿去梳头。贾母又说："你且别忙，我问你：前儿你说要办几件事，
可办了不曾？"凤姐儿回说："正要回老祖宗，都办妥了。"
"""

# 新闻数据
news_data = [
    {
        'title': '人工智能发展最新进展',
        'content': """
        近日，多家科技公司发布了最新的人工智能研究成果。
        其中包括自然语言处理、计算机视觉等多个领域的重要突破。
        专家表示，这些进展将推动人工智能技术在更多领域的应用。
        """
    },
    {
        'title': '环保技术创新',
        'content': """
        随着环保意识的提升，新能源技术不断突破。
        太阳能发电效率显著提高，风能利用率也达到新高。
        多项环保技术的创新为实现碳中和目标提供了有力支持。
        """
    }
]

# 文学作品数据
literature_data = [
    {
        'title': '三国演义片段',
        'content': text1
    },
    {
        'title': '水浒传片段',
        'content': text2
    },
    {
        'title': '红楼梦片段',
        'content': text3
    }
]

def import_all_data():
    # 导入文学作品
    print("正在导入文学作品...")
    for doc in literature_data:
        Document.objects.create(
            title=doc['title'],
            content=doc['content']
        )
    
    # 导入新闻
    print("正在导入新闻数据...")
    for news in news_data:
        Document.objects.create(
            title=news['title'],
            content=news['content']
        )
    
    print(f"成功导入 {len(literature_data) + len(news_data)} 个文档")

if __name__ == "__main__":
    import_all_data() 