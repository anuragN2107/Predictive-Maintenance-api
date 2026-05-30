import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np
X = np.random.rand(100, 7)
y = np.random.randint(0, 2, 100)
model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)
joblib.dump(model, 'predictive_maintenance_rf.pkl')
print('New predictive_maintenance_rf.pkl created successfully!')
