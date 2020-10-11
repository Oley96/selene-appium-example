## To integrate PyCharm with PyTest
Preferences -> Tools -> Default test runner -> pytest

## Necessary installations
1. Xcode
2. iOS Emulator
3. Appium + carthage

## Don't forget to check diagnostic via appium doctor
Run in terminal: npm install appium-doctor -g
Check diagnostic for necessary dependencies by running in terminal:
appium-doctor --ios


## How to start?
1. Create .env file in root directory
2. Copy content form .env.example to .env file
3. Install requirements
4. Start Appium
5. Run in terminal: pytest ./tests
