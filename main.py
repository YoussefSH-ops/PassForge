def get_input():
    first_name = str(input("Enter the target's name: ")).strip()
    nickname = str(input("Enter the target's nickname: ")).strip()
    birthyear = str(input("Enter the target's birthyear: ")).strip()
    country = str(input("Enter the target's country: ")).strip()
    favnumber = str(input("Enter the target's favnumber: ")).strip()
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
                            print("You can only have numbers in numbers config")
                            numbers = []
                            break
                        else:
                            numbers.append(number)
            if config == "symbols":
                tokens = value.split(",")
                for token in tokens:
                    sym = token.strip()
                    if not sym:
                        print("No valid symbols present in the config's value")
                        continue
                    if len(sym) != 1:
                        print("Symbol cannot exceeded a max length of 1")
                        continue
                    if sym.isalnum() or sym.isspace():
                        continue
                    symbols.add(sym)

        return numbers , list(symbols)


def processing(variants, numbers, symbols):
    passwords = set()
    for w1 in variants:
        for w2 in variants:
            for number in numbers:
                for sym in symbols:
                    p1 = w1 + number + sym + w2
                    p2 = number + w1 + sym + w2
                    p3 = sym + w1 + number + w2
                    p4 = w2 + sym + w1 + number
                    p5 = w1 + w2 + number + sym
                    p6 = w1 + sym +  number
                    p7 = w1 + number + sym
                    for p in (p1,p2,p3,p4,p5,p6,p7):
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
    numbers, symbols = read_config("config.txt")
    inputs = get_input()
    variations = create_variations(inputs)
    passwords = processing(variations, numbers, symbols)
    save_to_file(passwords)

if __name__ == "__main__":
    main()
