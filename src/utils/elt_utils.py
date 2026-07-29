import os 
import sys 
import pickle
import pandas as pd 
import numpy as np 
from scipy import sparse
from src.exception.exception import CustomeException



def save_to_csv(data:pd.DataFrame,path:str):

    try:
        dir_name = os.path.dirname(path)
        
        os.makedirs(dir_name,exist_ok=True)
       
        data.to_csv(path,index=False)
    except Exception as e:
        raise CustomeException(e,sys)



def save_numpy_array_data(file_path: str, array):
    """
    Save numpy array or sparse matrix to file path
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # If array is sparse matrix
        if sparse.issparse(array):
            if not file_path.endswith(".npz"):
                file_path = file_path

            sparse.save_npz(file_path, array)

        # If array is normal numpy array
        else:
            if not file_path.endswith(".npy"):
                file_path = file_path

            with open(file_path, "wb") as file:
                np.save(file, array)

    except Exception as e:
        raise CustomeException(e, sys)



def load_numpy_array_data(file_path: str):
    """
    Load numpy array or sparse matrix
    """
    try:

        # Load sparse matrix
        if file_path.endswith(".npz"):
            return sparse.load_npz(file_path)

        # Load numpy array
        else:
            with open(file_path, "rb") as file_obj:
                return np.load(file_obj)

    except Exception as e:
        raise CustomeException(e, sys)


def save_object(file_path:str,object)-> None:
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(object,file_obj)
    except Exception as e:
        raise CustomeException(e,sys)


def load_object(file_path:str)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception("File doesn't exist in this path")
        
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomeException(e,sys)