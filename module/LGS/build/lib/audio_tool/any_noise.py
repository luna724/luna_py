import sox
import tensorflow.compat.v1 as tf
import math
import random
import subprocess
import tempfile

def add_noise(input_filename, output_filename, noise_vol, noise_type):

  args = ['sox', input_filename, '-p', 'synth', noise_type, 'vol',
          str(noise_vol), '|', 'sox', '-m', input_filename, '-',
          output_filename]
  command = ' '.join(args)
  tf.logging.info('Executing: %s', command)

  process_handle = subprocess.Popen(
      command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  process_handle.communicate()