from django.core.management.base import BaseCommand
from search.models import Document
from search.search_indexes import create_index
from datetime import datetime

class Command(BaseCommand):
    help = '更新Whoosh搜索索引'

    def handle(self, *args, **options):
        try:
            self.stdout.write('开始创建索引...')
            ix = create_index()
            writer = ix.writer()
            
            document_count = 0
            for document in Document.objects.all():
                writer.add_document(
                    id=str(document.id),
                    title=document.title,
                    content=document.content,
                    created_at=document.created_at
                )
                document_count += 1
            
            writer.commit()
            self.stdout.write(self.style.SUCCESS(f'成功更新搜索索引，共处理了 {document_count} 个文档'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'更新索引时发生错误: {str(e)}')) 