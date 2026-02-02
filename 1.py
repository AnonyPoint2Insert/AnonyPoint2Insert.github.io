from diffusers.utils import load_video, export_to_video
import numpy as np
import os
from tqdm import tqdm

a = load_video(f"Demo_anony.mp4")
a = [np.array(i) for i in a]
a = np.array(a)
a = a.astype(float)/255
export_to_video(a, f"Demo_anony_quality.mp4", quality=5)