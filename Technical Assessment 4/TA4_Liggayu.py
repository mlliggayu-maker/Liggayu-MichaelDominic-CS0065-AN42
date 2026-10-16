# CS0065 - Intelligent Systems
# Technical Assessment 4
#Study recommendation system

# PART 1 - KNOWLEDGE REPRESENTATION


print("==========================================")
print("       STUDY RECOMMENDATION SYSTEM")
print("==========================================")

# Get the student's current study conditions
study_time = input("Enter study time (short/long): ").lower()
energy = input("Enter energy level (low/normal): ").lower()
difficulty = input("Enter difficulty (easy/normal/hard): ").lower()
focus = input("Enter focus level (low/normal/high): ").lower()
exam_near = input("Is the exam near? (yes/no): ").lower()

# Convert exam answer to True or False
if exam_near == "yes":
    exam_near = True
else:
    exam_near = False


# Knowledge Base
# Stores facts about the student's current study condition
facts = {
    "study_time": "short",
    "energy": "low",
    "difficulty": "hard",
    "focus": "low",
    "exam_near": True
}

print("KNOWLEDGE BASE")
print(facts)


# PART 2 - RULE-BASED REASONING


# Rule 1
def rule_short_time(facts):
    if facts["study_time"] == "short":
        return "Focus on the most important topics."


# Rule 2
def rule_low_energy(facts):
    if facts["energy"] == "low":
        return "Take a short break before studying."


# Rule 3
def rule_hard_subject(facts):
    if facts["difficulty"] == "hard":
        return "Study the difficult topics first."


# Rule 4
def rule_low_focus(facts):
    if facts["focus"] == "low":
        return "Study in a quiet place and remove distractions."


# Rule 5
def rule_exam_near(facts):
    if facts["exam_near"] == True:
        return "Review your notes and practice questions."


# Inference Engine
rules = [
    rule_short_time,
    rule_low_energy,
    rule_hard_subject,
    rule_low_focus,
    rule_exam_near
]

print("\nRULE-BASED REASONING")
print("Study Recommendations:")

for rule in rules:
    result = rule(facts)

    if result:
        print("-", result)



# PART 3 - CASE-BASED REASONING


# Past Cases
case_base = [

    {
        "problem": {
            "study_time": "short",
            "energy": "normal",
            "difficulty": "hard"
        },
        "solution": "Focus on the most important and difficult topics."
    },

    {
        "problem": {
            "study_time": "long",
            "energy": "low",
            "difficulty": "normal"
        },
        "solution": "Take breaks and study using shorter sessions."
    },

    {
        "problem": {
            "study_time": "short",
            "energy": "low",
            "difficulty": "hard"
        },
        "solution": "Take a short break, then focus on the difficult topics."
    }
]


# New Problem
new_problem = {
    "study_time": "short",
    "energy": "low",
    "difficulty": "hard"
}


# RETRIEVE


best_case = None
highest_score = 0

for case in case_base:

    score = 0

    for feature in new_problem:

        if new_problem[feature] == case["problem"][feature]:
            score += 1

    if score > highest_score:
        highest_score = score
        best_case = case



# REUSE


solution = best_case["solution"]



# REVISE



revised_solution = solution



# RETAIN


new_case = {
    "problem": new_problem,
    "solution": revised_solution
}

case_base.append(new_case)



# DISPLAY CBR RESULT

print("\nCASE-BASED REASONING")

print("New Problem:", new_problem)

print("Most Similar Case:", best_case["problem"])

print("Similarity Score:", highest_score)

print("Reused Solution:", solution)

print("Revised Solution:", revised_solution)

print("New case added to the case base.")