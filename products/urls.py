from django.conf.urls import url,patterns
from products import views

urlpatterns = patterns('',
        url(r'^$',views.index)
        )
