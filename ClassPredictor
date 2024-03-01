import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Assuming you have your data in separate lists
data = {
    'Class': unit_classes,
    'HP': hp,
    'ATK': atk,
    'DEF': defense,
    'Cost': cost,
    'RES': res,
    'BLK': blk,
    'RDP': rdp,
    'SPE': spe,
}

# Create a DataFrame
df = pd.DataFrame(data)

# Extract features (X) and labels (y)
X = df.drop('Class', axis=1)
y = df['Class']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the classifier
clf = RandomForestClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Predict the classes for the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

new_hp = int(input("Input predicting operator hp stat: "))   
new_atk = int(input("Input predicting operator attack stat: "))  
new_defense = int(input("Input predicting operator defense stat: "))  
new_cost = int(input("Input predicting operator cost stat: "))  
new_res = int(input("Input predicting operator resistance stat: "))  
new_blk = int(input("Input predicting operator block stat: "))  
new_rdp = int(input("Input predicting operator redeploy time stat: "))  
new_spe = float(input("Input predicting operator attack speed: ")) 

# Recommend using on colab
new_stats = [new_hp, new_atk, new_defense, new_cost, new_res, new_blk, new_rdp, new_spe]
predicted_class = clf.predict([new_stats])
print("Predicted Class:", predicted_class)
