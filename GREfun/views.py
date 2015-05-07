from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from GREfun.models import Word,Meaning,Question,Student
from random import shuffle
from django.contrib.auth import authenticate,logout, login
from django.contrib.auth.models import User


# Create your views here.
def index(request):
	if request.user.is_authenticated():
		return redirect('/GREfun/dashboard')
	else:
		return render(request, 'GREfun/index.html', {})

def logout_view(request):
	logout(request)
	return redirect('/GREfun')

def leaderboard(request):
	all_users = User.objects.all().order_by('student__points')
	return render(request, 'GREfun/leaderboard.html', {"users":all_users})

def dashboard(request):
	print request.user.is_authenticated()
	if request.user.is_authenticated():
		if request.user.student.questions_total == 0:
			ratio = 0
		else:
			ratio = 100*(request.user.student.questions_correct/float(request.user.student.questions_total))
		print ratio
		return render(request, 'GREfun/dashboard.html', {'username': request.user, 'correct_ratio': ratio })
	elif((request.POST.get('username','') != '') and (request.POST.get('password', '') != '')):
		user = authenticate(username=request.POST['username'],password=request.POST['password'])
		print user
		if user is not None:
			login(request,user)
			if user.student.questions_total == 0:
				ratio = 0
			else:
				ratio = 100*(user.student.questions_correct/float(user.student.questions_total))
			return render(request, 'GREfun/dashboard.html', {'user': user, 'correct_ratio': ratio})
		else:
			return HttpResponse("Username/password incorrect.")
	else:
		return redirect('/GREfun')

def wordlist(request):
	meaning_list = Meaning.objects.all()	
	context = {'meaning_list': meaning_list}
	return render(request, 'GREfun/wordlist.html', context)

def word_meaning(request, word):
	meaning_list = Meaning.objects.all()
	try:
		word_ob = Word.objects.get(word_text=word)
	except:
		raise Http404("Word does not exist")
	return render(request, 'GREfun/word_meaning.html', {'word_ob' : word_ob})

def question(request, question_id):
	print 'question: user auth = ' + str(request.user.is_authenticated())
	if not request.user.is_authenticated():
		return HttpResponse("You do not have enough rights to view this page. Please log in.")
	q = get_object_or_404(Question, pk=question_id)
	choices = []
	choices.append(q.meaning.word.word_text)
	choices.append(q.choice1.word_text)
	choices.append(q.choice2.word_text)
	choices.append(q.choice3.word_text)
	shuffle(choices)
	if(request.POST.get('choice',False) != False):
		request.user.student.questions_total += 1
		if(request.POST['choice'] == q.meaning.word.word_text):
			ans = 1
			request.user.student.questions_correct += 1
		else:
			ans = 2
		request.user.student.save()
	else:
		ans = 0
	return render(request, 'GREfun/question.html', {'ans':ans, 'q': q, 'q_prev_id':q.id-1, 'q_next_id':q.id+1, 'choices': choices})