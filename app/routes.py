from app import app
from flask import render_template
from app.forms import UserInfoForm, PostForm, Phonebook
from app.models import User, Post, Address
from app import db

@app.route('/')
def index():
    name = 'Suzette'
    title = 'Coding Temple Flask'
    return render_template('index.html', name_of_user=name, title=title)

@app.route('/products')
def products():
    title = 'Products'
    products = ['apple', 'banana', 'peach', 'orange']
    return render_template('products.html', title=title, products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = UserInfoForm()
    if register_form.validate_on_submit():
        print('Hello this form has been submitted correctly')
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        print(username, email, password)
        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()

    return render_template('register.html', form=register_form)

@app.route('/createpost', methods=['GET', 'POST'])
def createpost():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_post = Post(title, content, user_id=1)
        db.session.add(new_post)
        db.session.commit()
    return render_template('createpost.html', form=form)

@app.route('/registerphone', methods=['GET', 'POST'])
def registerphone():
    new_form = Phonebook()
    if new_form.validate_on_submit():
        firstname = new_form.firstname.data
        lastname = new_form.lastname.data
        address = new_form.address.data
        phonenumber = new_form.phonenumber.data
        new_entry = Address(firstname, lastname, address, phonenumber)
        db.session.add(new_entry)
        db.session.commit()
    return render_template('registerphone.html', form=new_form)
