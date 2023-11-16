import random
import re
def transform(data, num_sample: int, r: random.Random, dataset_name: str):
    text = f"{data['passage'][0]}\n{data['passage'][1]}\nIs the sentence below entailed by the sentence above?\nA. Yes\nB. No\nAnswer: "
    index_of_correct_answer = list(data['target_scores'].values()).index(1)
    answers = ['A', 'B']
    correct_answer = answers[index_of_correct_answer]

    return {"input": text, "output": correct_answer, "processed_output": correct_answer}