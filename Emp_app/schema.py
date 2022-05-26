from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from numpy import product, require
from .models import Employee

  
class Emp_details(DjangoObjectType):
    class Meta: 
        model = Employee
        fields = ('empID','empName','empDescription','empCategory', 'empCity')  


class Query(graphene.ObjectType):
    Emp = graphene.List(Emp_details)

    def resolve_emp(root, info, **kwargs):
        # Querying a list
        return Employee.objects.all()

# schema = graphene.Schema(query=Query)



class CategoryMutation(graphene.InputObjectType):
        empID = graphene.Int()
        empName = graphene.String()
        empDescription = graphene.String()
        empCategory = graphene.String()
        empCity = graphene.String()
        

class CreateEmp(graphene.Mutation):
    class Arguments:
        input = CategoryMutation(required=True)

    category = graphene.Field(Emp_details)

    @classmethod
    def mutate(cls,root, info,  input):
        category = Employee.objects.get(pk=input.empID)
        category.empName = input.empName
        category.empDescription = input.empDescription
        category.empCategory = input.empCategory
        category.empCity = input.empCity
        category.save()
        return CategoryMutation(category=category)

class UpdateEmp(graphene.Mutation):
    class Arguments:
        input = CategoryMutation(required=True)
    category = graphene.Field(Emp_details)

    @classmethod
    def mutate(cls, root, info, input):
        category = Employee.objects.get(pk=input.empID)
        category.empName = input.empName
        category.empDescription = input.empDescription
        category.empCategory = input.empCategory
        category.empCity = input.empCity
        category.save()
        return UpdateEmp(category=category)


class Mutation(graphene.ObjectType):
    create_emp = CreateEmp.Field()
    update_emp = UpdateEmp.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)