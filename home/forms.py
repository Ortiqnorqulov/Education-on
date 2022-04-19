from django import forms
from home.models import ContactMessage, NewsLatter, CourseCommentsMessage, CourseBuy


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'phone', 'message',)

class NewsLatterForm(forms.ModelForm):
    class Meta:
        model = NewsLatter
        fields = ( 'email',)


class CourseCommentForm(forms.ModelForm):
    class Meta:
        model = CourseCommentsMessage
        fields = ('name', 'email', 'message',)

class CourseBuyForm(forms.ModelForm):
    class Meta:
        model = CourseBuy
        fields = ('username', 'title', 'email', 'phone',)
