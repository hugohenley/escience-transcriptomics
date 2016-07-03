import glob, os
command = "/home/hugo/storage/TrabalhoFinal_eScience_shell/subread-1.5.0-p3-Linux-x86_64/bin/featureCounts -T 4 -O -R --primary -F GTF -p -a Drosophila_melanogaster.BDGP5.70.gtf -o teste.table"
for file in glob.glob("*.sort.bam"):
  command += ' ' + file
os.system(command)
