from flask import Flask
import RPi.GPIO as GPIO          
from time import sleep
import pyttsx3
import requests

in_f1 = 24
in_b1 = 23
en_s1 = 25
in_f2 = 5
in_b2 = 6
en_s2 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(in_f1,GPIO.OUT)
GPIO.setup(in_b1,GPIO.OUT)
GPIO.setup(en_s1,GPIO.OUT)
GPIO.output(in_f1,GPIO.LOW)
GPIO.output(in_b1,GPIO.LOW)
p1=GPIO.PWM(en_s1,1000)
p1.start(100)
GPIO.setup(in_f2,GPIO.OUT)
GPIO.setup(in_b2,GPIO.OUT)
GPIO.setup(en_s2,GPIO.OUT)
GPIO.output(in_f2,GPIO.LOW)
GPIO.output(in_b2,GPIO.LOW)
p2=GPIO.PWM(en_s2,1000)
p2.start(100)

app = Flask(__name__)
engine = pyttsx3.init()
engine.setProperty('volume', 1)
engine.setProperty('rate', 150)

@app.route('/')
def index():
	return open("index.html", "r").read()

@app.route("/f")
def forward():
	print("forward")
	GPIO.output(in_f1,GPIO.HIGH)
	GPIO.output(in_b1,GPIO.LOW)
	GPIO.output(in_f2,GPIO.HIGH)
	GPIO.output(in_b2,GPIO.LOW)
	return "forward"

@app.route("/s")
def stop():
	print("stop")
	GPIO.output(in_f1,GPIO.LOW)
	GPIO.output(in_b1,GPIO.LOW)
	GPIO.output(in_f2,GPIO.LOW)
	GPIO.output(in_b2,GPIO.LOW)
	return "stop"

@app.route("/b")
def backward():
	print("backward")
	GPIO.output(in_f1,GPIO.LOW)
	GPIO.output(in_b1,GPIO.HIGH)
	GPIO.output(in_f2,GPIO.LOW)
	GPIO.output(in_b2,GPIO.HIGH)
	return "backward"

@app.route("/l")
def left():
    print("left")
    GPIO.output(in_f1,GPIO.HIGH)
    GPIO.output(in_b1,GPIO.LOW)
    GPIO.output(in_f2,GPIO.LOW)
    GPIO.output(in_b2,GPIO.HIGH)
    return "left"

@app.route("/r")
def right():
    print("right")
    GPIO.output(in_f1,GPIO.LOW)
    GPIO.output(in_b1,GPIO.HIGH)
    GPIO.output(in_f2,GPIO.HIGH)
    GPIO.output(in_b2,GPIO.LOW)
    return "right"

@app.route("/setspeed/<spd>")
def speed(spd):
    print("Speed: " + spd)
    p1.ChangeDutyCycle(int(spd))
    p2.ChangeDutyCycle(int(spd))
    return "Speed: " + spd

@app.route("/matrix.avif")
def matrix_bkg():
    return open("matrix.avif", "rb")


@app.route("/hello/<name>")
def hello(name):
    with open("cmd.txt", "w") as f:
        f.write("say")
    '''
    try:
        engine.say("Hello " + name)
        engine.runAndWait()
    except RuntimeError:
        print("I am in error")
        engine.endLoop()
        engine.say("Hello " + name)
        engine.runAndWait()
    '''
    print("Hello, " + name)
    requests.get("http://127.0.0.1:5000/hello/" + name)
    '''
    with open("cmd.txt", "w") as f:
        f.write("stop")
    '''
    return "Hello, " + name

if __name__ == '__main__':
    app.run(host="10.42.0.1", port=80, debug=True)
