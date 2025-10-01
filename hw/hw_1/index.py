name = "John"
age = 36
is_student = False

# Comment
# print(name)
# print(age)
# print(is_student)


total_money = 120
price = 17
divide_money = total_money
jar_count = 0


while True:
    if total_money == divide_money:
        print(f"start: {divide_money}")
    divide_money = divide_money - price
    jar_count += 1
    print(f"покупка: {jar_count}, остаток: {divide_money}")
    if price > divide_money:
        break

print("=====")
print(f"остаток: {divide_money}")
print(f"всего куплено банок: {jar_count}")


for i in range((total_money * -1), 0, price):
    print(f"{abs(i)}")

for i in range(total_money, 0, -price):
    print(f"{abs(i)}")

a = 3
b = 7
c = -10

x_1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
x_2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)


print(x_1, x_2)

print(3 * x_1**2 + 7 * x_1 - 10)
print(3 * x_2**2 + 7 * x_2 - 10)

tasks_my = ["Сходить в магазин", "Позвонить друзьям"]
tasks_friends = ["Забрать манишну", "Посетить супермаркет"]

deal_list = tasks_my + tasks_friends
print(deal_list)


deal_list_advance = [
    {1: "Полить цветы"},
    {0: "Покормить кота"},
    {1: "Забрать посылку"},
    {2: "Почитать книгу по программированию"},
    {3: "Ответить на письмо двоюродной тети"},
]

deal_list_advance_correct = {
    0: ["Покормить кота"],
    1: ["Полить цветы", "Забрать посылку", "Мой кот с приоритетом 1"],
    2: ["Почитать книгу по программированию", "Мой кот с приоритетом 2"],
    3: ["Ответить на письмо двоюродной тети"],
}

print(deal_list_advance_correct[0])

if deal_list_advance_correct[0]:
    print("Срочные дела имеются")
else:
    print("Отдыхаем")


values = []
for key in deal_list_advance_correct:
    values.append(deal_list_advance_correct[key])

print(values)

for key in deal_list_advance_correct:
    print(key, deal_list_advance_correct[key])


for key, value in deal_list_advance_correct.items():
    print(key, value)

doings = []

for key in deal_list_advance_correct:
    for deal in deal_list_advance_correct[key]:
        doings.append(deal)
print(doings)


answer = []

for key in deal_list_advance_correct:
    for deal in deal_list_advance_correct[key]:
        if "кот" in deal:
            answer.append(deal)

print(answer)

answer_2 = []

for key in deal_list_advance_correct:
    for deal in deal_list_advance_correct[key]:
        if "кот" in deal:
            if len(answer_2) >= 2:
                break
            answer_2.append(deal)

print(answer_2)


tasks = {
    0: ["Покормить кота", "Покормить кота"],
    1: ["Покормить кота", "Забрать посылку"],
}

new_tasks = {}
for key in tasks:
    new_tasks[key] = set(tasks[key])

print(new_tasks)
