from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import fbeta_score, precision_score, recall_score


def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.
    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """
    random_forest_trainer = RandomForestClassifier(random_state=42, n_jobs=-1)

    random_forest_trainer.fit(X_train, y_train)

    return random_forest_trainer


def inference(model, X):
    """ Run model inferences and return the predictions.
    Inputs
    ------
    model : pkl
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    return model.predict(X)


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.
    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    f_beta : float
    """
    f_beta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, f_beta