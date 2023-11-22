from django.urls import path
from main.views import product_list, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, registrasi, login_user, logout_user, product_management, add_product, subtract_product, delete_product, get_product_json, add_product_ajax, delete_product_ajax, create_product_flutter

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
    path('product_management/', product_management, name='product_management'),
    path('add_product/<int:product_id>/', add_product, name='add_product'),
    path('subtract_product/<int:product_id>/', subtract_product, name='subtract_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-ajax/', delete_product_ajax, name='delete_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]