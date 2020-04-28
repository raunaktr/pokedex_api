from flask import Flask, json, request
from service import connection


def get_pokemon(name):
    return connection.get_pokemon_by_name(name)
