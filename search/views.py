from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from whoosh.qparser import QueryParser, MultifieldParser
from whoosh import index
from django.conf import settings
from .models import Document, SearchHistory
import os

def search_view(request):
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    search_results = []
    
    if query:
        if os.path.exists(settings.WHOOSH_INDEX):
            try:
                ix = index.open_dir(settings.WHOOSH_INDEX)
                with ix.searcher() as searcher:
                    parser = MultifieldParser(["title", "content"], ix.schema)
                    q = parser.parse(query)
                    results = searcher.search(q, limit=None)
                    
                    search_results = [{
                        'id': r['id'],
                        'title': r['title'],
                        'content': r['content'][:200] + '...',  # 只显示预览
                        'score': r.score
                    } for r in results]
                    
                    # 保存搜索历史
                    SearchHistory.objects.create(
                        query=query,
                        results_count=len(search_results)
                    )
                    
                    search_results.sort(key=lambda x: x['score'], reverse=True)
            except Exception as e:
                print(f"搜索错误: {str(e)}")
                search_results = []
    
    # 分页处理
    paginator = Paginator(search_results, 10)  # 每页显示10条结果
    try:
        current_results = paginator.page(page)
    except PageNotAnInteger:
        current_results = paginator.page(1)
    except EmptyPage:
        current_results = paginator.page(paginator.num_pages)
    
    # 获取最近的搜索历史
    recent_searches = SearchHistory.objects.all()[:5]
    
    return render(request, 'search/search.html', {
        'query': query,
        'results': current_results,
        'recent_searches': recent_searches
    })

def index_view(request):
    # 获取最近的搜索历史
    recent_searches = SearchHistory.objects.all()[:5]
    return render(request, 'search/index.html', {
        'recent_searches': recent_searches
    })

def document_detail(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    return render(request, 'search/document_detail.html', {
        'document': document
    }) 