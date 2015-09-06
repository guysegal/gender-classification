from sklearn import svm


def classify_with_svm(x_train, y_train, x_test, y_test):
    clf_svm = svm.SVC()
    clf_svm = clf_svm.fit(x_train, y_train)
    z_svm = clf_svm.predict(x_test)

    successful_predictions = 0
    total_predictions = len(y_test)
    for i in range(len(y_test)):
        if y_test[i] == z_svm[i]:
            successful_predictions += 1

    accuracy = float(successful_predictions) / total_predictions

    return accuracy



