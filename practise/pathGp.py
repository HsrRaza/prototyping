def gpath(nums ,maxDiff ,queries):
    component =[0]
    count =  0
    ans= []
    for i in range(1 , len(nums)):
        if nums[i] -nums[i-1] > maxDiff:
            count +=1

        component.append(count)

    for u , v in queries:
        ans.append(component[u]== component[v])
    return ans
       
        

        

