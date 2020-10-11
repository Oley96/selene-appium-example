## To integrate PyCharm with PyTest
Preferences -> Tools -> Default test runner -> pytest

## Necessary installations
1. Xcode, Android Studio
2. iOS and Android emulators
3. Appium + carthage

## Don't forget to check diagnostic via appium doctor
1. Install appium doctor: npm install appium-doctor -g
2. Check diagnostic for necessary dependencies by running in terminal:
- appium-doctor --ios
- appium-doctor --android


## How to start?
1. Clone repo
2. Create .env file in root directory
3. Install requirements: pip install -r requirements.txt
4. Start Appium
5. Run test via terminal on iOS platform: pytest ./tests (ios emulator starts automatically)
6. Run test via terminal on Android platform: pytest --platform=android ./tests (android simulator needs to be started manually)
