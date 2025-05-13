from textdistance import levenshtein

class Arbiter:
    def __init__(self):
        self.cps = 0
        self.wpm = 0
        self.acc = 0

    def calculate_score(self, words: str, reference: str, time: int, method: str) -> dict:
        if time == 0:
            time = 0.10

        if method == "levenshtein":
            errors = levenshtein.distance(words, reference)
        elif method == "classic":
            len_diff = abs(len(words) - len(reference))
            errors = 0
            for i in range(0, len(reference)):
                if words[i] != reference[i]:
                    errors += 1

            errors += len_diff
        else:
            raise ValueError(f"Invalid method argument. Expected 'levenshtein' or 'classic', got '{method}' instead.")

        chars = len(words)

        self.acc = 1 - (errors / len(reference))
        net_chars = chars * self.acc

        self.cps = net_chars / time
        self.wpm = net_chars / (5 * (time / 60))

        return {"cps": self.cps, "wpm": self.wpm, "acc": self.acc * 100}







