import math

available_function = ["Cosine", "standard"]

def cosine(
        initial_lr: float,
        epoch: int,
        total_epochs: int):
  lr = initial_lr * 0.5 * (1 + math.cos(math.pi * (epoch / total_epochs)))
  return lr

def standard(lr: float, lr_decay: float):
  return lr * lr_decay