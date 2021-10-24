# Import seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from seaborn.rcmod import set_palette

# Apply the default theme
sns.set_theme(style="whitegrid", palette="pastel")

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill",
    y="tip",
    col="time",
    hue="smoker",
    style="smoker",
    size="size",
)
sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")

plt.show()
