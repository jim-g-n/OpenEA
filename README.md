# OpenEA Noisy Implementation

This is an extended version of the OpenEA library that requires additional filename extension arguments in loading the KGs and seed alignments. This is used to allow for noise in the data. 

## Overview

The general use of the package is similar to the original OpenEA. To ensure operability, we explicitly include the version numbers for a working GPU implementation. 

#### Dependencies
* Python==3.6.15
* Tensorflow==1.12
* Scipy==1.2.1 
* Numpy==1.16.0
* Graph-tool==2.40
* Pandas==0.24.0
* Scikit-learn==0.20.0
* Matching==0.1.1
* Gensim==3.7.3
* psutil==5.8.0
* smart_open==1.10.0
* python-igraph==0.9.6

#### GPU Installation
The package can be installed using a similar procedure as the original OpenEA.
```bash
conda create --name openea python=3.6.15 graph-tool==2.40 -c conda-forge
conda activate openea
conda install tensorflow-gpu==1.12
```

Then, OpenEA can be installed using pip with the following steps:

```bash
git clone https://github.com/jim-g-n/OpenEA.git OpenEA
cd OpenEA
pip install -e .
```
The `setup.py` file defines explicit versions of dependencies for a GPU implementation. These can be manually updated for a CPU implementation based on the version numbers in the `cpu_requirements.txt` file. Users should also change their TensorFlow to version 1.13.1 if wanting to use a CPU.

#### Usage
The main adjustment is in the number of inputs when reading KGs from a folder. Filename extensions are now required for the seed alignments file and source and target triples files, with the idea to define these in terms of the percentage error. Additionally, validation sets are no longer taken as input. More concretely, KGs can be read using the following function:

```python
read_kgs_from_folder_no_valid(training_data_folder, division, mode, ordered, align_error_rate, source_kg_error, target_kg_error, remove_unlinked=False)
```

where
 * _training_data_folder_, _division_, _mode_, _ordered_ all function as before
 * Train links are read from the file `'train_links_' + str(align_error_rate)`
 * Source triples are read from the file `'rel_triples_1_' + str(source_kg_error)`
 * Target triples are read from the file `'rel_triples_2_' + str(target_kg_error)`

The files `main_from_args.py` and `main_from_args_wo_attr.py` have also been updated to allow for these changes. For example, an experiment on IDS15K with a training size of 30% and 10% error in each of the seed alignments, source triples, and target triples can be run using:

```bash
python main_from_args.py ./args/bootea_args_15K.json IDS15K 0_3/ 10 10 10
```
