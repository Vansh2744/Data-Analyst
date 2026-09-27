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

# def infinite_gen():
#     count = 1
#     while True:
#         yield f"Count : {count}"
#         count += 1

# loop_gen = infinite_gen()
# loop_gen1 = infinite_gen()

# for _ in range(5):
#     print(next(loop_gen))

# for _ in range(5):
#     print(next(loop_gen))

# for _ in range(5):
#     print(next(loop_gen1))

#--------------Send Value----------------

# def send_data():
#     name = yield
#     while True:
#         print(name)
#         name = yield

# send_name = send_data()

# next(send_name)

# send_name.send("Vansh")
# send_name.send("Aman")

#-------------Yield From-------------------

# def dis_names():
#     yield "Vansh"
#     yield "Aman"

# def dis_scores():
#     yield 45
#     yield 89

# def dis_all():
#     yield from dis_names()
#     yield from dis_scores()

# all = dis_all()

# for i in all:
#     print(i)

# def display():
#     try:
#         while True:
#             name = yield "Vansh"
#     except:
#         print("Completed")

# dis = display()

# print(next(dis))
# dis.close()