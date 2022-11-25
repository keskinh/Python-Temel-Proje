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
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]\nl2 = []\ndef flatten(n):\n    for i in n :\n        if isinstance(i,list):\n            flatten(i)\n        else:\n            l2.append(i)\n\nflatten(l)\nprint(l2)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 1,
      "outputs": [
        {
          "name": "stdout",
          "text": "[1, 'a', 'cat', 2, 3, 'dog', 4, 5]\n",
          "output_type": "stream"
        }
      ]
    }
  ]
}
