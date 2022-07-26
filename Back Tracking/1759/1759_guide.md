## 백준 1759 암호 만들기
[문제 링크](https://www.acmicpc.net/problem/1759)

## 문제
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

## 핵심 포인트
```
- 백트래킹을 이용하여 서로 다른 L개의 조합이 만들어졌을 때 최소 한 개의 모음과 최소 두 개의 자음 조건이 만족되는지 확인한다.
- 중복되는 것이 없어야 하므로 전에 추가한 알파벳보다 현재 추가하려는 알파벳은 커야 한다.
```

## 핵심 코드
> 백트래킹을 활용한 암호 만들기
```
def is_possible():
    # 현재 모음과 자음의 개수를 나타내는 변수 선언
    cur_vo, cur_con = 0, 0
    for p in pw:
        if p in ['a', 'e', 'i', 'o', 'u']:
            cur_vo += 1
        else:
            cur_con += 1

    # 현재 모음과 자음이 최소 조건을 만족하는지 검사
    if cur_vo >= 1 and cur_con >= 2:
        print(''.join(pw))

def back_tracking(count):
    # l개의 조합이 완성되었을 때 조건을 만족하는지 검사
    if count == l: 
        is_possible()
        return

    for a in alpha:
        # 서로 다른 문자로 이루어진 암호
        if a not in pw:
            # 중복은 없다고 했으므로 항상 전에 삽입한 알파벳보다는 커야 함
            if len(pw) == 0 or a > pw[-1]:
                # 백트래킹 진행
                pw.append(a)
                back_tracking(count + 1)
                pw.pop()
```
> 조합을 이용한 암호 만들기
```
from itertools import combinations

alpha = sorted(input().split())
# 조합을 이용하여 암호가 될 수 있는 모든 경우의 수 탐색
pw = combinations(alpha, l)

for p in pw:
    for i in range(len(p)):
        if p[i] in ['a', 'e', 'i', 'o', 'u']:
            cur_vo += 1
        else:
            cur_con += 1

    # 해당 조합이 최소 조건을 만족하는지 검사
    if cur_vo >= 1 and cur_con >= 2:
        print(''.join(p))
```
