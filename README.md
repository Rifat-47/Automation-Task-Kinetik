
# Project Title

Automation task for Kinetik.

Automated Test Implementation:
1. Launch browser(Chrome/Firefox)
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Add products to cart
5. Click 'Cart' button
6. Verify that cart page is displayed
7. Click Proceed To Checkout
8. Click 'Register / Login' button
9. Fill all details in Sign up and create account
10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
11. Verify ' Logged in as username' at top
12. Click 'Cart' button
13. Click 'Proceed To Checkout' button
14. Verify Address Details and Review Your Order
15. Enter description in comment text area and click 'Place Order'
16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
17. Click 'Pay and Confirm Order' button
18. Verify the success message 'Your order has been placed successfully!'



## Run Locally

Clone the project

```bash
  https://github.com/Rifat-47/Automation-Task-Kinetik.git
```

Go to the project directory
```bash
  cd Automation-Task-Kinetik
```

Install virtual environment
```bash
   pip install virtualenv
```

Create a virtual environment with name 'venvname'
```bash
  python -m venv venvname
```

Activate virtual environment
```bash
  venvname\Scripts\activate
```

Install dependencies
```bash
  pip install -r requirements.txt
```

Run the python script
```bash
  python kinetik.py
```
Execution results will be printed in the terminal according to the screenshot given below.

Now, Deactivate virtual environment (on windows command prompt/powetshell)
```bash
   deactivate
```
## Screenshots

![ScreenShot-1](https://github.com/Rifat-47/Automation-Task-Kinetik/blob/main/Screenshot_1.png)


## Documentation

To remove virtual environment completely: 
```bash
  Remove-Item -Recurse -Force .\venvname
```

Project can be run without using virtual environment.
```bash
  https://github.com/Rifat-47/Automation-Task-Kinetik.git
  cd Automation-Task-Kinetik
  pip install -r requirements.txt
  python kinetik.py
```

## Authors

- [@Rifat-47](https://github.com/Rifat-47)


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/Rifat-47)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rifat-ibn-taher/)

