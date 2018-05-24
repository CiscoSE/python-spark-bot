"""
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

import flask_sijax
import json
import requests
from app import app
from flask import request


@flask_sijax.route(app, '/')
def hello():
    data = json.loads(request.data)
    url = "https://api.ciscospark.com/v1/messages/" + data["data"]["id"]
    if (data["data"]["personEmail"] != 'Cerjeezy@sparkbot.io'):
        headers = {
            'Content-type': "application/json; charset=utf-8",
            'Authorization': "Bearer YOURTOKEN",
        }

        response = requests.request("GET", url, headers=headers)

        message = json.loads(response.text)
        print("Message received! :" + message["text"])

        payload = {
            "roomId": data["data"]["roomId"],
            "text": "Got it!"
        }

        replyUrl = "https://api.ciscospark.com/v1/messages/"
        response = requests.request("POST", replyUrl, data=json.dumps(payload), headers=headers)

        return 'OK'
