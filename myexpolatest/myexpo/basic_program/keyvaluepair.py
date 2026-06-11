def example():
    from copy import deepcopy
    question={"name":"","age":""}
    names=[("kavi",21),("ani",33),("nivi",45)]
    result = []
    for name,age in names:
        new_qn = deepcopy(question)
        new_qn["name"]=name
        new_qn["age"]=age
        result.append(new_qn)
    return result
obj=example()
print("obj",obj)
        

    