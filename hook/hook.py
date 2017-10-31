# hook.py
#!/usr/bin/env python
# coding=utf-8
from github_webhook import Webhook
from flask import Flask
import os

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/",methods=['GET', 'POST'])        # Standard Flask endpoint
def hello_world():
    print('https://hook.jiangtao.tech')
    os.chdir('/root/hexo/source/_posts')
    os.system('git pull origin master')
    os.chdir('/root/hexo/')
    print('tart generate file...')
    os.system('hexo g')
    return "Hello, World!"

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    os.system(blog.sh)
    print("Got push with: {0}".format(data))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
