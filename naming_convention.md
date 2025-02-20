# Python Naming Conventions – A Detailed Guide

Naming conventions in Python help maintain readability, consistency, and best practices when writing code. Python follows PEP 8 (Python Enhancement Proposal 8), which is the official style guide for Python code. Below is a detailed breakdown of Python naming conventions, including how different types of identifiers should be named.

## 1. General Rules for Naming in Python

*   **Use meaningful and descriptive names**
    *   ✅ `user_count` instead of `uc`
    *   ✅ `calculate_total_price` instead of `ctp`
*   **Use lowercase with underscores for readability (snake_case)**
    *   ✅ `user_name` (preferred)
    *   ❌ `username` (less readable)
    *   ❌ `UserName` (reserved for classes)
*   **Avoid using single-character names** (unless in loops or mathematical contexts)
    *   ✅ `for i in range(10):` (acceptable in loops)
    *   ❌ `x = 10` (not descriptive, avoid outside mathematical functions)
*   **Do not use Python keywords as variable names**
    *   ❌ `class = "Hello"` → `SyntaxError`
    *   ✅ `class_name = "Hello"`
*   **Use underscores to improve readability**
    *   ✅ `max_value` instead of `maxvalue`

## 2. Variable Naming Conventions

### a) General Variables
*   Use `snake_case` for normal variables
    *   ✅ `first_name = "Alice"`
    *   ✅ `total_count = 100`

### b) Constants (Immutable Values)
*   Use `UPPER_CASE` with underscores
    *   ✅ `PI = 3.14159`
    *   ✅ `MAX_USERS = 1000`
    *   ✅ `DATABASE_URL = "postgres://user:pass@host/db"`
    *   Python does not enforce constants, but using uppercase helps signal that the variable should not be modified.

## 3. Function Naming Conventions

*   Use `snake_case` for function names
    *   ✅ `def get_user_data():`
    *   ✅ `def calculate_total():`
    *   ❌ `def GetUserData():` (reserved for classes)
    *   ❌ `def getUserData():` (not Pythonic, Java style)

### Private Functions (Internal Use Only)
*   Prefix with a single underscore `_`
    *   ✅ `_compute_hash()`

### Strongly Private Functions
*   Use double underscores `__`
    *   ✅ `__encrypt_password()` (name mangling happens, prevents accidental access)

## 4. Class Naming Conventions

*   Use `PascalCase` (also called `CapWords` or `CamelCase`)
    *   ✅ `class UserProfile:`
    *   ✅ `class DatabaseConnection:`
    *   ❌ `class user_profile:` (not Pythonic)

### a) Class Attributes
*   Use `snake_case`
    *   ✅ `self.user_name = "Alice"`
    *   ❌ `self.UserName = "Alice"`
*   Private attributes should start with an underscore `_`
    *   ✅ `_password` (indicates internal use)
*   Strongly private attributes start with double underscores `__`
    *   ✅ `__api_key` (name mangling happens)

### b) Class Methods
*   Use `snake_case` for method names
    *   ✅ `def get_user_info(self):`

### Private Methods
*   ✅ `_calculate_discount()`

### Strongly Private Methods
*   ✅ `__generate_token()`

## 5. Module and Package Naming Conventions

### Modules (Python files)
*   Use `lowercase_with_underscores.py`
    *   ✅ `user_management.py`
    *   ✅ `data_processing.py`

### Packages (Folders with `__init__.py`)
*   Use lowercase without underscores
    *   ✅ `utilities/`
    *   ✅ `authentication/`
    *   ❌ `AuthTools/` (Avoid capital letters)

---