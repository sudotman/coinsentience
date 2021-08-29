# Sort through perp list

f = open('sym28.txt','r')
f_w = open('out.txt', 'w', newline='')
each_line = f.readlines()

counter = 9

for item in each_line:
    counter = counter + 1
    split_string = item.split(" ",1)
    substring = split_string[0]
    f_w.write("sym" + str(counter) + " = " + ' "' + substring + '" ' +" \n") 


# f.close()
# f_w.close()


# Sort through securities
# f_w = open('out2.txt', 'w', newline='')

# counter = 10

# for x in range(123):
#     counter = counter + 1
#     f_w.write("sec" + str(counter) + " = " + "security(sym"+ str(counter)+ ",_tf,close,lookahead=barmerge.lookahead_on)" +" \n") 
    

# f_w.close()

# Sort through securities
# f_w = open('out4.txt', 'w', newline='')

# counter = 10

# for x in range(123):
#     counter = counter + 1
#     f_w.write("array.push(a1,(correlation(main01,sec"+ str(counter)+ ",length)*100))" +" \n") 
    

# f_w.close()