# cpr
Python module for validating and generating ID numbers as used in the Danish CPR-registry.\
By A. S. Nielsen, 2021. Released under the MIT License. The full licence is included in the LICENSE.txt-file.

## Description
Small personal pet project intented teach myself how the Danish CPR-numbers are created and can be used in a larger IT-system.
The project has the dual purpose of giving me insight into the CPR-system, while also being used to (re-)familiarise myself with a numbber of technical concepts such as:
- Python,
- git/Github,
- UNIX-like terminals.

As this is an educational project the code presented here should not be considered best practise. As an example I have implemented number of for-loops which could be fairly easily be replaced by vector-procedures to optimise performance.
I am currently also debating with myself how to store the data. Currently CPR-numbers are kept in strings, but I am considering using a char-vector, or a custom object.

#### Litterature:
[Opbygningen af CPR nummeret](https://cpr.dk/cpr-systemet/opbygning-af-cpr-nummeret/)

#### Inspirational examples:
[Jan Schrøder Hansens CPR generator](https://janosh.neocities.org/javascript-personal-id-check-and-generator/index.html)

#### Missing functionalities:
- Support for CPR-numbers without Modulus 11 control,
- Input validation.

#### Possible expansions:
- Release project as a package,
- Statistical likelihood of a CPR number being in use,
- Check on wether a CPR number not complying with Modulus 11 is in used (I recall seeing information on which dates the limit was passed),
- Object oriented version.
