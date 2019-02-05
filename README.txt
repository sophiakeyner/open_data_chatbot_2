Install the requirements
### together with spacy install english model 'en_core_web_sm' 

1) run actions server

python -m rasa_core_sdk.endpoint -p 5002 --actions actions

2) train NLU and CORE

python trainer.py train-all-s

3) run http server from webchat folder

python -m http.server 80

4) run webchat

python run_webchat.py

5) chatbot is running at http://localhost/index.html


