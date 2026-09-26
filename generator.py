def run_tasks():
    yield "Task 1"
    yield "Task 2"
    yield "Task 3"
    yield "Task 4"

res = run_tasks()

# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

for task in res:
    print(task)