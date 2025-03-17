
from django.urls import path
from . import views  # Import views from the same app
from .views import contact_view
urlpatterns = [
    path('', views.index, name='index'),  # Home page route
       path('home/', views.home, name='home'), 
          path('about/', views.about, name='about'), 
             path('project/', views.project, name='project'), 
                path('contact/', views.contact, name='contact'),
                
                   path("submissions/", views.view_submissions, name="submissions"),
 
]
