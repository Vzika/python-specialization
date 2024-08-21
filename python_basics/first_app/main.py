import json

with open('config.json', 'r') as file:
    config = json.load(file)

print(config)
#url = f'{config["dialect"]}+{config["driver"]}://{config["username"]}:{config["password"]}@{config["host"]}:{config["port"]}/{config["database"]}'
#engine = create_engine(url)
