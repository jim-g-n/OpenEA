# OpenEA Noisy Implementation

This is an extended version of the OpenEA library that allows for additional filename extension arguments in loading the KGs and seed alignments. This is used to allow for noise in the data. 

## Overview

The general use of the package is similar to the original OpenEA. To ensure reproducibility, we explicitly include the version numbers of the GPU implementation used in our experiments. 

#### Dependencies
* Python 3.6.15
* Tensorflow 1.12
* Scipy 1.2.1 
* Numpy 1.16.0
* Graph-tool 2.40
* Pandas 0.24.0
* Scikit-learn 0.20.0
* Matching 0.1.1
* Gensim 3.7.3
* psutil 5.8.0
* smart_open 1.10.0
* python-igraph 0.9.6

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

#### Usage
The following is an example about how to use OpenEA in Python (We assume that you have already downloaded our datasets and configured the hyperparameters as in the [examples](https://github.com/nju-websoft/OpenEA/tree/master/run/args).)
```python
import openea as oa

model = oa.kge_model.TransE
args = load_args("hyperparameter file folder")
kgs = read_kgs_from_folder("data folder")
model.set_args(args)
model.set_kgs(kgs)
model.init()
model.run()
model.test()
model.save()

```
More examples are available [here](https://github.com/nju-websoft/OpenEA/tree/master/run)

To run the off-the-shelf approaches on our datasets and reproduce our experiments, change into the ./run/ directory and use the following script:

```bash
python main_from_args.py "predefined_arguments" "dataset_name" "split"
```

For example, if you want to run BootEA on D-W-15K (V1) using the first split, please execute the following script:

```bash
python main_from_args.py ./args/bootea_args_15K.json D_W_15K_V1 721_5fold/1/
```
