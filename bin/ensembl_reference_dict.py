import os, subprocess

def slice_reference():
    with open("../reference/transcript.gtf", 'r') as t:
        t = t.readlines()
        # for z, line in enumerate(t):
        ref = open("../reference/ensembl_ref_dict.txt", 'w')
        genes = "gene_name\tgene_id"
        transcript = "transcript_id\ttsl"
        ref.write(genes+'\t'+transcript+'\n')
        for line in t:
            line = line.split()
            for z, feature in enumerate(line):
                # gene_length = str(int(line[4])+1-int(line[3]))
                if feature == 'gene_id':
                    gene_id = line[z+1].replace(";","").replace("\"", "")
                if feature == 'gene_name':
                    gene_name = line[z+1].replace(";","").replace("\"", "")
                if feature == 'transcript_id':
                    transcript_id = line[z+1].replace(";","").replace("\"", "")
                if feature == 'transcript_support_level':
                    tsl = line[z+1].replace(";","").replace("\"", "")
            ref.write(gene_name+'\t'+gene_id+'\t')
            ref.write(transcript_id+'\t'+tsl+'\n')
            # print (gene_id, gene_name, gene_length)
            # print (transcript_id, tsl)
        ref.close()
        print ("Done!")
        return True

if os.path.isfile("../reference/transcript.gtf") == False:
    print ("Transcript.gtf is not found, generating...")
    os.chmod('generate_transcript.sh', 0o755)
    subprocess.call("./generate_transcript.sh")
    print ("Transcript.gtf generated. Creating dictionary file...")
    slice_reference()
else:
    print ("Transcript.gtf found, generating dictionary...")
    slice_reference()

###ARCHIVED 2018.01.15
