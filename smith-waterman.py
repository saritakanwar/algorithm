# Importing Modules
import numpy as np

#Ask for sequences from the user
#sequence_1 = input("Enter or paste sequence 1:")
#sequence_2 = input("Enter or paste sequence 2:")

sequence_1 = "ATGCT"
sequence_2 = "AGCT"

#Create Matrices
main_matrix = np.zeros((len(sequence_1)+1,len(sequence_2)+1))
match_checker_matrix = np.zeros((len(sequence_1),len(sequence_2)))

# Providing the scores for match ,mismatch and gap
match_reward = 1
mismatch_penalty = -1
gap_penalty = -2

#Fill the match checker matrix accrording to match or mismatch
for i in range(len(sequence_1)):
    for j in range(len(sequence_2)):
        if sequence_1[i] == sequence_2[j]:
            match_checker_matrix[i][j]= match_reward
        else:
            match_checker_matrix[i][j]= mismatch_penalty

#print(match_checker_matrix)

#Filling up the matrix using Needleman_Wunsch algorithm
#STEP 1 : Initialisation
for i in range(len(sequence_1)+1):
    main_matrix[i][0] = i * 0
for j in range(len(sequence_2)+1):
    main_matrix[0][j] = j * 0

#STEP 2 : Matrix Filling
for i in range(1,len(sequence_1)+1):
    for j in range(1,len(sequence_2)+1):
        m = max(main_matrix[i-1][j-1]+match_checker_matrix[i-1][j-1],
                                main_matrix[i-1][j]+gap_penalty,
                                main_matrix[i][j-1]+ gap_penalty)
        if(m<0):
            main_matrix[i][j]=0
        else:
            main_matrix[i][j]=m

#print(main_matrix)
