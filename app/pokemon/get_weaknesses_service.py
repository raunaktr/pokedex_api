from flask import Flask, json, request
from service import connection


def get_weaknesses(weaknesses):
    return connection.get_pokemons_by_weaknesses(weaknesses)


