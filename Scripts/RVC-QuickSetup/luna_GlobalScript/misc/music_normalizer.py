import numpy as np
def normalize(audio):
    return (audio - np.mean(audio)) / np.std(audio)