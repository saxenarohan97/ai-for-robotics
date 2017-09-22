def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # >>> Insert your code here <<<

    pnew = p

    for x in range(len(motions)):

        '''move'''
        for r in range(len(p)):

            for c in range(len(p[r])):

                print 'p[0][1]: %f \n' % p[0][1]

                row = (r - motions[x][0]) % len(pnew)
                col = (c - motions[x][1]) % len(pnew[r])

                print '[%d, %d] ---> [%d, %d] \n' % (row, col, r, c)

                pnew[r][c] = p[row][col] * p_move + p[r][c] * (1 - p_move)

                print p[row][col]

        show(pnew)

        '''sense'''
        s = 0.0
        for r in range(len(p)):

            for c in range(len(p[r])):

                if colors[r][c] == measurements[x]:
                    pnew[r][c] *= sensor_right

                else:
                    pnew[r][c] *= (1 - sensor_right)

                s += pnew[r][c]

        for r in range(len(p)):

            for c in range(len(p[r])):

                pnew[r][c] /= s        

        p = pnew

        show(p)
    
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    print
    
#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]

measurements = ['G','G','G','G','G']

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

p = localize(colors,measurements,motions,sensor_right = 1.0, p_move = 1.0)

#show(p) # displays your answer
