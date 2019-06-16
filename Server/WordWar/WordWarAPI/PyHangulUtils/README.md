# [Python] Hangul Utils | 한글 유틸리티 모듈

![status](https://img.shields.io/badge/Status-done-success.svg)
![version](https://img.shields.io/badge/Version-v1.1903-informational.svg)
![license](https://img.shields.io/badge/License-MIT-important.svg)
![python](https://img.shields.io/badge/Python-3.5+-informational.svg)
![paltform](https://img.shields.io/badge/Platform-windows_10_x64-lightgray.svg)

이 파이썬 모듈은 한글 문자/문자열에 대해 다양한 클래스 메서드/모듈 메서드를 제공합니다.

> + 한글문자의 자음/모음, 초성/중성/종성 분리 및 합성 등
> + 문자열의 한글 합성 및 분리, 초성 검색 등
> + 한글 문자(**char**)에 대해서는 `KorChar` 클래스 및 관련 메서드를 제공하며, 
> + 문자열(**string**)에 대해서는 모듈 레벨의 메서드를 제공합니다.


## Installation & Usage

### Installation

+ [`hangulutil.py`](https://github.com/mohenjo/HangulUtils/blob/master/hglpkg/hangulutils.py) 모듈에 대해 `[from hglpkg] import hangulutil` 합니다.

### Desciption of Methods

+ 인스턴스 생성:

    + `KorChar(<한글문자>)`

+ 인스턴스 메서드: 한글 문자(**char**)에 대한 메서드

    + `getchar()`: 인스턴스의 문자열을 반환합니다.
    
    + `isonset()`, `isnucleus()`, `iscoda()`: 초성/중성/종성으로 사용할 수 있는지 판단합니다.
    
    + `isconsonant()`, `isvowel()`: 자음/모음인지 판단합니다.
    
    + `issyllable()`: 완전한 한글 음절인지 판단합니다.
    
    + `iskorchar()`: 한글 문자인지 판단합니다. (자음/모음, 한글 음절)
    
    + `splitsyllable()`: 초성/중성/종성 음소를 분리합니다. 
    
        + 첫번째 요소는 분리 가능 여부, 두번째는 분리된 음소(문자열)입니다.
        + 분리가 불가능할 경우, 두번째 요소는 인스턴스 문자를 그대로 반환합니다.
    
    + `countstrokes()`: 한글 획수를 반환합니다. 한글 문자가 아닌 경우 0을 반환합니다.
    
    + `countkbdstrokes()`: 2벌식 한글 키보드에서의 키보드 타이핑 횟수를 반환합니다.
    
        + 반환값은 `(<SHIFT-KEY 타이핑 횟수>, <문자 타이핑 횟수>)`의 튜플입니다.
        + 한글이 아닌 문자에도 적용되며, 영대소문자의 `SHIFT-KEY` 카운팅은 하지 않습니다. 

+ 클래스 메서드: 

    + `join2syllable(<string>)`: 음소(초/중/종성)으로 구성된 문자열을 합성하여 한글 음절을 반환합니다.
    
        + 튜플의 첫번째 부울 값은 합성 가능 여부를 나타내며, 두번째 값은 합성된 문자입니다.
        + 합성이 불가능할 경우 인자의 문자열을 그대로 반환합니다.
    
    + `ismatch(<char>, <char>)`: 검색 문자가 대상 문자와 일치하는지 판단합니다. 검색문자가 초성인 경우 초성 검색을 실시합니다.

+ 모듈 메서드: 문자열(**string**)에 대한 메서드

    + `getlength(<string>)`: 문자열의 길이, 바이트 길이의 튜플을 반환합니다.
    
    + `iskorstring(<string>, <option>)`: 옵션에 따라 문자열이 일부 또는 전부 한글로 구성돼 있는지 판단합니다.
    
    + `separatestring(<string>)`: 문자열에서 한글 문자열과 나머지 문자열을 분리하여 반환합니다.
    
    + `splitstring(<string>)`: 문자열 내 한글을 음소(초/중/종성)로 분리합니다.
    
    + `joinstring(<string>)`: 문자열 내에서 음소(초/중/종성)로 분리된 한글 문자열을 찾아 합성합니다.
    
    + `searchonset(<string>, <string>)`: 문자열을 (초성) 검색합니다.
    
        + 검색 문자열 중 초성이 주어진 경우는 초성을 검색하고, 그렇지 않은 경우는 일치 여부를 검색합니다.
        + 첫번째 반환 인자는 (초성)검색이 성공하였는지 여부를 나타냅니다.
        + 조건에 맞는 문자열이 검색된 경우, 두번째 반환 인자는 (매치 위치의 인덱스, 일치하는 문자열)의 튜플로 구성된 리스트입니다.
        + 조건에 맞는 문자열이 검색되지 않을 경우, 두번째는 빈 리스트를 반환합니다.
        
    + `countstrokes(<string>)`: 문자열의 총 한글 획수를 반환합니다.
      
        + 문자열 내 한글이 아닌 문자가 있을 경우, 해당 문자열의 획수는 0입니다.
        
    + `countkbdstrokes(<string>)`: 2벌식 키보드에서 문자열을 만들기 위해 필요한 키보드 타이핑 횟수를 구합니다.
    
        + `(<SHIFT-KEY 타이핑 횟수>, <문자 타이핑 횟수>)`의 튜플을 반환합니다.
        + 한글이 아닌 문자열도 가능하며, 영대소문자는 `SHIFT-KEY` 카운트를 하지 않습니다.
    

### Usage

+ 인수 및 반환값에 대한 자세한 내용은 각 메서드의 docstring을 참조하시기 바랍니다.
+ 유닛테스트 파일 [`test_hangulutils.py`](https://github.com/mohenjo/HangulUtils/blob/master/tests/test_hangulutils.py)의 사용 예를 참조하시기 바랍니다.


## Project Info

### Version

+ Version 1.1903

### Dev Tools

+ [Python 3.7.2 x86](https://www.python.org/)
+ [PyCharm Community Edition](https://www.jetbrains.com/pycharm/)
+ [Notepad++](https://notepad-plus-plus.org/)

### Environments

+ Test Environment

    + Microsoft Windows 10 (x64)
    + Python 3.7.2 x86

+ Code Compatibility

    + Python 3.5, 3.6, 3.7

+ Dependencies / 3rd-party package(s)

    + None


## Contributor

+ [Haennim Park](https://github.com/mohenjo)


## License

+ [MIT License](https://github.com/mohenjo/HangulUtils/blob/master/LICENSE)




