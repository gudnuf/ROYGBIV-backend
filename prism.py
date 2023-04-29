#!/usr/bin/env python3
import time
from pyln.client import Plugin # We import `Plugin` from the `pyln-client` pip package, which does all the hard work for us

plugin = Plugin() # This is our plugin's handle

@plugin.init() # Decorator to define a callback once the `init` method call has successfully completed
def init(options, configuration, plugin, **kwargs):
    plugin.log("Plugin helloworld.py initialized")

@plugin.method("hello")
def hello(plugin, name="world"):
  greeting = 'hello'
  s = '{} {}'.format(greeting, name)
  plugin.log(s)
  return s

plugin.add_option('greeting', 'Hello', 'The greeting I should use.')

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