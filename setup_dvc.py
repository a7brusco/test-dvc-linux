import os

dna_data_path = os.environ.get("DNA_DATA_PATH")
os.system(f"dvc remote modify main url {dna_data_path}")
os.system(f"dvc cache dir {dna_data_path}/cache")