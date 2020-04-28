
def es_verify(val):
    if val.get('_shards').get('failed') <= 0:
        return "its-working!"
    else:
        return "es-failure"
