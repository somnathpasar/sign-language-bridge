import os
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier


DATASET_FOLDER = "dataset"

all_data = []


for file_name in os.listdir(DATASET_FOLDER):

    if file_name.endswith(".csv"):

        label = file_name.replace(".csv", "")

        file_path = os.path.join(
            DATASET_FOLDER,
            file_name
        )

        df = pd.read_csv(
            file_path,
            header=None
        )

        df["label"] = label

        all_data.append(df)


dataset = pd.concat(
    all_data,
    ignore_index=True
)


X = dataset.drop(
    "label",
    axis=1
)

y = dataset["label"]


model = RandomForestClassifier(
    n_estimators=100
)

model.fit(
    X,
    y
)


joblib.dump(
    model,
    "trained_model/sign_model.pkl"
)


print("Model trained successfully")
print("Classes:", model.classes_)