def bayesian_inference(P_A, P_B_given_A, P_B_given_not_A):
    # P(A | B) = (P(B | A) * P(A)) / P(B)
    
    # P(B) = P(B | A) * P(A) + P(B | not A) * P(not A)
    P_not_A = 1 - P_A
    P_B = P_B_given_A * P_A + P_B_given_not_A * P_not_A

    # Applying Bayes' theorem
    P_A_given_B = (P_B_given_A * P_A) / P_B
    return P_A_given_B

# Example data (for a disease diagnosis)
P_A = 0.1  # Prior probability of having the disease (10%)
P_B_given_A = 0.95  # Probability of a positive test given that you have the disease (95%)
P_B_given_not_A = 0.05  # Probability of a positive test given that you don't have the disease (5%)

# Calculate the posterior probability (probability of having the disease given a positive test)
P_A_given_B = bayesian_inference(P_A, P_B_given_A, P_B_given_not_A)
print(f"Probability of having the disease given a positive test result: {P_A_given_B:.4f}")
