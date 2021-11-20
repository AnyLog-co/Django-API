from django.urls import path
import anylog_deploy.views as views

view_options = views.FormViews()

urlpatterns = [
    path('', view_options.file_config, name='index'),
    path('base-configs/', view_options.basic_config, name='base-configs'),
    #path('general-configs/', view_options.general_info, name='general-configs'),
    #path('network-configs/', view_options.networking_info, name='network-configs'),
    #path('db-configs/', view_options.db_info, name='db-configs'),
    #path('operator-configs/', view_options.operator_info, name='operator-configs'),
    #path('mqtt-configs/', view_options.mqtt_info, name='mqtt-configs'),
    #path('full/', views.index, name='full-info'),
]