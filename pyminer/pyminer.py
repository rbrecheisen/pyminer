__author__ = 'Ralph'

from ui.app import Application


if __name__ == '__main__':

    application = Application()
    application.run()

    # node1 = ImportARFF()
    # node2 = SelectAttributes()
    # node3 = SupportVectorMachine()
    # node4 = SelectAttributes()
    # node5 = ApplyModel()
    #
    # node1.get_config().set('file_name', '/Users/Ralph/datasets/imagemend/out/prepared/features_prepared.arff')
    #
    # node2.get_config().set('selector_type', 'subset')
    # node2.get_config().set('attributes', ['M', 'F', 'age', 'id'])
    #
    # node3.get_config().set('kernel_type', 'rbf')
    # node3.get_config().set('target', 'diagnosis')
    # node3.get_config().set('auto_detect', True)
    # node3.get_config().set('performance_measure', 'accuracy')
    # node3.get_config().set('n_folds', 2)
    # node3.get_config().set('n_grid_folds', 2)
    # node3.get_config().set('model_output_dir', '/Users/Ralph/tmp/model')
    #
    # node4.get_config().set('selector_type', 'single')
    # node4.get_config().set('attributes', ['diagnosis'])
    #
    # Connection(
    #     # ImportARFF -> SelectAttributes
    #     node1.get_output_port('output'), node2.get_input_port('input'))
    # Connection(
    #     # SelectAttributes -> SVM
    #     node2.get_output_port('output'), node3.get_input_port('input'))
    # Connection(
    #     # SelectAttributes -> SelectAttributes
    #     node2.get_output_port('output'), node4.get_input_port('input'))
    # Connection(
    #     # SelectAttributes -> ApplyModel
    #     node4.get_output_port('output'), node5.get_input_port('input'))
    # Connection(
    #     # SVM -> ApplyModel
    #     node3.get_output_port('model'), node5.get_input_port('model'))
    #
    # node1.execute()
    #
    # print('predictions: {}'.format(node5.get_output_port('output').get_data()))