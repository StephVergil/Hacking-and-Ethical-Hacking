# Password Strength Checker with Python

## Overview

This project involves creating and enhancing a Python script to evaluate password strength using the `zxcvbn` library. The improved script calculates password entropy, provides detailed feedback on password complexity, and allows saving results to a file for single or bulk password analysis. These improvements make it a robust tool for analyzing and improving password policies.

---

## Key Features

1. **Password Strength Evaluation**:
   - Test single passwords interactively or analyze multiple passwords from a file.
   - Evaluate passwords based on a score ranging from 0 (weak) to 4 (very strong).
   - Provide time estimates for password cracking (online and offline attacks).

2. **Entropy Calculation**:
   - Calculate password entropy to quantify randomness and resistance to brute-force attacks.

3. **Result Saving Options**:
   - Save results to a specified file for record-keeping or further analysis.
   - View results directly in the terminal for quick assessments.

4. **Bulk Password Testing**:
   - Analyze multiple passwords in one session with clear and structured outputs.

---

## Workflow Steps

### **1. Set Up the Development Environment**

1. **Create a Virtual Environment**:
   - Isolate dependencies to ensure a clean setup:
     ```bash
     python3 -m venv myenv
     source myenv/bin/activate
     ```

2. **Install the Required Library**:
   - Install the `zxcvbn` library for password strength evaluation:
     ```bash
     pip install zxcvbn
     ```

---

### **2. Script and Input Preparation**

1. **Create the Python Script**:
   - Write the password strength checker script:
     ```bash
     nano check_password_strength.py
     ```

2. **Prepare a Password List (Optional)**:
   - Create a file with one password per line for bulk testing:
     ```bash
     nano passwords.txt
     ```

---

### **3. Execute the Script**

1. **Single Password Testing**:
   - Run the script to analyze a single password interactively:
     ```bash
     python check_password_strength.py
     ```

2. **Bulk Password Testing**:
   - Test multiple passwords from a file and save results to an output file:
     ```bash
     python check_password_strength.py passwords.txt results.txt
     ```

3. **Sample Output**:
   - The script generates detailed results, including:
     ```
     Password: mySecurePa$$word!
     Score: 4 (Very Strong)
     Crack Time (Online): 10 years
     Crack Time (Offline): 50,000 years
     Entropy: 58.2 bits
     Feedback: Great password! No improvements needed.
     ```

---

### **4. Clean Up**

- Deactivate the virtual environment after completing the analysis:
  ```bash
  deactivate
  ```

---

## Improvements in the Script

- **Original Script Limitations**:
  - Basic password strength evaluation without entropy calculations.
  - Results displayed only in the terminal, with no option to save for further analysis.

- **Enhanced Script Features**:
  1. **Entropy Metrics**:
     - Adds entropy calculations to provide deeper insights into password complexity.
  2. **Result Saving**:
     - Allows saving results to a file, enabling long-term record-keeping and analysis.
  3. **Bulk Testing Capability**:
     - Efficiently processes multiple passwords with structured outputs for easier review.
  4. **Enhanced Feedback**:
     - Provides actionable suggestions for improving weak passwords.

---

## Learning Objectives

1. **Understand Password Security Metrics**:
   - Learn about password scores, entropy, and their significance in resisting attacks.

2. **Hands-On Python Development**:
   - Gain experience using Python libraries and improving script functionality.

3. **Managing Python Environments**:
   - Use virtual environments for project isolation and dependency management.

4. **Real-World Applications**:
   - Apply bulk password analysis to organizational audits and enhance security policies.

---

## Real-World Applications

1. **Organizational Security Audits**:
   - Test and strengthen enterprise password policies by analyzing bulk password lists.

2. **End-User Awareness**:
   - Educate users on creating stronger passwords through actionable feedback.

3. **Integration with Security Tools**:
   - Embed the script into larger security systems to automate password strength evaluations.

---

## Resources

1. **Project Documentation**:
   - [Password Strength Checker Documentation](https://github.com/StephVergil/Password-Strength-Checker/blob/main/Documentation.docx)

2. **Code Files**:
   - [Original Python Code](https://github.com/StephVergil/Hacking-and-Ethical-Hacking/blob/main/Original%20Python%20Code.py)
   - [Improved Python Code](https://github.com/StephVergil/Hacking-and-Ethical-Hacking/blob/main/Improved%20Python%20Code.py)

---
# Comprehensive Resources for Password Strength Checking and Security

## Advanced Libraries and Tools

1. **Passlib**  
   [Passlib Documentation](https://passlib.readthedocs.io/en/stable/)  
   - A robust Python library for secure password hashing, offering support for multiple algorithms and best practices for password storage.

2. **Argon2**  
   [Argon2 Password Hashing](https://argon2.online/)  
   - A state-of-the-art password hashing algorithm recognized for its memory-hard and computational resistance to brute-force attacks.

---

## International Guidelines and Standards

1. **NIST Password Guidelines**  
   [NIST Special Publication 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html)  
   - Comprehensive guidelines for secure password management and modern authentication practices.

2. **OWASP Authentication Cheat Sheet**  
   [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)  
   - A detailed resource for implementing secure authentication mechanisms and minimizing vulnerabilities.

---

## Disclaimer

This project is intended for educational purposes in controlled environments. Unauthorized use of password testing techniques on systems without explicit permission may violate ethical guidelines and legal regulations. Always ensure compliance with organizational policies and laws.

---

