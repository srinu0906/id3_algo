# id3_algo/id3.py

import pandas as pd

class Node:
    def __init__(self, feature=None, value=None, results=None, children=None):
        self.feature = feature
        self.value = value
        self.results = results
        self.children = children or {}

class ID3Classifier:
    def __init__(self):
        self.tree = None

    def fit(self, X, y):
        data = X.copy()
        data['label'] = y
        self.tree = self.build_tree(data)

    def predict(self, sample):
        node = self.tree
        while node.results is None:
            value = sample.get(node.feature)
            node = node.children.get(value)
            if node is None:
                return None
        return list(node.results.keys())[0]

    def build_tree(self, data):
        if len(data['label'].unique()) == 1:
            return Node(results={data['label'].iloc[0]: 1})

        if len(data.columns) == 1:
            return Node(results=dict(data['label'].value_counts()))

        best_feature = self.best_feature(data)
        tree = Node(feature=best_feature, children={})

        for value in data[best_feature].unique():
            subset = data[data[best_feature] == value]
            subset = subset.drop(columns=[best_feature])
            subtree = self.build_tree(subset)
            tree.children[value] = subtree

        return tree

    def best_feature(self, data):
        from math import log2

        def entropy(labels):
            probs = labels.value_counts(normalize=True)
            return -sum(p * log2(p) for p in probs)

        base_entropy = entropy(data['label'])
        best_gain = 0
        best_feature = None

        for feature in data.columns.drop('label'):
            subsets = [data[data[feature] == value] for value in data[feature].unique()]
            weighted_entropy = sum((len(subset)/len(data)) * entropy(subset['label']) for subset in subsets)
            gain = base_entropy - weighted_entropy
            if gain > best_gain:
                best_gain = gain
                best_feature = feature

        return best_feature

    def visualize(self, node=None, indent=""):
        if node is None:
            node = self.tree
        if node.results:
            print(indent + str(node.results))
        else:
            print(indent + str(node.feature))
            for value, child in node.children.items():
                print(indent + f"->{value}:")
                self.visualize(child, indent + "  ")
