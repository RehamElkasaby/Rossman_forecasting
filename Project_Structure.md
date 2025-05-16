# Project Structure:
**configs**: in configs we define every single thing that can be configurable and can be changed in the future. Good examples are:
- training hyperparameters, 
- folder paths, 
- the model architecture, 
- metrics, 
- flags
  
**dataloader**:All the data loading and data preprocessing classes and functions live here.

**evaluation** is a collection of code that aims to evaluate the performance and accuracy of our model.

**executor**: in this folder, we usually have all the functions and scripts that train the model or use it to predict something in different environments. And by different environments I mean: executors for GPUs, executors for distributed systems. This package is our connection with the outer world and it’s what our “main.py” will use.

**model** contains the actual deep learning code (we talk about tensorflow, pytorch etc)

**notebooks** include all of our jupyter/colab notebooks in one place.

**utils**: utilities functions that are used in more than one places and everything that don't fall in on the above come here.


inspired by:
[reference_best_practices](https://theaisummer.com/best-practices-deep-learning-code/)


another one could be:
```
├──  config
│    └── defaults.py  - here's the default config file.
│
│
├──  configs  
│    └── train_mnist_softmax.yml  - here's the specific config file for specific model or dataset.
│ 
│
├──  data  
│    └── datasets  - here's the datasets folder that is responsible for all data handling.
│    └── transforms  - here's the data preprocess folder that is responsible for all data augmentation.
│    └── build.py  		   - here's the file to make dataloader.
│    └── collate_batch.py   - here's the file that is responsible for merges a list of samples to form a mini-batch.
│
│
├──  engine
│   ├── trainer.py     - this file contains the train loops.
│   └── inference.py   - this file contains the inference process.
│
│
├── layers              - this folder contains any customed layers of your project.
│   └── conv_layer.py
│
│
├── modeling            - this folder contains any model of your project.
│   └── example_model.py
│
│
├── solver             - this folder contains optimizer of your project.
│   └── build.py
│   └── lr_scheduler.py
│   
│ 
├──  tools                - here's the train/test model of your project.
│    └── train_net.py  - here's an example of train model that is responsible for the whole pipeline.
│ 
│ 
└── utils
│    ├── logger.py
│    └── any_other_utils_you_need
│ 
│ 
└── tests					- this foler contains unit test of your project.
│    ├── test_data_sampler.py
│ 
│ 
└── app					- for deployment.
     ├── client.py
     |__ sever.py
```
[inspired by](https://github.com/L1aoXingyu/Deep-Learning-Project-Template)


```
pytorch-project/
├── README.md
├── config.py
├── train.py
├── test.py
├── evaluate.py
├── models/
│   ├── __init__.py
│   ├── model.py
│   ├── cnn/
│   │   ├── __init__.py
│   │   ├── cnn.py
│   │   └── resnet.py
│   └── rnn/
│       ├── __init__.py
│       ├── rnn.py
│       └── lstm.py
├── data/
│   ├── __init__.py
│   ├── data.py
│   ├── dataset.py
│   ├── dataloader.py
│   └── transforms.py
├── losses/
│   ├── __init__.py
│   ├── loss.py
│   └── cross_entropy.py
├── metrics/
│   ├── __init__.py
│   ├── metric.py
│   └── accuracy.py
├── optimizers/
│   ├── __init__.py
│   ├── optimizer.py
│   └── adam.py
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   ├── timer.py
│   └── plotter.py
├── results/
│   ├── model.pth
│   ├── predictions.csv
│   └── plots/
│       ├── loss.png
│       └── accuracy.png
└── logs/
    ├── train.log
    └── test.log
```

[inspired by](https://www.geeksforgeeks.org/how-to-structure-a-pytorch-project/)