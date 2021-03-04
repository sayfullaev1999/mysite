import graphene
import library.schema


# Our Project Level Schema
# If we had multiple apps, we'd import them here
# Then, inherit from their Queries and Mutations
# And, finally return them as one object

class Query(library.schema.Query, graphene.ObjectType):
    pass


class Mutation(library.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
