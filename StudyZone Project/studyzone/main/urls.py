from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('New-Registation',views.New_Registation,name='New-Registation'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('contact',views.contactPage,name='contact'),
    path('about',views.about,name='about'),
    path('codding',views.codding,name='codding'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit',views.chngeProfile,name='edit'),
    path('chng-pwd',views. userChangePassword,name='chng-pwd'),
    path('view_programing',views.showCode,name='view_programing'),
    path('read_code/<int:id>',views.viewsubject_modeles,name='read_code'),
    path('sub_content/<int:sub_module_id>',views.viewSubject_Content,name='sub_content'),
    path('exam',views.examination,name='exam'),
]
