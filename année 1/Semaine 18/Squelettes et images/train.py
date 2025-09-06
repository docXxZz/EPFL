import numpy as np
from PIL import Image
from skimage.color import rgb2lab, lab2rgb
import torch
from torch import nn, optim
from torchvision import transforms
from torch.utils.data import DataLoader
from dataset import Dataset
from unet_model import UNet
import matplotlib.pyplot as plt
import os
import utils

# Hyperparamètres
NUM_EPOCHS = 10
BATCH_SIZE = 1
LEARNING_RATE = 1e-9
MOMENTUM = 0.9
WEIGHT_DECAY = 1e-5
ROOT_TRAIN = './TRAIN_images'
ROOT_TESTING_IMAGES = './TEST_images'
ROOT_OUTPUT = './OUTPUT'
MODEL_PATH = './model.pth'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Création du modèle
model = UNet(1, 3).to(device)

# Chargement des poids si existants
if os.path.exists(os.path.join(ROOT_OUTPUT, './model.pth')):
    model.load_state_dict(torch.load(os.path.join(ROOT_OUTPUT, './model.pth')))

# Création du dataset représentant les données ainsi que du DataLoader
ds = Dataset(ROOT_TRAIN)
train_dataloader = DataLoader(ds, batch_size=BATCH_SIZE, shuffle=True, drop_last=True)

# Création de l'optimiseur
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE, momentum=MOMENTUM, nesterov=True, weight_decay=WEIGHT_DECAY)

# L'erreur quadratique sera conservée pour visualisation
losses = []

# Pour chacune des époques
for e in range(NUM_EPOCHS):
    print('Epoch', e)

    # Pour chacun des paquets de données aléatoires avec la taille de paquet spécifiée par BATCH_SIZE
    for i, (X, Y) in enumerate(train_dataloader):

        # Préparation des données pour le réseau
        X = X.to(device)
        Y = Y.to(device)

        # Remise à zéro des gradients
        optimizer.zero_grad()

        # Prédiction du réseau
        Y_hat = model(X)

        # Calcul de l'erreur
        loss = nn.MSELoss(reduction='mean')(Y_hat, Y)

        # Rétropropagation
        loss.backward()
        # Mise à jour des poids en utilisant la méthode de descente de gradient
        optimizer.step()

        # Affichage de l'erreur
        print('    ', loss.item())
        losses.append(loss.item())

    # Visualisation de l'erreur
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    line, = ax.plot(losses, color='blue', lw=2)
    ax.set_yscale('log')
    plt.savefig(os.path.join(ROOT_OUTPUT, 'losses.png'))
    plt.clf()

    # Sauvegarde des poids
    torch.save(model.state_dict(), os.path.join(ROOT_OUTPUT, 'model.pth'))

    model.eval()
    for image in os.listdir(ROOT_TESTING_IMAGES):
        image_fp = os.path.join(ROOT_TESTING_IMAGES, image)
        X, _ = utils.prepare_image_for_network(image_fp)
        X = X.to(device)
        network_output = model(X.unsqueeze(0))
        decoded_output = utils.decode_network_output(network_output)

        # Visualisation
        input_image = np.array(Image.open(image_fp))
        gray = np.repeat(utils.ntsc_grayscale(input_image)[:, :, np.newaxis], 3, axis=2)
        res = np.concatenate((gray, decoded_output, input_image), axis=1)

        image_pil = Image.fromarray(res.astype(np.uint8))

        fn = os.path.join(ROOT_OUTPUT, image[:-4] + '_' + str(e).zfill(2) + '.png')
        image_pil.save(fn)
    model.train()


