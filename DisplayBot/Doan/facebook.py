from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import os
from rasa_core.utils import EndpointConfig

# load your trained agent
interpreter = RasaNLUInterpreter("models/nlu/default/botneu/")
MODEL_PATH = "models/dialogue"
print(MODEL_PATH)
action_endpoint = EndpointConfig(url="https://doanneu1-actions.herokuapp.com/webhook")
print("action_endpoint", action_endpoint)
agent = Agent.load(MODEL_PATH, interpreter=interpreter, action_endpoint=action_endpoint)
print("agent")
input_channel = FacebookInput(
        fb_verify="chat-bot",
        # you need tell facebook this token, to confirm your URL
        fb_secret="06191183529878f9ed1041db6aa07d41",  # your app secret
        fb_access_token="EAAFvxZClqvowBAKnZBZBZAJq6EyY3pISAcOCwG0KQCVeZBPZAa3OAYL9Vvbvyw6dSsa552UDtxCyFu0MlV1hLbTMYGwEDXPEiRqtp1mX8FJN5LZAZB4puN3gmaEZC6vNuqAcnZA4Tc25j2kf0QYXIbb7whbLrZCMEOR0l3AL6tNjhZC6FyLTkYnKvGtt"
        # token for the page you subscribed to
)
print("here")
# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel],  int(os.environ.get('PORT', 5004)), serve_forever=True)
