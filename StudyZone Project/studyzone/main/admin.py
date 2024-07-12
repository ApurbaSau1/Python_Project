from django.contrib import admin
from django.http.request import HttpRequest
from . models import Contact,Subject,SubjectModules,SubjectDetails,CustomUser,Question,Notice
from django.utils.html import mark_safe

admin.site.site_header='StudyZone Admin'
admin.site.site_title='Administrator'
admin.site.index_title='StudyZone'

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    
    readonly_fields = ['subject_Img']
    list_display=('sub_name','subject_Img')
    
@admin.register(SubjectModules)
class AdminSubjectModulesAdmin(admin.ModelAdmin):
    list_display=('module_name','module_desc','subjects')
    raw_id_fields=['subject']
    
    def subjects(self,obj):
        return obj.subject.sub_name

@admin.register(SubjectDetails)
class AdminSubjectDetailsAdmin(admin.ModelAdmin):
    list_display=('Subject_Modeles','subjects','sub_cont','module_desc')
    raw_id_fields=['sub_module','subject']
    # raw_id_fields=['subject',]
    
    def Subject_Modeles(self,obj):
        return obj.sub_module.module_name
    
    
    def subjects(self,obj):
        return obj.subject.sub_name
    
        
    def module_desc(self,obj):
        return obj.sub_module.module_desc
    
      
@admin.register(Contact)
class AdminContactAdmin(admin.ModelAdmin):
    list_display=('name','email','msg')
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    
@admin.register(CustomUser)
class AdminCustomUserAdmin(admin.ModelAdmin):
    list_display=('username','first_name','last_name','email','contact_no')
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Question)
class UploadQuestion(admin.ModelAdmin):
    list_display=('question','op1','op2','op3','op4','ans')


@admin.register(Notice)
class UploadNotice(admin.ModelAdmin):
    list_display=('notice',)