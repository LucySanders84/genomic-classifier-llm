def main():
    #data pipeline tasks
    #coding sequences
        #add sequence to csv file
            #get sequence file
            #parse sequence into single str
            #open coding_sequences csv file
            #add sequence and label to csv file
    #non-coding sequences
        #concat full candida genome
        #for gene fasta files
            #parse header for location
            #remove location from genome file
        #split remaining genome into 500bp segments
        #test whether segment is coding or not
        #append segments that don't code to csv file
    #create pipeline script to generate csv files
    pass


if __name__ == '__main__':
    main()