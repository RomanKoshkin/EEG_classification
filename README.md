# EEG_classification

This repository contains different DL model implementations for EEG-based classification of mental states (attention vs. inattention to continuous auditory input). 

EEGnet... notebooks implement CNN-based binary classifiers that attempt to predict whether the subject was attending to the auditory input or mindwandering.

...stim_reconst notebooks implement a stimulus reconstruction approach, in which a convolutional neural net minimises the MSE loss between the ground truth auditory stimulus and its reconstruction from EEG signal.

Althernative architectures are also present, including capsule networks, and Siamese networks.
