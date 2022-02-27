#!/usr/bin/env python3
import subprocess
from multiprocessing import Pool
import os

src = "./data/prod/"
dest = "./data/prod_backup"

def run(directory):
  # Do something with task here
  subprocess.call(["rsync", "-arq", directory, dest])
if __name__ == "__main__":
  folder_names = os.listdir(src)
  dir_names = [src + folder for folder in folder_names]
  # Create a pool of specific number of CPUs
  p = Pool(len(dir_names))
  # Start each task within the pool
  p.map(run, dir_names)
