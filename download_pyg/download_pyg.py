# https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.MoleculeNet.html
from torch_geometric.datasets import MoleculeNet

# mkdir
root = './molecule_data'

# datasets in pyg
dataset_names = [
    "ESOL", "FreeSolv", "Lipo", "PCBA", "MUV", 
    "HIV", "BACE", "BBBP", "Tox21", "ToxCast", 
    "SIDER", "ClinTox"
]

# download
for name in dataset_names:
    print(f"Downloading dataset: {name}...")
    dataset = MoleculeNet(root=root, name=name)
    print(f"Dataset {name} successfully downloaded and processed!")
