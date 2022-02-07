import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger

import math
import shutil

def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    
    #Extracting path for train and val
    train_path = os.path.join(data_dir,'train')
    val_path = os.path.join(data_dir,'val')   
    
    f_list =[]
    for name in glob.glob(f'{data_dir}/training_and_validation/*.tfrecord'):
        f_list.append(name)
    
    random.shuffle(f_list)    
    f_no = len(f_list)
    
    #creating the split length of 80% for train and 20% for validation
    train_no = math.ceil((f_no*80)/100)
    val_no = math.ceil((f_no * 20 )/100)
    
    for i , list in enumerate(f_list):
        if i <= train_no:
            shutil.move(list,train_path)
        if i > train_no and i <= train_no+ val_no:
            shutil.move(list,val_path)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)