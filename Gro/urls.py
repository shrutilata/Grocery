from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="Gro-home"),
    path('add_item',views.add_item,name="Gro-Add_List"),
    path('update_item',views.update_item,name='Gro-Update_List'),
    path('add_submit',views.add_submit,name='add_submit'),
    path('update_submit',views.update_submit,name='update_submit')
]
# path('update/<int:id>',views.update,name='update')