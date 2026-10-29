 
# Decision Tree using ID3
 
import math
import matplotlib.pyplot as plt
 
# Dataset: Size, Orbit, Habitable, Count
data = [
    ("Big", "Near", "Yes", 20),
    ("Big", "Far", "Yes", 170),
    ("Small", "Near", "Yes", 139),
    ("Small", "Far", "Yes", 45),
    ("Big", "Near", "No", 130),
    ("Big", "Far", "No", 30),
    ("Small", "Near", "No", 11),
    ("Small", "Far", "No", 255)
]
 
# Calculate entropy
def entropy(yes, no):
    total = yes + no
    result = 0
 
    for count in [yes, no]:
        if count > 0:
            probability = count / total
            result -= probability * math.log2(probability)
 
    return result
 
# Calculate total counts
yes_total = sum(row[3] for row in data if row[2] == "Yes")
no_total = sum(row[3] for row in data if row[2] == "No")
total = yes_total + no_total
 
base_entropy = entropy(yes_total, no_total)
 
# Calculate information gain
def information_gain(attribute_index):
    groups = {}
 
    for row in data:
        attribute = row[attribute_index]
 
        if attribute not in groups:
            groups[attribute] = [0, 0]
 
        if row[2] == "Yes":
            groups[attribute][0] += row[3]
        else:
            groups[attribute][1] += row[3]
 
    weighted_entropy = 0
 
    for yes, no in groups.values():
        count = yes + no
        weighted_entropy += (
            count / total
        ) * entropy(yes, no)
 
    return base_entropy - weighted_entropy
 
 
# Display calculations
size_gain = information_gain(0)
orbit_gain = information_gain(1)
 
print("PLANET HABITABILITY - ID3")
print("-------------------------")
print("Total planets:", total)
print("Habitable:", yes_total)
print("Inhabitable:", no_total)
print("Dataset Entropy:", round(base_entropy, 5))
print("Information Gain (Size):", round(size_gain, 5))
print("Information Gain (Orbit):", round(orbit_gain, 5))
 
# Prediction function
def predict(size, orbit):
    counts = {
        ("Big", "Near"): (20, 130),
        ("Big", "Far"): (170, 30),
        ("Small", "Near"): (139, 11),
        ("Small", "Far"): (45, 255)
    }
 
    yes, no = counts[(size, orbit)]
    return "Yes" if yes > no else "No"
 
 
print("\nPREDICTIONS")
print("Big, Far:", predict("Big", "Far"))
print("Small, Near:", predict("Small", "Near"))
 
 
# -------------------------------------
# DRAW THE DECISION TREE USING MATPLOTLIB
# -------------------------------------
 
fig, ax = plt.subplots(figsize=(13, 8))
 
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis("off")
 
# Draw a node with a box and text
def draw_node(x, y, text, color="#DCEAFE",
              width=1.8, height=0.65,
              fontsize=10):
    ax.text(
        x, y, text,
        ha="center", va="center",
        fontsize=fontsize,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.5",
            facecolor=color,
            edgecolor="#2563A6",
            linewidth=1.5
        )
    )
 
# Draw a branch with its label
def draw_branch(x1, y1, x2, y2, label):
    ax.annotate(
        "",
        xy=(x2, y2 + 0.35),
        xytext=(x1, y1 - 0.35),
        arrowprops=dict(
            arrowstyle="->",
            color="black",
            linewidth=1.5
        )
    )
 
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
 
    ax.text(
        mid_x, mid_y,
        label,
        fontsize=10,
        fontweight="bold",
        ha="center",
        bbox=dict(facecolor="white", edgecolor="none")
    )
 
 
# Root node
draw_node(6, 9, "Size?")
 
# Second-level nodes
draw_node(3, 7, "Orbit?")
draw_node(9, 7, "Orbit?")
 
# Connect root to second-level nodes
draw_branch(6, 9, 3, 7, "Big")
draw_branch(6, 9, 9, 7, "Small")
 
# Leaf positions and their counts
leaves = [
    (1.5, "Near", "Yes: 20 | No: 130\nTotal: 150",
     "Prediction: No", "#F8D7DA"),
    (4.5, "Far", "Yes: 170 | No: 30\nTotal: 200",
     "Prediction: Yes", "#D4EDDA"),
    (7.5, "Near", "Yes: 139 | No: 11\nTotal: 150",
     "Prediction: Yes", "#D4EDDA"),
    (10.5, "Far", "Yes: 45 | No: 255\nTotal: 300",
     "Prediction: No", "#F8D7DA")
]
 
# Connect Orbit nodes to the four leaves
draw_branch(3, 7, 1.5, 4.5, "Near")
draw_branch(3, 7, 4.5, 4.5, "Far")
draw_branch(9, 7, 7.5, 4.5, "Near")
draw_branch(9, 7, 10.5, 4.5, "Far")
 
# Draw the leaf boxes
for x, orbit, counts, prediction, color in leaves:
    ax.text(
        x, 4.1,
        counts + "\n" + prediction,
        ha="center",
        va="center",
        fontsize=9,
        bbox=dict(
            boxstyle="round,pad=0.6",
            facecolor=color,
            edgecolor="#555555",
            linewidth=1.3
        )
    )
 
# Title and information gain
ax.set_title(
    "ID3 Decision Tree - Planet Habitability",
    fontsize=16,
    fontweight="bold",
    pad=20
)
 
ax.text(
    6, 1.8,
    f"Entropy = {base_entropy:.5f}\n"
    f"Information Gain (Size) = {size_gain:.5f}\n"
    f"Information Gain (Orbit) = {orbit_gain:.5f}",
    ha="center",
    va="center",
    fontsize=11,
    bbox=dict(
        boxstyle="round,pad=0.6",
        facecolor="#FFF3CD",
        edgecolor="#B8860B"
    )
)
 
plt.tight_layout()
plt.show()
 