# Python Programming Practice

## Environment Setup
- Create a virtual environment:
  ```
  conda create -p environment_name python=3.12
  conda create -n environment_name python=3.12
  ```
- List all environments:
  ```
  conda env list
  ```
- Activate environment:
  ```
  conda activate environment_name
  ```

## Install Requirements
- Install required modules for web scraping:
  ```
  pip install -r requirements.txt

  ```

## Project Structure & Topics

### 1. Basics
- Python datatypes: `str`, `int`, `float`, `bool`, `list`, `tuple`, `dict`, `set`
- Block comments and dunder methods
- Jupyter Notebook vs Python Script

### 2. Collections
- List, Tuple, Set, Dictionary examples

### 3. Loops & Statements
- If statements and logical conditions

### 4. Functions
- Function definitions, keyword arguments, variable arguments

### 5. Exception Handling (`4-exceptions`)
- Try-except blocks
- Handling specific exceptions: `ValueError`, `ZeroDivisionError`
- Multiple except blocks ([`try_multiple_except.py`](4-exceptions/try_multiple_except.py))
- Finally blocks ([`example3.py`](4-exceptions/example3.py), [`try_except_finally.py`](4-exceptions/try_except_finally.py))
- Raising custom exceptions ([`raise_error.py`](4-exceptions/raise_error.py))
- System exit examples ([`system_exit_example1.py`](4-exceptions/system_exit_example1.py), [`system_exit_example2.py`](4-exceptions/system_exit_example2.py))
- Exception handling in scripts ([`script.py`](4-exceptions/script.py))

### 6. Web Scraping (`4-webscrapping`)
- Using `requests` and `beautifulsoup4`
- Scraping book data from Amazon ([`scrape_books.py`](4-webscrapping/scrape_books.py))
- Output saved to [`books.csv`](books.csv)

## How to Run
  ```
  python 4-webscrapping/scrape_books.py
  ```
  ```
  python 4-exceptions/script.py
  python 4-exceptions/raise_error.py
  python 4-exceptions/try_multiple_except.py
  python 4-exceptions/try_except_finally.py
  python 4-exceptions/system_exit_example1.py
  python 4-exceptions/system_exit_example2.py
  ```

# Notes
- Each topic is organized in its respective folder for easy navigation.
- Practice notebooks and scripts are included for hands-on learning.