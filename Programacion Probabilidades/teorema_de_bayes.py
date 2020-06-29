
def calc_bayes(prior_A, prob_B_given_A, prob_B):
    return (prior_A * prob_B_given_A) / prob_B


if __name__ == '__main__':
    prob_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10/99999
    prob_no_cancer= 1-prob_cancer  

    prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * prob_no_cancer)

    # este resultado sera el nuevo prior dados mas eventos B, en otras palabras, bayes puede ser recursivo
    prob_cancer_dado_sintoma = calc_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)

    print(prob_cancer_dado_sintoma)