import glob, os
command = "featureCounts -T 4 -O -R --primary -F GTF -p -a Drosophila_melanogaster.BDGP5.70.gtf -o teste.table"
for file in glob.glob("*.sort.bam"):
  command += ' ' + file
os.system(command)
