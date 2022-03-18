# django-tutorial-15th
CEOS 15th 백엔드 Django-tutorial

## 1주차
Django Tutorial Part. 1부터 Part. 4까지 따라하기

### path()의 인수
- route
  - path()의 필수 인수
  - URL 패턴을 가진 문자열
  - urlpatterns에서 일치하는 패턴을 찾는다.
  
- view
  - path()의 필수 인수
  - route를 이용하여 일치하는 패턴을 찾은 경우, 해당 view 함수를 호출한다.
  
- kwargs
  - 목표한 view에 사전형으로 전달한다.
  
- name
  - Django 어디에서나 명확하게 참조할 수 있도록 URL에 이름을 짓는다.

### model
- 부가적인 메타데이터를 가진 데이터베이스의 구조
- 데이터베이스의 각 필드는 Field 클래스의 인스턴스로 표현된다.
- Field 클래스들 중에는 필수 인수가 필요한 클래스가 있으며, 다양한 선택적 인수들을 가질 수 있다.

### model 변경 과정
1. models.py 에서 모델을 변경한다.
2. `python manage.py makemigrations`로 마이그레이션을 만든다.
3. `python manage.py migrate`로 데이터베이스에 적용한다.

### View 작동시키기
- HttpResponse 객체 반환
  1. 단순 방법
  ```python
  def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
  ```

  2. render()
  ```python
  def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
  ```

- Http404 예외 발생
  1. 단순 방법
  ```python
  def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
  ```

  2. get_object_or_404()
  ```python
  def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
  ```
  
### Generic View
- 일반적인 패턴을 추상화한 View
- URL에서 전달된 매개변수에 따라 데이터베이스에서 데이터를 가져오는 경우
- 템플릿을 로드하고 렌더링된 템플릿을 리턴하는 경우

### Generic View 사용하기
1. URLconf 수정
```python
  urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
  ```
  제너릭 뷰는 URL의 기본키 값을 pk로 인식하기 때문에 question_id를 pk로 변경한다.

3. views 수정
- ListView

  개체 목록 표시
```python
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
  ```
  
- DetailView

  특정 개체 유형에 대한 세부 정보 페이지 표시
```python
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
  ```
