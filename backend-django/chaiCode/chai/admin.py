from django.contrib import admin
from .models import ChaiVarity ,ChaiReview ,ChaiCertificate ,Store

# Register your models here.

class ChaiReviewInLine(admin.TabularInline):
    model = ChaiReview
    extra =2

class ChaiVarietyAdmin(admin.ModelAdmin):
    


admin.site.register(ChaiVarity)


