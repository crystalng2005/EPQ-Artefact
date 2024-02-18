from flaskblog import app
from threading import Thread
from twisted.internet import reactor

app.config['THREADING'] = True
#if __name__ == '__main__':
    #app.run(debug=True)

def run_flask():
    app.run()

def run_reactor():
    reactor.run()

if __name__ == '__main__':
    # Run Flask in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Run Twisted reactor in the main thread
    run_reactor()
