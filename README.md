# 智能搜索引擎项目

一个基于 Django 和 Whoosh 的中文全文搜索引擎，支持大规模文档搜索、文档预览和历史记录功能。

## 功能特点

### 1. 搜索功能
- 支持中文分词搜索
- 实时搜索结果预览
- 相关度排序
- 分页展示搜索结果
- 支持标题和内容的多字段搜索
- 空搜索提示功能

### 2. 用户界面
- 现代化的响应式界面
- 搜索结果卡片式展示
- 搜索结果预览功能（显示前200字）
- 文档详情页面
- 优雅的渐变背景
- 美观的卡片阴影效果
- 返回首页快捷导航

### 3. 分页功能
- 每页显示10条搜索结果
- 支持页码导航（首页、上一页、下一页、末页）
- 支持直接跳转到指定页码
- 显示当前页码和总页数
- 显示搜索结果总数
- 支持键盘回车跳转页面

### 4. 历史记录
- 记录最近5条搜索查询
- 显示搜索时间
- 显示每次搜索的结果数量
- 支持点击历史记录重新搜索
- 按时间倒序排列

## 项目依赖
- bash
-  Django>=4.0
- whoosh
- jieba
- faker
- tqdm
- requests
- beautifulsoup4


## 快速开始

1. 克隆项目并安装依赖：

```bash
git clone https://github.com/ChicaChan/Whoosh_search_ngine.git
cd Whoosh_search_ngine
pip install -r requirements.txt
```

2. 初始化数据库：

```bash
python manage.py makemigrations
python manage.py migrate
```

3. 创建超级用户（可选，用于后台管理）：

```bash
python manage.py createsuperuser
```

4. 导入测试数据：

```bash
python scripts/import_news_bulk.py


5. 创建搜索索引：

```bash
python manage.py update_index
```

6. 运行开发服务器：

```bash
python manage.py runserver
```

7. 访问网站：
- 搜索页面：http://127.0.0.1:8000
- 后台管理：http://127.0.0.1:8000/admin

## 项目结构
README.md
- search_engine_Django/
- ├── search/ # 主应用目录
- │ ├── models.py # 数据模型（Document和SearchHistory）
- │ ├── views.py # 视图函数
- │ ├── search_indexes.py # Whoosh搜索配置
- │ └── admin.py # 后台管理配置
- ├── templates/ # 模板目录
- │ └── search/
- │ ├── index.html # 搜索首页
- │ ├── search.html # 搜索结果页
- │ └── document_detail.html # 文档详情页
- ├── scripts/ # 数据导入脚本
- │ ├── import_news_bulk.py # 生成测试新闻数据
- │ └── import_wiki_bulk.py # 爬取维基百科数据
- └── manage.py # Django管理脚本
