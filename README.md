# PassForge

Targeted password worldlist generator for security testing and CTFs

PassForge creates custom worldlists based on personal target data and configurable rules in config.txt

## Disclaimer
Do not use this to harm any real world applications
This program is for authorized testing only!

## Features:
- targeted pass generation
- configurable symbols and numbers
- case variations
- no duplicate pass output
- length filtering (8-20 chars)
- no external dependencies
- Argparsing now allowed

## Configuration (config.txt)
Example:
letters = a,b,c,d,e,ff,FF,Aa

numbers = 1, 2, 07, 123

symbols = !, @, #, $, %

## Usage
- py main.py -h or python main.py -h
Flags : --firstname <name> --nickname <nickname> --birthyear <birthyear> --country <country> --number <favnumber>

- Example Input:
- py main.py --firstname john --nickname jojo --birthyear 1984 --country australia --number 61
- Example Output
- Generated 96144 passwords.
- Passwords saved to wordlist.txt


After completion program will save generated content to worldlist.txt

## Plans
This program is still in beta and many more feautures will be added

## Author
Youssef Shamas