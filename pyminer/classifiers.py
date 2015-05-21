__author__ = 'Ralph'

import pandas as pd

from base import Node
from base import InputPort
from base import OutputPort

from sklearn.svm import SVC


class Classifier(Node):

    def __init__(self, name):

        super(Classifier, self).__init__(name)
        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='model', data_type=str))
        self.add_output_port(
            OutputPort(name='performance', data_type=str))


class SupportVectorMachine(Classifier):

    def __init__(self):

        super(SupportVectorMachine, self).__init__('SupportVectorMachine')
        self.set_required_config_items(['kernel_type', 'target'])
        self._kernel_types = ['linear', 'rbf']

    def execute(self):

        self.check_config()

        # Get SVM kernel type. Only 'linear' and 'rbf' are currently supported
        kernel_type = self.get_config().get('kernel_type')
        if kernel_type not in self._kernel_types:
            raise RuntimeError('Kernel type ' + kernel_type + ' not supported')

        # Check if hyperparameters should be auto-detected or not. For the
        # RBF kernel we need a C and gamma parameter. For the linear kernel
        # only the C parameter needs to be optimized
        auto_detect = self.get_config().get_bool('auto_detect', True)

        C = 1
        gamma = 0.001

        if kernel_type == 'rbg':
            if not auto_detect:
                C = self.get_config().get_float('kernel_type.rbf.C')
                if C is None:
                    raise RuntimeError('Property \'C\' missing')
                gamma = self.get_config().get_float('kernel_type.rbf.gamma')
                if gamma is None:
                    raise RuntimeError('Property \'gamma\' missing')
            else:
                pass
        elif kernel_type == 'linear':
            pass

        # Get target feature vector
        target = self.get_config().get('target')
        if target is None:
            raise RuntimeError('Property \'target\' missing')

        # Get data and check target feature exists
        data = self.get_input_port('input').get_data()
        if data is None:
            print('WARNING: no data')
            return
        if target not in data.columns:
            raise RuntimeError('Feature \'' + target + '\' does not exist')

        # Split data into X,y
        predictors = list(data.columns)
        predictors.remove(target)
        X = data[predictors].to_matrix()
        y = data[target].to_matrix()

        # Create SVM model based on given kernel type and hyperparameters
        if kernel_type == 'rbf':
            classifier = SVC(kernel='rbf', C=C, gamma=gamma)
            classifier.fit(X, y)
        elif kernel_type == 'linear':
            classifier = SVC(kernel='linear', C=C)
            classifier.fit(X, y)

class GaussianProcesses(Classifier):

    def __init__(self):

        super(GaussianProcesses, self).__init__('GaussianProcesses')

    def execute(self):
        pass


class RandomForests(Classifier):

    def __init__(self):

        super(RandomForests, self).__init__('RandomForests')

    def execute(self):
        pass