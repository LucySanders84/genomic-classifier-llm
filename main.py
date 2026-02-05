# Prepare resources
    #create requirements.txt detailing libraries that need to be installed
    #import required libraries

#Configure fine-tuning
    #PEFT?
    #QLoRAs?
#Prepare the tokenizer

#Prepare data
    #source coding and non-coding sequences
        #annotated genes are coding sequences
        #non-coding seq idea
            #remove gene sequences from genome
            #check for remaining sequences starting with ATG and ending with stop codon and remove
            #remainder of genome is non-coding?
            #break into sequences 500bp long
    #create pipeline to add fasta sequences to train.csv, test.csv files

#Load and Configure the Model for Sequence Classification
    #DNABERT-2
#Initialize the Trainer

#Start the training

#Evaluate Model Performance


def main():
    pass

if __name__ == '__main__':
    main()