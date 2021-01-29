#!/usr/bin/env python

import random
from index import *

# Enter or decrypt the seed value
X_SIZE = 26
Y_SIZE = 26

f = open("word_list_length.txt", "r")
word_list_length = eval(f.read())
f.close()

f = open("decrypted_notes.txt", "r")
decrypted_notes = eval(f.read())
f.close()

f = open("random_seed.txt", "r")
seed = eval(f.read())
f.close()

# creating a 2D matrix (26 x 26) to show the impossible transitions between letters
# If it happens to be an impossible transition then we assign the corresponding cell in the 2D matrix to 0, else 1
a = [[1 for i in range(26)] for j in range(26)]

# impossible transitions from character 'b': bg, bk, bq, bw, bx, bz
a[1][6] = a[1][10] = a[1][16] = a[1][22] = a[1][23] = a[1][25] = 0

# impossible transitions from character 'c': cb, cf, cg, cj, cm, cn, cp, cv, cw, cx, cz
a[2][1] = a[2][5] = a[2][6] = a[2][9] = a[2][12] = a[2][13] = a[2][15] = a[2][21] = a[2][22] = a[2][23] = 0

# impossible transitions from character 'd': dq, dt, dx, dz
a[3][16] = a[3][23] = a[3][25] = 0

# impossible transitions from character 'f': fb, fd, fg, fj, fk, fm, fn, fp, fq, fv, fw, fz
a[5][3] = a[5][6] = a[5][9] = a[5][10] = a[5][12] = a[5][13] = a[5][15] = a[5][16] = a[5][21] = a[5][22] = a[5][25] = 0

# impossible transitions from character 'g': gb, gc, gj, gk, gq, gv, gw, gx, gz
a[6][1] = a[6][2] = a[6][9] = a[6][10] = a[6][16] = a[6][21] = a[6][22] = a[6][23] = a[6][25] = 0

# impossible transitions from character 'h': hg, hh, hj, hk, hq, hv, hx, hz
a[7][6] = a[7][9] = a[7][10] = a[7][16] = a[7][21] = a[7][23] = a[7][25] = 0

# impossible transitions from character 'j': jb, jc, jd, jf, jg, jh, jj, jk, jl, jm, jn, jp, jq, jr, js, jt, jv, jw, jx, jy, jz
a[9][1] = a[9][2] = a[9][3] = a[9][5] = a[9][6] = a[9][7]  = a[9][9] = a[9][10] = a[9][11] = a[9][12] = a[9][13] = a[9][15] = a[9][16] = a[9][17] = a[9][18] = a[9][19] = a[9][21] = a[9][22] = a[9][23] = a[9][24] = a[9][25] = 0

# impossible transitions from character 'k': kf, kj, kq, kt, kv, kx, kz
a[10][9] = a[10][16] = a[10][19] = a[10][21] = a[10][23] = a[10][25] = 0

# impossible transitions from character 'l': lh, lj, lq, lx, lz
a[11][7] = a[11][9] = a[11][16] = a[11][23] = 0

# impossible transitions from character 'm': mc, md, mg, mh, mj, mk, mq, mt, mv, mw, mx, mz
a[12][2] = a[12][3] = a[12][6] = a[12][7] = a[12][9] = a[12][10] = a[12][16] = a[12][19] = a[12][21] = a[12][22] = a[12][23] = a[12][25] = 0

# impossible transitions from character 'o': oq
a[14][16] = 0

# impossible transitions from character 'p': pb, pc, pf, pj, pn, pq, pv, px, pz
a[15][1] = a[15][2] = a[15][5] = a[15][9] = a[15][13] = a[15][16] = a[15][21] = a[15][23] = a[15][25] = 0

# impossible transitions from character 'q': qa, qb, qc, qd, qe, qf, qg, qh, qi, qj, qk, ql, qm, qn, qo, qp, qq, qr, qs, qt, qv, qw, qx, qy, qz
for i in range(26):
    if i == 20:
        continue
    else:
        a[16][i] = 0

# impossible transitions from character 'r': rx, rz
a[17][23] = a[17][25] = 0

# impossible transitions from character 's': sv, sx, sz
a[18][21] = a[18][23] = a[18][25] = 0

# impossible transitions from character 't': tj, tk, tq, tv, tx
a[19][9] = a[19][10] = a[19][16] = a[19][21] = a[19][23] = 0

# impossible transitions from character 'u': uh, uj, uq, uw
a[20][7] = a[20][9] = a[20][16] = a[20][22] = 0

# impossible transitions from character 'v': vb, vc, vd, vf, vg, vh, vj, vk, vl, vm, vn, vp, vq, vs, vt, vw, vx, vz
a[21][1] = a[21][2] = a[21][3] = a[21][5] = a[21][6] = a[21][7] = a[21][9] = a[21][10] = a[21][11] = a[21][12] = a[21][13] = a[21][15] = a[21][16] = a[21][18] = a[21][19] = a[21][22] = a[21][23] = a[21][25] = 0

# impossible transitions from character 'w': wg, wj, wq, wv, ww, wx, wz
a[22][6] = a[22][9] = a[22][16] = a[22][21] = a[22][23] = a[22][25] = 0
 
# impossible transitions from character 'x': xb, xd, xf, xg, xj, xk, xm, xn, xr, xs, xv, xw, xx, xz
a[23][1] = a[23][3] = a[23][5] = a[23][6] = a[23][9] = a[23][10] = a[23][12] = a[23][13] = a[23][17] = a[23][18] = a[23][21] = a[23][22] = a[23][25] = 0

# impossible transitions from character 'y': yj, yk, yq, yv, yy
a[24][9] = a[24][10] = a[24][16] = a[24][21] = a[24][24] = 0

# impossible transitions from character 'z': zb, zc, zd, zf, zg, zj, zk, zm, zn, zp, zq, zr, zs, zt, zw, zx
a[25][1] = a[25][2] = a[25][3] = a[25][5] = a[25][6] = a[25][9] = a[25][10] = a[25][12] = a[25][13] = a[25][15] = a[25][16] = a[25][17] = a[25][18] = a[25][19] = a[25][22] = a[25][23] = 0


tuple_list = []
for i in range(128):
    for j in range(16):
        if j == 9:
            continue
        else:
            tuple1 = (i, j)
            tuple_list.append(tuple1)
                
b = 0
for i in range(26):
    b += a[i].count(0)
    
# print b

# random seed value being assigned          
# print
# print "The seed value is: ", seed
random.seed(seed)

random.shuffle(tuple_list)
# key = [[[tuple_list[random.sample(range(1920), 1920)] if a[i][j] == 1 else 0 for k in range(4)] for j in range(Y_SIZE)] for i in range(X_SIZE)]
count = 0
key = []
for i in range(X_SIZE):
    cols = []
    for j in range(Y_SIZE):
        third_dim = []
        for k in range(random.randint(2,5)):
            if a[i][j] == 1:
                third_dim.append(tuple_list[count])
                count += 1
            else:
                third_dim.append(0)
        cols.append(third_dim)
    key.append(cols)
    
letter_dict = {}
number_list = range(26)
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(number_list)):
    letter_dict[number_list[i]] = alphabet_list[i]

msg = ''

chunks = []
i = 0
for length in word_list_length:
    chunks.append(decrypted_notes[i: i + length])
    i += length

for i in range(len(chunks)):
    start = True
    for j in range(len(chunks[i])):
        ind = find(chunks[i][j], key)
        # print ind
    
        if start:
            msg += ' '
            msg += letter_dict[ind[1]]
            start = False
        elif ind == None:
            if chunks[i][j][0] == 33:
                msg += '!'
            elif chunks[i][j][0] == 44:
                msg += ','
            elif chunks[i][j][0] == 63:
                msg += '?'
            elif chunks[i][j][0] == 58:
                msg += ':'
            elif chunks[i][j][0] == 59:
                msg += ';'
            else:
                msg += '.'
        else:
            msg += letter_dict[ind[1]]

print            
print "The decrypted message is:" + msg
print
