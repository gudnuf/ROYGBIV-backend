#!/usr/bin/env python3
import time
from pyln.client import Millisatoshi, Plugin, RpcError
plugin = Plugin() # This is our plugin's handle

@plugin.init() # Decorator to define a callback once the `init` method call has successfully completed
def init(options, configuration, plugin, **kwargs):
    plugin.log("Plugin prism.py initialized")

@plugin.method("prism")
def createPrism(destination, amount, request, plugin):
    try:
        print('hello')
    except RpcError as e:
        print(e)

@plugin.subscribe("connect")
def on_connect(plugin, id, address, **kwargs):
    plugin.log("Received connect event for peer {}".format(id))


@plugin.subscribe("disconnect")
def on_disconnect(plugin, id, **kwargs):
    plugin.log("Received disconnect event for peer {}".format(id))

@plugin.hook("htlc_accepted")
def on_htlc_accepted(onion, htlc, plugin, **kwargs):
    plugin.log('on_htlc_accepted called')
    time.sleep(20)
    return {'result': 'continue'}

plugin.run() # Run our plugin