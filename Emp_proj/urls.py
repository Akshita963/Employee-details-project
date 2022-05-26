from django.contrib import admin
from django.urls import path , include
from graphene_django.views import GraphQLView
import Emp_app
from Emp_app.schema import schema
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    path('',include('Emp_app.urls'))
    ]