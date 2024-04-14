import flask
import pyttsx3

# DEFINITION
app = flask.Flask(__name__)
engine = pyttsx3.init()

# CONFIG
engine.setProperty('volume', 1)
engine.setProperty('rate', 150)
# engine.setProperty('voice', "com.apple.eloquence.en-US.Shelley")


# CODE
@app.route("/")
def index():
    return open("ttsindex.html", "r").read()


@app.route("/hello/<name>")
def hello(name):
    with open("cmd.txt", "w") as f:
        f.write("say")
    try:
        engine.say("Hello " + name)
        engine.runAndWait()
    except RuntimeError:
        print("I am in error")
        engine.endLoop()
        engine.say("Hello " + name)
        engine.runAndWait()
    print("Hello, " + name)
    with open("cmd.txt", "w") as f:
        f.write("stop")
    return "Hello, " + name


app.run(host="0.0.0.0", port=5000, debug=True)
