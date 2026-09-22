# Challenge 7 - Deep Learning on real data

**Topic:** Deep learning from scratch &nbsp;|&nbsp; **Techniques:** Feedforward network topology, custom activation functions (e.g. Leaky ReLU), epoch sensitivity &nbsp;|&nbsp;
**Data:** student-selected: at least 10 features

## Description

During the last lecture we created a set of classes that can be used to build a deep feed-forward
neural network with an arbitrary number of layers, each one characterized by a variable number of
neurons and an activation function.

In Notebook 3 (Deep Learning) you can find all the code. In the section *A few examples of Neural
Network instances* you can find three examples covering from a simple linear regressor to a
three-layer network. You can also find code to test these examples against the Boston Housing dataset.

As you can see, different network architectures will produce different performance. We expect such
performance to be affected by the following factors:

- number of layers
- number of neurons for each layer
- activation functions

## Your task

You are challenged to design a few network architectures, by changing the aforementioned parameters,
and execute a batch of tests to determine which architecture works best with your data. Specifically
you have to:

1. **Select a new dataset.** Find a new dataset that contains at least 10 distinct features.
2. **Design a few different networks.** Change both the topology (number of layers and neurons) and
   one or more activation functions. You are welcome to add your own activation functions by extending
   the `Operation` class, following the example code that defines the Sigmoid activation. Try for
   instance to add the Leaky ReLU.
3. **Compare the networks.** Test them with the same dataset and observe the effect of each factor.
   Also try to find out whether the number of epochs has any relevant effect.

> **Course materials.** This statement refers to lecture notebooks that are distributed separately and
> are not part of this repository. If you are working the challenge independently, treat the reference
> as background and implement the pieces yourself.

## Solutions

A reference solution exists but is kept in a separate private repository so the challenge stays
solvable. If you are an instructor or reviewer and need access, contact the author.
