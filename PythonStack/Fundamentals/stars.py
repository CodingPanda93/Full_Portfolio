x = [4, 6, 1, 3, 5, 7, 25]
char = ''
i = 0
def draw_stars(num_list):
  for num in num_list:
    char = ''
    for i in range(num):
      char += '*'
    print char

y = draw_stars(x)
print y
