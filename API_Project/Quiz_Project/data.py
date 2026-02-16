import requests

param = {"amount":5,
         "type":"boolean"}

response = requests.get(url="https://opentdb.com/api.php",params=param)
response.raise_for_status()
question_data = response.json()["results"]
# print(data["results"])


# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]
