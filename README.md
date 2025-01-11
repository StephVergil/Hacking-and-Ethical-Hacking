# Password Strength Checker with Python

## Overview
This project involves creating and improving a Python script to check password strength using the `zxcvbn` library. The improved script calculates password entropy, provides detailed feedback on password complexity, and allows saving results to a file for single or bulk password analysis.

---

## Key Features
1. **Password Strength Evaluation**:
   - Test single passwords or multiple passwords from a file.
   - Evaluate passwords based on score (0–4) and provide cracking time estimates.
2. **Entropy Calculation**:
   - The improved script calculates password entropy for added complexity metrics.
3. **Result Saving Options**:
   - Save results to a specified file or view directly in the terminal.
   - Flexibility for single password analysis or bulk testing.

---

## Lab Steps

1. **Setup Virtual Environment**:
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv myenv
     source myenv/bin/activate
     ```
   - Install the required library:
     ```bash
     pip install zxcvbn
     ```

2. **Prepare Files**:
   - Create a Python script:
     ```bash
     nano check_password_strength.py
     ```
   - Create a password list:
     ```bash
     nano passwords.txt
     ```

3. **Run the Script**:
   - Test a single password:
     ```bash
     python check_password_strength.py
     ```
   - Test multiple passwords:
     ```bash
     python check_password_strength.py passwords.txt results.txt
     ```

4. **Deactivate Virtual Environment**:
   - Once done, deactivate the environment:
     ```bash
     deactivate
     ```

---

## Improvements in the Script
- **Original Script**:
  - Tests password strength but lacks entropy calculations.
  - Displays results only in the terminal, with no save option.
- **Improved Script**:
  - Adds entropy calculation for complexity insights.
  - Provides options to save results or skip saving during analysis.
  - Clearer, formatted output for better readability during bulk testing.

---

## Learning Objectives
- Understand password strength metrics like scores and entropy.
- Gain hands-on experience with Python's `zxcvbn` library for password analysis.
- Learn to manage Python virtual environments for project isolation.

---

## Resources
- [Check Password Strength with Python - The Python Code](https://thepythoncode.com/article/test-password-strength-with-python)

---

## Documentation
For detailed project steps and scripts, refer to:
- [Project Details](https://github.com/StephVergil/Cybersecurity-Projects/blob/main/Project.docx)
- [Original Python Code](https://github.com/StephVergil/Cybersecurity-Projects/blob/main/Original%20Python%20Code.py)
- [Improved Python Code](https://github.com/StephVergil/Cybersecurity-Projects/blob/main/Improved%20Python%20Code.py)
