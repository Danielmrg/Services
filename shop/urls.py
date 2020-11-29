from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    #---------------home url----------------#
    path('', views.home , name='home'),
    path('category/<str:title>/',views.category,name='category'),
    #---------------expert url----------------#
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/settings/',views.expert_update,name='settings'),
    
    #---------------customer url----------------#
    path('profile/',views.profile ,name='profile'),
    path('profile/settings/',views.customer_update ,name='p_settings'),
    path('profile/request/add/<int:expert>/',views.request_srv ,name='request_srv'),
    path('profile/request/update/<int:pk>/',views.upadte_request ,name='update_request'),
    path('profile/request/delete/<int:pk>/',views.delete_request ,name='delete_request'),
    
    #---------------regestarions url----------------#
    path('signup_customer/',views.signup_customer,name='signup_customer'),
    path('signup_expert/',views.signup_expert,name='signup_expert'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
