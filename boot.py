#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello(name=None):
    return render_template('index.html', name=name)

@app.route("/template.ipxe")
def template():
    resp = make_response(render_template('template.ipxe.txt', name=request.args.get('name', '')))
    resp.mimetype = 'text/plain'
    return resp

@app.route("/localboot.ipxe")
def localboot(name=None):
    resp = make_response(render_template('localboot.ipxe.txt', name=name))
    resp.mimetype = 'text/plain'
    return resp

@app.route("/boot.ipxe")
def bootipxe(name=None):
    resp = make_response(render_template('boot.ipxe.txt', name=name))
    resp.mimetype = 'text/plain'
    return resp

@app.route("/netboot.ipxe")
def netbootipxe(name=None):
    resp = make_response(render_template('netboot.ipxe.txt', name=name))
    resp.mimetype = 'text/plain'
    return resp

@app.route("/undionly.ipxe")
def undionlyipxe(name=None):
    resp = make_response(render_template('undionly.ipxe.txt', name=name))
    resp.mimetype = 'text/plain'
    return resp

@app.route("/remote.ipxe")
def remoteipxe(name=None):
    resp = make_response(render_template('remote.ipxe.txt', name=name))
    resp.mimetype = 'text/plain'
    return resp

@app.route("/menu.ipxe")
def menuipxe(name=None):
    resp = make_response(render_template('menu.ipxe.txt', name=name))
    resp.mimetype = 'text/plain'
    return resp

@app.route("/boot.itest")
def bootipxetest(name=None):
    return render_template('boot.ipxe.txt', name=name)


@app.route("/google3528ba40472779da.html")
def google(name=None):
    return render_template('google3528ba40472779da.html', name=name)


if __name__ == "__main__":
    app.debug = True
    app.run()
