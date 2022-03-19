# django-tutorial-15th
CEOS 15th 백엔드 Django-tutorial

## Refactoring

### mysite.settings.py
INSTALLED_APPS의 'polls.apps.PollsConfig'를 'polls'로 바꿈   
polls.apps.PollsConfig'가 더 정확한 표현하긴 하나 polls/__init__.py의 default_app_config = 'polls.apps.Polls'라 'polls'라고 적어도 똑같이 동작함


### polls.views.py
1. vote함수에서 가독성을 위해 context를 따로 빼서 적음
2. vote함수에서 return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))대신 django.shortcuts에 있는 redirect를 활용해 return redirect('polls:results', pk=question_id)로 바꿈

---------------------------------------
##알게된 내용

### 제너릭 뷰
1. 제네릭 뷰 사용하는 이유 : 매개 변수에 따라 데이터베이스에서 데이터를 가져 오는 것과 템플릿을 로드하고 렌더링 된 템플릿을 리턴하는
기본 웹 개발의 매우 일반적인 경우를 위해 Django는 "제너릭 뷰"시스템이라는 지름길을 제공함
2. from django.views import generic 
3. model속성 : 제너릭 뷰는 어떤 모델이 적용될 것인지 알아야 하므로 model 속성을 사용하여 제공
4. 제너릭 뷰는 URL에서 캡쳐 된 기본 키 값이 "pk" 라고 기대하기 때문에 urls.py에서 <int:pk>를 사용 & view이름 뒤에 .as_view()를 적어야함
5. template_name 속성: Django에게 자동 생성 된 기본 템플릿 이름 대신에 특정 템플릿 이름을 사용하도록 알려주기 위해 사용됨
6. def get_queryset(self): queryset을 queryset속성으로 받으면 고정적이므로 함수를 사용해 유동적으로 받기 위해 사용

### get_list_or_404
get_object_or_404() 함수처럼 동작    
But, get() 대신 filter() 를 쓴다는 것이 다르다.   
리스트가 비어있을 경우, Http404 예외를 발생시킴.


### Python 쉘
1. $ python manage.py shell 으로 들어가고 exit()으로 빠져나옴
2. from polls.models import Choice, Question ->  
q = Question(question_text="What's new?", pub_date=timezone.now()) -> q.save() 객체 생성
3. q = Question.objects.get(pk=1)으로 객체 하나를 가져와 q.choice_set.create(choice_text='Not much', votes=0) 
-> q.choice_set.all()    Choice모델이 Question모델을 FK로 사용할 때 위와 같이 사용 가능