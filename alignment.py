import Bio as Bio
from Bio import Phylo
import subprocess
import os

email = "karthraj1@gmail.com"
stype = "dna"
sequence = "output.txt"

# Run clustalo.py with command line arguments
command = "clustalo.py --email " + email + "--stype " + stype + "--sequence " + sequence
subprocess.call(command, shell=True)

# # Find .dnd file in current directory to construct phylogenetic tree
# for file in os.listdir("C:\\Users\\karth\\Desktop\\Fall 2022\\gbrl"):
#     if file.endswith(".dnd"):
#         tree_info = file

# # Draw phylogenetic tree
# tree = Phylo.read(tree_info, "newick")
# tree.ladderize()  #Clean up
# Phylo.draw(tree)
