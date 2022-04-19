from modeltranslation.translator import register, TranslationOptions
from course.models import Category, Courses


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Courses)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'level', 'lenguage',)
