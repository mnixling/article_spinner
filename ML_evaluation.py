import sys
import warnings


import matplotlib.pyplot as plt
import pandas
from pandas import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# This is to suppress warnings
if not sys.warnoptions:
    warnings.simplefilter('ignore')

# Load dataset
with open('mc_feat_names.txt') as name_file:
    names = name_file.read().strip().split('\t')
len_names = len(names)
with open('mc_features.csv') as mc_file:
    dataset = pandas.read_csv(mc_file, names=names,  # pandas DataFrame object
                              keep_default_na=False, na_values=['_'])  # avoid 'NA' category being interpreted as missing data  # noqa
print(type(dataset))

with open('project_results.txt', 'a') as final_output:

    # Summarize the data
    print('"Shape" of dataset:', dataset.shape,
          '({} instances of {} attributes)'.format(*dataset.shape), file=final_output)
    print()
    print('"head" of data:\n', dataset, file=final_output)  # head() is a method of DataFrame
    print()
    print('Description of data:\n:', dataset.describe(), file=final_output)
    print(file=final_output)
    print('Class distribution:\n', dataset.groupby('REGISTER').size(), file=final_output)
    print(file=final_output)

    # Visualize the data
    print('Drawing boxplot...')
    grid_size = 0
    while grid_size ** 2 < len_names:
        grid_size += 1
    dataset.plot(kind='box', subplots=True, layout=(grid_size, grid_size),
                 sharex=False, sharey=False)
    fig = plt.gcf()  # get current figure
    fig.savefig('boxplots.png')

    # histograms
    print('Drawing histograms...')
    dataset.hist()
    fig = plt.gcf()
    fig.savefig('histograms.png')

    # scatter plot matrix
    print('Drawing scatterplot matrix...')
    scatter_matrix(dataset)
    fig = plt.gcf()
    fig.savefig('scatter_matrix.png')
    print()

    print('Splitting training/development set and validation set...', file=final_output)
    # Split-out validation dataset
    array = dataset.values  # numpy array
    feats = array[:, 0:len_names - 1]  # to understand comma, see url in next line:
    labels = array[:, -1]  # https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html#advanced-indexing
    print('\tfull original data ([:5]) and their respective labels:', file=final_output)
    print(feats[:5], labels[:5], sep='\n\n', end='\n\n\n', file=final_output)
    validation_size = 0.20
    seed = 7  # used to make 'random' choices the same in each run
    split = model_selection.train_test_split(feats, labels,
                                             test_size=validation_size,
                                             random_state=seed)
    feats_train, feats_validation, labels_train, labels_validation = split

    # Test options and evaluation metric
    print(file=final_output)

    print('Initializing models...', file=final_output)
    # Spot Check Algorithms
    models = [('LR', LogisticRegression()),
              ('LDA', LinearDiscriminantAnalysis()),
              ('KNN', KNeighborsClassifier()),
              ('CART', DecisionTreeClassifier()),
              ('NB', GaussianNB()),
              ('SVM', SVC())]
    print('Training and testing each model using 10-fold cross-validation...', file=final_output)
    # evaluate each model in turn
    results = []
    names = []
    for name, model in models:
        # https://chrisjmccormick.files.wordpress.com/2013/07/10_fold_cv.png
        kfold = model_selection.KFold(n_splits=10, random_state=seed)
        cv_results = model_selection.cross_val_score(model, feats_train,
                                                     labels_train, cv=kfold,
                                                     scoring='accuracy')
        results.append(cv_results)
        names.append(name)
        msg = '{}: {} ({})'.format(name, cv_results.mean(), cv_results.std())
        print(msg, file=final_output)
    print(file=final_output)

    print('Drawing algorithm comparison boxplots...', file=final_output)
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    fig = plt.gcf()
    fig.savefig('compare_algorithms.png')
    print(file=final_output)

    # Make predictions on validation dataset
    best_model = KNeighborsClassifier()
    best_model.fit(feats_train, labels_train)
    predictions = best_model.predict(feats_validation)
    print('Accuracy:', accuracy_score(labels_validation, predictions), file=final_output)
    print(file=final_output)
    print('Confusion matrix:', file=final_output)
    cm_labels = 'Real Fake'.split()
    print('labels:', cm_labels, file=final_output)
    print(confusion_matrix(labels_validation, predictions, labels=cm_labels), file=final_output)
    print(file=final_output)
    print('Classification report:', file=final_output)
    print(classification_report(labels_validation, predictions), file=final_output)
