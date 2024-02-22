# Fast Speech Recognizer with Selenium and JS WebKit Speech Recognition

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

This project implements a fast speech recognizer using Selenium and JavaScript WebKit Speech Recognition. It provides a seamless voice interface, allowing users to easily integrate voice recognition into their applications for various use cases.

## Features

- **Fast Recognition:** Utilizes Selenium and JavaScript WebKit Speech Recognition for rapid and reliable speech recognition.
- **Easy Integration:** Simple integration with existing projects or applications, providing a user-friendly voice interface.
- **Customizable:** Easily adaptable for different applications and scenarios.
- **Browser Compaitability:** Need to Install Chrome or Edge Browser for this to work.

## How it Works

The project consists of two main components:

1. **SpeechRecognizer.py:** The Python script that uses Selenium to interact with a web page containing the voice recognition functionality.

2. **voice.html:** The HTML file containing JavaScript code for live speech recognition using WebKit Speech Recognition.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/DebadritoCG/SpeechRecognizer_Selenium.git
   cd SpeechRecognizer_Selenium
   ```
2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Use The Speech Recognizer
   ```py
   from SpeechRecognizer import Listen
   print('Listening...')
   result = Listen()
   print(f'You Said: {result}')
   ```
