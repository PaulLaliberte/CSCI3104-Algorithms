"""recurrence for finding min path of frog jumps"""

import copy

def frogGame(game_state, frog, energy, path, solution_paths):
    if game_state[frog] == 'B':
        energy += 5
        
    if frog == len(game_state)-1:
        #print('c')
        path.append(frog)
        solution_paths.append(path)
    elif energy <= 0:
        #print('a')
        path.append('FAILED PATH')
        solution_paths.append(path)
    elif game_state[frog] == 'D':
        #print('b')
        path.append('FAILED PATH')
        solution_paths.append(path)
    else:
        #print('d')
        path.append(frog)
        p1 = copy.copy(path)
        frogGame(game_state, frog+1, energy-1, p1, solution_paths)
        frogGame(game_state, frog+2, energy-3, path, solution_paths)


if __name__ == '__main__':
    intitial_frog_poisiton = 0
    intitial_energy = 9
    path = []
    solution_paths = []

    a = ['S','S','S','S','D','B','S','S','S','S','S','D','B','D','S','S','D','S']

    """
    *******************
    #Testing for part D
    *******************
    b = ['S']
    c = ['S', 'D', 'S']
    d = ['S','S','D','S']
    e = ['B','D','S','S','D','S']
    f = ['S','D','B','D','S','S','D','S']
    g = ['S','S','D','B','D','S','S','D','S']
    h = ['S','S','S','D','B','D','S','S','D','S']
    i = ['S','S','S','S','D','B','D','S','S','D','S']
    j = ['S','S','S','S','S','D','B','D','S','S','D','S']
    k = ['B','S','S','S','S','S','D','B','D','S','S','D','S']
    l = ['S','D','B','S','S','S','S','S','D','B','D','S','S','D','S']
    m = ['S','S','D','B','S','S','S','S','S','D','B','D','S','S','D','S']
    n = ['S','S','S','D','B','S','S','S','S','S','D','B','D','S','S','D','S']
    """

    frogGame(a,intitial_frog_poisiton,intitial_energy,path,solution_paths)

    s = []

    for i in solution_paths:
        if 'FAILED PATH' in i:
            pass
        else:
            s.append(i)
    
    #print(len(s))    #for part D
  
    x = min(s)
    #do not count first step, i.e. position 0
    print(len(x) - 1, ':',  x)
    


    
