from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
# ORM의 역할 : SQL을 직접 작성하지 않아도 데이터베이스로 접근해 CRUD(조회/추가/수정/삭제)가 가능하게 해준다.

class Article(models.Model) :
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)

class User(models.Model):
    userid = models.CharField(max_length=64, verbose_name='아이디', primary_key=True)
    #charField는 문자열 필드
    # max_length 최대 길이, 길이 제한
    # verbose_name : 별칭
    username = models.CharField(max_length=64, verbose_name='사용자명', null=False)
    password = models.CharField(max_length=64, verbose_name='비밀번호', null=False)
    memberemail = models.EmailField(max_length=128, verbose_name='이메일', null=False)
    registered = models.DateTimeField(auto_now_add=True, verbose_name='등록')
  # DateTimeField auto_now_add=True -> 자동으로 DateTime값을 넣어줌
  # 0000-00-00 00:00:00 datetime
    GENDERS = (('M','남성(men)'), ('W', '여성(women)'))
    gender = models.CharField(max_length=1, verbose_name='성별', choices=GENDERS)

    ROOTSS = (('c','카페(cafe)'), ('s','검색(search)'))
    roots = models.CharField(max_length=1, verbose_name='가입 경로', choices=ROOTSS)

    ping_num = models.IntegerField(verbose_name='핑 상태')
    TEACHER = (('T','선생님(teacher)'), ('S', '학생(student)'))
    teachers = models.CharField(max_length=1, verbose_name='선생님', choices=TEACHER)

class Wine(models.Model):
    wine_name = models.CharField(max_length=64, verbose_name='와인명')
    wine_price = models.IntegerField(verbose_name='와인 가격')
    wine_photo = models.TextField(max_length=128, verbose_name='와인 사진')
    wine_discribe = models.TextField(max_length=255, verbose_name='와인 설명')
    
class manwine(models.Model):
    id_user = models.ForeignKey("User", related_name="user", on_delete=models.CASCADE, db_column="userid", verbose_name='구매자 아이디')
    name_wine = models.ForeignKey("Wine", related_name="wine", on_delete=models.CASCADE, db_column="wine_name", verbose_name='구매 와인')
    wine_num = models.IntegerField( verbose_name='구매 와인 수량')

  # enum('M', 'W') : 둘 중에 하나를 골라라

  # TextField (문자열)
  # IntegerField (숫자열)
  # Null = True (기본값은 False) : null을 허용한다(true)
  # default

