"""
4 Quadrants Division Theory Classification

This script implements a classification algorithm based on the 4 Quadrants Division Theory.
It classifies individuals into four categories (Visual, Active, Logical, Traditional) based on
their reasons for using educational resources, rated by complexity and interactiveness.

Author: Irfan
Date: August 16, 2024
"""

import numpy as np
import matplotlib.pyplot as plt

# Reasons data from Image 2
reasons_data = {
    "Nice Visuals and Audio": {"complexity": 3, "interactiveness": 5},
    "Supplement to Class": {"complexity": 4, "interactiveness": 1},
    "Revise Old Topics": {"complexity": 2, "interactiveness": 2},
    "Relearn Class Topics": {"complexity": 4, "interactiveness": 3},
    "Learn Diverse Subjects": {"complexity": 5, "interactiveness": 2},
    "Get Expert Knowledge": {"complexity": 5, "interactiveness": 1},
    "Prepare for Tests": {"complexity": 3, "interactiveness": 1},
    "Practice Questions": {"complexity": 2, "interactiveness": 2},
    "Watch Practical Demonstrations": {"complexity": 4, "interactiveness": 4},
    "Connect with Communities": {"complexity": 4, "interactiveness": 5}
}

# Synthetic data for 5 individuals
individuals = [
    {"name": "Person A", "reasons": ["Nice Visuals and Audio", "Revise Old Topics", "Learn Diverse Subjects"]},
    {"name": "Person B", "reasons": ["Supplement to Class", "Prepare for Tests", "Connect with Communities"]},
    {"name": "Person C", "reasons": ["Relearn Class Topics", "Watch Practical Demonstrations", "Practice Questions"]},
    {"name": "Person D", "reasons": ["Get Expert Knowledge", "Nice Visuals and Audio", "Revise Old Topics"]},
    {"name": "Person E", "reasons": ["Learn Diverse Subjects", "Connect with Communities", "Watch Practical Demonstrations"]}
]

def classify_individual(individual):
    """
    Classifies an individual based on their average complexity and interactiveness scores.

    Args:
    individual (dict): A dictionary containing the individual's name and reasons.

    Returns:
    str: The quadrant classification (Logical, Visual, Traditional, or Active).
    """
    reasons = individual["reasons"]
    avg_complexity = np.mean([reasons_data[r]["complexity"] for r in reasons])
    avg_interactiveness = np.mean([reasons_data[r]["interactiveness"] for r in reasons])
    
    if avg_complexity < 3.5:
        if avg_interactiveness < 3:
            return "Logical"
        else:
            return "Visual"
    else:
        if avg_interactiveness < 3:
            return "Traditional"
        else:
            return "Active"

# Main execution
if __name__ == "__main__":
    plt.figure(figsize=(10, 8))
    colors = {'Logical': 'blue', 'Visual': 'green', 'Traditional': 'red', 'Active': 'purple'}

    for individual in individuals:
        avg_complexity = np.mean([reasons_data[r]["complexity"] for r in individual["reasons"]])
        avg_interactiveness = np.mean([reasons_data[r]["interactiveness"] for r in individual["reasons"]])
        quadrant = classify_individual(individual)
        
        plt.scatter(avg_complexity, avg_interactiveness, color=colors[quadrant], label=quadrant)
        plt.annotate(individual["name"], (avg_complexity, avg_interactiveness))

    plt.axhline(y=3, color='k', linestyle='--')
    plt.axvline(x=3.5, color='k', linestyle='--')
    plt.xlim(1, 5)
    plt.ylim(1, 5)
    plt.xlabel("Complexity")
    plt.ylabel("Interactiveness")
    plt.title("4 Quadrants Division Theory")
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.show()

    for individual in individuals:
        quadrant = classify_individual(individual)
        print(f"{individual['name']} is classified as: {quadrant}")