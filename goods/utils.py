import keyword
from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchVector,
)

from goods.models import Products


# def q_search(query):

#     if query.isdigit() and len(query) <= 5:
#         return Products.objects.filter(id=int(query))

#     keywords = [word for word in query.split() if len(word) > 2]

#     q_object = Q()

#     for token in keywords:
#         q_object |= Q(description__icontains=token)
#         q_object |= Q(name__icontains=token)

#     return Products.objects.filter(q_object)


def q_search(query):

    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    return Products.objects.annotate(
        rank=SearchRank(vector, query),
    ).order_by("-rank")

    # return Products.objects.filter(description__search=query)
    # return Products.objects.annotate(
    #     search=SearchVector("name", "description"),
    # ).filter(search=query)
