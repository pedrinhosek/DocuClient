from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cliente.views import *

urlpatterns = [
    path('', ClienteList.as_view(), name='cliente_list'),
    path('add/', ClienteCreate.as_view(), name='cliente_create'),
    path('<int:pk>/att/', ClienteUpdate.as_view(), name='cliente_update'),

    path('<int:pk_pessoa>/contrato/', ContratoCreate.as_view(), name='contrato_create'),
    path('<int:pk_pessoa>/excluir/<int:pk_doc>/doc/', DeleteDocContrato.as_view(), name='contrato_delete_documento'),
    path('<int:pk_pessoa>/pdf/', PDFContrato.as_view(), name='pdf_contrato'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
