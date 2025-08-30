# AISE 2026
# Let’s get started with Python and Pandas!

import pandas as pd
import numpy as np

# Store passenger data of the Titanic
df = pd.DataFrame({
   "Name": [
      "Braund, Mr. Owen Harris",
      "Allen, Mr. William Henry",
      "Bonnell, Miss. Elizabeth",
   ],
   "Age": [22, 35, 58],
   "Sex": ["male", "male", "female"],
})

print(df)