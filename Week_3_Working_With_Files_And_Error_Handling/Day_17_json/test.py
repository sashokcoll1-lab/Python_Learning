import json

data = {"name": "Саша", "age": 21, "hobbies": ["программирование", "шахматы"]}

# Запись в JSON
with open("user_test.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

data["name"]="Саша"

with open("user_test.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Чтение из JSON
with open("user_test.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded["name"])