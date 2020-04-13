"""
This module contains plot functions in EDA and performance evaluation.
"""

import matplotlib.pyplot as plt


def plot_history(history, figsize=(10, 4)):
    """Plot the loss and accuracy during a NN training process.

       history: get from NNmodel.fit()."""

    history_dict = history.history
    loss_values = history_dict['loss']
    acc_values = history_dict['accuracy']
    val_loss_values = history_dict['val_loss']
    val_acc_values = history_dict['val_accuracy']

    epochs = range(1, len(acc_values) + 1)

    plt.figure(figsize=figsize)

    plt.subplot(121)
    plt.plot(epochs, loss_values, 'bo', label='Training loss')
    plt.plot(epochs, val_loss_values, 'b-', label='Validation loss')
    plt.title('Training and validattion loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.subplot(122)
    plt.plot(epochs, acc_values, 'bo', label='Training accuracy')
    plt.plot(epochs, val_acc_values, 'b-', label='Validation accuracy')
    plt.title('Training and validattion accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.tight_layout()
    plt.show()
