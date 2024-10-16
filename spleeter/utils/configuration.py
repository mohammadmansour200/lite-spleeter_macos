#!/usr/bin/env python
# coding: utf8

"""Module that provides configuration loading function."""

import json
from typing import Dict


__email__ = "spleeter@deezer.com"
__author__ = "Deezer Research"
__license__ = "MIT License"


config = """{
    "train_csv": "path/to/train.csv",
    "validation_csv": "path/to/test.csv",
    "model_dir": "2stems",
    "mix_name": "mix",
    "instrument_list": ["vocals", "accompaniment"],
    "sample_rate":44100,
    "frame_length":4096,
    "frame_step":1024,
    "T":512,
    "F":1024,
    "n_channels":2,
    "separation_exponent":2,
    "mask_extension":"zeros",
    "learning_rate": 1e-4,
    "batch_size":4,
    "training_cache":"training_cache",
    "validation_cache":"validation_cache",
    "train_max_steps": 1000000,
    "throttle_secs":300,
    "random_seed":0,
    "save_checkpoints_steps":150,
    "save_summary_steps":5,
    "model":{
            "type":"unet.unet",
            "params":{}
            }
}"""


def load_configuration() -> Dict:
    """
    Loads the 2stems configuration
    """
    return json.loads(config)
