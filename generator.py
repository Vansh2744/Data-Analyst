# def run_tasks():
#     yield "Task 1"
#     yield "Task 2"
#     yield "Task 3"
#     yield "Task 4"

# res = run_tasks()

# # print(next(res))
# # print(next(res))
# # print(next(res))
# # print(next(res))

# for task in res:
#     print(task)


#----------Infinite Generator-------------

def infinite_gen():
    count = 1
    while True:
        yield f"Count : {count}"
        count += 1

loop_gen = infinite_gen()
loop_gen1 = infinite_gen()

for _ in range(5):
    print(next(loop_gen))

for _ in range(5):
    print(next(loop_gen))

for _ in range(5):
    print(next(loop_gen1))