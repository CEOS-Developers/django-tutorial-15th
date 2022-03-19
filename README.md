# django-tutorial-15th

CEOS 15th 백엔드 Django-tutorial

### 1주차 과제<hr>

#### 파트 2<p>

- 로컬 시간 설정
  - settings.py `TIME_ZONE='Asia/Seoul'`<br>

#### 파트 3<p>

- URL namespace
  - 특정 앱 URL 구분
  - 앱 이름/urls.py `app_name='앱 이름'`
  - index.html `{% url '앱 이름:함수명' %}`

#### 파트 4<p>

- 제너릭 뷰
  - 자주 등장하는 일반적인 패턴 추상화
  - 간결한 코드 작성 가능
  - <https://docs.djangoproject.com/en/4.0/ref/class-based-views/>
