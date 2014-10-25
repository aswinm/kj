from django.conf.urls import url,patterns
from products import views

urlpatterns = patterns('',
        url(r'^$',views.index),
        url(r'^about/?$',views.about),
        url(r'^contacts/?$',views.contacts)
        )
