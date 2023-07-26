import math
import sox
import numpy as np

def liner_uniform(min, max):
    return np.random.uniform(min, max)
def log_uniform(min, max):
    log_min_value = math.log(min)
    log_max_value = math.log(max)
    return math.exp(np.random.uniform(log_min_value, log_max_value))
def eq_sound(x):
    tfm = sox.Transformer()
    tfm.pitch(liner_uniform(-0.1, 0.1))
    tfm.contrast(liner_uniform(0.0, 100.0))
    tfm.equalizer(log_uniform(32.0, 4096.0), liner_uniform(2.0, 2.0), liner_uniform(-20.0, 5.0))
    tfm.equalizer(log_uniform(32.0, 4096.0), liner_uniform(2.0, 2.0), liner_uniform(-20.0, 5.0))
    tfm.reverb(liner_uniform(0.0, 70.0))
    return tfm.build_array(input_array=x, sample_rate_in=S_R)