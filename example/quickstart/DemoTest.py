import os
from random import random
import mlflow
from mlflow import log_metric, log_param, log_artifacts

if __name__ == "__main__":
    print("Running test.py")
    mlflow.set_tracking_uri('..\\')

    log_param("param1", 5)
    
    log_metric("foo", random())
    log_metric("foo", random() + 1)
    log_metric("foo", random() + 2)

    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world!")

    log_artifacts("outputs")
