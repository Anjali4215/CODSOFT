# 🔑 Advanced Password Generator

## 📌 Project Overview
This project is a **customizable password generator** developed in Python.  
It enables users to generate strong and secure passwords by selecting from multiple character sets and defining the password length. The program ensures at least one character from each selected category, enhancing the overall security of the generated password.

---

## 🎯 Features
- 🔠 **Uppercase letters** support  
- 🔡 **Lowercase letters** support  
- 🔢 **Numeric digits** support  
- 🔒 **Special symbols** support  
- ✔️ Ensures at least one character from each chosen category  
- 🛡️ Prevents weak or empty password generation  
- 🔄 Option to generate multiple passwords in a single run  
- 🧩 Simple, interactive command-line interface  

---

## 🛠️ Tech Stack
- **Programming Language:** Python 3  
- **Modules Used:**  
  - `random` – for secure random generation  
  - `string` – for predefined character sets  

---

## ▶️ How to Run the Program
1. **Clone this repository** or download the project folder.  
   ```bash
   git clone https://github.com/Anjali4215/CODSOFT/blob/main/Task-3-PasswordGenerator/password_generator.py
   cd CodSoft/Task-3-PasswordGenerator
Run the script using Python:

bash
Copy code
python password_generator.py
Follow the instructions displayed on the screen:

Choose character sets (e.g., 1,2,3,4)

Enter the desired password length

View your secure password

📊 Example Execution
markdown
Copy code
Password Generator Options:
1. Uppercase letters
2. Lowercase letters
3. Digits
4. Special symbols
You can select multiple options by separating numbers with commas (e.g., 1,3,4)

Enter your choice(s): 1,2,3,4
Enter password length: 12

Generated Password: A@k9LmP#2zQ7
📂 Project Structure
bash
Copy code
Task-3-PasswordGenerator/
│── password_generator.py   # Main program file
│── README.md               # Project documentation
✅ Learning Outcomes
Hands-on experience with Python’s string and random modules

Implementation of user input validation and error handling

Practical understanding of secure password generation techniques

📌 Future Enhancements
Add option to save generated passwords to a file

Add GUI interface using Tkinter

Add option for copy-to-clipboard functionality
