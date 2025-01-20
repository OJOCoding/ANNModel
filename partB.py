"""
FINAL PROJECT SUBMISSION
STUDENT NAME: ONI LUCA
STUDENT CODE: 20200008
PART: B
CLASS: CS340 – INTRODUCTION TO ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING USING PYTHON
EXTRA WORK --- Function that creates data from scratch.
EXTRA WORK *** Neural network from scratch using only numpy library!!! ***
"""


import numpy as np
import matplotlib.pyplot as plt
import os

# EXTRA WORK FUNCTION CREATES TRAINING FILE AND INPUT FILE
def file_creator():
    training_file = open("training_data.txt", 'w')
    input_file = open("input_data.txt", 'w')

    for x in range(10):
        input_file.write("1" * x + "0" * (10 - x) + "\n")
        if x % 2 == 0:
            if x <= 4:
                training_file.write("1" * x + "0" * (10 - x) + ",0,0" + "\n")
            else:
                training_file.write("1" * x + "0" * (10 - x) + ",0,1" + "\n")
        else:
            if x > 4:
                training_file.write("1" * x + "0" * (10 - x) + ",1,1" + "\n")
            else:
                training_file.write("1" * x + "0" * (10 - x) + ",1,0" + "\n")


file_creator()

# Function used in order to read the training_data file

def file_reader(training_file='training_data.txt'):
    inputs = []
    outputs = []

    file = open(training_file)
    for n in file:
        unary_num, target1, target2 = n.strip('\n').split(',')
        inputs.append(list(map(int, list(unary_num))))
        outputs.append([int(target1), int(target2)])
    return inputs, outputs

# EXTRA WORK --- ARTIFICIAL NEURAL NETWORK BACKPROPAGATION ALGORITHM FROM SCRATCH ---

class ANN(object):
    #input and output vectors created from training_data file
    inputs, outputs = file_reader(training_file='training_data.txt')
    inputs = inputs / np.amax(inputs)
    outputs = outputs / np.amax(outputs)

    #neural network layers and weights
    def __init__(self, in_size: object = 10, hiddenSize: object = 5, outputSize: object = 2) -> object:
        self.inputSize = 10
        self.outputSize = 2
        self.hiddenSize = 3

        self.WEIGHTS_IN_HI_LAYER = np.random.randn(self.inputSize, self.hiddenSize)
        self.WEIGHTS_HI_OUT_LAYER = np.random.randn(self.hiddenSize, self.outputSize)

    #feedforward algorithm
    def feedforwardpropagation(self, inputs):
        self.z = np.dot(inputs, self.WEIGHTS_IN_HI_LAYER )  #Dot product of inputs and first set of weights
        self.z2 = self.sigmoid(self.z)                      #Activation function
        self.z3 = np.dot(self.z2, self.WEIGHTS_HI_OUT_LAYER)#Dot product of hidden layer and second sets of weights
        predicted_output = self.sigmoid(self.z3)
        return predicted_output

    #sigmoid activation function
    def sigmoid(self, sig, deriv=False):
        return 1 / (1 + np.exp(-sig))

    def sigmoid_derivative(self,sig):
        return sig * (1 - sig)

    #backpropagation algorithm
    def backwardspropagation(self, inputs, outputs, predicted_output, learningRate=1):
        self.output_error = outputs - predicted_output
        self.output_delta = self.output_error * self.sigmoid_derivative(predicted_output)

        self.z2_error = self.output_delta.dot(self.WEIGHTS_HI_OUT_LAYER.T)
        self.z2_delta = self.z2_error * self.sigmoid_derivative(self.z2)

        self.WEIGHTS_IN_HI_LAYER  += inputs.T.dot(self.z2_delta) * learningRate  # Adjusting IN_HI_LAYER weights
        self.WEIGHTS_HI_OUT_LAYER += self.z2.T.dot(self.output_delta) * learningRate# Adjusting HI_OUT_LAYER weights

    #training algorithm
    def train(self, inputs, outputs, learningRate):
        predicted_output = self.feedforwardpropagation(inputs)
        self.backwardspropagation(inputs, outputs, predicted_output, learningRate)

"""
    Menu option 1: Enter network topology.
        Enter a new network topology to be implemented, consisting of 2-3 layers. For
        instance, if the user indicates 10-5-2 that should mean that the input layer accepts vectors
        of 10 values, the middle layer comprises 5 neurons and the output layer comprises 2
        neurons.
"""
def opt1(inputSize, hiddenSize, outputSize):
    neuralnetworkmodel = ANN(inputSize, hiddenSize, outputSize)
    return neuralnetworkmodel

"""
    Menu option 2: initiate a training pass.
        The user should be asked for a training data set file (default file name:
        training_data.txt), a learning step and a number of training epochs (hitting enter in
        any of these input questions should resort to reasonable default values). The values of the
        weights post-training should be maintained in memory, while the decreasing output of the
        cost function should be recorded in a text file named training_progress.txt (along with the
        training epoch number).
"""
def opt2(neuralnetworkmodel, training_file, epochs, learning_rate):  # code for option2
    inputs, outputs = file_reader(training_file)
    inputs = inputs / np.amax(inputs)
    outputs = outputs / np.amax(outputs)
    progress_writer = open('training_progress.txt', 'w')
    graph_data_writer = open('graph_data.txt', 'w')
    for i in range(epochs):  # trains the NN 1000 times
        if (i % 100 == 0):
            progress_writer.write("In the epoch " + str(i) + " the loss was calculated at: " + str(
                np.mean(np.square(outputs - neuralnetworkmodel.feedforwardpropagation(inputs)))) + "\n")
            graph_data_writer.write(str(i) + "," + str(np.mean(np.square(outputs - neuralnetworkmodel.feedforwardpropagation(inputs)))) + "\n")
        neuralnetworkmodel.train(inputs, outputs, learning_rate)

    #Saving post training weight
    weight1=neuralnetworkmodel.WEIGHTS_IN_HI_LAYER
    weight2=neuralnetworkmodel.WEIGHTS_HI_OUT_LAYER

    return neuralnetworkmodel

"""
    Menu option 3: classify test data.
        Present the network with a series of input vectors for classification, contained in a text
        file called input_data.txt. The network should process these vectors and add the
        corresponding output vectors at the end of each line, then save the data into a comma
        delimited text file named training_output.txt.
"""
def opt3(neuralnetworkmodel):  # code for option3
    def input_reader():
        inputs = []

        file = open("input_data.txt")
        for x in file:
            unary_num = x.strip('\n')
            inputs.append(list(map(int, list(unary_num))))
        return inputs

    inputs = input_reader()
    inputs = inputs / np.amax(inputs)

    predicted_outputs = neuralnetworkmodel.feedforwardpropagation(inputs)
    predicted_outputs_rounded = np.round_(predicted_outputs)
    np.savetxt('predicted_outputs_vector.txt', predicted_outputs_rounded , delimiter=',', fmt='%i')
    print("The predicted output file is created as training_output!")
    prediction_vector_file = open("predicted_outputs_vector.txt", "r")
    output_prediction = open("training_output.txt", "w")
    with open("input_data.txt", "r") as input_r:
        for lines in input_r:
            output_prediction.write(str(lines).rstrip('\n') + "," + str(prediction_vector_file.readline(int(lines) - 1)))

""""
    Menu option 4: display training result graphics.
        Upon conclusion of training of the ANN in part B, there should be a menu option for the
        user to select in order to have a graph displayed (in a GUI pop up window), depicting the
        gradually improving classification accuracy every 10 or every 100 training epochs or so (y
        axis: cost function output and/or success percentage and/or training error; x axis: training
        epochs). This graph should have clearly labelled axes and could be based on the same
        data which is saved into the comma delimited text file training_progress.txt.
"""

def opt4():
    x_axis = []
    y_axis = []
    with open("graph_data.txt", "r") as filestream:
        for line in filestream:
            currentline = line.split(",")
            x_axis.append(int(currentline[0]))
            y_axis.append(float(currentline[1]))
    plt.plot(x_axis, y_axis)
    plt.xlabel('TRAINING EPOCHS')
    plt.ylabel('COST FUNCTION OUTPUT')
    plt.title('TRAINING PROGRESS')
    plt.tight_layout()
    plt.show()

# Variables used throughout the project
global inputSize
global outputSize
global hiddenSize
global epochs
global learningRate
global training_file
global inputs
global outputs
global route_checker

# PART B PROGRAM MENU
def progmenu():
    # variable used in order to make the user run through options one by one
    route_checker: int = 0

    # ERROR HANDLING ON USER INPUT
    while True:
        try:
            print("\n")
            print(" Fall 2023 CS 340 PROJECT ")
            print(" Option 1: Enter network topology.")
            print(" Option 2: Initiate a training pass.")
            print(" Option 3: Classify test data.")
            print(" Option 4: Display training result graphics.")
            print(" Option 5: EXIT.")
            choice = int(input("\nEnter the option you want to see: *(Integers only!)\n"))

        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")

        else:
            if choice == 1:
                #OPTION 1 *(as this model is trained on a specific dataset, only input 10 and output 2 are accepted)

                print('\nPlease enter the topology of the ANN:' + '\n')
                try:
                    inputSize = int(input(
                        "First please enter the number of neurons in the input layer *(Press enter for default:10) : "))
                    if inputSize != 10:
                        print("\nThis module only works for input layer 10! Work in progress! \n")
                        inputSize = 10
                except ValueError:
                    inputSize = 10
                    print("\nInput Layer -> 10\n")
                try:
                    hiddenSize = int(input(
                        "First please enter the number of neurons in the input layer *(Press enter for default:5) : "))
                except ValueError:
                    hiddenSize = 15
                    print("\nHidden Layer -> 15\n")
                try:
                    outputSize = int(input(
                        "First please enter the number of neurons in the input layer *(Press enter for default:2) : "))
                    if outputSize != 2:
                        print("\nThis module only works for input layer 10! Work in progress! \n")
                        outputSize = 2
                except ValueError:
                    outputSize = 2
                    print("\nOutput Layer -> 2\n")
                print("Your chosen typology is : Input Layer -> " + str(inputSize) + ", Hidden Layer -> " + str(
                    hiddenSize) + ", Output Layer -> " + str(outputSize))
                opt1(inputSize, hiddenSize, outputSize)  # calls option 1
                route_checker = 1

            elif choice == 2:  # OPTION 2 *(only given dataset is used)
                if route_checker >= 1:
                    print('Initiate a training pass!' + '\n')
                    try:
                        training_file = input(
                            "First please enter the filename containing training data *(Press enter for default:'training_data.txt') :")
                        print("\nThis module only works for training_data.txt only! Work in progress! \n")
                        training_file = 'training_data.txt'
                    except ValueError:
                        print("File chosen -> training_data.txt")
                        training_file = 'training_data.txt'
                    try:
                        epochs = int(input(
                            "First please enter the number of epochs you want to train the model for: *(Press enter for default:1000) :"))
                    except ValueError:
                        epochs = 1000
                        print("Number of epochs chosen -> "+str(epochs)+"\n")
                    try:
                        learningRate = int(input(
                            "First please enter the number of the learning rate: *(Press enter for default:1) :"))
                    except ValueError:
                        learningRate = 1
                        print("Learning rate chosen -> " + str(learningRate) + "\n")

                    print("You have chosen file 'training_data.txt', number of epochs: "+str(epochs)+" and the learning rate of: "+str(learningRate)+".\n")
                    opt2(opt1(inputSize, hiddenSize, outputSize), training_file, epochs, learningRate)
                    route_checker = 2
                else:
                    print("Please run the first option in order to continue!")

            elif choice == 3:  #OPTION 3
                if route_checker >= 2:
                    print('Classify test data')
                    opt3(opt2(opt1(inputSize, hiddenSize, outputSize), training_file, epochs,
                              learningRate))  # calls option 3
                    route_checker = 3
                else:
                    print("Please run the second option in order to continue!")

            elif choice == 4:  #OPTION 4

                if route_checker >= 3:
                    print('Display training result graphics.\n')
                    print("Loading...")
                    opt4()

            elif choice == 5:  # OPTION 5
                print('\n\nThank you for checking my CS340 project submission!\n\n')
                # Deleting files created throughout the project
                if os.path.exists("graph_data.txt"):
                    os.remove("graph_data.txt")
                if os.path.exists("predicted_outputs_vector.txt"):
                    os.remove("predicted_outputs_vector.txt")

                break
            else:  #ERROR HANDLING In case the input is an integer, but not a valid menu option
                print('Please enter one of the valid choices!\n')

#STARTING THE PROGRAM

progmenu()

