from flask import Flask, render_template, redirect, url_for
from forms import AddPetForm, EditPetForm
from models import Pet, db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'pets hooray'

db.init_app(app)


def create_database():
    with app.app_context():
        db.create_all()

create_database()

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data,
            available=True
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit_pet.html', form=form, pet=pet)

if __name__ == '__main__':
    app.run(debug=True)
