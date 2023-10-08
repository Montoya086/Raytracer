import math

def nMatMult(mats):
    res = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
    
    for mat in mats:
        res = matMult(res,mat)
    return res

def matMult(m1,m2):
    res = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    for x in range(4):
        for y in range(4):
            for i in range(4):
                res[x][y] += m1[x][i] * m2[i][y]
    return res

def matVectMult(mat, vect):
    res = [0,0,0,0]
    for x in range(4):
        for y in range(4):
                res[x] += mat[x][y] * vect[y]
    return res

#baricentric coordinates

def barycentricCoords(A, B, C, P):
    areaPCB = (B[1]-C[1])*(P[0]-C[0])+(C[0]-B[0])*(P[1]-C[1])
    
    areaACP = (C[1]-A[1])*(P[0]-C[0])+(A[0]-C[0])*(P[1]-C[1])
    
    areaABC = (B[1]-C[1])*(A[0]-C[0])+(C[0]-B[0])*(A[1]-C[1])

    try:
        u= areaPCB/areaABC
        v= areaACP/areaABC
        w= 1-u-v
        return u,v,w
    except:
        return -1,-1,-1


#inverse of a matrix

def subMat(mat, row, col):
    #obtain the submatrix of a matrix
    return [row[:col] + row[col + 1:] for row in (mat[:row] + mat[row + 1:])]

def matCofact(mat, row, col):
    #obtain the cofactor of a matrix
    return (-1) ** (row + col) * matDet(subMat(mat, row, col))

def matDet(mat):
    n = len(mat)
    # base case for 2x2 matrix
    if(n == 1):
        return mat[0][0]
    # case for 3x3 matrix
    if(n == 2):
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    det = 0
    # case for any larger square matrix
    for col in range(n):
        det += mat[0][col] * matCofact(mat, 0, col)
    return det

def matTranspose(mat):
    #obtain the transpose of a matrix
    return [[mat[j][i] for j in range( len(mat))] for i in range(len(mat[0] ))]

def inverseMat(mat):
    #obtain the inverse of a matrix
    det = matDet(mat)
    #check if the matrix is singular
    if(det== 0):
        raise ValueError("Can't find inverse of singular matrix (Determinant is 0)")
    n = len(mat)
    #adjugate matrix
    adjMatrix = [[matCofact(mat, i, j) for j in range(n)] for i in range(n)]
    adjMatrix = matTranspose(adjMatrix)
    #inverse matrix
    invMatrix = [[adjMatrix[i][j] / det for j in range(n)] for i in range(n)]
    return invMatrix

def subVec(v0, v1):
    #substraction of two vectors
    return (v0[0]-v1[0], v0[1]-v1[1], v0[2]-v1[2])

def addVec(v0, v1):
    #addition of two vectors
    return (v0[0]+v1[0], v0[1]+v1[1], v0[2]+v1[2])

def normVec(v):
    vectorList = list(v)
    #obtain the magnitude of the vector
    mag = math.sqrt(sum(comp ** 2 for comp in vectorList))
    #check if the magnitude is 0
    if mag == 0:
        raise ValueError("Can't normalize the zero vector")
    #normalize the vector
    normVector = [comp / mag for comp in vectorList]
    #convert to tuple
    normVector = tuple(normVector)
    return normVector

def magVec(v):
    vectorList = list(v)
    #obtain the magnitude of the vector
    return math.sqrt(sum(comp ** 2 for comp in vectorList))

def crossProd(v0, v1):
    #cross product of two vectors
    x = v0[1]*v1[2] - v0[2]*v1[1]
    y = v0[2]*v1[0] - v0[0]*v1[2]
    z = v0[0]*v1[1] - v0[1]*v1[0]
    return (x,y,z)

def dotProd(v0, v1):
    vect0 = list(v0)
    vect1 = list(v1)
    #dot product of two vectors
    return sum((a*b) for a, b in zip(vect0, vect1))

def negativeTuple(t):
    #negative of a tuple
    return (-t[0],-t[1],-t[2])

def escMultVector(s, v):
    #scalar multiplication of a vector
    result = [s * x for x in v]
    return result

def vectorDivEsc(v, s):
    #division of a vector by a scalar
    result = [x / s for x in v]
    return result

def rotateVec(vec, rotation):
    x, y, z = vec
    rx = math.radians(rotation[0])
    ry = math.radians(rotation[1])
    rz = math.radians(rotation[2])
    sinx, cosx = math.sin(rx), math.cos(rx)
    siny, cosy = math.sin(ry), math.cos(ry)
    sinz, cosz = math.sin(rz), math.cos(rz)

    # Apply rotation around x-axis
    y, z = y * cosx - z * sinx, y * sinx + z * cosx

    # Apply rotation around y-axis
    x, z = x * cosy + z * siny, x * -siny + z * cosy

    # Apply rotation around z-axis
    x, y = x * cosz - y * sinz, x * sinz + y * cosz

    return (x, y, z)