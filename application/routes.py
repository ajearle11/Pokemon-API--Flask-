from application import app, db
from flask import request, jsonify, render_template, redirect
from application.models import Pokemon
from application.forms import AddPokemonForm

def format_pokemon(pokemon):
    return {
        "id": pokemon.id,
        "name": pokemon.name,
        "type": pokemon.type,
        "ability": pokemon.ability
    }

@app.route("/")
def hello_world():
    return "<p>Hello, Pokemon Trainers/p>"

@app.route("/pokemons/", methods=["POST", "GET"])
def pokemon_requests():
    form = AddPokemonForm()
    if request.method == "POST":
        if form.validate_on_submit():
            pokemon = Pokemon(form.name.data, form.type.data, form.ability.data)
            db.session.add(pokemon)
            db.session.commit()
            return redirect('/pokemons/')
        else:
            return redirect('/pokemons/')

    elif request.method == "GET":
        pokemons = Pokemon.query.all()
        pokemon_list = []
        for pokemon in pokemons:
            pokemon_list.append(format_pokemon(pokemon))
        return render_template("pokemons.html", pokemons=pokemon_list, form=form)

@app.route("/pokemons/<id>/")
def get_pokemon(id):
    pokemon = Pokemon.query.filter_by(id = id).first()
    # return format_character(character)
    return render_template("pokemon.html", pokemon=pokemon)

# @app.route("/characters/<id>/", methods=["DELETE"])
# def delete_character(id):
#     character = Pokemon.query.filter_by(id = id).first()
#     db.session.delete(character)
#     db.session.commit()

# @app.route("/characters/<id>/", methods=["PATCH"])
# def update_character(id):
#     character = Pokemon.query.filter_by(id = id)
#     data = request.json
#     character.update(dict(name=data["name"], age=data["age"], catch_phrase=data["catch_phrase"]))
#     db.session.commit()
#     updated_character = character.first()
#     return jsonify(name=updated_character.name, age=updated_character.age, catch_phrase=updated_character.catch_phrase)

