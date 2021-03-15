def dot(arr1, arr2):
  res = 0
  for i in range(len(arr1)):
    res += arr1[i] * arr2[i]
  return res

def sign(x):
  return 1 if x > 0 else -1

# arr var = besar a1, a2, a3
# supp vecs = poin poin support vector
# supp vecs classes = kelas dari support vector (berurutan)
# new coordinate = koordinat baru
# signfunc = sign function
def predictKelas(arrVar, suppVecs, suppVecsClasses, newCoord, signFunc):
  res = 0
  rumus = "-----RUMUS: \n KELAS = SIGN(\n"
  for i in range(len(suppVecs)):
    res += arrVar[i] * suppVecsClasses[i] * dot(suppVecs[i], newCoord)
    rumus += f"\t {arrVar[i]} * {suppVecsClasses[i]} * dot({suppVecs[i]}, {newCoord}) + \n"
  # ditambah bias
  res += arrVar[-1]
  rumus += f"\t {arrVar[-1]} )"
  print(rumus)
  return signFunc(res)

arrVar = [0.157, -0.028, 0.065, -0.063]
suppVecs = [[1,6], [4,11], [7,6]]
suppVecsClasses = [1,1,-1]
newCoord = [8,12]
signFunc = sign
print(predictKelas(arrVar, suppVecs, suppVecsClasses, newCoord, signFunc))