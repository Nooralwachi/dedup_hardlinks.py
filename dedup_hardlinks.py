import os
from collections import defaultdict
def dedup_hardlinks(folder):
	nodes=defaultdict(list)
	cwd = os.getcwd()
	for file in os.listdir(cwd):
		if not os.path.islink(file):
			inode=os.stat(file).st_ino
			# print(inode, file)
			nodes[inode].append(file)
	# print(nodes)
	for inode, files in nodes.items():
		while len(files)>1:
			print(f'removing duplicate hardlink {files[-1]}')
			os.remove(files[-1])
			files =files[:-1]	

dedup_hardlinks('file_dir')

