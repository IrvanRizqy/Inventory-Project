from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'IrvanRizqy',
        'class': 'PBP A',
        'name1': "ArmsKore Coil Gun",
        'name2': "Reinforced Power Drills",
        'name3': 'Pickaxe',
        'amount1': '11',
        'amount2': '20',
        'amount3': '68',
        'description1': 'A miniaturized electromagnetic coilgun surrounded by technological components as part of its bulky exterior which fires projectiles capable of piercing through solid rock and enemies.',
        'description2': 'The Drillers mobility tool. They are a pair of massive handheld drills mounted up to the Drillers forearms.',
        'description3': 'The Pickaxe is a fundamental Support Tool available to every class. It allows the player to shape the environment around them.',
        'cateory1':'Secondary Weapon',
        'cateory2':'Support Tool',
        'cateory3':'Support Tool',
        'stats1a':'Damage : 130',
        'stats1b':'Magazine Size : 1',
        'stats1c':'Max Ammo : 640',
        'stats1d':'Reload Time : 2.5s',
        'stats1e':'Charged Shot Ammo Use : 40',
        'stats2a': 'Damage : 5 Melee',
        'stats2b': 'Max Fuel : 38',
        'stats2c': 'Fear Factor : 50%',
        'stats2d': 'Mining Rate : 1.5',
        'stats2e': 'Armor Break : 10000%',
        'stats3a': 'Damage : 27.5 Melee',
        'stats3b': 'Armor Breaking : 150%',
    }

    return render(request, "main.html", context)