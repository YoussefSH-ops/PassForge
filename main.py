import argparse

parser = argparse.ArgumentParser(description="PassForge V1.1")
parser.add_argument("--firstname", help="Input firstname of target", required=True)
parser.add_argument("--nickname", help="Input nickname of target", required=True)
parser.add_argument("--birthyear", help="Input birthyear of target", required=True)
parser.add_argument("--country", help="Input country of target", required=True)
parser.add_argument("--number", help="Input favorite number of target", required=True)

args = parser.parse_args()

def get_input():
    first_name = str(args.firstname).strip()
    nickname = str(args.nickname).strip()
    birthyear = str(args.birthyear).strip()
    country = str(args.birthyear).strip()
    favnumber = str(args.number).strip()
    return [first_name, nickname, birthyear, country, favnumber]

def create_variations(inputs):
    variants = []
    leetspeak = {
    "a": "@",
    "e": "3",
    "o": "0",
    "s": "$",
    "i": "1",
    "t": "7"
}
    for w in inputs:
        new_word = ""
        if w:
            variants.append(w.lower())
            variants.append(w.upper())
            variants.append(w.capitalize())
            for char in w:
                if char in leetspeak:
                    new_word += leetspeak[char]
                else:
                    new_word += char
            variants.append(new_word)

    return list(set(variants))

def read_config(filename):
    with open(filename, "r") as f:
        numbers = []
        symbols = set()
        letters = set()
        for line in f:
            if line.startswith("#"):
                continue
            if not line.strip():
                continue
            if "=" not in line:
                print(f"Config Error , No '=' between config")
                continue
            config , value = line.split("=", 1)
            config = config.strip()
            if config == "numbers":
                numbers_uncleaned = value.split(",")
                for number in numbers_uncleaned:
                    number = number.strip()
                    if number != "":
                        try:
                            int(number)
                        except ValueError:
                            print("[-] You can only have numbers in numbers config")
                            numbers = []
                            break
                        else:
                            numbers.append(number)
            if config == "symbols":
                tokens = value.split(",")
                for token in tokens:
                    sym = token.strip()
                    if not sym:
                        print("[-] No valid symbols present in the config's value")
                        continue
                    if len(sym) != 1:
                        print("[-] Symbol cannot exceeded a max length of 1")
                        continue
                    if sym.isalnum() or sym.isspace():
                        continue
                    symbols.add(sym)
            if config == "letters":
                lettertok = value.split(",")
                for letter in lettertok:
                    char = letter.strip()
                    if not char:
                        print("[-] No valid letters in the configs value")
                        continue
                    if len(char) > 2:
                        print("[-] Letter cannot exceeded a max length of 2")
                        continue
                    if char.isnumeric() or char.isspace():
                        print("[-] Letter cannot be a number or space")
                        continue
                    letters.add(char)
        return numbers , list(symbols), letters


def processing(variants, numbers, symbols, letters):
    passwords = set()
    for w1 in variants:
        for w2 in variants:
            for number in numbers:
                for sym in symbols:
                    for letter in letters:
                        p1 = w1 + number + sym + w2 
                        p1a = w1 + number + sym + w2 + letter
                        p2 = number + w1 + sym + w2
                        p2a = number + w1 + sym + w2 + letter
                        p3 = sym + w1 + number + w2
                        p3a = sym + w1 + number + w2 + letter
                        p4 = w2 + sym + w1 + number
                        p4a = w2 + sym + w1 + number + letter
                        p5 = w1 + w2 + number + sym
                        p5a = w1 + w2 + number + sym + letter
                        p6 = w1 + sym +  number
                        p6a = w1 + sym +  number + letter
                        p7 = w1 + number + sym
                        p7a = w1 + number + sym + letter
                        for p in (p1,p2,p3,p4,p5,p6,p7,p1a,p2a,p3a,p4a,p5a,p6a,p7a):
                            if 8 <= len(p) <= 20:
                                passwords.add(p)
    return passwords

def save_to_file(passwords):
    with open("wordlist.txt", "w") as f:
        for p in passwords:
            f.write(f"{p}\n")
        print(f"Generated {len(passwords)} passwords.")
        print(f"Passwords saved to wordlist.txt")

def main():
    numbers, symbols, letters = read_config("config.txt")
    inputs = get_input()
    variations = create_variations(inputs)
    passwords = processing(variations, numbers, symbols, letters)
    save_to_file(passwords)

if __name__ == "__main__":
    main()
