class TreeNode:
    def __init__(self, feature=None, value=None, result=None, left=None, right=None):
        self.feature = feature  # Feature to split on
        self.value = value      # Value to compare
        self.result = result    # Result if leaf node
        self.left = left        # Left child
        self.right = right      # Right child


def build_decision_tree(data):
    # Assuming data is a list of dictionaries, where each dictionary represents a data point with features and label
    # For example: [{'color': 'red', 'size': 'small', 'texture': 'smooth', 'label': 'apple'}, ...]

    # If all labels are the same, create a leaf node
    labels = [point['label'] for point in data]
    if len(set(labels)) == 1:
        return TreeNode(result=labels[0])

    # If no features left, create a leaf node with the majority label
    if len(data[0].keys()) == 1:
        return TreeNode(result=max(set(labels), key=labels.count))

    # Find the best feature and value to split on
    best_feature = None
    best_value = None
    best_gain = 0

    for feature in data[0].keys():
        unique_values = set(point[feature] for point in data)
        for value in unique_values:
            left_data = [point for point in data if point[feature] == value]
            right_data = [point for point in data if point[feature] != value]
            gain = information_gain(left_data, right_data, labels)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_value = value

    if best_gain == 0:
        return TreeNode(result=max(set(labels), key=labels.count))

    # Split data and build subtrees
    left_data = [point for point in data if point[best_feature] == best_value]
    right_data = [point for point in data if point[best_feature] != best_value]
    left_child = build_decision_tree(left_data)
    right_child = build_decision_tree(right_data)

    return TreeNode(feature=best_feature, value=best_value, result=None, left=left_child, right=right_child)


def classify(tree, data_point):
    if tree.result is not None:
        return tree.result

    if data_point[tree.feature] == tree.value:
        return classify(tree.left, data_point)
    else:
        return classify(tree.right, data_point)


def gini_impurity(labels):
    total_samples = len(labels)
    class_counts = {label: labels.count(label) for label in set(labels)}
    impurity = 1
    for count in class_counts.values():
        impurity -= (count / total_samples) ** 2
    return impurity

def information_gain(left_data, right_data, labels):
    p = len(left_data) / (len(left_data) + len(right_data))
    return gini_impurity(labels) - p * gini_impurity([point['label'] for point in left_data]) - (1 - p) * gini_impurity([point['label'] for point in right_data])


def run_decision_tree_example():
    data = [
        {'color': 'red', 'size': 'small', 'texture': 'smooth', 'label': 'apple'},
        {'color': 'yellow', 'size': 'large', 'texture': 'bumpy', 'label': 'banana'},
        # Add more data points as needed
    ]

    tree = build_decision_tree(data)

    # Classify a new data point
    new_data_point = {'color': 'red', 'size': 'small', 'texture': 'smooth'}
    predicted_label = classify(tree, new_data_point)
    print(f"The predicted label is: {predicted_label}")

# Call the function
run_decision_tree_example()