student_scores = [250, 124, 165, 300, 189, 200, 146]
largest_score = 0
index = 0

for score in student_scores:
    if largest_score <= score:
       largest_score = score

print(f"Largest Score: {largest_score}")