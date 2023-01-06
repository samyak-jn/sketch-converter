<p align="center">
  <img style="width:40%;" src="logo/sketch.png" />
</p>

<h1 align="center">Image to Sketch Converter</h1>

<h3 align="center">Fond of **sketches**, but bad at **art**? 🥴</h3>
<br>

[![main-ci](https://github.com/samyak-jn/detect/actions/workflows/main.yml/badge.svg)](https://github.com/samyak-jn/detect/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/samyak-jn/detect/master.svg)](https://results.pre-commit.ci/latest/github/samyak-jn/detect/master)

<a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/samyak-jn/detect/blob/master/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python">


Here's a little something for people like you and me.
This is a simple python script that converts your **captured images** into a **sketch** in real-time with just one line of command, fascinating? 😎

This script is written with the help of the OpenCV library in python.All the sketches will be saved in the parent directory itself.

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/samyak-jn/detect.git
poetry shell
poetry install
sketch_converter --help
```

## Camera Usage

```bash
# video_src = 1 , grayscale mode = 1
sketch_converter video-capture 1 1
```

### Contributing ✔️

- Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/fraction/readme-boilerplate/compare/).

- All the issues/features are welcome. Open a PR and let's have a discussion.

### License
sketch-converter is licensed under [MIT](https://github.com/samyak-jn/detect/blob/master/LICENSE), hence it is open source for all.

---
Copyright © 2023 Onuralp SEZER, Samyak Jain
