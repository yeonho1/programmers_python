def solution(participant, completion):
    for p in participant:
        if participant.count(p) != completion.count(p):
            return p