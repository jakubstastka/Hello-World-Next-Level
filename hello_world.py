class HelloWorld:
    ALPHABET = []
    HELLO_WORLD_LETTERS = ['d', 'e', 'h', 'l', 'o', 'r', 'w']

    def __init__(self):
        alphabet_user_input = input("Please press every alphabetic character key on your keyboard:\n")
        if alphabet_user_input:
            self.ALPHABET.extend(list(set(alphabet_user_input)))
        else:
            print("You did not put in any characters. :(")
            exit()

    @staticmethod
    def get_letter_indexes(letter, input_list):
        try:
            return input_list.index(letter)
        except (AttributeError, ValueError):
            print("You did not put in enough letters. How dare you.")
            exit()

    @staticmethod
    def assign_letter(letter_dict, looking_for, tuple_index=1):
        for letter in letter_dict.items():
            if letter[tuple_index] == looking_for:
                return letter[tuple_index]

    @classmethod
    def get_letters(cls):
        letters_indexes = {}

        for letter in cls.HELLO_WORLD_LETTERS:
            letter_index = HelloWorld.get_letter_indexes(letter, HelloWorld.ALPHABET)
            letters_indexes.update({letter_index: letter})

        d = HelloWorld.assign_letter(letters_indexes, "d")
        e = HelloWorld.assign_letter(letters_indexes, "e")
        h = HelloWorld.assign_letter(letters_indexes, "h")
        l = HelloWorld.assign_letter(letters_indexes, "l")
        o = HelloWorld.assign_letter(letters_indexes, "o")
        r = HelloWorld.assign_letter(letters_indexes, "r")
        w = HelloWorld.assign_letter(letters_indexes, "w")

        return d, e, h, l, o, r, w

    def print_hello_world(self):
        d, e, h, l, o, r, w = HelloWorld.get_letters()
        hello = f"{h}{e}{l}{l}{o}"
        world = f"{w}{o}{r}{l}{d}"
        hello_world = f"{hello.capitalize()}, {world.capitalize()}"

        print(hello_world)


if __name__ == "__main__":
    hw = HelloWorld()
    hw.print_hello_world()
