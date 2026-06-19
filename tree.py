from schema import feature, branch, features_branches, feature_IG
from entropy import get_entropy, information_gain


def piles(features: list[feature], play: list[str], indices: list[int]):
    parsed_features: list[features_branches] = []
    for feature in features:
        branches: list[branch] = []
        total = len(indices)
        values = []

        for i in indices:
            if feature["array"][i] not in values:
                values.append(feature["array"][i])

        for value in values:
            member_indices = [i for i in indices if feature["array"][i] == value]
            yes_no_arr = [play[i] for i in member_indices]

            branches.append(
                {
                    "value": value,
                    "numerator": len(member_indices),
                    "yes_no_arr": yes_no_arr,
                    "indices": member_indices,
                }
            )

        parsed_features.append(
            {"name": feature["name"], "total": total, "branches": branches}
        )

    return parsed_features


def majority(labels: list[str]):
    return "Yes" if labels.count("Yes") >= labels.count("No") else "No"


def build_tree(indices: list[int], features: list[feature], play: list[str]):
    labels = [play[i] for i in indices]
    entropy = get_entropy(labels)

    if entropy == 0:
        return labels[0]
    if not features:
        return majority(labels)

    parsed_features = piles(features, play, indices)

    features_IG: list[feature_IG] = []
    for f in parsed_features:
        IG = information_gain(entropy, f["branches"], f["total"])
        features_IG.append({"name": f["name"], "IG": IG})

    next_node = max(features_IG, key=lambda ig: ig["IG"])
    next_node_feature = next(f for f in parsed_features if f["name"] == next_node["name"])

    remaining = [f for f in features if f["name"] != next_node["name"]]

    tree = {"feature": next_node["name"], "branches": {}}
    for branch in next_node_feature["branches"]:
        tree["branches"][branch["value"]] = build_tree(branch["indices"], remaining, play)

    return tree


def model(features: list[feature], play: list[str]):
    indices = list(range(len(play)))
    tree = build_tree(indices, features, play)
    return tree


def predict(tree, day):
    steps = []
    node = tree
    while not isinstance(node, str):
        feature = node["feature"]
        value = day[feature]
        steps.append(feature + "=" + value)
        node = node["branches"][value]
    return steps, node
