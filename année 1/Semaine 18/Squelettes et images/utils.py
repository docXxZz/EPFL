from PIL import Image
import numpy as np
import skimage.color as sc
import torch
from torchvision import transforms

def ntsc_grayscale(numpy_image):
    return numpy_image[:, :, 0] * 0.299 + numpy_image[:, :, 1] * 0.587 + numpy_image[:, :, 2] * 0.114

def prepare_image_for_network(image_fp):
    img = Image.open(image_fp).convert("RGB")

    img = np.array(img)
    gray = np.expand_dims(ntsc_grayscale(img), axis=-1)

    img = img / 255.
    gray = gray / 255.

    img_lab = sc.rgb2lab(img)  # Converting RGB to L*a*b
    img_lab[0] = img_lab[0] / 50. - 1
    img_lab[1:] = img_lab[1:] / 128.

    img_lab = transforms.ToTensor()(img_lab).float()
    gray = transforms.ToTensor()(gray).float()

    return gray, img_lab

def decode_network_output(output):
    output = output.cpu().detach().numpy()[0].transpose(1, 2, 0)
    output[0] = (output[0] + 1) * 50
    output[1:] = output[1:] * 128.
    output = sc.lab2rgb(output)

    return (output * 255).astype(np.uint8)