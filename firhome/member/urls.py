from django.urls import path, re_path
from . import views

app_name = 'user'
urlpatterns = [
      path("ok", views.hello ),
      path("send", views.send ),
      path("rec", views.rec ),
      path("novel/<int:chapter>/<str:player1>/<str:player2>", views.novel1),
      path("static", views.static ),
      path("login", views.login ),
      path("join", views.join ),
      path("search", views.search ),      
      path("logged", views.logged ),
      path("delete", views.delete ),
      path("deleted", views.deleted ),
      path("changed", views.changed ),
      path("change", views.change ),
      path("check", views.check ),
      path("logout", views.logout ),
      path("schedule", views.schedule ),
      path("ajax", views.ajax2),
      path("login2", views.login2 ),
      path("upload", views.upload_file),
      path("multibox", views.multibox),
      path("multiview", views.multiview),
      path("ping", views.ping),
      path("homeboot", views.homeboot),
      path("gprat", views.gprat),
      path("buy", views.buy, name='buy'),
      path("shop", views.shop),
      path("wineup", views.wineup),
      re_path(r'^buy/(?P<pk>[0-9]+)/$', views.buy, name='buy'),
      path("buy/<int:pk>", views.buy, name='buy'), 
      path("bought", views.bought),
      path("ai", views.ai),

      ]
