def genes(genome):
    startIndexOfGene = genome.find("ATG") + 3  # ATG
    a = genome.find("TAG")
    b = genome.find("TAA")
    c = genome.find("TGA")

    # Figure out which of a, b, and c has the smallest index and earliest occurrence of ending triplet.
    if 0 < a and 0 < b and 0 < c:  # If all 3 are found in genome:
        if a < b < c or a < c < b:
            endIndexOfGene = a
        elif b < a < c or b < c < a:
            endIndexOfGene = b
        elif c < a < b or c < b < a:
            endIndexOfGene = c
    elif 0 < a and 0 < b:  # If only "TAG" and "TAA" are found:
        if a < b:
            endIndexOfGene = a
        else:
            endIndexOfGene = b
    elif 0 < a and 0 < c:  # If only "TAG" and "TGA" are found:
        if a < c:
            endIndexOfGene = a
        else:
            endIndexOfGene = c
    elif 0 < b and 0 < c:  # If only "TAA" and "TGA" are found:
        if b < c:
            endIndexOfGene = b
        else:
            endIndexOfGene = c
    elif 0 < a:            # If only "TAG" is found:
        endIndexOfGene = a
    elif 0 < b:            # If only "TAA" is found:
        endIndexOfGene = b
    elif 0 < c:            # If only "TGA" is found:
        endIndexOfGene = c
    else:                  # If no ending triplet is found:
        endIndexOfGene = -1
        print("no gene is found")

    if endIndexOfGene > 0:
        gene = genome[startIndexOfGene: endIndexOfGene]  # Split the index
        print(gene)  # Print the gene sequence

        if endIndexOfGene + 3 < len(genome):
            newStartIndex = endIndexOfGene + 1
            newGenome = genome[newStartIndex: len(genome)]
            genes(newGenome)


def main():
    # gene = ("TTATGTTTTAAGGATGGGGCGTTAGTT")
    # nGene = gene.split("ATG")
    # print(nGene)
    genes("TTATGTTTTAAGGATGGGGCGTTAGTT")


main()

'''
TTT
GGGCGT
no gene is found

Process finished with exit code 0
'''