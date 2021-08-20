from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


def esearch(city="", state=""):
    client = Elasticsearch()
    q = Q("bool", should=[Q("match", city=city), Q("match", state=state)], minimum_should_match=1)
    s = Search(using=client, index="trial").query(q)[0:20]
    response = s.execute()
    print("Total {} hits found".format(response.hits.total))
    search = get_results(response)
    return search


def get_results(response):
    results = []
    for hit in response:
        result_tuple = (hit.city, hit.state)
        results.append(result_tuple)
    return results

#
# if __name__ == '__main__':
#     print(esearch(city="JACKSON HEIGHTS"))
#     print(esearch(state="NY"))
