## 백준 2309 일곱 난쟁이
[문제 링크](https://www.acmicpc.net/problem/2309)

## 문제
왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

## 핵심 포인트
```
- 조합을 이용하여 난쟁이가 될 수 있는 경우를 모두 고려한 후 합이 100이 되는지 확인한다.
- 일곱 난쟁이가 되기 위해서는 두 명의 난쟁이만 찾으면 되므로 반복문을 두 번 실행하여 합을 비교한다.
```

## 핵심 코드
> 조합을 이용하여 일곱 난쟁이를 찾는 프로그램
```
    from itertools import combinations
    # 일곱 난쟁이가 될 수 있는 모든 경우를 탐색
    d_list = list(combinations(dwarf, 7))

    for d in d_list:
        # 각 조합 중 합이 100인 것이 올바른 일곱 난쟁이 조합
        if sum(d) == 100:
            print('\n'.join(map(str, d)))
```
> 브루트 포스를 이용하여 일곱 난쟁이를 찾는 프로그램
```
    # 반복문 2개를 활용하여 일곱 난쟁이가 아닌 두 난쟁이를 탐색
    # 원래의 리스트에서 값을 제거하기 위해 두 난쟁이의 키를 리스트에 저장

    for i in range(9):
        for j in range(i + 1, 9):
            if (sum(dwarf) - dwarf[i] - dwarf[j]) == 100:
                not_dwarf.append(dwarf[i])
                not_dwarf.append(dwarf[j])
                break

    # 리스트에서 두 난쟁이 키를 제거
    drawf.remove(not_dwarf[0])
    drawf.remove(not_dwarf[1])
    print('\n'.join(map(str, dwarf))) 
```
