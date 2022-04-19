from django.urls import path
from order import views
urlpatterns = [
    path('addtocart/<int:pk>/', views.addtocart, name='addtocart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
]