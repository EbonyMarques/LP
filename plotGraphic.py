import matplotlib.pyplot as plt

def plotGraphic(a,b,c,d):
    names = ['SVM(1,1)', 'Naive(1,1)', 'SVM(1,4)', 'Naive(1,4)']
    values = [a,b,c,d]

    #plt.figure(figsize=(2, 2))

    #plt.subplot(131)
    plt.bar(names, values)
    plt.suptitle('F-measure')
    plt.yticks([0.905, 0.910, 0.915, 0.920, 0.925, 0.930, 0.935, 0.940, 0.945, 0.950])
    plt.ylim(bottom=0.9)  # this line
    plt.show()

#, 'Precisão SVM', 'Precisão Naive', 'F-measure SVM', 'F-measure Naive'
 
