{
  "metadata": {
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    },
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "l = [[1, 2], [3, 4], [5, 6, 7]]\nl.reverse()\nfor i in range(len(l)):\n    (l[i])=(l[i])[::-1]\n\nprint(l)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 2,
      "outputs": [
        {
          "name": "stdout",
          "text": "[[7, 6, 5], [4, 3], [2, 1]]\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "l2 = [[1,2], [3,4], [5,6,7],[8,9,10]]\nl2.reverse()\nfor i in range(len(l2)):\n    (l2[i])=(l2[i])[::-1]\nprint(l2)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 5,
      "outputs": [
        {
          "name": "stdout",
          "text": "[[10, 9, 8], [7, 6, 5], [4, 3], [2, 1]]\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    }
  ]
}
