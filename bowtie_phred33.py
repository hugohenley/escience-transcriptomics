import glob, os
for file in glob.glob("*.fastq"):
  sam_file = file.replace("fastq", "sam")
  os.system("bowtie2 -x dm70 -U {0} -S {1} -p 4 --phred33".format(file, sam_file))
