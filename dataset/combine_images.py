import os
import argparse
import numpy as np

from PIL import Image
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--original', type=str, default='../data/original')
parser.add_argument('--grayscale', type=str, default='../data/grayscale')
parser.add_argument('--combined', type=str, default='../data/combined')
args = parser.parse_args()


if not os.path.exists(args.combined):
	os.makedirs(args.combined)

for root, dirs, files in os.walk(args.original, topdown=False):
	for name in tqdm(files):
		try:
			both = Image.new('RGB', (512, 256))
			img = Image.open(os.path.join(args.original, name))
			img2 = Image.open(os.path.join(args.grayscale, name))

			#img = img.resize((256, 256), Image.LANCZOS)
			#img2 = img2.resize((256, 256), Image.LANCZOS)

			both.paste(img2, (0, 0, 256, 256))
			both.paste(img.convert('RGB'), (256, 0, 512, 256))
			both.save(os.path.join(args.combined, name))
		except Exception as e:
			print('Error: {}'.format(e))
