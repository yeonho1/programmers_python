from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque()
    onBridge = 0
    for w in truck_weights:
        while (len(trucks) > 0 and answer - trucks[0]['start'] == bridge_length) \
              or onBridge + w > weight \
              or len(trucks) + 1 > bridge_length:
            first = trucks.popleft()
            answer = first['start'] + bridge_length
            onBridge -= first['weight']
        trucks.append({'start': answer, 'weight': w})
        onBridge += w
        answer += 1
    return answer + bridge_length