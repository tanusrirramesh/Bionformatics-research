fasta=input("Enter the FASTA sequence: ")
dna=""
for bp in fasta:
    if bp!=">":
        dna+=bp.upper()

        
def revcomp(dseq):
    n=len(dseq)
    revcomp1= ""
    for i in range(n-1,-1,-1):
        if dseq[i]=="A":
            revcomp1+="T"
        elif dseq[i]=="T":
            revcomp1+="A"
        elif dseq[i]=="G":
            revcomp1+="C"
        elif dseq[i]=="C":
            revcomp1+="G"
        else:
            print("Invalid")
            exit()
    return revcomp1



def revpalin(dseq2):
    n1=len(dseq2)
    result=[]
    for i in range(4,13):          
        for j in range(n1-i+1):
            subs=dseq2[j:j+i]
            if subs==revcomp(subs):
                result.append((j+1,i))   

    return result



palindromes=revpalin(dna)


print("Position\tLength")
for i,j in palindromes:
    print(i,"\t \t",j)
