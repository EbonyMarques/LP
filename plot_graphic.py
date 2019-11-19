import matplotlib.pyplot as plt

def plot_graphic(title, names, values, x_title, y_title):
    #plt.figure(figsize=(2, 2))
    #plt.subplot(131)
    plt.bar(names, values)
    plt.suptitle(title)
    plt.xlabel(x_title, fontsize=15)
    plt.ylabel(y_title, fontsize=13)
    #plt.yticks([0.905, 0.910, 0.915, 0.920, 0.925, 0.930, 0.935, 0.940, 0.945, 0.950])
    plt.ylim(bottom=0.9)  # this line
    plt.show()
#, 'Precisão SVM', 'Precisão Naive', 'F-measure SVM', 'F-measure Naive'
 
