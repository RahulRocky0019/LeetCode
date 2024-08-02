def name_to_pyfile(s):
    if len(s) <= 0:
        return ""
    
    # pyfile = s.replace(" ", "_")
    # pyfile = pyfile.replace(".","")
    # pyfile = pyfile + ".py"
    
    pyfile = s.split()
    pyfile[0] = pyfile[0][:-1]
    
    while len(pyfile[0]) < 4:
        pyfile[0] = "0" + pyfile[0]
        
    pyfile = "_".join(pyfile)
    pyfile = pyfile + ".py"
    
    return pyfile


if __name__ == "__main__":
    # prob_name = "Problem Name"
    prob_name = str(input())
    print(name_to_pyfile(prob_name), end = "")
