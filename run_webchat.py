from rasa_core.channels.socketio import SocketIOInput

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig


# load your trained agent
interpreter = RasaNLUInterpreter("../models/nlu/default/spacy")
action_endpoint = EndpointConfig(url="http://localhost:5002/webhook")


agent = Agent.load('../models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)

input_channel = SocketIOInput(
        # event name for messages sent from the user
        user_message_evt="user_uttered",
        # event name for messages sent from the bot
        bot_message_evt="bot_uttered",
        # socket.io namespace to use for the messages
        namespace=None
)

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5055, serve_forever=True)