import os
import random

import numpy as np
import torch


def seed_everything(seed: int):
    """seed値を固定する関数

    Args:
        seed (int): seed値
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
