## About

This project is a simple Python calculator built with Tkinter. It runs locally on your machine and provides basic arithmetic operations through a graphical user interface. Its purpose is to demonstrate how Python’s core logic can be connected to a desktop UI, making calculations accessible and easy to use.

<img width="325" height="453" alt="image" src="https://github.com/user-attachments/assets/9ecbe7c2-935d-468f-b924-21f02c026930" />

**Core Module**: Handles the main calculation logic (addition, subtraction, multiplication, division).  

**GUI Module**: Implements the Tkinter interface for user interaction.  

**Tests**: Includes unit tests for the core functions to ensure reliability.  

## What I Learned

This project helped me understand how to separate core logic from a graphical interface. I gained experience with Python’s Tkinter library, organizing code into modules, and writing unit tests with Pytest. It also taught me how to handle errors gracefully (like division by zero) and how to structure a small but complete Python application.


## How To Run

1. Clone the repository:  
```bash
git clone https://github.com/les1g/Calculator-App.git
cd Calculator-App
```

2. Create a virtual environment:  
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Activate virtual environment:  
```bash
.\venv\Scripts\Activate 
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

Run the GUI:  
```bash
python -m calculator.gui
```

Run tests:  
```bash
python -m pytest
```
