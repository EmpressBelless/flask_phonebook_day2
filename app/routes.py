from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import UserInfoForm, PostForm, Phonebook, LoginForm
from app.models import User, Post, Address

@app.route('/')
def index():
    name = 'Suzette'
    title = 'Coding Temple Flask'
    return render_template('index.html', title=title)

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
        
        #check if username already exists
        # existing_user = User.query.filter_by(username=username).all()
        # if existing_user:
        #     #Flash a warning message
        #     flash(f'The username {username} is already in use. Do it again!', 'danger')
        #     return redirect(url_for('register'))
            #redirect back to the register

        new_user = User(username, email, password)
        
        db.session.add(new_user)
        db.session.commit()

        # flash(f'Thank you {username}, you have successfully registered!', 'success')
        #flash takes two arguments, second argument we can use a category to change the color of our flashes
        
        return redirect(url_for('index'))
    
    return render_template('register.html', form=register_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            flash('Your username or password is incorrect', 'danger')
            return redirect(url_for('login'))
        login_user(user)

        # # flash(f'Welcome {user.username} You have successfully logged in.', 'success')
    return render_template('login.html', login_form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/createpost', methods=['GET', 'POST'])
@login_required
def createpost():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_post = Post(title, content, current_user.id)
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
