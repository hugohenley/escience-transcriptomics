import glob, os
for file in glob.glob("*.fastq"):
  os.system("fastq_quality_trimmer -Q33 -t 10 -l 10 -i {0} -o {1}".format(file, file))
  #print("fastq_quality_trimmer -Q33 -t 10 -l 10 -i {0} -o {1}".format(file, file))
