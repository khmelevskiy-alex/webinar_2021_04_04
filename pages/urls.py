from django.urls import path

import pages.views as views

urlpatterns = [
    path('justpage/', views.JustStaticPage.as_view())
]
