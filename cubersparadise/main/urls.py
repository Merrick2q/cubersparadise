from django.urls import path
from main.views import product_list, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, registrasi, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('registrasi/', registrasi, name='registrasi'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
