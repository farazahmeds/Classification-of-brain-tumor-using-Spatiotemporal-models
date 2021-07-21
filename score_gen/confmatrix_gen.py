import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


labels = ['LGG', 'HGG', 'Healthy']

c = ([[399  , 1767 , 138],
       [306   , 7033  , 149],
       [61 , 148 , 6991]])

# c = ([[854, 417, 1],
#        [269, 3862, 3],
#        [12, 30, 3933]])

c=np.asarray(c)
group_names = ['LGG', 'HGG', 'Healthy']

k = c / c.astype(np.float).sum(axis=1)
# print (k)

df_cm = pd.DataFrame(k, index = [i for i in "ABC"],
                  columns = [i for i in "ABC"])
plt.figure(figsize = (3,3))
sns.heatmap(df_cm,  annot=True, fmt='.2%', cmap='Blues')

plt.show()

#

def plot_confusion_matrix(cm,
                          target_names,
                          title='R(2+1)D without data augmentation',
                          cmap=None,
                          normalize=True):
    """
    given a sklearn confusion matrix (cm), make a nice plot

    Arguments
    ---------
    cm:           confusion matrix from sklearn.metrics.confusion_matrix

    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']

    title:        the text to display at the top of the matrix

    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues

    normalize:    If False, plot the raw numbers
                  If True, plot the proportions

    Usage
    -----
    plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
                                                              # sklearn.metrics.confusion_matrix
                          normalize    = True,                # show proportions
                          target_names = y_labels_vals,       # list of names of the classes
                          title        = best_estimator_name) # title of graph

    Citiation
    ---------
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html

    """
    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / np.sum(cm).astype('float')
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(7, 5))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")


    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()

alpha= ['LGG', 'HGG', 'Healthy']

plot_confusion_matrix(c, target_names=alpha)

tp_and_fn = k.sum(1)
tp_and_fp = k.sum(0)
tp = k.diagonal()

precision = tp / tp_and_fp
recall = tp / tp_and_fn
# SPC = TN / (FP + TN)

print (precision)

print (recall)

fscore = 2*precision*recall / (precision + recall)
print (fscore)

#########################################################3
k = pd.DataFrame(k)

FP = k.sum(axis=0) - np.diag(k)
FN = k.sum(axis=1) - np.diag(k)
TP = np.diag(k)
TN = k.values.sum() - (FP + FN + TP)

# Sensitivity, hit rate, recall, or true positive rate
TPR = TP/(TP+FN)
# Specificity or true negative rate
TNR = TN/(TN+FP)
# Precision or positive predictive value
PPV = TP/(TP+FP)
# Negative predictive value
NPV = TN/(TN+FN)
# Fall out or false positive rate
FPR = FP/(FP+TN)
# False negative rate
FNR = FN/(TP+FN)
# False discovery rate
FDR = FP/(TP+FP)

# Overall accuracy
ACC = (TP+TN)/(TP+FP+FN+TN)

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# print (PPV)
#
# print (FNR)


print (TNR)
