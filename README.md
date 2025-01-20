# ANN Model: Python-Based Artificial Neural Network

## Overview
This project demonstrates proficiency in Python programming and foundational machine learning concepts through two distinct parts:

1. **Part A:** Data manipulation and visualization using Python.
2. **Part B:** Creation, training, and validation of an artificial neural network (ANN) built from scratch.

The project aims to highlight Python coding skills, machine learning understanding, and experimentation with ANN architectures and parameters.

## Part A: Python Data Manipulation and Visualization
### Features
1. **Menu Options:**
   - **Option 1:** Read and display data from `partA_input_data.txt`.
   - **Option 2:** Filter and sort data based on user-defined criteria.
   - **Option 3:** Calculate and add a new column, save the modified data to `partA_output_data.txt`, and display the updated table.
   - **Option 4:** Sort data from the 7-column file by user-specified fields and order.
   - **Option 5:** Display a GUI column graph showing average lap times per driver.
   - **Option 6:** Exit the program.

2. **Data Handling:**
   - Worked with CSV files using Pandas.
   - Scraped data directly from a website to create a CSV file.

3. **Visualization:**
   - Created graphs using Matplotlib.

4. **Error Handling:**
   - Implemented input validation for robust user interaction.

### Libraries Used
- **Pandas:** For data manipulation and scraping.
- **Matplotlib:** For graph plotting.
- **Tabulate:** For displaying data tables.

### Challenges and Solutions
- **Switch-Case Alternative:** Used `if` statements instead of `switch-case` due to compatibility issues with older Python versions.
- **Enhanced Functionality:** Added error handling and extended the project by automating data scraping.

## Part B: Artificial Neural Network Development
### Features
1. **Menu Options:**
   - **Option 1:** Specify ANN topology (e.g., `10-5-2` for input, hidden, and output layers).
   - **Option 2:** Train the ANN using `training_data.txt` with user-defined epochs and learning rates.
   - **Option 3:** Classify test data from `input_data.txt` and save results to `training_output.txt`.
   - **Option 4:** Display training progress as a graph.
   - **Option 5:** Exit the program.

2. **Extra Features:**
   - Automatically generated input and training datasets.
   - Neural network implemented from scratch using NumPy.

3. **Graphing and Analysis:**
   - Visualized cost function reduction and classification accuracy during training.

### Libraries Used
- **NumPy:** For ANN implementation.
- **Matplotlib:** For training progress visualization.

### Experimentation and Results
- Tested the ANN with varying epochs, learning rates, and hidden layers to observe changes in learning speed and accuracy.
- Identified the impact of network topology on performance.

### Optimization Ideas
- Use gradient descent optimization algorithms.
- Implement regularization techniques to minimize overfitting.
- Randomize training data for more robust learning.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/OJOCoding/ANNModel.git
   cd ANNModel
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python main.py
   ```

## Project Structure
```plaintext
ANNModel/
├── partA/              # Part A implementation
│   ├── data/           # Input and output data files
│   ├── scripts/        # Python scripts for menu options
├── partB/              # Part B implementation
│   ├── ann.py          # ANN class implementation
│   ├── training/       # Training and input data files
├── graphs/             # Generated graphs
├── README.md           # Project documentation
├── requirements.txt    # List of dependencies
└── LICENSE             # License file
```

## Key Files
- `partA_input_data.txt`: Initial dataset for Part A.
- `training_data.txt`: Training dataset for Part B.
- `training_progress.txt`: Logs of training progress for Part B.

## License
This project is licensed under the **MIT License**. For more details, see the [LICENSE](LICENSE) file.

## Contact
For questions or additional details:
- **Author:** Oni Luca
- **Email:** [oniluca@ymail.com](mailto:oniluca@ymail.com)

---

Thank you for reviewing the ANN Model project. This comprehensive exploration into Python programming and ANN development demonstrates a deep understanding of foundational AI and machine learning concepts.
