from flask import Flask, json, request
from service import connection


def evolution(name):
    return connection.get_pokemon_evolutions(name)


