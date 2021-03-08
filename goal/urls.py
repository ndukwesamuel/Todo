from django.urls import path


from . import views


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.taskList, name='taskList'),
    path('task-detail/<str:pk>/', views.taskDetail, name='taskdetail'),
    path('task-create/', views.taskCreate, name='taskcreate'),
    path('task-update/<str:pk>/', views.taskUpdate, name='taskupdate'),
    
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]