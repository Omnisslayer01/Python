def valid_Parentheses(userinput=input("Enter")):
    input_list=list(userinput)
    output_list=[]
    current_index=-1

    for i in input_list:
        output_list.append(i)
        current_index+=1

        if len(output_list)==1:
            continue

        if output_list[current_index]==")" and output_list[current_index-1]=="(":
            output_list.pop()
            output_list.pop()
            current_index-=2
            continue

        if output_list[current_index]=="]" and output_list[current_index-1]=="[":
            output_list.pop()
            output_list.pop()
            current_index-=2
            continue

        if output_list[current_index]=="}" and output_list[current_index-1]=="{":
            output_list.pop()
            output_list.pop()
            current_index-=2
            continue
    
    if len(output_list)==0 and current_index==-1:
        return True
    else:
        return False
    

print(valid_Parentheses())







