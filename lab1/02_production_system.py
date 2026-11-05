# A small production system for deciding whether a student can sit an exam.
# A production system has rules, working memory (facts), and a control strategy.

facts = {
    "attendance": 78,
    "fees_paid": True,
    "assignment_submitted": True
}

rules = [
    ("attendance >= 75", lambda f: f["attendance"] >= 75,
     "Attendance requirement is satisfied."),
    ("fees_paid is True", lambda f: f["fees_paid"],
     "Fee payment is complete."),
    ("assignment_submitted is True", lambda f: f["assignment_submitted"],
     "Assignment requirement is satisfied.")
]

print("Initial facts:", facts)
all_ok = True

for rule_name, condition, message in rules:
    if condition(facts):
        print("Fired rule:", rule_name, "->", message)
    else:
        print("Rule failed:", rule_name)
        all_ok = False

if all_ok:
    print("Result: Student is eligible for the exam.")
else:
    print("Result: Student is not eligible for the exam.")
