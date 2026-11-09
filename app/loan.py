# c = capital emprunté
# r = taux mensuel
# n = nombre de mensualités
# m = mensualité

def compute_loan(c, r, n):
	try:
		m = (c * r) / ((1 + r) ** n)
	except ZeroDivisionError:
		break
	return m