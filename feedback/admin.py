from django.contrib import admin
from feedback.models import Feedback,AGREEMENT

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(AGREEMENT)
class AgreementbackAdmin(admin.ModelAdmin):
    pass