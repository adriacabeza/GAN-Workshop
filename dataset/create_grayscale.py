import os
import argparse

from tqdm import tqdm
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('--original', type=str, default='../data/original')
parser.add_argument('--grayscale', type=str, default='../data/grayscale')
args = parser.parse_args()

if not os.path.exists(args.grayscale):
	os.makedirs(args.grayscale)

for root, dirs, files in os.walk(args.original, topdown=False):
	for name in tqdm(files):
		try:
			image_file = Image.open(os.path.join(args.original, name))# open colored image
			image_file = image_file.convert('L')
			image_file.save(os.path.join(args.grayscale, name), quality=95)
		except Exception as e:
			print(e)
