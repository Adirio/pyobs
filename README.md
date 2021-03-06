# pyobs
Python library to communicate with an [obs-websocket](
https://github.com/Palakis/obs-websocket) server.

_Licensed under the MIT License_

Based on the work of [Guillaume "Elektordi" Genty](https://github.com/Elektordi
) in [obs-websocket-py](https://github.com/Elektordi/obs-websocket-py).

## Project pages

GitHub project: https://github.com/Adirio/pyobs

PyPI package: https://pypi.python.org/pypi/pyobs

## Installation

Just run `pip install pyobs` in your Python venv or directly on your system.

For manual install, git clone the github repo and copy the directory **pyobs** 
in your python project root.

**Requires**: websocket-client (from pip)

## Usage

See python scripts in the [samples](
https://github.com/Adirio/pyobs/tree/master/samples) directory.

Or take a look at the documentation below:

_Output of `pydoc pyobs.Client`:_

```
Help on class Client in pyobs:

pyobs.Client = class Client(builtins.object)
 |  Core class for using pyobs
 |
 |  Simple usage:
 |      >>> from pyobs import Client, requests as obsrequests
 |      >>> client = Client("localhost", 4444, "secret")
 |      >>> client.connect()
 |      >>> client.call(obsrequests.GetVersion()).getObsWebsocketVersion()
 |      u'4.1.0'
 |      >>> client.disconnect()
 |
 |  For advanced usage, including events callback, see the 'samples' directory.
 |
 |  Methods defined here:
 |
 |  __init__(self, host='localhost', port=4444, password='')
 |      Construct a new Client wrapper
 |
 |      :param host: Hostname to connect to
 |      :param port: TCP Port to connect to (Default is 4444)
 |      :param password: Password for the websocket server (Leave this field
 |          empty if no auth enabled on the server)
 |
 |  call(self, obj)
 |      Make a call to the OBS server through the Websocket.
 |
 |      :param obj: Request (class from obswebsocket.requests module) to send
 |          to the server.
 |      :return: Request object populated with response data.
 |
 |  connect(self, host=None, port=None)
 |      Connect to the websocket server
 |
 |      :return: Nothing
 |
 |  disconnect(self)
 |      Disconnect from websocket server
 |
 |      :return: Nothing
 |
 |  reconnect(self)
 |      Restart the connection to the websocket server
 |
 |      :return: Nothing
 |
 |  register(self, func, event=None)
 |      Register a new hook in the websocket client
 |
 |      :param func: Callback function pointer for the hook
 |      :param event: Event (class from obswebsocket.events module) to trigger
 |          the hook on. Default is None, which means trigger on all events.
 |      :return: Nothing
 |
 |  send(self, data)
 |      Make a raw json call to the OBS server through the Websocket.
 |
 |      :param data: Request (python dict) to send to the server. Do not
 |          include field "message-id".
 |      :return: Response (python dict) from the server.
 |
 |  unregister(self, func, event=None)
 |      Unregister a new hook in the websocket client
 |
 |      :param func: Callback function pointer for the hook
 |      :param event: Event (class from obswebsocket.events module) which
 |          triggered the hook on. Default is None, which means unregister this
 |          function for all events.
 |      :return: Nothing
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```

## Problems?

Please check on [Github project issues](https://github.com/Adirio/pyobs/issues
), and if nobody else has experienced it before, you can [file a new issue](
https://github.com/Adirio/pyobs/issues/new).

