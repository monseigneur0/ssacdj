from django.shortcuts import render
from .models import User #data
from django.views.decorators.csrf import csrf_exempt #token err

from django.http import HttpResponseRedirect, request
from .forms import UploadFileForm 
# to uplaod files
import random
import os
# Imaginary function to handle an uploaded file.


def upload_file(request):
      if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                  handle_uploaded_file(request.FILES['file'])
                  return render(request, "uplaod.html", {'fil': request.FILES['file'].name })
                  # return HttpResponseRedirect('/success/url/')
      else:
            form = UploadFileForm()
      return render(request, 'upload.html', {'form': form})
def handle_uploaded_file(f):
      with open(os.path.abspath('./member/static/' + f.name), 'wb+') as destination:
            for chunk in f.chunks():
                  destination.write(chunk)


def hello(req) :
      return render(req, "a.html" ) 
def rec(req) :
      new_member = User( userid = req.POST.get('id'), username = req.POST.get('name'), password = req.POST.get('pw'), gender = req.POST.get('gender'),)
      new_member.save() 
      return render(req, 'tttt.html', {'username':req.POST.get('name'), 'info2':req.POST.get('address')} )
def send(req) :
      return render(req, 'd.html', {'info1':req.POST.get('name'), 'info2':req.POST.get('address')} )
def novel1(req,chapter, player1,player2) :
      return render(req, 'e.html', {"n1":chapter, "p1":player1 , "p2": player2 } )
def static(req) :
      return render(req, 'f.html')
def schedule(req) :
      return render(req, 'g.html')
def login(req) :
      return render(req, 'login.html')
def join(req) :
      return render(req, 'join.html')
def search(req) :
      all_member = User.object.filter(username="김탁호", password="1234")
      return render(req, 'join.html', {'total_member : all_member'} )
def logged(req) :
      logged_member = User.objects.filter( userid = req.POST.get('user_id'))
      if logged_member :
            req.session['userid'] = req.POST.get('user_id')
            #req.session.get['userid'] 
            #세션 저장
            #req.session['password'] = req.POST.get('pwd')
            #세션 로드
            #req.session.get['password'] = req.POST.get('pwd')
            #세션삭제
            #req.session.pop['password'] = req.POST.get('pwd')
            #alert(req.session['userid'])
            print("로그인 성공")
            return render(req, 'success.html',{'total_member' : logged_member[0]} )
      elif req.session.get('userid') :
            print(req.session.get('userid'))
            logged_member = User.objects.filter( userid = req.session.get('userid'))
            # logged_member = User.objects.filter( userid = req.session.get('userid'))
            #return render(req,'logged.html',{'total_member' : req.session.get('userid')})
            #return render(req,'check.html')
            print("세션 로드 성공")
            return render(req,'success.html', {'total_member' : logged_member[0]})
      else: 
            print("로그인실패")
            return render(req, 'login.html')
def check(req) :
      if req.session.get('userid') :
            print(req.session.get('userid'))
            logged_member = User.objects.filter( userid = req.session.get('userid'))
            #return render(req,'logged.html',{'total_member' : req.session.get('userid')})
            #return render(req,'check.html')
            return render(req,'check.html', {'total_member' : logged_member[0]})
      else :
            return render(req, 'login.html')
def logout(req) :
      req.session.pop('userid')
      return render(req, 'login.html')
def change(req) :
      return render(req, 'change.html')
def changed(req) :
      logged_member = User.objects.get( userid = req.POST.get('user_id'),)
      if logged_member :
            user = User.objects.get(userid = req.POST.get('user_id'))
            print("비밀번호 변경")
            print(logged_member)
            user.password = req.POST.get('pw_changed')
            user.save()  
            return render(req, 'success.html', {'total_member' : logged_member[0]})
      else :
            print("로그인실패")
            return render(req, 'failure.html')
def delete(req) :
      #   records = User.objects.all()
      #   records.delete()
      return render(req, 'delete.html')
def deleted(req) :
      logged_member = User.objects.filter( userid = req.POST.get('user_id'), password = req.POST.get('pwd'))
      if logged_member :
            user = User.objects.get(userid = req.POST.get('user_id'))
            print(user)
            user.delete()
            print("유저정보 삭제")
            return render(req, 'deleted.html')
      else :
            print("유저정보 확인 실패")
            return render(req, 'logged.html')
def login2(req) :
      if req.session.get('userid') :
            print(req.session.get('userid'))
            #return render(req,'logged.html',{'total_member' : req.session.get('userid')})
            #return render(req,'check.html')
            print("세션 로드 성공")
            return render(req,'tttt.html')
      else :
            return render(req,'tttt.html')
# 'parameter1' : req.POST.get( 'id_' ), 'parameter2' : req.POST.get( 'pw_' )}
def ajax2(req) :
      logged_member = User.objects.get( userid = req.POST.get('id_'), password = req.POST.get('pw_'))
      print(req.POST.get('id_'))
      print(req.POST.get('pw_'))
      print(logged_member.password)
      if logged_member.password:
            req.session['userid'] = req.POST.get('id_')
            #req.session.get['userid'] 
            #세션 저장
            #req.session['password'] = req.POST.get('pwd')
            #세션 로드
            #req.session.get['password'] = req.POST.get('pwd')
            #세션삭제
            #req.session.pop['password'] = req.POST.get('pwd')
            #alert(req.session['userid'])
            print(req.session.get('userid'))
            print("로그인 성공")
            print(logged_member)
            return render(req, 'ttt3.html',{'total_member' : logged_member })
      elif req.session.get('userid') :
            print(req.session.get('userid'))
            #return render(req,'logged.html',{'total_member' : req.session.get('userid')})
            #return render(req,'check.html')
            print("세션 로드 성공")
            return render(req,'ttt3.html', {'total_member' : logged_member })
      else:      
            print("로그인실패")
            return render(req, 'failure.html',)
def multibox(req) :

      return render(req, 'multibox.html')
def multiview(req) :
      # fruits = req.POST.getlist('fruit')
      return render(req, 'multiboxview.html', {'objects': req.POST.getlist('fruit')})

      # {'info1':req.POST.getlist('objects'), 'info2':req.POST.get('objects')}
def ping(req) :
      return render(req, 'ping.html')
def gprat(req) :
      return render(req, 'gprat.html')
