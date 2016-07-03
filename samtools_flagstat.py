import glob, os
for file in glob.glob("*.sort.bam"):
  flag_file = file.replace(".sort.bam", ".flagstat")
  os.system("samtools flagstat {0} > {1}".format(file, flag_file))
