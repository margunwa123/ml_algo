import numpy as np
class Sign:
  @staticmethod
  def defaultSign(x):
    return 1 if x > 0 else -1

class SVM:
  suppVecs = np.array([])
  suppVecsClasses = np.array([])
  coefficients = np.array([])
  hasCalcVars = False

  def __init__(self, suppVecs, suppVecsClasses):
    assert(len(suppVecs) == len(suppVecsClasses))
    self.suppVecs = np.array(suppVecs)
    self.suppVecsClasses = np.array(suppVecsClasses)
    self.calcVars()

  # someone pls clean this code, im too inexperienced to cleanse it
  def calcVars(self):
    sigmaXZero = [np.append(self.suppVecsClasses, 0)]
    linearEquations = np.array([
      [self.suppVecs[i].dot(self.suppVecs[j]) * self.suppVecsClasses[j] for j in range(len(self.suppVecs))] + [1] for i in range(len(self.suppVecs))
    ])
    linearEquations=  np.append(linearEquations, sigmaXZero, axis=0)
    print("-------Linear Equations:--------")
    print(linearEquations)
    #using np magic in https://stackabuse.com/solving-systems-of-linear-equations-with-pythons-numpy/
    self.coefficients = np.linalg.inv(linearEquations).dot(np.append( self.suppVecsClasses, 0))
    print("-------Coeficients:-------")
    print(self.coefficients)
    self.hasCalcVars = True


  # predict the value
  def predict(self, coord, signFunc=Sign.defaultSign):
    assert(self.hasCalcVars == True)
    res = 0
    rumus = "----- PREDIKSI------: \n KELAS = SIGN(\n"
    for i in range(len(self.suppVecs)):
      res += self.coefficients[i] * self.suppVecsClasses[i] * self.suppVecs[i].dot(coord)
      rumus += f"\t {self.coefficients[i]} * {self.suppVecsClasses[i]} * dot({self.suppVecs[i]}, {coord}) + \n"
    # ditambah bias
    res += self.coefficients[-1]
    rumus += f"\t {self.coefficients[-1]} ) = {signFunc(res)}"
    print(rumus)
    return signFunc(res)

if(__name__ == "__main__"):
  svm = SVM([[1,6], [4,11], [7,6]], [1,1,-1])
  svm.calcVars()
  kelas = svm.predict([8,12])