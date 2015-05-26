__author__ = 'Ralph'

import os

import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

from pyminer.network.base import Node
from pyminer.network.base import InputPort
from pyminer.network.base import OutputPort


class Classifier(Node):

    def __init__(self, name):

        super(Classifier, self).__init__(name)
        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='model', data_type=str))
        self.add_output_port(
            OutputPort(name='performance', data_type=float))


class SupportVectorMachine(Classifier):

    def __init__(self):

        super(SupportVectorMachine, self).__init__('SupportVectorMachine')
        self.set_required_config_items(['kernel_type', 'target'])
        self._kernel_types = ['linear', 'rbf']

    def execute(self):

        self.check_config()

        # Get data from input port
        data = self.get_input_port('input').get_data()
        if data is None:
            return

        # Get SVM kernel type. Only 'linear' and 'rbf' are currently supported
        kernel_type = self.get_config().get('kernel_type')
        if kernel_type not in self._kernel_types:
            raise RuntimeError('Kernel type ' + kernel_type + ' not supported')

        # Check if hyper parameters should be auto-detected or not. For the
        # RBF kernel we need a C and gamma parameter. For the linear kernel
        # only the C parameter needs to be optimized
        auto_detect = self.get_config().get_bool('auto_detect', True)

        # Get target feature name
        target = self.get_config().get('target')
        if target is None:
            raise RuntimeError('Property \'target\' missing')

        # Get performance measure to calculate
        perf_measure = self.get_config().get('performance_measure')
        if perf_measure is None:
            print('WARNING: no performance measure configured, using accuracy')
            perf_measure = 'accuracy'

        # Get nr. grid search CV folds. Set to 5 if not configured
        n_grid_folds = self.get_config().get_int('n_grid_folds', 5)

        # Check if target feature exists in input data
        if target not in data.columns:
            raise RuntimeError('Feature \'' + target + '\' does not exist')

        # Split data into X,y
        predictors = list(data.columns)
        predictors.remove(target)
        X = data[predictors].as_matrix()
        y = data[target].as_matrix()

        C = 1
        gamma = 0

        if kernel_type == 'rbf':

            if auto_detect:

                grid_search = GridSearchCV(
                    estimator=SVC(),
                    param_grid=self._get_param_grid(kernel_type),
                    scoring=perf_measure,
                    cv=n_grid_folds,
                    refit=True)
                grid_search.fit(X, y)
                C = grid_search.best_params_['C']
                gamma = grid_search.best_params_['gamma']

            else:

                C = self.get_config().get_float('C')
                if C is None:
                    raise RuntimeError('Property \'C\' missing')

                gamma = self.get_config().get_float('gamma')
                if gamma is None:
                    raise RuntimeError('Property \'gamma\' missing')

        elif kernel_type == 'linear':

            if auto_detect:

                grid_search = GridSearchCV(
                    estimator=SVC(),
                    param_grid=self._get_param_grid(kernel_type),
                    scoring=perf_measure,
                    cv=n_grid_folds,
                    refit=True)
                grid_search.fit(X, y)
                C = grid_search.best_params_['C']

            else:

                C = self.get_config().get_float('C')
                if C is None:
                    raise RuntimeError('Property \'C\' missing')
        else:
            raise RuntimeError('Unknown kernel type \'' + kernel_type + '\'')

        # Get nr. cross validation folds to estimate performance
        n_folds = self.get_config().get_int('n_folds', 10)

        # Train SVM on cross-validated data to estimate its performance. If the
        # hyper parameters were given, use these. If not, apply grid search in
        # each fold before calculating the score.
        scores = []

        for i, (train, test) in enumerate(StratifiedKFold(y, n_folds=n_folds)):

            if auto_detect:

                # Hyper parameters were already optimized earlier so just
                # plug them into the classifier
                classifier = SVC(kernel=kernel_type, C=C, gamma=gamma)
                classifier.fit(X[train], y[train])

            else:

                # Optimize hyper parameter to get most realistic
                # generalization performance
                classifier = GridSearchCV(
                    estimator=SVC(kernel=kernel_type),
                    param_grid=self._get_param_grid(kernel_type),
                    cv=n_grid_folds,
                    refit=True)
                classifier.fit(X[train], y[train])

            # Calculate performance measure
            y_pred = classifier.predict(X[test])
            y_true = y[test]
            score = accuracy_score(y_true, y_pred)
            scores.append(score)

        # Calculate mean performance score
        mean_score = np.mean(np.asarray(scores))

        # Train SVM model on the full data set
        if auto_detect:

            classifier = GridSearchCV(
                estimator=SVC(kernel=kernel_type),
                param_grid=self._get_param_grid(kernel_type),
                cv=5,
                refit=True)
            classifier.fit(X, y)

        else:

            classifier = SVC(kernel=kernel_type, C=C, gamma=gamma)
            classifier.fit(X, y)

        # Save model to output if configured to do so
        model_output_dir = self.get_config().get('model_output_dir')
        if model_output_dir is not None:

            if model_output_dir.endswith(os.sep):
                model_output_dir = model_output_dir[:1]

            if not os.path.isdir(model_output_dir):
                os.makedirs(model_output_dir)

            model_output_file = os.path.join(model_output_dir, 'classifier.pkl')
            joblib.dump(classifier, model_output_file)
            self.get_output_port('model').set_data(model_output_file)

        # Set output port performance data
        self.get_output_port('performance').set_data(mean_score)

    @staticmethod
    def _get_param_grid(kernel):
        """
        Returns parameter grid for given classifier name, or None
        if classifier is not supported.
        :param kernel: Kernel type
        :return: Parameters
        """
        if kernel == 'linear':
            return [{
                'C': [2**x for x in range(-5, 15, 2)],
                'kernel': ['linear']}]
        if kernel == 'rbf':
            return [{
                'C': [2**x for x in range(-5, 15, 2)],
                'gamma': [2**x for x in range(-15, 4, 2)],
                'kernel': ['rbf']}]
        return None

    @staticmethod
    def _calculate_score(perf_measure, y_true, y_pred):
        """
        Calculates score of performance measure using true and predicted labels.
        Some scores, like accuracy, precision and recall are natively
        supported by SciKit Learn. Others like sensitivity need to
        manually calculated from the confusion matrix.
        :param perf_measure: Performance measure
        :param y_true: True labels
        :param y_pred: Predicted labels
        :return: Score
        """
        if perf_measure == 'accuracy':
            return accuracy_score(y_true, y_pred)

        if perf_measure == 'precision':
            return precision_score(y_true, y_pred)

        if perf_measure == 'recall':
            return recall_score(y_true, y_pred)

        if perf_measure == 'f1_score':
            return f1_score(y_true, y_pred)

        cm = confusion_matrix(y_true, y_pred)
        tp = float(cm[0][0])
        tn = float(cm[1][1])
        fp = float(cm[1][0])
        fn = float(cm[0][1])

        if perf_measure == 'sensitivity':
            sensitivity = tp / (tp + fn)
            return sensitivity

        if perf_measure == 'specificity':
            specificity = tn / (tn + fp)
            return specificity

        if perf_measure == 'likelihood_ratio':
            sensitivity = tp / (tp + fn)
            specificity = tn / (tn + fp)
            return sensitivity / (1 - specificity)

        raise RuntimeError('Unsupported performance measure ' + perf_measure)


class ApplyModel(Node):

    def __init__(self):

        super(ApplyModel, self).__init__('ApplyModel')
        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_input_port(
            InputPort(name='model', data_type=str))
        self.add_output_port(
            OutputPort(name='output', data_type=pd.Series))

    def execute(self):

        self.check_config()

        data = self.get_input_port('input').get_data()
        if data is None:
            return

        model_input_file = self.get_input_port('model').get_data()
        if model_input_file is None:
            return

        # Load classifier from file
        classifier = joblib.load(model_input_file)

        # Perform prediction on each example in X
        X = data.as_matrix()
        y_pred = pd.Series(classifier.predict(X))

        # Set output port data
        self.get_output_port('output').set_data(y_pred)