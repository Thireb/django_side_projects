from django.test import TestCase
from .models import Question, Choice
from django.utils import timezone
import datetime
from django.urls import reverse

class DateCheck(TestCase):
    def test_future_published_date(self):
        
        #check if future date is false or not.
        
        question = Question.objects.create(question_text='something',published_at=timezone.now()+ datetime.timedelta(days=20))
        self.assertIs(question.was_published_recently(),False)
        
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(published_at=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(published_at=time)
        self.assertIs(recent_question.was_published_recently(), True)
  
#pass values to create Question object      
def create_question(question_text,days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,published_at=time)

class QuestionIndexTest(TestCase):
    
    def test_index_is_blank_or_not(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'No polls to show')
        self.assertQuerysetEqual(response.context['latest_questions'],[])

    def test_past_question(self):
        question = create_question(question_text='past',days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_questions'],[question])
        
    def test_future_question(self):
        question = create_question(question_text='future question',days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_questions'],[])
    
    def test_past_and_future_question(self):
        question = create_question(question_text='past', days=-5) 
        create_question(question_text='future',days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_questions'],[question])
        
    def test_past_2_questions(self):
        question1=create_question(question_text='past one',days=-30)
        question2=create_question(question_text='past two',days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_questions'],[question2,question1])
        
class QuestionDetailViewTests(TestCase):
    def test_future_question_in_detail_view(self):
        
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question_in_detail_view(self):
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)