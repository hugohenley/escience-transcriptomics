import glob, os
for file in glob.glob("*.sam"):
  bam_file = file.replace("sam", "bam")
  os.system("samtools view -b -S {0} > {1}".format(file, bam_file))
