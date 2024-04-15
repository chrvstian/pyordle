<div align="center">
  <h1 align="center">Pyordle</h1>
  <img alt="PyShot Logo" src="https://github.com/chrvstian/pyordle/blob/main/.github/logo.png" width="50%" height="50%">
  <h3>A terminal-based wordle clone written in Python 3.</h3>

</div>

<br/>

<div align="center">
  <a href="https://github.com/chrvstian/pyordle/stargazers"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/chrvstian/pyordle"></a>
  <a href="https://github.com/chrvstian/pyordle/blob/main/.github/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-AGPLv3-purple"></a>
</div>

<br/>

Pyordle is a terminal-based wordle clone. Unlike the original worldle, you can play it offline!

## Features

- **Random word generation:** Generates completely random five-letter words. None of the answers are hard-coded.
- **No duplicate guesses:** Doesn't allow you to incorrectly guess a word more than once. 
- **CLI:** Pyordle has a very visually appealing CLI.

## Demo

https://github.com/chrvstian/pyshot/assets/141359845/55a53f8a-4e3f-4f89-9103-493e3965981a.mov

## Tech Stack

- [Python](https://www.python.org/) – Language
- [Rich](https://rich.readthedocs.io/en/stable/introduction.html) - User Interface

## Getting Started

### Prerequisites

Here's what you need to be able to use PyShot:

- Python 3+
- Rich

### 1. Clone the repository

```shell
git clone https://github.com/chrvstian/pyordle.git
cd pyordle
```

### 2. Install the rich module

```shell
pip3 install rich
```

### 3. Generate your secret key for session management

**Step 1:** Open your terminal & input the following code
```shell
python3
```

**Step 2:** Generate your secret key
```shell
import secrets; secrets.token_hex()
```

**Step 3:** Copy your token & paste it into app.py
- Copy the token that it creates and locate the 27th line in app.py
- Paste the key into the line that says:
```shell
app.secret_key = "AddYourSecretKeyHere" # Secret key used for session management
```

### 4. Run the program

```shell
python3 pyordle.py
```
## Contributing

Pyordle is an open-source project and we welcome contributions from the community.

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.
