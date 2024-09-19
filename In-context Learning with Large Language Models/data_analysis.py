import json
from collections import Counter

# with open('data/ARC-Easy-train.jsonl', 'r') as file:
# with open('data/ARC-Challenge-train.jsonl', 'r') as file:
# with open('data/ARC-Easy-validation.jsonl', 'r') as file:
# with open('data/ARC-Challenge-validation.jsonl', 'r') as file:
# with open('data/ARC-Easy-test.jsonl', 'r') as file:
with open('data/ARC-Challenge-test.jsonl', 'r') as file:

    # Create a counter object to count answerKey
    answer_key_counts = Counter()
    for line in file:
        json_data = json.loads(line)
        # Extract the value of the answerKey field and perform statistics
        answer_key = json_data['answerKey']
        answer_key_counts[answer_key] += 1
sorted_results = sorted(answer_key_counts.items(), key=lambda x: x[0])
for key, count in sorted_results:
    print(f"Answer Key: {key}, Count: {count}")
print(f"Number of questions: {sum(answer_key_counts.values())}")