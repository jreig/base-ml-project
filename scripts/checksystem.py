print("==================")
print("== SYSTEM CHECK ==")
print("==================")

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"

import keras
import tensorflow as tf
import pandas as pd
import numpy as np

print("TF version:", tf.__version__)
print("Keras version:", keras.__version__)
print("Pandas version:", pd.__version__)
print("Numpy version:", np.__version__)

print()

print("Num GPU available:", len(tf.config.list_physical_devices("GPU")))