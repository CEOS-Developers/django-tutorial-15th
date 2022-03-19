# django-tutorial-15th
CEOS 15th 백엔드 Django-tutorial

### [1주차] Git/Github 사용법, Python 가상환경, Django 기본, MTV 패턴 


<details>
<summary></summary>
<div markdown="1">
   
--- 
1. window / pycharm / powershell 가상환경 진입 `venv\Scripts\activate`
2. git status - .idea/ 폴더의 정체 = pycharm의 회사 IntelliJ 프로젝트별 생성파일  
   (git ignore 에 추가해야 한다는 의견과 그렇지 않다는 의견)
---

      [1] Step 1 : Run Server
    

- `python manage.py runserver` 
- `python manage.py runserver 8080` pass the port number
- To call the view(view.py), we need to map it to a URL(urls.py) - URLconf.
- `include()` : including other URL patterns. (only exception -`admin.site.urls`)
- `path()` : `path(route, view, kwargs, name)`
- path() argument: (required) route, view

---

   
      [2] Step 2 : Database Setting


- `TimeZone` : setting.py -> `TIME_ZONE ='Asia/Seoul'`, `USE_TZ = False`
- `python manage.py migrate` :  creates any necessary database tables
- `models.CharField(max_length=)` : `max_length` is required
- Model 변경
```
- Modify `models.py`
- `python manage.py makemigrations polls`
- `python manage.py migrate`
```
- DATABASE API : use double underscores to separate relationships.
``` 
e.g ) `question__pub_date__year`, `choice_text__startswith`
```
---

      [3] Step 3 : View & Templates


- `app_name = 'polls'` => `polls:detail`.
---



      [4] Step 4 : Form & Generic Views System



- Generic View
```
- URLconf 변환
- 불필요한 오래된 보기 중 일부 삭제
- Django의 generic view 사용
```

- `DetailView 제너릭 뷰`는 URL에서 캡쳐 된 기본 키 값이 `pk` 라고 기대
---
</div>
</details>
