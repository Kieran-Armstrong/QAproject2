from flask import Flask
import random

app = Flask(__name__)

weapon = ['Longsword', 'Scythe', 'Dagger', 'Crossbow', 'Bow', 'Spear', 'Club']

@app.route('/get/weapon')
def get_weapon():
    return random.choice(weapon)

if __name__ == '__main__':
    app.run(host='0.0.0.0')