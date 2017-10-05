#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return render_template('index.html', name=request.args.get('name', ''))

@app.route("/template.ipxe")
def template():
    resp = make_response(render_template('template.ipxe.txt', name=request.args.get('name', '')))
    resp.mimetype = 'text/plain'
    return resp

@app.route("/arrival.ipxe")
def arrival():
    # This will set the boot-host variable in iPXE.
    build_template = render_template('arrival.ipxe.txt',
                        url_root=request.url_root)
    resp = make_response(build_template)
    resp.mimetype = 'text/plain'
    return resp

@app.route("/inventory.ipxe")
def inventory():
    # This will get various variables in iPXE.
    mac_address = request.args.get('mac', '')
    ip_address = request.args.get('ip', '')
    uuid_address = request.args.get('uuid', '')

    # do something with the collected data here.

    build_template = render_template('inventory.ipxe.txt',
        mac=mac_address, ip=ip_address, uuid=uuid_address)
    resp = make_response(build_template)
    resp.mimetype = 'text/plain'
    return resp

@app.route("/boot.ipxe")
def bootipxe():
    build_template = render_template('boot.ipxe.txt', next=request.args.get('next', ''))
    resp = make_response(build_template)
    resp.mimetype = 'text/plain'
    return resp

@app.route("/netboot.ipxe")
def netbootipxe():
    build_template = render_template('netboot.ipxe.txt', name=request.args.get('name', ''))
    resp = make_response(build_template)
    resp.mimetype = 'text/plain'
    return resp

@app.route("/undionly.ipxe")
def undionlyipxe():
    build_template = render_template('undionly.ipxe.txt', name=request.args.get('name', ''))
    resp = make_response(build_template)
    resp.mimetype = 'text/plain'
    return resp

@app.route("/remote.ipxe")
def remoteipxe():
    build_template = render_template('remote.ipxe.txt', name=request.args.get('name', ''))
    resp = make_response(build_template)
    resp.mimetype = 'text/plain'
    return resp

@app.route("/menu.ipxe")
def menuipxe():
    build_template = render_template('menu.ipxe.txt', name=request.args.get('name', ''))
    resp = make_response(build_template)
    resp.mimetype = 'text/plain'
    return resp

@app.route("/boot.itest")
def bootipxetest():
    return render_template('boot.ipxe.txt', name=request.args.get('name', ''))


@app.route("/google3528ba40472779da.html")
def google():
    return render_template('google3528ba40472779da.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
