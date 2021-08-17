# Django-3-by-Example

myshop 项目
```
# Linux下开启celery worker  
celery -A myshop worker -l info

# windows下开启celery worker
# windows下运行celery 4以后版本，还需额外安装eventlet库
celery -A myshop worker -l info -P eventlet

# windows下如果报Pid错误  
celery -A myshop worker -l info --pool=solo

# 启用Flower监控任务执行状态
celery flower -A myshop --address=127.0.0.1 --port=5555
```
