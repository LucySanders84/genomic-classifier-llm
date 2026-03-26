
# Genomic Classifier Transformer Model

Implementation of a genomic RNA coding classification pipeline using baseline models and fine-tuned Transformer-based architectures (DNABERT-2) (Zhou et al, 2024). In this project, datasets are built from the Candida Albicans genome. Coding sequences are defined as those occurring on an exon region. Non-coding sequences are sourced from intergenic regions. Data obtained from [Candida Genome Database](http://www.candidagenome.org/).

## Contributors
Jessica Riguero
<br>Lucy Sanders
<br>Mahan Fouladi
<br>Naziha James
<br>Tao Ma

## Requirements

Python 3.13
## Installation

Install git:
```shell
pip install git
```

Clone genomic classifier repository:
```shell
git clone https://github.com/LucySanders84/genomic-classifier-llm.git
```

Install dependencies:
```shell
pip install -r requirements.txt
```

## Usage

This guide provides a step-by-step walkthrough of using this project to build datasets and fine-tune the DNABERT-2 model. 

### Annotation-based Dataset Pipeline

To run the annotation-based dataset pipeline, we must first download source data and set the necessary parameters.

#### Setup
##### Data Sources
In order to build datasets, we must first obtain the Candida Albicans genome data:

Linux:
```shell
# from project root navigate to data_files directory
cd data_files

# download necessary data files (chromosomes.fasta)
wget http://www.candidagenome.org/download/sequence/C_albicans_SC5314/Assembly22/current/C_albicans_SC5314_A22_current_chromosomes.fasta.gz
wget http://www.candidagenome.org/download/gff/C_albicans_SC5314/Assembly22/C_albicans_SC5314_A22_current_features.gff
wget http://www.candidagenome.org/download/gff/C_albicans_SC5314/Assembly22/C_albicans_SC5314_A22_current_intergenic.gff

# unzip .gz file and remove 
gunzip C_albicans_SC5314_A22_current_chromosomes.fasta.gz
rm C_albicans_SC5314_A22_current_chromosomes.fasta.gz
```
##### Data Source Parameters
Once the necessary source files are available, the data source parameters should be assigned to a dictionary:
```python
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent  
  
DATA_PATH = ROOT_DIR / 'data_files'

data_source_parameters = {  
	# labels used to identify the classification groups
    'labels': {  
        '0': '0',  
        '1': '1'  
    },  
    # feature source file for each group
    'fsf': {  
        '0': DATA_PATH / 'C_albicans_SC5314_A22_current_intergenic.gff',  
        '1': DATA_PATH / 'C_albicans_SC5314_A22_current_features.gff'  
    },
    # name of target feature in data source  
    'target': {  
        '0': 'intergenic_region',  
        '1': 'exon'  
    },
    # sequence source data 
    'ss': {  
        'filename': DATA_PATH / 'C_albicans_SC5314_A22_current_chromosomes.fasta', 
        'id_pattern': re.compile(r'Ca22chr\S+_C_albicans_SC5314')  
    }  
}
```

##### Input Parameters
Inputs in this project are the individual datapoints found in the datasets. The input parameters variable defines values for the input length, stride used to produce the inputs and max N percentage to allow in an input. This project creates inputs 512 characters long, with a stride of 50% the length and allows 2% Ns:
```python
INPUT_LENGTH = 512

input_parameters = {
'length': INPUT_LENGTH,  
'stride': int(INPUT_LENGTH/2),  
'max_n_percentage': 0.02
}
```

#### Running the pipeline
The annotation-based dataset pipeline is comprised of four steps:
- Input generation
- Data validation
- Dataset balancing
- Data file creation
All of these steps are contained within the pipeline.run function. Call this function passing the parameter variables as parameters:
```python
from data_pipeline import pipeline


pipeline.run(data_source_parameters, input_parameters)
```

The pipeline will create train.csv (80% of total inputs generated), test.csv (10% of total inputs generated) and val.csv (10% of total inputs generated) files in the project's data files directory. The datasets are now ready for use within the model training workflow.

#### Complete pipeline script
```python
from pathlib import Path
from data_pipeline import pipeline


ROOT_DIR = Path(__file__).resolve().parent.parent  
DATA_PATH = ROOT_DIR / 'data_files'
INPUT_LENGTH = 512

data_source_parameters = {  
	# labels used to identify the classification groups
    'labels': {  
        '0': '0',  
        '1': '1'  
    },  
    # feature source file for each group
    'fsf': {  
        '0': DATA_PATH / 'C_albicans_SC5314_A22_current_intergenic.gff',  
        '1': DATA_PATH / 'C_albicans_SC5314_A22_current_features.gff'  
    },
    # name of target feature in data source  
    'target': {  
        '0': 'intergenic_region',  
        '1': 'exon'  
    },
    # sequence source data 
    'ss': {  
        'filename': DATA_PATH / 'C_albicans_SC5314_A22_current_chromosomes.fasta', 
        'id_pattern': re.compile(r'Ca22chr\S+_C_albicans_SC5314')  
    }  
}

input_parameters = {
'length': INPUT_LENGTH,  
'stride': int(INPUT_LENGTH/2),  
'max_n_percentage': 0.02
}

pipeline.run(data_source_parameters, input_parameters)
```
### Model Training Workflow
The model training workflow is contained in a Jupyter notebook. This file type can be ran to perform model training in Google Colab with a T4 GPU runtime. The model training workflow is available in the project Github repository. Open the notebook and run all coding cells to fine-tune DNABERT-2 to classify coding and non-coding sequences from the Candida Albicans genome. 

## License

[MIT](https://choosealicense.com/licenses/mit/)

## References 
Zhou, Z., Ji, Y., Li, W., Dutta, P., Davuluri, R., & Liu, H. (2024). _DNABERT-2: Efficient Foundation Model and Benchmark For Multi-Species Genome_ (arXiv:2306.15006). arXiv. [https://doi.org/10.48550/arXiv.2306.15006](https://doi.org/10.48550/arXiv.2306.15006)
