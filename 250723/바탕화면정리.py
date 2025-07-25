def solution(wallpaper):
    answer = []
    files = []
    n = len(wallpaper)
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                files.append([i,j])
    files.sort(key = lambda x : (x[0], x[1]))
#     answer.append(files[0][0])

#     files.sort(key = lambda x: (x[1], x[0]))

#     answer.append(files[0][1])
    lux, luy, rdx, rdy = 1e9, 1e9, 0, 0
    for file in files:
        lux = min(lux, file[0])
        luy = min(luy, file[1])
        rdx = max(rdx, file[0])
        rdy = max(rdy, file[1])
        
    answer = [lux, luy, rdx+1, rdy+1]
    return answer