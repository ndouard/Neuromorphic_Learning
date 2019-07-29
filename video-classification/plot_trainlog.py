"""
Given a training log file, plot something.
"""
import csv
import matplotlib.pyplot as plt

def main(training_log):
    with open(training_log) as fin:
        reader = csv.reader(fin)
        next(reader, None)  # skip the header
        train_accuracies = []
        test_accuracies = []
        # top_5_accuracies = []
        cnn_benchmark = []  # this is ridiculous
        for epoch,acc,loss,val_acc,val_loss in reader:
            test_accuracies.append(float(val_acc))
            train_accuracies.append(float(acc))
            cnn_benchmark.append(0.25)  # ridiculous
        fig = plt.figure()
        plt.plot(test_accuracies, '-g', label='Test')
        plt.plot(train_accuracies, '-b', label='Train')
        plt.plot(cnn_benchmark, '--r')
        fig.suptitle('Model Accuracy', fontsize=20)
        plt.xlabel('Epoch', fontsize=18)
        plt.ylabel('Accuracy', fontsize=16)
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()

if __name__ == '__main__':
    training_log = 'data/logs-seq_length=1000-patience=20/lstm-training-1525650286.9679956.log'
    main(training_log)
