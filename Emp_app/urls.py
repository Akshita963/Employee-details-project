from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Emp_app import views
from graphene_django.views import GraphQLView
from Emp_app.schema import schema
router = DefaultRouter()
urlpatterns = [
    # path('', include(router.urls))
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema))
]
