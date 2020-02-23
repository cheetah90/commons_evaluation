from pathlib import Path
import shutil
import sys


def read_img_ids(img_ids_file_name):
	with open(img_ids_file_name) as f:
		img_ids = f.readlines()
	img_ids = [id.strip() for id in img_ids]
	return img_ids


def prepare_folders(dest_dir):
	# remove folder if exists
	shutil.rmtree(dest_dir, ignore_errors=True)

	# create folder
	Path(dest_dir).mkdir(parents=True, exist_ok=True)


def gather_imgs_by_ids(img_ids, root_dir, dest_dir):
	# prepare the destination folder
	prepare_folders(dest_dir)

	# search only jpg files
	root_dir_path = Path(root_dir)
	for f in root_dir_path.rglob("*"):
		if f.is_file() and f.stem in img_ids:
			shutil.copy(f, dest_dir)


def main():
	# read the img_ids which are contained in a csv file
	img_ids = read_img_ids(sys.argv[1])

	gather_imgs_by_ids(img_ids, sys.argv[2], "filtered_imgs/{}_imgs".format(sys.argv[3]))


if __name__ == '__main__':
	main()