import numpy as np

# Get the list of exam scores from the user
exam_scores = input().split()

# Convert the input strings to integers
exam_scores = [int(score) for score in exam_scores]

# Create a NumPy array from the list of exam scores
# Your code here
import numpy as np
exam_scores_array=np.array(exam_scores)
# Print the resulting NumPy array
print(exam_scores_array)
