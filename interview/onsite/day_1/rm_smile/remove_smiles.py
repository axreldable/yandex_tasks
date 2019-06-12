# Input is a string;
# Output is a string without smiles;
# Smile is sequence like ':-)...)' or ':-(...(';
from unittest import TestCase


def rm_smiles(in_str):
    rez = []
    cond = 'A'
    for c in in_str:
        if cond == 'A':
            if c == ':':
                cond = 'B'
            else:
                rez.append(c)
                cond = 'A'
        elif cond == 'B':
            if c == '-':
                cond = 'C'
            else:
                rez.append(':')
                rez.append(c)
                cond = 'A'
        elif cond == 'C':
            if c == '(':
                cond = 'D'
            elif c == ')':
                cond = 'E'
            else:
                rez.append(':')
                rez.append('-')
                rez.append(c)
                cond = 'A'
        elif cond == 'D':
            if c == '(':
                cond = 'D'
            else:
                if c == ':':
                    cond = 'B'
                else:
                    rez.append(c)
                    cond = 'A'
        elif cond == 'E':
            if c == ')':
                cond = 'E'
            else:
                if c == ':':
                    cond = 'B'
                else:
                    rez.append(c)
                    cond = 'A'

    if cond == 'B':
        rez.append(':')
    elif cond == 'C':
        rez.append(':')
        rez.append('-')

    return ''.join(rez)


class TestRemoveSmile(TestCase):
    def test_1(self):
        in_str = '???:-)???'
        result = rm_smiles(in_str)
        expected = '??????'
        self.assertEqual(expected, result)

    def test_2(self):
        in_str = '???:-(???'
        result = rm_smiles(in_str)
        expected = '??????'
        self.assertEqual(expected, result)

    def test_3(self):
        in_str = '???:-))???'
        result = rm_smiles(in_str)
        expected = '??????'
        self.assertEqual(expected, result)

    def test_4(self):
        in_str = ''
        result = rm_smiles(in_str)
        expected = ''
        self.assertEqual(expected, result)

    def test_5(self):
        in_str = '????????????'
        result = rm_smiles(in_str)
        expected = '????????????'
        self.assertEqual(expected, result)

    def test_6(self):
        in_str = ':-'
        result = rm_smiles(in_str)
        expected = ':-'
        self.assertEqual(expected, result)

    def test_7(self):
        in_str = ':-?'
        result = rm_smiles(in_str)
        expected = ':-?'
        self.assertEqual(expected, result)

    def test_8(self):
        in_str = ':-?)))'
        result = rm_smiles(in_str)
        expected = ':-?)))'
        self.assertEqual(expected, result)

    def test_9(self):
        in_str = ':-)?????????'
        result = rm_smiles(in_str)
        expected = '?????????'
        self.assertEqual(expected, result)

    def test_10(self):
        in_str = ':-))))?????????'
        result = rm_smiles(in_str)
        expected = '?????????'
        self.assertEqual(expected, result)

    def test_11(self):
        in_str = '?????????:-((('
        result = rm_smiles(in_str)
        expected = '?????????'
        self.assertEqual(expected, result)

    def test_12(self):
        in_str = '?:-)()'
        result = rm_smiles(in_str)
        expected = '?()'
        self.assertEqual(expected, result)

    def test_13(self):
        in_str = '?:-:)'
        result = rm_smiles(in_str)
        expected = '?:-:)'
        self.assertEqual(expected, result)

    def test_14(self):
        in_str = ':'
        result = rm_smiles(in_str)
        expected = ':'
        self.assertEqual(expected, result)

    def test_15(self):
        in_str = ':-))):'
        result = rm_smiles(in_str)
        expected = ':'
        self.assertEqual(expected, result)

    def test_16(self):
        in_str = ':-))):-'
        result = rm_smiles(in_str)
        expected = ':-'
        self.assertEqual(expected, result)

    def test_17(self):
        in_str = ':-))):-(('
        result = rm_smiles(in_str)
        expected = ''
        self.assertEqual(expected, result)
