import json


class Config:
    settings = json.load(open('container_settings.json', 'r'))
    VERSION = settings["VERSION"]

    CTR_ENTITIES_LIMIT_DEFAULT = 50
