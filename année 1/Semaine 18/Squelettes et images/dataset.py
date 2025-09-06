import os
import utils

class Dataset:
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.files = [x for x in os.listdir(root_dir) if x.endswith('.jpg') or x.endswith('.png')]

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        return utils.prepare_image_for_network(os.path.join(self.root_dir, self.files[idx]))
