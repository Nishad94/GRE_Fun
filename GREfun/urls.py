from django.conf.urls import patterns, url
from GREfun import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about$', views.about, name='about'),
	url(r'^dashboard$', views.dashboard, name="dashboard"),
	url(r'^leaderboard$',views.leaderboard,name='leaderboard'),
	url(r'^logout$',views.logout_view, name="logout"),
	url(r'^wordlist$',views.wordlist, name='wordlist'),
	url(r'^word/(?P<word>\w+)$',views.word_meaning, name='word_meaning'),
	url(r'^question/(?P<question_id>\d+)$', views.question, name='question'),
)