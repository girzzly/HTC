def td(data):
    
    resultList = ["t*d"]
    
    for x in data:
        
        result = x[0] / x[1] * 1000
        resultList.append(result)
    
    return resultList