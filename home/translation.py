from modeltranslation.translator import TranslationOptions, register
from home.models import Aboutus, Informations, FAQs, Slider, Adversiting, Blog, OurTeam


@register(Informations)
class InformationsTranslationOptions(TranslationOptions):
    fields = ('title', 'address', 'description',)


@register(Aboutus)
class AboutusTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(FAQs)
class InformationsTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Adversiting)
class AdversitingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(OurTeam)
class OurTeamTranslationOptions(TranslationOptions):
    fields = ('title', 'description')