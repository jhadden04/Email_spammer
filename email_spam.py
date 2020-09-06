# gmail
import ezgmail, time
x = 'Poopy Pants!'
y = 'You are Stinky '
for i in range(1):
    time.sleep(0.1)
    ezgmail.send('a@gmail.com', y, x)
    x += 'Poopy Pants! '
    y += 'You are Stinky '
    if len(x) > 2000:
           x = 'Poopy Pants '
           y = 'You are stinky '
