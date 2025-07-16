f1 = open('input/numbers.txt')
content = f1.read()
f1.close()

#process
total = sum(map(int, content.split()))

#output
f2 = open('Output/output02.txt', 'w')
f2.write(f"total: {total}")
f2.close()
