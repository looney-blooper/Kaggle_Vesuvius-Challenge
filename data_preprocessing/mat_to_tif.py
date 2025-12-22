import tifffile as tiff
import scipy.io as sio
import os

def convert_mat_to_tif(mat_path, tif_path):
    data = sio.loadmat(mat_path)
    img = data['image']
    tiff.imwrite(tif_path, img)

if __name__ == "__main__":
    input_mat = "input.mat"  
    output_tif = "output.tif"  
    convert_mat_to_tif(input_mat, output_tif)