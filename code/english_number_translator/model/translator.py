class Translator(object):
    @staticmethod
    def num_to_string(num):
        simple_nums_to_str = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve"
        }
        return simple_nums_to_str[num]
