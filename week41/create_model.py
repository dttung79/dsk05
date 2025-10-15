"""Train a RandomForest model (using ApplicantIncome and LoanAmount)
and save it to Random_Forest.sav in the same folder.

Usage: python3 create_model.py
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os


def load_and_prepare(path='loan_dataset.csv'):
    df = pd.read_csv(path)
    # keep only the two features expected by tut09.py
    # Ensure numeric and drop rows with missing target or features
    df = df[['ApplicantIncome', 'LoanAmount', 'Loan_Status']].copy()
    df['LoanAmount'] = pd.to_numeric(df['LoanAmount'], errors='coerce')
    df = df.dropna(subset=['ApplicantIncome', 'LoanAmount', 'Loan_Status'])
    # map target: Y -> 1, N -> 0
    df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})
    df = df.dropna(subset=['Loan_Status'])
    X = df[['ApplicantIncome', 'LoanAmount']].values
    y = df['Loan_Status'].astype(int).values
    return X, y


def train_and_save(X, y, out_path='Random_Forest.sav'):
    print('Training RandomForest model...')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f'Training complete — test accuracy: {acc:.4f}')
    print('\nClassification report:\n', classification_report(y_test, preds))
    with open(out_path, 'wb') as f:
        pickle.dump(clf, f)
    print(f'Model saved to: {os.path.abspath(out_path)}')


def main():
    csv_path = 'loan_dataset.csv'
    if not os.path.exists(csv_path):
        raise SystemExit(f"Required dataset not found: {csv_path}. Place loan_dataset.csv in this folder.")
    X, y = load_and_prepare(csv_path)
    if len(y) < 10:
        raise SystemExit('Not enough data after cleaning to train a model.')
    train_and_save(X, y, out_path='Random_Forest.sav')


if __name__ == '__main__':
    main()
