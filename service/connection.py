from elasticsearch import Elasticsearch, helpers, RequestsHttpConnection
import os, json, traceback
import time
from app.utils.es_connection import es_verify

# es = Elasticsearch([{"host": "localhost", "port": "9200"}])

host = "https://sb4o82i21a:swljdq394@pokedex-cluster-3943745536.ap-southeast-2.bonsaisearch.net:443"

es = Elasticsearch(
    hosts=host,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection,
)

if not es.ping:
    raise ValueError("Connection failed to establish")


def json_to_es(name):
    try:
        duplicacy_check = es.search(
            index="pokedex",
            body={"query": {"bool": {"must": [{"term": {"name.keyword": name}}]}}},
        )
        duplicates_found = duplicacy_check.get("hits").get("hits")

        if len(duplicates_found) != 0:
            print({"msg": "Pokemon exists", "error": "true"})
        elif len(duplicates_found) == 0:
            path_to_file = (
                "/home/raunak/Project/pokemon_RESTful/resources" + "/pokedex.json"
            )
            doc = json.loads(open(path_to_file).read())
            doc_obj = doc.get("pokemon")
            for obj in doc_obj:
                es.index(
                    index="pokedex",
                    id=obj["id"],
                    body={
                        "id": obj["id"],
                        "num": obj["num"],
                        "name": obj["name"],
                        "img": obj["img"],
                        "type": obj["type"],
                        "height": obj["height"],
                        "weight": obj["weight"],
                        "candy": obj["candy"],
                        "egg": obj["egg"],
                        "spawn_chance": obj["spawn_chance"],
                        "avg_spawns": obj["avg_spawns"],
                        "multipliers": obj["multipliers"],
                        "weaknesses": obj["weaknesses"],
                        "prev_evolution": obj.get("prev_evolution"),
                        "next_evolution": obj.get("next_evolution"),
                    },
                )
                print(obj["id"])
            return {"msg": "Successful", "error": "false"}
    except Exception as e:
        traceback.print_exc()
        return "Error occured", str(e)


def get_pokemon_by_name(name):
    try:
        fetch_val = es.search(
            index="pokedex",
            body={
                "query": {
                    "bool": {"must": [{"term": {"name.keyword": name.capitalize()}}]}
                }
            },
        )
        if es_verify(fetch_val) != "its-working!":
            return "es-failure"

        fetched_val = fetch_val.get("hits").get("hits")

        if len(fetched_val) != 0:
            init_list = []
            for i in fetched_val:
                init_list.append(i.get("_source"))
            return {"msg": init_list[0], "error": "true"}
        else:
            return {"msg": "Pokemon not found", "error": "true"}
    except Exception as e:
        traceback.print_exc()
        return "Error occured:", str(e)


def get_pokemon_evolutions(name):
    try:
        fetch_val = es.search(
            index="pokedex",
            body={
                "query": {
                    "bool": {"must": [{"term": {"name.keyword": name.capitalize()}}]}
                }
            },
        )

        fetched_val = fetch_val.get("hits").get("hits")

        if len(fetched_val) != 0:
            init_list = []
            for i in fetched_val:
                init_list.append(i.get("_source"))
            p_evol = init_list[0]["prev_evolution"]
            n_evol = init_list[0]["next_evolution"]
            return {
                "msg": {"prev_evolution": p_evol, "next_evolution": n_evol},
                "error": "false",
            }
        else:
            return {"msg": "Pokemon not found", "error": "true"}
    except Exception as e:
        traceback.print_exc()
        return "Error occured:", str(e)


def get_pokemon_by_types(type):
    try:
        fetch_val = es.search(
            index="pokedex",
            body={
                "query": {
                    "bool": {"must": [{"term": {"type.keyword": type.capitalize()}}]}
                }
            },
        )
        fetched_val = fetch_val.get("hits").get("hits")

        if len(fetched_val) != 0:
            init_list = []
            for i in fetched_val:
                init_list.append(i.get("_source"))
            return {"msg": init_list, "error": "false"}
        else:
            return {"msg": "Pokemon not found", "error": "true"}
    except Exception as e:
        traceback.print_exc()
        return "Error occured:", str(e)


def get_pokemons_by_weaknesses(weaknesses):
    try:
        fetch_val = es.search(
            index="pokedex",
            body={
                "query": {
                    "bool": {"must": [{"term": {"weaknesses.keyword": weaknesses}}]}
                }
            },
        )
        temp = fetch_val.get("hits").get("hits")

        if len(temp) != 0:
            init_list = []
            for i in temp:
                init_list.append(i.get("_source", {}))

            return {"msg": init_list, "error": "false"}
        else:
            return {"msg": "Pokemon not found", "error": "true"}
    except Exception as e:
        traceback.print_exc()
        return "Error occured:", str(e)


# response filtering function
def get_pokemonsssss_by_weaknesses(weaknesses):
    try:
        fetch_val = es.search(
            index="pokedex", filter_path=["hits.hits._id", "hits.hits._type"]
        )
        print(fetch_val)
    except Exception as e:
        traceback.print_exc()
        return "Error occured:", str(e)


# get_pokemon_by_types('flying')

#### use N-gram tokenizer (To be worked on)
# def get_pokemon_by_height(lower_bound, upper_bound):
#     try:
#         fetch_val = es.search(
#             index="pokedex",
#             body={"query": {"bool": {"must": [{"term": {"height.keyword": height}}]}}},
#         )
#         temp = fetch_val.get("hits").get("hits")

#         if len(temp) != 0:
#             init_list = []
#             for i in temp:
#                 init_list.append(i.get("_source", {}))
#             return print(init_list)
#         else:
#             return print({"msg": "Pokemon not found", "error": "true"})
#     except Exception as e:
#         traceback.print_exc()
#         return "Error occured:", str(e)

# get_pokemon_by_height("1.60 m")
# def get_pokemon_by_weight():


############################################
############ function tests ################
# json_to_es("Bulbasaur")
# get_pokemon_by_name('Ivysaur')
# get_pokemon_by_type("Electric")
# get_pokemons_by_weaknesses("Rock")
# get_pokemonsssss_by_weaknesses("poison")
# get_pokemon_evolutions("Bulbasaur")
