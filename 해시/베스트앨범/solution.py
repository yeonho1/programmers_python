def solution(genres, plays):
    genrePlays = {}
    songPlays = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        genrePlays[g] = genrePlays.get(g, 0) + p
        songPlays[g] = songPlays.get(g, []) + [i]
    l = sorted(genrePlays.items(), reverse=True, key=lambda x: x[1])
    result = []
    for genre in l:
        result += sorted(songPlays[genre[0]], key=lambda song: (-plays[song], song))[:2]
    return result