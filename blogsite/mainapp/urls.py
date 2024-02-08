from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_page, name='index'),

    path('home', views.index_page, name='index'),
    path('home/', views.index_page, name='index'),

    path('about', views.about_page, name='about'),
    path('about/', views.about_page, name='about'),

    path('contact', views.contact_page, name='contact'),
    path('contact/', views.contact_page, name='contact'),

    path('article/<int:article_id>', views.article_page, name='article'),
    path('article/<int:article_id>/', views.article_page, name='article'),

    path('comment/<int:article_id>', views.commentpost, name='postcomment'),
    path('comment/<int:article_id>/', views.commentpost, name='postcomment'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)