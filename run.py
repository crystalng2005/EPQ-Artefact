from flaskblog import app

#db.init_app(app)

#app.app_context().push()
#db.create_all()
#SQLAlchemy.orm.Session.expire_on_commit = False
'''
Session = sessionmaker(app)
session = Session()
session.expire_on_commit=False
'''

'''
with app.app_context():
    db.create_all()
    user_1 = User(username='Crystal', email='crystalngshulu9909@gmail.com', password='password')
    db.session.add(user_1)
    user_2 = User(username='Isaac', email='isaachangcheeyuan56@gmail.com', password='password')
    db.session.add(user_2)
    db.session.commit()
'''

if __name__ == '__main__':
    app.run(debug=True)