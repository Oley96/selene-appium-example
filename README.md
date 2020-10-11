## To integrate PyCharm with PyTest
Preferences -> Tools -> Default test runner -> pytest

## Necessary installations
1. Xcode
2. iOS Emulator
3. Appium + carthage

## Don't forget to check diagnostic via appium doctor
1. Run in terminal: npm install appium-doctor -g
2. Check diagnostic for necessary dependencies by running in terminal:
appium-doctor --ios


## How to start?
1. Clone repo
2. Create .env file in root directory
3. Copy content form .env.example to .env file
4. Install requirements: pip install -r requirements.txt
5. Start Appium
6. Run via terminal on iOS platform: pytest ./tests (ios emulator starts automatically)
7. Run via terminal on Android platform: pytest --platform=android ./tests (android simulator needs to be started manually)
