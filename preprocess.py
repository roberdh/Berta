import os
import time


def SamtoText(input_dir, current, bamfile_name, chromosomes):
	output_dir = input_dir+'/'+bamfile_name[:-4]+'/'
	os.makedirs(output_dir, exist_ok=True)

	cmd1 = current+"/samtools index "+input_dir+"/"+bamfile_name		## make samtools index filename.bam.bai
	os.system(cmd1)
	print("Samtools index run completed.")

	for chrom in chromosomes:
		print("Start of ", chrom)
		tt = time.time()
		cmd2 = current+"/samtools view -b "+input_dir+"/"+bamfile_name+" "+chrom+" -o "+output_dir+"/"+chrom+".bam"
		cmd3 = current+"/samtools pileup "+output_dir+"/"+chrom+".bam | cut -f 1,2,4 > "+output_dir+"/"+chrom+".txt"    ### Need to use pileup, not mpileup
		command = cmd2+";"+cmd3
		os.system(command)
		print("Samtools Time: ", time.time()-tt)
	print("Input text file generation completed")
	return
