# 참여자와 완주자의 길이를 동일하게 설정한 후, 각각의 그룹을 정렬한다.
# 같은 순서에 위치한 요소들을 짝을 이루도록 하고 짝을 이루고 있는 요소들이 서로 같지않을 때의 참여자 이름을 불러온다.

def solution(participant, completion):
    completion.append('z'*20)
    zips = zip(sorted(participant), sorted(completion))
    return [z[0] for z in zips if z[0] != z[1]][0]
