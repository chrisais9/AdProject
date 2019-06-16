import unittest
from PyHangulUtils.hglpkg import hangulutils as hu


# 인스턴스 메서드에 대한 테스트 클래스입니다.
# 문자에 대해서는 인스턴스/클래스 메서드를 제공합니다.
class KorCharTest(unittest.TestCase):
    # --------------------
    # 0. 테스트 대상 문자
    # --------------------
    cc = ["한", "ㅎ", "ㅏ", "ㄺ", "A"]

    # --------------------
    # 1. 인스턴스 메서드 테스트
    # --------------------

    # 테스트 할 문자 집합의 인스턴스입니다. KorChar 인스턴스를 생성하여 사용합니다.
    tc = [hu.KorChar(c) for c in cc]

    # 문자열이 주어지지 않거나, 길이가 1 이상의 문자가 주어진 경우
    # 인스턴스 생성시 예외가 발생합니다.
    def test_Instanciation(self):
        with self.assertRaises(TypeError):
            err_instance = ''
            hu.KorChar(err_instance)
            err_instance = '가나'
            hu.KorChar(err_instance)

    # getchar():
    # 인스턴스로부터 원래의 문자를 얻습니다.
    def test_getchar(self):
        rst = [c.getchar() for c in KorCharTest.tc]
        ans = ["한", "ㅎ", "ㅏ", "ㄺ", "A"]
        self.assertEqual(ans, rst)

    # isonset():
    # 초성으로 사용될 수 있는지 여부를 판단합니다.
    def test_isonset(self):
        rst = [c.isonset() for c in KorCharTest.tc]
        ans = [False, True, False, False, False]
        self.assertEqual(ans, rst)

    # isnucleus():
    # 중성으로 사용될 수 있는지 여부를 판단합니다.
    def test_isnucleus(self):
        rst = [c.isnucleus() for c in KorCharTest.tc]
        ans = [False, False, True, False, False]
        self.assertEqual(ans, rst)

    # iscoda():
    # 종성으로 사용될 수 있는지 여부를 판단합니다.
    def test_iscoda(self):
        rst = [c.iscoda() for c in KorCharTest.tc]
        ans = [False, True, False, True, False]
        self.assertEqual(ans, rst)

    # isconsonant():
    # 자음인지 판단합니다.
    def test_isconsonant(self):
        rst = [c.isconsonant() for c in KorCharTest.tc]
        ans = [False, True, False, True, False]
        self.assertEqual(ans, rst)

    # isvowel():
    # 모음인지 판단합니다.
    def test_isvowel(self):
        rst = [c.isvowel() for c in KorCharTest.tc]
        ans = [False, False, True, False, False]
        self.assertEqual(ans, rst)

    # issyllable():
    # 완전한 한글 음절인지 판단합니다.
    def test_issyllable(self):
        rst = [c.issyllable() for c in KorCharTest.tc]
        ans = [True, False, False, False, False]
        self.assertEqual(ans, rst)

    # iskorchar():
    # 음소(자음/모음) 또는 한글 문자인지 판단합니다.
    def test_iskorchar(self):
        rst = [c.iskorchar() for c in KorCharTest.tc]
        ans = [True, True, True, True, False]
        self.assertEqual(ans, rst)

    # splitsyllable():
    # 초/중/종성 음소를 분리합니다.
    # 첫번째 요소는 분리 가능 여부, 두번째는 분리된 음소(문자열)입니다.
    # 분리가 불가능할 경우, 두번째 요소는 인스턴스 문자를 그대로 반환합니다.
    def test_splitsyllable(self):
        rst = [c.splitsyllable() for c in KorCharTest.tc]
        ans = [(True, 'ㅎㅏㄴ'), (False, 'ㅎ'), (False, 'ㅏ'),
               (False, 'ㄺ'), (False, 'A')]
        self.assertEqual(ans, rst)

    # countstrokes():
    # 한글 획수를 반환합니다. 한글이 아닌 경우 0을 반환합니다.
    def test_countstrokes(self):
        rst = [c.countstrokes() for c in KorCharTest.tc]
        ans = [6, 3, 2, 4, 0]
        self.assertEqual(ans, rst)

    # countkbdstrokes():
    # 키보드 타이핑 횟수(2벌식)를 반환합니다. (쉬프트 키 횟수, 문자 횟수)의 튜플입니다.
    def test_countkbdstrokes(self):
        rst = [c.countkbdstrokes() for c in KorCharTest.tc + [hu.KorChar("깎")]]
        ans = [(0, 3), (0, 1), (0, 1), (0, 2), (0, 1), (2, 3)]
        self.assertEqual(ans, rst)

    # --------------------
    # 2. 클래스 메서드 테스트
    # --------------------

    # join2syllable():
    # 음소(초/중/종성)으로 구성된 문자열을 합성하여 한글 음절을 반환합니다.
    # 튜플의 첫번째 부울 값은 합성 가능 여부를 나타내며, 두번째 값은 합성된 문자입니다.
    # 합성이 불가능할 경우 인자의 문자열을 그대로 반환합니다.
    def test_join2syllable(self):
        phonemes = ["ㅁ바", "ㅎㅏㄴ", "한", "ㅎㅏA", "ㄱㅏㅄ", "ㅋㅓ"]
        rst = [hu.KorChar.join2syllable(s) for s in phonemes]
        ans = [(False, 'ㅁ바'), (True, '한'), (False, '한'),
               (False, 'ㅎㅏA'), (True, '값'), (True, '커')]
        self.assertEqual(ans, rst)

    # ismatch():
    # 검색 문자가 대상 문자와 일치하는지 판단합니다.
    # 검색문자가 초성인 경우 초성 검색을 실시합니다.
    def test_ismatch(self):
        stra = ["ㅋ", "커", "피", 'C']
        strb = ["커", "ㅋ", "피", 'C']
        rst = [hu.KorChar.ismatch(stra[i], strb[i]) for i in range(len(stra))]
        ans = [True, False, True, True]
        self.assertEqual(ans, rst)


# 모듈 메서드에 대한 테스트 클래스입니다.
# 문자열에 대해서는 모듈 메서드를 제공합니다.
class ModTest(unittest.TestCase):
    # --------------------
    # 0. 테스트 대상 문자열
    # --------------------

    sc = ["안녕하세요", "하ㅋ12<>", "abc파이de123!@#썬", "AB 12%^"]

    # --------------------
    # 1. 모듈 메서드 테스트
    # --------------------

    # getlength():
    # 인수 문자열의 (글자 수, 바이트 수)를 반환합니다.
    def test_getlength(self):
        rst = [hu.getlength(s) for s in ModTest.sc]
        ans = [(5, 15), (6, 10), (14, 20), (7, 7)]
        self.assertEqual(ans, rst)

    # iskorstring(s):
    # 문자열이 한글로 구성돼 있는지 판단합니다.
    def test_iskorstring(self):
        # 일부 한글로 구성돼 있는지 판단
        rst = [hu.iskorstring(s) for s in ModTest.sc]
        ans = [True, True, True, False]
        self.assertEqual(ans, rst)
        # 전부 한글로 구성돼 있는지 판단
        rst = [hu.iskorstring(s, full_match=True) for s in ModTest.sc]
        ans = [True, False, False, False]
        self.assertEqual(ans, rst)

    # separatestring():
    # 문자열을 (한글 문자열, 나머지 문자열)로 분리하여 반환합니다.
    def test_separatestring(self):
        rst = [hu.separatestring(s) for s in ModTest.sc]
        ans = [('안녕하세요', ''), ('하ㅋ', '12<>'),
               ('파이썬', 'abcde123!@#'), ('', 'AB 12%^')]
        self.assertEqual(ans, rst)

    # splitstring():
    # 문자열 내 한글을 음소(초/중/종성)로 분리합니다.
    # joinstring():
    # 문자열 내에서 음소(초/중/종성)로 분리된 한글 문자열을 찾아 합성합니다.
    def test_splitstring_and_joinstring(self):
        case = """대한민국헌법
        제1장 총강
        제1조
        ① 대한민국은 민주공화국이다.
        ② 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.
        ..."""
        splited = hu.splitstring(case)  # -> 분리된 문자열
        recover = hu.joinstring(splited)  # -> 합성된 문자열
        self.assertEqual(case, recover)

    # searchonset():
    # 검색 문자열 중 초성이 주어진 경우는 초성을 검색하고, 그렇지 않은 경우는 일치 여부를
    # 검색합니다.
    # 첫번째 반환 인자는 (초성)검색이 성공하였는지 여부를 나타냅니다.
    # 조건에 맞는 문자열이 검색된 경우,
    # 두번째 반환 인자는 (매치 위치의 인덱스, 일치하는 문자열)의 튜플로 구성된 리스트입니다.
    # 조건에 맞는 문자열이 검색되지 않을 경우, 두번째는 빈 리스트를 반환합니다.
    def test_searchonset(self):
        case = "대한민국 ㄷㅎㅁㄱ ㄷㅎㅁ국 대한민ㄱ"
        rst = hu.searchonset("ㄷㅎㅁㄱ", case)
        ans = (True,
               [(0, '대한민국'), (5, 'ㄷㅎㅁㄱ'), (10, 'ㄷㅎㅁ국'), (15, '대한민ㄱ')])
        self.assertEqual(ans, rst)
        rst = hu.searchonset("ㄷㅎㅁ국", case)
        ans = (True, [(0, '대한민국'), (10, 'ㄷㅎㅁ국')])
        self.assertEqual(ans, rst)
        rst = hu.searchonset("ㄷㅎ국민", case)
        ans = (False, [])
        self.assertEqual(ans, rst)

    # countstrokes():
    # 인수 문자열의 한글 획수를 반환합니다.
    # 문자열 내 한글이 아닌 문자가 있을 경우 해당 문자의 획수는 0으로 취급합니다.
    def test_countstrokes(self):
        rst = [hu.countstrokes(s) for s in ModTest.sc]
        ans = [23, 7, 15, 0]
        self.assertEqual(ans, rst)

    # countkbdstrokes():
    # 인수의 문자열을 만들기 위해 필요한 키보드 타이핑 회수를 구합니다.
    # (쉬프트 키 프레스 수, 음소 프레스 수)의 튜플을 반환합니다.
    # 한글이 아닌 문자열도 가능하며, 영대소문자는 쉬프트 키 카운트를 하지 않습니다.
    def test_countkbdstrokes(self):
        sc = ["안녕하세요", "하ㅋ12<>", "abc파이de123!@#썬", "AB 12%^"]
        rst = [hu.countkbdstrokes(s) for s in ModTest.sc]
        ans = [(0, 12), (2, 7), (4, 18), (2, 7)]
        self.assertEqual(ans, rst)


if __name__ == "__main__":
    unittest.main()
