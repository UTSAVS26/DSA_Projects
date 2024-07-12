# Cash Flow Minimizer

## Description
Optimize cash flow among a group of people using graphs, multisets, and heaps to minimize the total number of transactions needed to settle all debts efficiently.

## Features
- Calculation of minimal transactions required to settle debts
- Graph representation of debt relationships
- Multisets and heaps for efficient debt settlement algorithms

## Folder Structure
```
CashFlowMinimizer/
├── src/
│   ├── __init__.py
│   ├── cash_flow.py
│   ├── graph.py
│   ├── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_cash_flow.py
│   ├── test_graph.py
│   ├── test_utils.py
├── README.md
├── requirements.txt
├── main.py
```

## How to Run
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the cash flow minimizer:
    ```bash
    python main.py
    ```

## Requirements
- Python 3.x
- Unittest (for testing)

## Project Structure
- **src/**: Contains the main project files.
  - **cash_flow.py**: Implements the main cash flow minimization logic.
  - **graph.py**: Defines the graph data structure and related operations.
  - **utils.py**: Utility functions for calculations and data manipulation.
- **tests/**: Unit tests for the project.
- **README.md**: This file, describing the project.
- **requirements.txt**: Lists dependencies required to run the project.
- **main.py**: Entry point of the project.