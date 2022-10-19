class Solution:
    def countOfAtoms(self, formula: str) -> str:
        atom = ''
        cnt = 0
        i = 0
        parsed = []
        multiplier = 1
        atom_dict = collections.defaultdict(int)
        for token in formula[::-1]:
            print(multiplier)
            if token.isdigit():
                cnt += int(token) * (10 ** i)
                i += 1
            elif token == ')':
                parsed.append(cnt or 1)
                multiplier *= cnt or 1
                i = cnt = 0
            elif token == '(':
                multiplier //= parsed.pop()
                i = cnt = 0
            elif token.isupper():
                atom += token
                atom_dict[atom[::-1]] += (cnt or 1) * multiplier
                atom = ''
                i = cnt = 0
            elif token.islower():
                atom += token

        return ''.join(atom + str(cnt > 1 and cnt or '') for atom, cnt in sorted(atom_dict.items()))