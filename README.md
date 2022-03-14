# django-tutorial-15th
CEOS 15th 백엔드 Django-tutorial

### [1주차] 22/03/13
1. window / pycharm / powershell 가상환경 진입 `venv\Scripts\activate`
2. git status - .idea/ 폴더의 정체 = pycharm의 회사 IntelliJ 프로젝트별 생성파일
   (git ignore 에 추가해야 한다는 의견과 그렇지 않다는 의견이 갈린다)
---
#### [1주차] 과제
1. `python manage.py runserver` 
2. `python manage.py runserver 8080` pass the port number
3. To call the view(view.py), we need to map it to a URL(urls.py) - URLconf.
4. `include()` : including other URL patterns. (only exception -`admin.site.urls`)
5. `path()` : `path(route, view, kwargs, name)`
6. path() argument: (required) route, view
