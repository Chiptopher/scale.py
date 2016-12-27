# scale.py
scale.py (pronounced "scale pie") is a Python-base command-line utility that calculates different scalling options of images.

## Usage
### Installation
scale.py can be installed from [PyPi using pip] (https://pypi.python.org/pypi/scalepy)
```
pip install scalepy
```
### Modifier
scale.py offers three different modifiers:
```
-x  -->  calculates the scaled y dimension using the given scaled x dimension
-y  -->  calculates the scaled x dimension using the given scaled y dimension
-s  -->  calculates the scaled dimensions using the given scale
```
### Arguments
scale.py commands follow the following format, where {scale} is either the scaled dimension or the scale
```

$ scalepy -param {original x} {original y} {scale}
 > {origanl x}x{orignal y} -> {scaled x}x{scaled y}
...
```
For example:
```
$ scalepy -x 100 150 300
 > 100x150 -> 300x450
```
### Invalid Input
scale.py offers the following error messages will be displayed with the corresponding error:
```
Invalid Argument Count       --> Either too many or too few arguments
Invalid Modifier: {modifier} --> An invalid modifier was entered
Invalid Argument: {argument} --> Something other than a number was entered
```
