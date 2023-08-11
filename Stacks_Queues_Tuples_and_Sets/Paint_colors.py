from collections import deque

color = deque(input().split(" "))
m_colors = ['red', 'yellow', 'blue']
second_colors = ['orange', 'purple', 'green']
final_color = deque()

while color:
    if len(color) > 1:
        first, last = color.popleft(), color.pop()

        substring = first + last
        substring_second = last + first
        if substring in m_colors or substring in second_colors:
            final_color.append(substring)
        elif substring_second in m_colors or substring_second in second_colors:
            final_color.append(substring_second)
        else:
            first_strip = first[:-1]
            last_strip = last[:-1]
            if first_strip:
                color.insert(len(color) // 2, first_strip)
            if last_strip:
                color.insert(len(color) // 2, last_strip)
    else:
        substring = color.popleft()
        if substring in m_colors or substring in second_colors:
            final_color.append(substring)
for idx in range(len(final_color)):
    if final_color[0] == 'orange':
        if 'red' not in final_color or 'yellow' not in final_color:
            final_color.popleft()
        else:
            final_color.append(final_color.popleft())
    elif final_color[0] == 'purple':
        if 'red' not in final_color or 'blue' not in final_color:
            final_color.popleft()
        else:
            final_color.append(final_color.popleft())
    elif final_color[0] == 'green':
        if 'blue' not in final_color or 'yellow' not in final_color:
            final_color.popleft()
        else:
            final_color.append(final_color.popleft())
    else:
        final_color.append(final_color.popleft())

print(list(final_color))
