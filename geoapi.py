#!/usr/bin/env python3
from flask import Flask
from flask import Response
import GeoIP
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Geolocate by IP or domain name<pre>/country_by_ip/&lt;ip_addr&gt;\n/country_by_name/&lt;domain_name&gt;</pre>"

@app.route("/country_by_ip/<ip_addr>")
def country_by_ip(ip_addr):
    gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
    response = {'ipaddr': ip_addr[:15], 'country': gi.country_code_by_addr(ip_addr[:15])}
    return Response(json.dumps(response),  mimetype='application/json')

@app.route("/country_by_name/<domain_name>")
def country_by_name(domain_name):
    gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
    response = {'domainname': domain_name[:70], 'country': gi.country_code_by_name(domain_name[:70])}
    return Response(json.dumps(response),  mimetype='application/json')

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
