import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

engine = create_engine(
    "mysql+pymysql://root:Oppk%402003@localhost/telecom_etl"
)

df = pd.read_sql(
    "SELECT * FROM telecom_network_data",
    engine
)

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Weather Values:")
print(df['weather'].unique())

print("\nCongestion Distribution:")
print(df['congestion'].value_counts())
# Convert timestamp to datetime

df['timestamp'] = pd.to_datetime(df['timestamp'])

# Create time features

df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.day
df['month'] = df['timestamp'].dt.month
df['day_of_week'] = df['timestamp'].dt.dayofweek

print(df[['timestamp','hour','day','month','day_of_week']].head())
le = LabelEncoder()

df['weather_encoded'] = le.fit_transform(df['weather'])

print(df[['weather', 'weather_encoded']].drop_duplicates())
# Create ML-ready dataset

df_clean = df.drop(
    columns=['timestamp', 'weather']
)

print(df_clean.head())
print("\nShape:", df_clean.shape)
print("\nColumns:")
print(df_clean.columns)
print(df_clean.dtypes)


X = df_clean.drop('congestion', axis=1)

y = df_clean['congestion']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
predictions_df = X_test.copy()

predictions_df['actual_congestion'] = y_test.values
predictions_df['predicted_congestion'] = y_pred

print(predictions_df.head())
df_clean.to_sql(
    'clean_network_data',
    engine,
    if_exists='replace',
    index=False
)
predictions_df.to_sql(
    'network_predictions',
    engine,
    if_exists='replace',
    index=False
)
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by='Importance',
    ascending=False
)

print(feature_importance)