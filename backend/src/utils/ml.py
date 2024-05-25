from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from concrete.ml.sklearn import LogisticRegression


current_state = {
    "1234": {
        # "name": "Peter",
        "submissions": [
            # {"bankid": 1, "bankname": "N25", "rating": "00"},
        ],
    }
}


def add_to_state(uid, submission):
    if uid not in current_state:
        current_state[uid] = {"submissions": []}
    current_state[uid]["submissions"].append(submission)
    return


def predict_score(uid):
    model = LogisticRegression()
    x, y = make_classification(n_samples=40, class_sep=2, n_features=5, random_state=42)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model.fit(x_train, y_train)
    model.compile(x_train)

    if uid not in current_state:
        return
    blob = str.join("", [submission["rating"] for submission in current_state[uid]["submissions"]])
    del current_state[uid]
    # return model.predict(blob)
    return ""
