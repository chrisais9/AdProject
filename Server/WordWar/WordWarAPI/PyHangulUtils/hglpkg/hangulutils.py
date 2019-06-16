# -*- coding:utf-8 -*-
"""한글 유틸리티 모듈

이 모듈은 한글 문자/문자열에 대해 다양한 클래스 메서드 및 모듈 메서드를 제공합니다.
한글 문자에 대해서는 KorChar 클래스 및 관련 메서드를 제공하며, 문자열에 대해서는
모듈 레벨의 메서드를 제공합니다.

Author: 박햇님 (https://github.com/mohenjo | haennim.park@hotmail.com)

Notes:
    1. 본 코드/문서에서 사용된 유니코드는 utf-8 인코딩을 기준으로 합니다.
    2. 현대 한글에서 사용하는 음절 및 초성, 중성, 종성 문자셋을 사용합니다.
"""


# region ------ KorChar Class ------

class KorChar:
    """한글 문자(char)에 대해 다양한 속성과 메서드를 제공하는 클래스입니다."""

    # 한글(Hangul Syllables)
    _BEGIN_CODE = 0xAC00  # 시작 유니코드 (44032)
    _END_CODE = 0xD7AF  # 끝 유니코드 (55215)

    # 초성, 중성, 종성
    _ONSET = ('ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ',
              'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
    _NUCLEUS = ('ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
                'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ')
    _CODA = ('', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ',
             'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ',
             'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')

    # 초성, 중성, 종성 획수
    _ONSET_STROKES = (1, 2, 1, 2, 4, 3, 3, 4, 8, 2, 4, 1, 2, 4, 3, 2, 3, 4, 3)
    _NUCLEUS_STROKES = (2, 3, 3, 4, 2, 3, 3, 4, 2, 4, 5, 3, 3, 2, 4, 5, 3, 3,
                        1, 2, 1)
    _CODA_STROKES = (0, 1, 2, 3, 1, 3, 4, 2, 3, 4, 6, 7, 5, 6,
                     7, 6, 3, 4, 6, 2, 4, 1, 2, 3, 2, 3, 4, 3)

    # 초성, 중성, 종성 키보드 프레스 횟수 (쉬프트키 프레스 횟수, 음소 프레스 수)
    _ONSET_KBD_STROKES = [(0, 1), (1, 1), (0, 1), (0, 1), (1, 1), (0, 1),
                          (0, 1), (0, 1), (1, 1), (0, 1), (1, 1), (0, 1),
                          (0, 1), (1, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]
    _NUCLEUS_KBD_STROKES = [(0, 1), (0, 1), (0, 1), (1, 1), (0, 1), (0, 1),
                            (0, 1), (1, 1), (0, 1), (0, 2), (0, 2), (0, 2),
                            (0, 1), (0, 1), (0, 2), (0, 2), (0, 2), (0, 1),
                            (0, 1), (0, 2), (0, 1)]
    _CODA_KBD_STROKES = [(0, 0), (0, 1), (1, 1), (0, 2), (0, 1), (0, 2), (0, 2),
                         (0, 1), (0, 1), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2),
                         (0, 2), (0, 2), (0, 1), (0, 1), (0, 2), (0, 1), (1, 1),
                         (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]

    # 쉬프트 키 사용 문자열
    _SHIFTED_CHARSET = """~!@#$%^&*()_+{}|:"<>?"""

    def __init__(self, arg: str):
        """클래스 생성자

        Parameters
        ----------
        arg : str
            길이가 1인 문자열

        Raises
        ------
        TypeError
            문자가 주어지지 않거나, 문자열의 길이가 1이 아닌 경우
        """

        # check = type(arg) == type(str()) and len(arg) == 1
        check = isinstance(arg, str) and len(arg) == 1
        if not check:
            raise TypeError("문자가 주어지지 않았거나, 문자열의 길이가 1이 아닙니다.")
        self._char = arg

    def getchar(self):
        """인스턴스의 문자입니다"""
        return self._char

    def isonset(self):
        """초성으로 사용될 수 있는지 판단합니다."""
        return self._char in KorChar._ONSET

    def isnucleus(self):
        """중성으로 사용될 수 있는지 판단합니다."""
        return self._char in KorChar._NUCLEUS

    def iscoda(self):
        """종성으로 사용될 수 있는지 판단합니다."""
        return self._char in KorChar._CODA

    def isconsonant(self):
        """자음인지 판단합니다."""
        return self._char in KorChar._ONSET or self._char in KorChar._CODA

    def isvowel(self):
        """모음인지 판단합니다."""
        return self._char in KorChar._NUCLEUS

    def issyllable(self):
        """자음/모음이 아닌 완전한 한글 음절인지 판단합니다."""
        return KorChar._BEGIN_CODE <= ord(self._char) <= KorChar._END_CODE

    def iskorchar(self):
        """한글 문자인지 판단합니다."""
        return self.issyllable() or self.isconsonant() or self.isvowel()

    def splitsyllable(self):
        """초/중/종성이 분리된 문자열을 반환합니다.

        인스턴스 문자가 (분리 가능한) 완전한 한글 음절이 아닌 경우, 인스턴스
        문자를 그대로 반환합니다.

        Returns
        -------
        tuple[bool,str]
            (분리 가능 여부, 초/중/종성이 분리된 문자열).
            반환 요소의 첫번째는 분리 가능 여부를 나타내는 부울 값입니다.

        """
        # 분리가 가능한 한글 음절이 아닌 경우 인스턴스 문자열을 그대로 반환
        if not self.issyllable():
            return False, self._char
        # 한글 음절인 경우 변환 수행
        foo = ord(self._char) - KorChar._BEGIN_CODE
        onsetidx = foo // 588
        nucleusidx = (foo - onsetidx * 588) // 28
        codaidx = foo - onsetidx * 588 - 28 * nucleusidx
        jamo = KorChar._ONSET[onsetidx] + KorChar._NUCLEUS[nucleusidx] + KorChar._CODA[codaidx]
        return True, jamo

    def countstrokes(self):
        """인스턴스 문자열의 획수를 반환합니다.

        Returns
        -------
        int
            문자열 획수. 한글이 아닌 경우 0을 반환합니다.
        """
        # {음소:획수} 딕셔너리를 구성합니다.
        dic1 = {c: KorChar._ONSET_STROKES[idx]
                for idx, c in enumerate(KorChar._ONSET)}
        dic2 = {c: KorChar._NUCLEUS_STROKES[idx]
                for idx, c in enumerate(KorChar._NUCLEUS)}
        dic3 = {c: KorChar._CODA_STROKES[idx]
                for idx, c in enumerate(KorChar._CODA)}
        strokedic = dict(dic1, **dic2, **dic3)

        count = 0
        if not self.iskorchar():  # 한글이 아닌 경우 0 반환
            return count
        # 한글인 경우 초, 중, 종성에 대한 획수 합 반환
        newstr = str(self.splitsyllable()[1])
        for c in newstr:
            count += strokedic[c]
        return count

    def countkbdstrokes(self):
        """2벌식 한글 키보드에서 인스턴스 문자열을 만들기 위해 필요한 키보드 프레스 수를 반환합니다.

        Returns
        -------
        tuple[int,int]
            (쉬프트 키 프레스 수, 음소 프레스 수)의 튜플입니다.
            한글이 아닌 문자도 카운트 가능하며, 영대소문자는 쉬프트 키 카운트를 하지 않습니다.
        """
        # {음소:(쉬프트키 프레스 수, 음소 프레스 수)} 딕셔너리를 구성합니다.
        dic1 = {tp: KorChar._ONSET_KBD_STROKES[idx]
                for idx, tp in enumerate(KorChar._ONSET)}
        dic2 = {tp: KorChar._NUCLEUS_KBD_STROKES[idx]
                for idx, tp in enumerate(KorChar._NUCLEUS)}
        dic3 = {tp: KorChar._CODA_KBD_STROKES[idx]
                for idx, tp in enumerate(KorChar._CODA)}
        kbdstrokedic = dict(dic1, **dic2, **dic3)

        sftcount, count = 0, 0  # 쉬프트 키 프레스 수, 음소 프레스 수
        if self.iskorchar():  # 한글인 경우
            newstr = str(self.splitsyllable()[1])
            for c in newstr:
                sftcount += kbdstrokedic[c][0]
                count += kbdstrokedic[c][1]
        else:  # 한글이 아닌 경우 (대소문자는 shift 키 횟수에 영향을 주지 않음)
            count += 1
            if self._char in KorChar._SHIFTED_CHARSET:
                sftcount += 1
        return sftcount, count

    @classmethod
    def join2syllable(cls, astr: str):
        """초/중/종성으로 구성된 문자열을 합성하여 한글 음절을 반환합니다.

        인자의 문자열로부터 한글 음절 합성이 불가능한 경우, 인자를 그대로 반환합니다.

        Parameters
        ----------
        astr : str
            초/중/종성 순으로 공백없이 구성된 2~3글자 문자열입니다.

        Returns
        -------
        tuple[bool, str]
            (합성 가능 여부, 초/중/종성이 합성된 한글 음절).
            반환 요소의 첫번째는 합성 가능 여부를 나타내는 부울 값입니다.
        """
        # 입력 문자열의 길이 2, 3 글자가 아닌 경우
        if not (2 <= len(astr) <= 3):
            return False, astr
        # 입력 문자열이 합성 가능한 초/중/종성으로 이루어져 있는지 판단
        onset, nucleus = astr[:2]
        coda = astr[2] if len(astr) == 3 else ''
        check = onset in KorChar._ONSET and nucleus in KorChar._NUCLEUS and coda in KorChar._CODA
        if not check:
            return False, astr
        # 초/중/종성 코드 합성
        onsetidx = KorChar._ONSET.index(onset)
        nucleusidx = KorChar._NUCLEUS.index(nucleus)
        codaidx = KorChar._CODA.index(coda)
        newcode = KorChar._BEGIN_CODE + (onsetidx * 588) + (nucleusidx * 28) + codaidx
        # 합성된 문자가 한글 음절에 포함되어 있는지 판단
        if KorChar._BEGIN_CODE <= newcode <= KorChar._END_CODE:
            return True, chr(newcode)
        else:
            return False, astr

    @classmethod
    def ismatch(cls, searchstr: str, targetstr: str):
        """검색문자가 대상문자와 일치하는지 판단합니다.

        검색문자가 초성인 경우 대상문자의 초성과 비교하고, 검색문자가 한글 음절 또는
        한글이 아닌 경우 대상문자와 완전히 일치하는지 비교합니다. 

        Parameters
        ----------
        searchstr : str
            검색문자
        targetstr : str
            대상문자

        Returns
        -------
        bool
            문자가 일치(초성-초성일치, 음절or한글아님-완전일치)할 경우 참을 반환합니다.
        """
        searchchar = KorChar(searchstr)
        targetchar = KorChar(targetstr)

        if searchchar.isonset():
            return str(searchchar.splitsyllable()[1])[0] == \
                   str(targetchar.splitsyllable()[1])[0]
        else:
            return searchstr == targetstr


# endregion ------------


# region ------ Module Methods ------

def getlength(astr: str):
    """인수 문자열의 글자 수 및 바이트 수를 구합니다.

    Parameters
    ----------
    astr : str
        문자열

    Returns
    -------
    tuple[int, int]
        (글자 수, 바이트 수)로 구성된 튜플입니다.
    """
    return len(astr), len(astr.encode("-utf-8"))


def iskorstring(astr: str, full_match=False):
    """인수로 주어진 문자열이 한글 문자로 구성돼 있는지 판단합니다.

    Parameters
    ----------
    astr : str
        판단 대상 문자열
    full_match : bool
        False: 한글 문자열을 포함하고 있는지 판단합니다.
        True: 전체가 한글로 구성된 문자열인지 판단합니다.

    Returns
    -------
    bool
    """
    func = all if full_match else any
    return func((KorChar(c).iskorchar() for c in astr))


def separatestring(astr: str):
    """인수로 주어진 문자열을 한글 부분과 나머지 부분으로 분리합니다.

    Parameters
    ----------
    astr : str
        대상 문자열

    Returns
    -------
    tuple[str, str]
        (한글문자열, 나머지 문자열)로 구성된 튜플
    """
    korstr = ""
    elsestr = ""
    for c in astr:
        if KorChar(c).iskorchar():
            korstr += c
        else:
            elsestr += c
    return korstr, elsestr


def splitstring(astr: str):
    """한글 문자열을 초/중/종성으로 분리합니다.

    인수로 주어진 문자열 중 한글 부분을 초/중/종성으로 분리하여 반환합니다.

    Parameters
    ----------
    astr : str
        대상 문자열

    Returns
    -------
    str

    """
    return "".join((str(KorChar(c).splitsyllable()[1]) for c in astr))


def joinstring(astr: str):
    """초/중/종성이 분리된 한글 문자열을 합성합니다.

    인수로 주어진 문자열 중 초/중/종성이 분리된 한글을 합성하여 반환합니다.

    Notes
    -----
    한글 음소(자음, 모음)와 분리된 한글 음절이 섞여 있는 조건도 충분히 고려하도록
    설계되었지만 음소의 위치에 따라 의도하지 않은 결과를 반환할 수도 있습니다.

    따라서, 일반적으로 사용하는 방식의 (완전한 한글 음절이 분리된) 자음/모음으로
    구성된 문자열을 인수로 사용할 것을 권장합니다. 예시를 참조바랍니다.

    Examples
    --------
    예시 1:
        '값이 비쌉니다.'를 얻기 위해 인수로서 'ㄱㅏㅄㅇㅣ ㅂㅣㅆㅏㅂㄴㅣㄷㅏ.'를
        사용하는 것이 일반적인 경우이며 권장됩니다.

    예시 2:
        'ㅇㅇ 대답에 기분이 ㅠㅠ'를 얻기 위해
        인수로서 'ㅇㅇ ㄷㅐㄷㅏㅂㅇㅔ ㄱㅣㅂㅜㄴㅇㅣ ㅠㅠ'를 사용하더라도 정상적으로
        합성된 문자열을 얻을 수 있습니다.

    예시 3:
        단, 'ㄱㅣㅂㅜㄴㅇㅣㅎ ㅈㅗㅎㄷㅏ'를 인수로 사용할 경우,
        기대 가능한 반환값은 '기분잏 좋다' 또는 '기분이ㅎ 좋다'입니다. 이 경우
        본 메서드는 합성을 우선하여 전자의 문자열을 반환합니다.

    Parameters
    ----------
    astr : str
        대상 문자열

    Returns
    -------
    str
        합성된 문자열입니다.
    """
    astr += " " * 6  # 마지막 인덱스 판단을 피하기 위해 공백 임시 추가
    newstr = ""
    idx = 0
    while idx < len(astr) - 6:
        # ------ 판단 변수들
        # --- 현재 글자
        curinst = KorChar(astr[idx])  # 현재 글자
        # --- 3글자 고려시
        # 현재 3글자 합성
        cur3span = KorChar.join2syllable(astr[idx:idx + 3])
        # 현재 3글자 이후 2글자 합성
        cur3nxt2span = KorChar.join2syllable(astr[idx + 3:idx + 5])
        # 현재 3글자 이후 1번쨰 글자
        cur3nxt1inst = KorChar(astr[idx + 3])
        # 현재 3글자 이후 2번쨰 글자
        cur3nxt2inst = KorChar(astr[idx + 4])
        # -- 2글자 고려시
        # 현재 2글자 합성
        cur2span = KorChar.join2syllable(astr[idx:idx + 2])
        # 현재 2글자 이후 2글자 합성
        cur2nxt2span = KorChar.join2syllable(astr[idx + 2:idx + 4])
        # 현재 2글자 이후 1번째 글자
        cur2nxt1inst = KorChar(astr[idx + 2])

        # ------ 판단부
        # 현재 글자가 한글 글자가 아닌 경우 현재 글자 추가
        if not curinst.iskorchar():
            newstr += curinst.getchar()
            idx += 1
        # 아니면, 현재 3개의 글자가 합성이 가능한 상황에서
        # - 다음 2개의 글자 합성 가능하거나
        # - 다음 1개의 글자가 한글이 아니거나
        # - 다음 2개의 글자가 모두 자음이거나
        elif cur3span[0] \
                and (cur3nxt2span[0] or not cur3nxt1inst.iskorchar() or
                     (cur3nxt1inst.isconsonant() and cur3nxt2inst.isconsonant())):
            newstr += cur3span[1]
            idx += 3
        # 아니면, 현재 2개의 글자가 합성이 가능한 상황에서
        # - 다음 2개의 글자가 합성 가능하거나
        # - 다음 1개의 글자가 한글이 아니거나
        elif cur2span[0] and (cur2nxt2span[0] or not cur2nxt1inst.iskorchar()):
            newstr += cur2span[1]
            idx += 2
        # 아니면, (한글이지만 합성 없이) 현재 글자 추가
        else:
            newstr += curinst.getchar()
            idx += 1
    return newstr.strip()


def searchonset(searchstr: str, targetstr: str):
    """대상 문자열에 대한 (초성)검색 결과를 반환합니다.

    검색문자열에서 초성이 주어진 경우 초성을 비교하고, 그렇지 않은 경우 일치 여부를
    비교합니다.

    Parameters
    ----------
    searchstr : str
        검색할 문자열. 초성 검색이 필요할 경우 초성을 넣으면 됩니다.
    targetstr : str
        검색 대상 문자열

    Returns
    -------
    Tuple[bool, List[Tuple[int, str]]]
        첫번째 반환 인자는 (초성)검색이 성공하였는지 여부를 나타냅니다.
        조건에 맞는 문자열이 없을 경우, 두번쨰 반환 인자는 빈 리스트를 반환합니다.
        조건에 맞는 문자열이 검색된 경우, 두번째 반환 인자는 (매치 위치의 인덱스,
        일치하는 문자열)의 튜플로 구성된 리스트입니다.

    """
    if searchstr == '' or len(searchstr) > len(targetstr):
        raise ValueError("인수의 문자열이 유효하지 않습니다.")
    length = len(searchstr)
    success = False
    matchlst = []
    for idx in range(len(targetstr) - (length - 1)):
        fragtarget = targetstr[idx: idx + length]
        check = all([KorChar.ismatch(searchstr[i], fragtarget[i])
                     for i in range(len(fragtarget))])
        if check:
            success = True
            matchlst.append((idx, fragtarget))
    return success, matchlst


def countstrokes(astr: str):
    """인수 문자열의 획수를 반환합니다.

    Parameters
    ----------
    astr : str
        획수를 확인할 한글 문자열입니다.

    Returns
    -------
    int
        한글 획수입니다. 문자열 내 한글이 아닌 문자가 있을 경우 해당 문자의 획수는
        0으로 취급합니다.
    """
    count = 0
    for s in astr:
        count += KorChar(s).countstrokes()
    return count


def countkbdstrokes(astr: str):
    """인수의 문자열을 만들기 위해 필요한 키보드 타이핑 회수를 구합니다.

    Parameters
    ----------
    astr : str
        총 키보드 타이핑 회수를 구할 문자열입니다.

    Returns
    -------
    tuple[int, int]
        (쉬프트 키 프레스 수, 음소 프레스 수)의 튜플입니다.
        한글이 아닌 문자열도 가능하며, 영대소문자는 쉬프트 키 카운트를 하지 않습니다.
    """
    sftcount, count = 0, 0
    for s in astr:
        foo = KorChar(s).countkbdstrokes()
        sftcount += foo[0]
        count += foo[1]
    return sftcount, count


# endregion ------------


def main():
    print("모듈로 임포트하여 사용하세요.")


if __name__ == "__main__":
    main()
