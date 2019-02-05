from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import warnings


from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy


def train_nlu_spacy():
    training_data = load_data('nlu_data.md')
    trainer = Trainer(config.load("nlu_config_spacy.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="spacy")
    return model_directory

def train_nlu_tensorflow():
    training_data = load_data('nlu_data.md')
    trainer = Trainer(config.load("nlu_config_tensorFlow.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="tensorFlow")
    return model_directory

def train_dialogue(
        domain_file="domain.yml",
        model_path="models/dialogue",
        training_data_file="stories.md"
        ):
    fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                          core_threshold=0.3,
                          nlu_threshold=0.3)
    agent = Agent(
        domain_file,
        policies=[MemoizationPolicy(max_history=3), KerasPolicy(), fallback]
        )
    training_data = agent.load_data(training_data_file) #, augmentation_factor = 0)
    agent.train(
        training_data,
        epochs=400,
        batch_size=100,
        validation_split=0.2
        )
    agent.persist(model_path)
    return agent


def train_all_spacy():
    model_directory = train_nlu_spacy()
    agent = train_dialogue()
    return [model_directory, agent]

def train_all_tensorFlow():
    model_directory = train_nlu_tensorflow()
    agent = train_dialogue()
    return [model_directory, agent]


if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot training')

    parser.add_argument(
            'task',
            choices=["train-nlu-s", "train-nlu-t", "train-dialogue", "train-all-s", "train-all-t"],
            help="what the bot should do?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu-s":
        train_nlu_spacy()
    elif task == "train-nlu-t":
        train_nlu_tensorflow()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "train-all-s":
        train_all_spacy()
    elif task == "train-all-t":
        train_all_tensorFlow()