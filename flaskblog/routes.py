from flask import render_template, url_for, flash, redirect, request, send_file
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import openai


openai.api_key = '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'
posts = [
    {
    'author': 'Crystal Ng (User_01)',
    'title': 'Proof by Induction Progress',
    'content': 'Report: 2 Past Year Papers Done',
    'date_posted': 'October 20, 2023'
},
    {
    'author': 'Name (User_02)',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'May 21, 2023'
}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}: You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page= request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Oops! Your login attempt danced a little out of step.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file)


@app.route("/OpenAI", methods=['GET', 'POST'])
def OpenAI():
    user_input = request.form.get("message")
    prompt = f"User: {user_input}\nChatbot: "
    chat_history = []
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        stop=["\nUser: ", "\nChatbot: "]
        )
    
    bot_response = response.choices[0].text
    return render_template('OpenAI.html', bot_response=bot_response)

@app.route("/PYP", methods=['GET', 'POST'])
def PYP():
    return render_template('PYP.html', title='Past Year Paper Generator')