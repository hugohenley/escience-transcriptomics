import glob, os
for file in glob.glob("*.bam"):
  sort_file = file.replace("bam", "sort")
  os.system("samtools sort {0} {1}".format(file, sort_file))
