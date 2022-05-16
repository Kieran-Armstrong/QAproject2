from flask import Flask, request, jsonify
import random

app = Flask(__name__)

effects = {
    0: "Fire",
    1: "Ice",
    2: "Lightning",
    3: "Water",
    4: "Earth",
    5: "Light",
    6: "Dark"
}

longswords = {
    "names": {
        0: "Sharp",
        1: "Slicing",
        2: "Piercing",
        3: "Powerful",
        4: "Useless"
    }
}

scythes = {
    "names": {
        0: "Sharp",
        1: "Slicing",
        2: "Powerful",
        3: "Swift",
        4: "Slow"
    }
}

daggers = {
    "names": {
        0: "Swift",
        1: "Hidden",
        2: "Piercing",
        3: "Blunt",
        4: "Useless"
    }
}

crossbows = {
    "names": {
        0: "Swift",
        1: "Slow",
        2: "Piercing",
        3: "Effective",
        4: "Loud"
    }
}

bows = {
    "names": {
        0: "Heavy",
        1: "Long",
        2: "Stunted",
        3: "Silent",
        4: "Short"
    }
}

spears = {
    "names": {
        0: "Heavy",
        1: "Long",
        2: "Short",
        3: "Piercing",
        4: "Useless"
    }
}

clubs = {
    "names": {
        0: "Heavy",
        1: "Long",
        2: "Short",
        3: "Light",
        4: "Useless"
    }
}

@app.route('/post/status', methods=['POST'])
def post_status():
    weapon = request.json['weapon']
    damage = request.json['damage']

    if weapon == 'longsword':
        name = random.choice(list(longswords["names"].values()))
    elif weapon == 'sycthe':
        name = random.choice(list(scythes["names"].values()))
    elif weapon == 'dagger':
        name = random.choice(list(daggers["names"].values()))
    elif weapon == 'crossbow':
        name = random.choice(list(crossbows["names"].values()))
    elif weapon == 'bow':
        name = random.choice(list(bows["names"].values()))
    elif weapon == 'club':
        name = random.choice(list(clubs["names"].values()))
    else:
        name = random.choice(list(spears["names"].values()))

    if damage <= 10:
        level = "Beginner"
    elif damage <= 20:
        level = "Adept"
    elif damage <= 30:
        level = "Journeyman"
    elif damage <= 40:
        level = "Master"
    elif damage <= 50:
        level = "Hero"
    else:
        level = "Legend"

    effect = random.choice(list(effects.values()))

    status = {
        "level": level,
        "name": name,
        "effect": effect
    }
    
    return jsonify(status) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')