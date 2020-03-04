#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
import os
import json
from flask import Flask,render_template,redirect, url_for, request,session,escape
#from tkinter.test.runtktests import this_dir_path

app = Flask(__name__)

@app.route('/')
def hello():
    # We have to take this from Fusion Home ? 
    path='C:\\MYHP\\CRM\\Omni\\omni\\fusion\\connectivity-services';
    d = {
  "children": [
    {
      "children": [
        {
          "rate": 10,
          "value": 769,
          "name": "canmicapi",
          "children": [
            {
                "rate": 0.5,
                "value": 1021,
                "name": "CanmicAPI.java"
            }
        ]
        },
        {
          "rate": 0.35092180546726004,
          "value": 1021,
          "name": "connection-designer",
          "children": [
            {
                "rate": 0.1,
                "value": 100,
                "name": "cd-app"
            },
            {
                "rate": 0.9,
                "value": 500,
                "name": "cd-client"
            },
            {
                "rate": 0,
                "value": 1021,
                "name": "cd-common"
            }
        ]
        },
        {
          "rate": 0.44886363636363635,
          "value": 291,
          "name": "connection-manager"
        },
        {
          "rate": 0.4716981132075472,
          "value": 28,
          "name": "connectivity-services-common"
        },
        {
          "rate": 0.234860883797054,
          "value": 935,
          "name": "connectivity-services-utilities"
        },
        {
          "rate": 0.234860883797054,
          "value": 935,
          "name": "plexxi-client"
        },
        {
          "rate": 0.234860883797054,
          "value": 935,
          "name": "sal"
        },
        {
          "rate": 0.234860883797054,
          "value": 935,
          "name": "sal-adapter-arista"
        },
        {
          "rate": 0.234860883797054,
          "value": 935,
          "name": "sal-adapter-aruba"
        },
        {
          "rate": 0.234860883797054,
          "value": 935,
          "name": "sal-adapter-chloride"
        },
        {
          "rate": 0.234860883797054,
          "value": 935,
          "name": "sal-adapter-hafnium"
        }
      ],
      "rate": 0.348458904109589,
      "name": "2544 years"
    }
  ],
  "rate": 0.28656039777712783,
  "name": "Omni"
}
    #d = json.dumps(path_to_dict(path))
    #print(d)
    #x = json.dumps(d);
    return render_template('try.html', x=d)
    #return json.dumps(path_to_dict(path));
def test():
    path='C:/MYHP/CRM/Omni/omni/';
    return json.dumps(path_to_dict(path));

def recursionForDirectoty(dir_path):
    for root, subdirs, files in os.walk(dir_path):
        print(subdirs)

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"        
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
    return d

if __name__ == "__main__":
   #app.run(threaded=True,ssl_context=('cert.pem', 'key.pem'))
   app.run(threaded=True, debug=True, host="0.0.0.0", port="443")


