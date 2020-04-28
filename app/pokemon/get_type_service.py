from flask import Flask, json, request
from service import connection


def get_types(type):
    return connection.get_pokemon_by_types(type)


