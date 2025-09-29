import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data= pd.read_csv('/content/DataBase.csv')
data = {
    'Class': unit_class,
    'HP': hp,
    'ATK': atk,
    'DEF': defense,
    'Cost': cost,
    'RES': res,
    'BLK': blk,
    'RDP': rdp,
    'SPE': spe,
}
df = pd.DataFrame(data)

X = df.drop(['Class', 'Sub_Class'], axis=1) 
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Predict new operator
new_hp = int(input("Input predicting operator hp stat: "))
new_atk = int(input("Input predicting operator attack stat: "))
new_defense = int(input("Input predicting operator defense stat: "))
new_cost = int(input("Input predicting operator cost stat: "))
new_res = float(input("Input predicting operator resistance stat: "))
new_blk = int(input("Input predicting operator block stat: "))
new_rdp = int(input("Input predicting operator redeploy time stat: "))
new_spe = float(input("Input predicting operator attack speed: "))

new_stats = [new_hp, new_atk, new_defense, new_res, new_rdp, new_cost, new_blk, new_spe]

# Reorder to match training features
new_stats_ordered = [new_hp, new_atk, new_defense, new_res, new_rdp, new_cost, new_blk, new_spe]

predicted_class = clf.predict([new_stats_ordered])
print("Predicted Class:", predicted_class[0])
