from django.urls import path 
from . import views

urlpatterns =[
    path('',views.UserAddShowView.as_view(), name='addandshow'),
    path('delete/<int:id>/', views.UserDeleteView.as_view, name="deletedata" ),
    path ('<int:id>/', views.UserUpdateView.as_view(), name="updatedata"),
    
]